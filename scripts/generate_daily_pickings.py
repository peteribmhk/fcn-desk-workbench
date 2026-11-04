#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FCN daily screen: rank worst-of baskets from today's public market data.

Dependency-free so it runs on GitHub Actions without installs.

Pipeline
  1. Price history per watchlist name (Nasdaq historical -> Yahoo chart -> Stooq):
     spot, 1D move, 6M high/drawdown, 20D realized vol, 2-session stabilization.
  2. Implied vol per name, ~3M and ~6M expiries, best source first:
       a. Tradier API with ORATS greeks (smoothed ATM IV, OI, 80% put skew), used
          only when a TRADIER_TOKEN is set (free sandbox token works);
       b. Nasdaq option chain: ATM straddle converted to an IV estimate (always
          fetched, used as fallback and as a cross-check);
       c. 20-day realized vol when no options read exists.
     Optional local cross-check: iv_inputs/manual_iv.csv (git-ignored), e.g. IV30
     read by hand from Market Chameleon. Never scraped; see iv_inputs/README.md.
  3. Next earnings date (Nasdaq, best effort).
  4. Name gates: liquidity, crypto exclusion, falling-knife, earnings hold.
  5. Basket search: cross-theme pairs and trios, realized correlation from history,
     ballpark coupon from scripts/fcn_model.py (6M, KO 100 monthly, KI at maturity).
  6. Report: daily/latest.md (phone readable), daily/latest.json (machine readable,
     used for requote classification on the next run), archive + index.

Everything is indicative only and never a firm quote.

Testing without network:  python scripts/generate_daily_pickings.py --fixture path.json --out /tmp/x
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import itertools
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fcn_model import FCNTerms, ballpark_range  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
WATCHLIST_PATH = REPO_ROOT / "watchlist.csv"
HKT = dt.timezone(dt.timedelta(hours=8))

LABEL = "Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems."

CRYPTO_LINKED = {"MSTR", "COIN", "MARA", "RIOT", "CLSK", "HUT", "BTBT", "BITF", "IREN", "WGMI", "CIFR", "CORZ", "HOOD_CRYPTO"}

# Screen settings (edit here, documented in PLAYBOOK.md)
TERMS = FCNTerms(tenor_months=6, ko=1.00, ki_levels=[0.50, 0.55, 0.59, 0.65, 0.70], rate=0.039)
HEADLINE_KI = 0.59
MIN_ATM_OI = 1000            # ATM call+put open interest across the two proxy expiries
FALLING_KNIFE_MOVE = -6.0    # % one-day drop that triggers the 2-session stabilization rule
EARNINGS_HOLD_DAYS = 14      # earnings within this many days -> event hold
MAX_LEG_VOL = 1.10           # names above this implied vol are watch-only (gap risk dominates)
POOL_SIZE = 22               # top names carried into basket search
PAIRS_TO_PRICE = 12  # per risk profile
TRIOS_TO_PRICE = 10
SCREEN_PATHS = 6000
FINAL_PATHS = 20000
MAX_NAME_REUSE = 2
IV_GAP_FLAG = 0.10           # flag (non-blocking) when two IV reads differ by more than 10 vol points

# Tradier API (ORATS greeks). Free sandbox: 15-min delayed, 60 market-data calls/min.
TRADIER_DEFAULT_BASE = "https://sandbox.tradier.com/v1"
TRADIER_MIN_INTERVAL = 1.1   # seconds between calls (~55/min, under the sandbox limit)

# Manual IV cross-check (local only, git-ignored)
MANUAL_IV_PATH = REPO_ROOT / "iv_inputs" / "manual_iv.csv"
MANUAL_IV_MAX_AGE_DAYS = 5
LOCAL_OUT = REPO_ROOT / "local" / "daily"   # git-ignored; default output when manual IV is loaded

NASDAQ_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.nasdaq.com",
    "Referer": "https://www.nasdaq.com/",
}

# Theme buckets: two legs from the same bucket are pseudo-diversification.
BUCKET_RULES = [
    ("China ADR", ["china"]),
    ("Quantum", ["quantum"]),
    ("Nuclear/Power", ["nuclear", "reactor", "power generation", "power equipment", "grid", "haleu"]),
    ("Space/Defense", ["space", "satellite", "lunar", "defense", "drone", "aerospace"]),
    ("Biotech/Health", ["biotech", "gene", "pharma", "health", "telehealth", "surgical", "obesity", "glp"]),
    ("EV/Auto", ["ev", "auto"]),
    ("Solar/Clean", ["solar", "clean"]),
    ("Fintech", ["fintech", "bnpl", "consumer finance"]),
    ("AI Cloud/DC", ["neocloud", "ai cloud", "data-center", "data center"]),
    ("Software", ["software", "adtech", "observability", "security", "data cloud", "cloud/software", "edge cloud"]),
    ("Semis/AI HW", ["semiconductor", "silicon", "server", "optical", "connectivity", "networking", "storage", "memory", "cpu", "glass"]),
    ("Mega-cap", ["mega-cap"]),
    ("Cyclical/Consumer", ["airline", "cyclical", "travel", "betting", "gaming", "e-commerce"]),
]


# --------------------------------------------------------------------------- utils

def bucket_of(theme: str) -> str:
    text = theme.lower()
    for bucket, keys in BUCKET_RULES:
        for key in keys:
            if key == "ev":
                if re.search(r"\bev\b", text):
                    return bucket
            elif key in text:
                return bucket
    return theme or "Other"


def clean_number(value) -> str:
    if value is None:
        return ""
    return str(value).replace("$", "").replace(",", "").replace("%", "").strip()


def to_float(value) -> float:
    try:
        text = clean_number(value)
        if text in {"", "N/D", "N/A", "-", "--"}:
            return float("nan")
        return float(text)
    except ValueError:
        return float("nan")


def to_int(value) -> int:
    number = to_float(value)
    return 0 if math.isnan(number) else int(number)


def get_json(url: str, headers: dict[str, str], timeout: int = 25):
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def fmt_pct(x: float | None, digits: int = 0, sign: bool = False) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/a"
    return f"{x:+.{digits}f}%" if sign else f"{x:.{digits}f}%"


def md_table(header: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(out)


# --------------------------------------------------------------------------- watchlist

def load_watchlist() -> list[dict[str, str]]:
    rows = []
    with WATCHLIST_PATH.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            ticker = (row.get("ticker") or "").strip().upper()
            if ticker and ticker not in CRYPTO_LINKED:
                cleaned = {k: (v or "").strip() for k, v in row.items()}
                cleaned["ticker"] = ticker
                rows.append(cleaned)
    return rows


def _parse_vol(text: str) -> float | None:
    """'40.5', '40.5%' or '0.405' -> 0.405. Values above 3 are read as percent."""
    value = to_float(text)
    if math.isnan(value) or value <= 0:
        return None
    return value / 100 if value > 3 else value


def load_manual_iv(path: Path, today: dt.date) -> tuple[dict[str, dict], list[str]]:
    """Read the optional hand-filled IV file. Returns ({ticker: row}, notes).

    Columns: ticker, date (YYYY-MM-DD), iv30, iv_6m (optional), source, notes (optional).
    Rows older than MANUAL_IV_MAX_AGE_DAYS are ignored so a forgotten file cannot
    silently feed stale vol into the screen.
    """
    if not path.exists():
        return {}, []
    out, stale, bad = {}, 0, 0
    with path.open(newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            ticker = (row.get("ticker") or "").strip().upper()
            if not ticker or ticker.startswith("#"):
                continue
            try:
                day = dt.date.fromisoformat((row.get("date") or "").strip())
            except ValueError:
                bad += 1
                continue
            iv30, iv6 = _parse_vol(row.get("iv30") or ""), _parse_vol(row.get("iv_6m") or "")
            if iv30 is None and iv6 is None:
                bad += 1
                continue
            if (today - day).days > MANUAL_IV_MAX_AGE_DAYS:
                stale += 1
                continue
            prior = out.get(ticker)
            if prior is None or day >= prior["date"]:
                out[ticker] = {"date": day, "iv30": iv30, "iv_6m": iv6,
                               "source": (row.get("source") or "manual").strip() or "manual"}
    notes = [f"Manual IV file: {len(out)} names loaded from `{path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path}`"
             + (f", {stale} stale rows ignored (older than {MANUAL_IV_MAX_AGE_DAYS} days)" if stale else "")
             + (f", {bad} unreadable rows skipped" if bad else "") + "."]
    return out, notes


# --------------------------------------------------------------------------- data fetch

def history_nasdaq(ticker: str, today: dt.date) -> list[tuple[dt.date, float]]:
    start = (today - dt.timedelta(days=200)).isoformat()
    query = urllib.parse.urlencode({"assetclass": "stocks", "fromdate": start, "todate": today.isoformat(), "limit": "200"})
    payload = get_json(f"https://api.nasdaq.com/api/quote/{ticker}/historical?{query}", NASDAQ_HEADERS)
    rows = ((((payload or {}).get("data") or {}).get("tradesTable") or {}).get("rows")) or []
    series = []
    for row in rows:
        try:
            day = dt.datetime.strptime(row.get("date", ""), "%m/%d/%Y").date()
        except ValueError:
            continue
        close = to_float(row.get("close"))
        if not math.isnan(close) and close > 0:
            series.append((day, close))
    return sorted(series)


def history_yahoo(ticker: str, today: dt.date) -> list[tuple[dt.date, float]]:
    query = urllib.parse.urlencode({"range": "6mo", "interval": "1d"})
    payload = get_json(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?{query}", {"User-Agent": "Mozilla/5.0"})
    result = ((payload.get("chart") or {}).get("result") or [None])[0] or {}
    stamps = result.get("timestamp") or []
    closes = (((result.get("indicators") or {}).get("quote") or [{}])[0]).get("close") or []
    series = []
    for stamp, close in zip(stamps, closes):
        if close:
            series.append((dt.datetime.fromtimestamp(int(stamp), tz=dt.timezone.utc).date(), float(close)))
    return series


def history_stooq(ticker: str, today: dt.date) -> list[tuple[dt.date, float]]:
    query = urllib.parse.urlencode({"s": f"{ticker.lower()}.us", "i": "d"})
    with urllib.request.urlopen(f"https://stooq.com/q/d/l/?{query}", timeout=25) as response:
        text = response.read().decode("utf-8", errors="replace")
    series = []
    for row in csv.DictReader(text.splitlines()):
        try:
            day = dt.date.fromisoformat(row["Date"])
        except (KeyError, ValueError):
            continue
        if day >= today - dt.timedelta(days=200):
            close = to_float(row.get("Close"))
            if not math.isnan(close):
                series.append((day, close))
    return series


def fetch_history(ticker: str, today: dt.date) -> tuple[list[tuple[dt.date, float]], str]:
    for name, func in (("Nasdaq", history_nasdaq), ("Yahoo", history_yahoo), ("Stooq", history_stooq)):
        try:
            series = func(ticker, today)
        except Exception:
            continue
        if len(series) >= 25:
            return series, name
    return [], "none"


def fetch_options(ticker: str, spot: float, today: dt.date) -> dict:
    query = urllib.parse.urlencode({"assetclass": "stocks", "fromdate": "all", "limit": "10000"})
    payload = get_json(f"https://api.nasdaq.com/api/quote/{ticker}/option-chain?{query}", NASDAQ_HEADERS, timeout=30)
    raw_rows = ((((payload or {}).get("data") or {}).get("table") or {}).get("rows")) or []
    chain = []
    expiry = None
    for raw in raw_rows:
        if raw.get("expirygroup"):
            try:
                expiry = dt.datetime.strptime(raw["expirygroup"], "%B %d, %Y").date()
            except ValueError:
                expiry = None
            continue
        strike = to_float(raw.get("strike"))
        if expiry is None or math.isnan(strike):
            continue
        mids = []
        for side in ("c", "p"):
            bid, ask = to_float(raw.get(f"{side}_Bid")), to_float(raw.get(f"{side}_Ask"))
            if not math.isnan(bid) and not math.isnan(ask) and ask > 0:
                mids.append((bid + ask) / 2)
        if len(mids) != 2:
            continue
        chain.append({
            "expiry": expiry,
            "strike": strike,
            "straddle": mids[0] + mids[1],
            "oi": to_int(raw.get("c_Openinterest")) + to_int(raw.get("p_Openinterest")),
        })
    result: dict = {"oi": 0}
    expiries = sorted({row["expiry"] for row in chain if (row["expiry"] - today).days >= 20})
    for label, target in (("3M", 91), ("6M", 182)):
        if not expiries:
            break
        exp = min(expiries, key=lambda e: abs((e - today).days - target))
        rows = [r for r in chain if r["expiry"] == exp]
        atm = min(rows, key=lambda r: abs(r["strike"] - spot))
        days = (exp - today).days
        t = days / 365.0
        # ATM straddle ~= 0.7979 * sigma * S * sqrt(T)
        iv = atm["straddle"] / (0.7979 * spot * math.sqrt(t))
        result[label] = {"expiry": exp.isoformat(), "days": days, "strike": atm["strike"],
                         "straddle_pct": atm["straddle"] / spot * 100, "iv": iv,
                         "gap": abs(days - target) > 45}
        result["oi"] += atm["oi"]
    return result


class Tradier:
    """Minimal Tradier market-data client: expirations + chains with ORATS greeks.

    Throttled to stay under the sandbox limit (60 market-data calls per minute).
    Three calls per name (expirations, ~3M chain, ~6M chain).
    """

    def __init__(self, token: str, base: str | None = None):
        self.base = (base or TRADIER_DEFAULT_BASE).rstrip("/")
        self.headers = {"Authorization": f"Bearer {token}", "Accept": "application/json",
                        "User-Agent": "fcn-desk-workbench"}
        self._last = 0.0
        self.calls = 0
        self.errors = 0

    def get(self, path: str, params: dict) -> dict:
        for attempt in (1, 2):
            wait = TRADIER_MIN_INTERVAL - (time.monotonic() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()
            self.calls += 1
            try:
                return get_json(f"{self.base}{path}?{urllib.parse.urlencode(params)}", self.headers) or {}
            except urllib.error.HTTPError as err:
                if err.code == 429 and attempt == 1:
                    time.sleep(61)
                    continue
                self.errors += 1
                if err.code in (401, 403):
                    raise PermissionError("Tradier token rejected (expired or wrong environment)") from err
                raise
        return {}

    @staticmethod
    def _as_list(value) -> list:
        if value is None:
            return []
        return value if isinstance(value, list) else [value]

    def expirations(self, ticker: str) -> list[dt.date]:
        data = self.get("/markets/options/expirations", {"symbol": ticker, "includeAllRoots": "false", "strikes": "false"})
        dates = self._as_list(((data.get("expirations") or {}).get("date")))
        out = []
        for d in dates:
            try:
                out.append(dt.date.fromisoformat(str(d)))
            except ValueError:
                continue
        return sorted(out)

    def chain(self, ticker: str, expiry: dt.date) -> list[dict]:
        data = self.get("/markets/options/chains", {"symbol": ticker, "expiration": expiry.isoformat(), "greeks": "true"})
        return self._as_list(((data.get("options") or {}).get("option")))


def _tradier_iv(option: dict) -> float | None:
    greeks = option.get("greeks") or {}
    for key in ("smv_vol", "mid_iv"):
        value = to_float(greeks.get(key))
        if not math.isnan(value) and 0.03 < value < 5:
            return value
    return None


def fetch_options_tradier(client: Tradier, ticker: str, spot: float, today: dt.date) -> dict:
    """Same shape as fetch_options(): {"oi", "3M": {...}, "6M": {...}} plus ORATS skew."""
    expiries = [e for e in client.expirations(ticker) if (e - today).days >= 20]
    result: dict = {"oi": 0, "source": "Tradier/ORATS"}
    seen: dict[dt.date, list[dict]] = {}
    for label, target in (("3M", 91), ("6M", 182)):
        if not expiries:
            break
        exp = min(expiries, key=lambda e: abs((e - today).days - target))
        if exp not in seen:
            seen[exp] = client.chain(ticker, exp)
        chain = [o for o in seen[exp] if not math.isnan(to_float(o.get("strike")))]
        if not chain:
            continue
        atm_strike = min({to_float(o["strike"]) for o in chain}, key=lambda k: abs(k - spot))
        atm = [o for o in chain if to_float(o["strike"]) == atm_strike]
        ivs = [iv for iv in (_tradier_iv(o) for o in atm) if iv]
        if not ivs:
            continue
        days = (exp - today).days
        entry = {"expiry": exp.isoformat(), "days": days, "strike": atm_strike,
                 "iv": sum(ivs) / len(ivs), "gap": abs(days - target) > 45,
                 "greeks_at": max(((o.get("greeks") or {}).get("updated_at") or "") for o in atm) or None}
        # Downside skew: 80%-strike put IV minus ATM IV (prices the KI put; info only)
        puts = [o for o in chain if o.get("option_type") == "put" and _tradier_iv(o)]
        if puts:
            p80 = min(puts, key=lambda o: abs(to_float(o["strike"]) - 0.8 * spot))
            if abs(to_float(p80["strike"]) / spot - 0.8) <= 0.05:
                entry["skew80"] = _tradier_iv(p80) - entry["iv"]
        result[label] = entry
        result["oi"] += sum(to_int(o.get("open_interest")) for o in atm)
    return result


def fetch_earnings(ticker: str, today: dt.date) -> str | None:
    payload = get_json(f"https://api.nasdaq.com/api/analyst/{ticker}/earnings-date", NASDAQ_HEADERS)
    text = json.dumps((payload or {}).get("data") or {})
    match = re.search(r"([A-Z][a-z]{2}) (\d{1,2}), (\d{4})", text)
    if not match:
        return None
    try:
        day = dt.datetime.strptime(" ".join(match.groups()), "%b %d %Y").date()
    except ValueError:
        return None
    return day.isoformat() if day >= today - dt.timedelta(days=3) else None


def collect_market(watchlist: list[dict], today: dt.date) -> dict:
    market = {"names": {}, "sources": {}, "tradier": {"configured": False}}
    token = os.environ.get("TRADIER_TOKEN", "").strip()
    client = Tradier(token, os.environ.get("TRADIER_BASE_URL", "").strip() or None) if token else None
    if client:
        market["tradier"] = {"configured": True, "base": client.base}
    for row in watchlist:
        t = row["ticker"]
        series, source = fetch_history(t, today)
        market["sources"][t] = source
        entry = {"history": [(d.isoformat(), c) for d, c in series]}
        if series:
            try:
                entry["options"] = fetch_options(t, series[-1][1], today)
            except Exception:
                entry["options"] = {}
            if client:
                try:
                    entry["options_api"] = fetch_options_tradier(client, t, series[-1][1], today)
                except PermissionError as err:
                    market["tradier"]["error"] = str(err)
                    client = None  # stop calling with a dead token; Nasdaq carries the run
                except Exception:
                    entry["options_api"] = {}
            try:
                entry["earnings"] = fetch_earnings(t, today)
            except Exception:
                entry["earnings"] = None
        market["names"][t] = entry
    if market["tradier"].get("configured"):
        market["tradier"]["calls"] = (client.calls if client else None)
    return market


# --------------------------------------------------------------------------- analytics

def log_returns(series: list[tuple[str, float]]) -> dict[str, float]:
    out = {}
    for (_, prev), (day, cur) in zip(series, series[1:]):
        if prev > 0 and cur > 0:
            out[day] = math.log(cur / prev)
    return out


def realized_vol(rets: list[float]) -> float:
    if len(rets) < 5:
        return float("nan")
    mean = sum(rets) / len(rets)
    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
    return math.sqrt(var * 252)


def correlation(a: dict[str, float], b: dict[str, float], window: int = 90) -> float:
    days = sorted(set(a) & set(b))[-window:]
    if len(days) < 30:
        return float("nan")
    xs, ys = [a[d] for d in days], [b[d] for d in days]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx <= 0 or vy <= 0:
        return float("nan")
    return cov / math.sqrt(vx * vy)


def _iv(opts: dict, label: str) -> float | None:
    value = (opts.get(label) or {}).get("iv")
    return value if value and 0.05 < value < 3 else None


def analyse_name(row: dict, entry: dict, today: dt.date, manual: dict | None = None,
                 manual_override: bool = False) -> dict:
    t = row["ticker"]
    hist = entry.get("history") or []
    info = {"ticker": t, "theme": row.get("theme", ""), "bucket": bucket_of(row.get("theme", "")),
            "risks": row.get("primary_risks", ""), "flags": [], "status": "no data"}
    if len(hist) < 25:
        return info
    closes = [c for _, c in hist]
    spot = closes[-1]
    rets_map = log_returns(hist)
    rets = list(rets_map.values())
    high_6m = max(closes[-126:])
    info.update({
        "spot": spot,
        "asof": hist[-1][0],
        "move_1d": (closes[-1] / closes[-2] - 1) * 100,
        "move_5d": (closes[-1] / closes[-6] - 1) * 100 if len(closes) > 6 else float("nan"),
        "drawdown": (spot / high_6m - 1) * 100,
        "rv20": realized_vol(rets[-20:]),
        "returns": rets_map,
    })
    nasdaq = entry.get("options") or {}
    api = entry.get("options_api") or {}
    # Prefer the API read when it has a usable IV; Nasdaq straddle otherwise.
    opts = api if (_iv(api, "6M") or _iv(api, "3M")) else nasdaq
    iv6, iv3 = _iv(opts, "6M"), _iv(opts, "3M")
    src_name = "ORATS" if opts is api else "straddle"
    info["iv3"], info["iv6"] = iv3, iv6
    info["oi"] = opts.get("oi", 0) or nasdaq.get("oi", 0)
    info["opts"] = opts
    info["iv_nasdaq"] = _iv(nasdaq, "6M") or _iv(nasdaq, "3M")
    info["iv_api"] = _iv(api, "6M") or _iv(api, "3M")
    info["skew80"] = (api.get("6M") or {}).get("skew80")
    info["manual"] = manual
    # vol used for a 6M note: 6M listed, else 3M listed, else realized
    if iv6:
        info["vol"], info["vol_src"] = iv6, f"6M {src_name}"
    elif iv3:
        info["vol"], info["vol_src"] = iv3, f"3M {src_name}"
    elif not math.isnan(info["rv20"]):
        info["vol"], info["vol_src"] = info["rv20"], "RV20 (no options)"
        info["flags"].append("no listed-options read")
    else:
        return info

    # Cross-checks (non-blocking): API vs Nasdaq straddle, manual IV30 vs ~3M listed
    if info["iv_api"] and info["iv_nasdaq"] and abs(info["iv_api"] - info["iv_nasdaq"]) > IV_GAP_FLAG:
        info["flags"].append(f"IV sources disagree: ORATS {info['iv_api']*100:.0f} vs straddle {info['iv_nasdaq']*100:.0f}")
    if manual:
        ref = iv3 or info["vol"]
        m_iv = manual.get("iv30")
        if m_iv and abs(m_iv - ref) > IV_GAP_FLAG:
            info["flags"].append(f"manual IV30 {m_iv*100:.0f} vs listed {ref*100:.0f}")
        if manual_override:
            chosen = manual.get("iv_6m") or m_iv
            if chosen:
                tag = "6M" if manual.get("iv_6m") else "IV30"
                info["vol"], info["vol_src"] = chosen, f"manual {tag} ({manual['source']})"

    dd = info["drawdown"]
    if dd > -10:
        info["entry"] = "near 6M high"
    elif dd > -20:
        info["entry"] = "mild pullback"
    elif dd >= -50:
        info["entry"] = "sweet spot (-20% to -50%)"
    else:
        info["entry"] = "deep drawdown (>50%)"

    # Falling-knife rule: fresh heavy drop, or a new 20D low in either of the last two sessions
    low20_prior = min(closes[-22:-2]) if len(closes) >= 22 else min(closes[:-2])
    new_low_recent = min(closes[-2:]) < low20_prior
    if info["move_1d"] <= FALLING_KNIFE_MOVE or new_low_recent:
        info["flags"].append("falling knife: wait 2 stable sessions")
    earnings = entry.get("earnings")
    info["earnings"] = earnings
    if earnings:
        days = (dt.date.fromisoformat(earnings) - today).days
        if -1 <= days <= EARNINGS_HOLD_DAYS:
            info["flags"].append(f"event hold: earnings {earnings}")
    if info["oi"] and info["oi"] < MIN_ATM_OI:
        info["flags"].append("thin listed options")
    if info["vol"] > MAX_LEG_VOL:
        info["flags"].append("vol too high for a core leg")
    for label in ("3M", "6M"):
        if (opts.get(label) or {}).get("gap"):
            info["flags"].append(f"{label} expiry gap (check option-expiry-quirks)")
            break

    blocking = [f for f in info["flags"] if f.startswith(("falling knife", "event hold", "thin", "vol too high"))]
    info["status"] = "conditional" if blocking else "eligible"
    info["score"] = info["vol"] * ENTRY_MULT[info["entry"]]
    return info


def basket_corr(names: list[dict]) -> list[list[float]]:
    n = len(names)
    m = [[1.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            c = correlation(names[i]["returns"], names[j]["returns"])
            if math.isnan(c):
                c = 0.75 if names[i]["bucket"] == names[j]["bucket"] else 0.45
            c = max(-0.2, min(0.95, c))
            m[i][j] = m[j][i] = c
    return m


def heuristic(names: list[dict], corr: list[list[float]]) -> float:
    vols = [x["vol"] for x in names]
    pairs = [corr[i][j] for i in range(len(names)) for j in range(i + 1, len(names))]
    avg_corr = sum(pairs) / len(pairs)
    return math.sqrt(sum(v * v for v in vols) / len(vols)) * (1 + 0.6 * (1 - avg_corr)) * (1 + 0.15 * (len(names) - 2))


def category(names: list[dict]) -> str:
    top = max(x["vol"] for x in names)
    if top < 0.50:
        return "Balanced"
    if top < 0.75:
        return "Higher coupon"
    return "Aggressive"


ENTRY_MULT = {"sweet spot (-20% to -50%)": 1.10, "mild pullback": 1.0, "near 6M high": 0.90, "deep drawdown (>50%)": 0.95}
PAIR_MIX = {"Balanced": 2, "Higher coupon": 2, "Aggressive": 1}
TRIO_MIX = {"Balanced": 1, "Higher coupon": 1, "Aggressive": 1}


def build_baskets(pool: list[dict], size: int, mix: dict[str, int], to_price: int) -> list[dict]:
    """Search cross-theme baskets and return a spread across risk profiles.

    Ranking inside each profile: mid ballpark coupon x average entry-quality multiplier,
    so a basket of names in the drawdown sweet spot beats one sitting at highs.
    """
    by_profile: dict[str, list] = {k: [] for k in mix}
    for combo in itertools.combinations(pool, size):
        if len({x["bucket"] for x in combo}) < size:  # every leg from a different theme bucket
            continue
        prof = category(list(combo))
        if prof not in by_profile:
            continue
        corr = basket_corr(list(combo))
        by_profile[prof].append((heuristic(list(combo), corr), combo, corr))
    chosen, usage = [], {}
    for prof, want in mix.items():
        cands = sorted(by_profile[prof], key=lambda c: -c[0])[:to_price]
        priced = []
        for _, combo, corr in cands:
            res = ballpark_range([x["vol"] for x in combo], corr, TERMS, n_paths=SCREEN_PATHS)
            mid = (res[HEADLINE_KI]["low"] + res[HEADLINE_KI]["high"]) / 2
            entry = sum(ENTRY_MULT[x["entry"]] for x in combo) / len(combo)
            priced.append((mid * entry, combo, corr))
        priced.sort(key=lambda c: -c[0])
        got = 0
        for _, combo, corr in priced:
            tickers = [x["ticker"] for x in combo]
            if any(usage.get(t, 0) >= MAX_NAME_REUSE for t in tickers):
                continue
            for t in tickers:
                usage[t] = usage.get(t, 0) + 1
            names = list(combo)
            chosen.append({"names": names, "corr": corr,
                           "final": ballpark_range([x["vol"] for x in names], corr, TERMS, n_paths=FINAL_PATHS)})
            got += 1
            if got >= want:
                break
    return chosen


def pick_anchor_pair(pool: list[dict], exclude: set[frozenset]) -> dict | None:
    """One familiar, deep-liquidity pair for clients who want recognizable names."""
    liquid = sorted([x for x in pool if x.get("oi", 0) >= 10000 and x["vol"] < 0.55], key=lambda x: -x["oi"])[:10]
    best = None
    for a, b in itertools.combinations(liquid, 2):
        if a["bucket"] == b["bucket"] or frozenset((a["ticker"], b["ticker"])) in exclude:
            continue
        corr = basket_corr([a, b])
        h = heuristic([a, b], corr)
        if best is None or h > best[0]:
            best = (h, [a, b], corr)
    if not best:
        return None
    names, corr = best[1], best[2]
    return {"names": names, "corr": corr, "final": ballpark_range([x["vol"] for x in names], corr, TERMS, n_paths=FINAL_PATHS)}


# --------------------------------------------------------------------------- report

def previous_baskets(path: Path) -> dict[str, dict]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {b["key"]: b for b in data.get("baskets", [])}


def requote_label(key: str, vols: list[float], prev: dict[str, dict]) -> str:
    if key not in prev:
        return "fresh"
    old = prev[key].get("vols") or []
    if len(old) == len(vols) and all(abs(a - b) < 0.05 for a, b in zip(vols, old)):
        return "repeat, same rationale"
    return "repeat, changed inputs"


def basket_row(rank: int, b: dict, prev: dict) -> tuple[list[str], dict]:
    names = b["names"]
    tickers = [x["ticker"] for x in names]
    key = "/".join(sorted(tickers))
    vols = [x["vol"] for x in names]
    pairs = [b["corr"][i][j] for i in range(len(names)) for j in range(i + 1, len(names))]
    head = b["final"][HEADLINE_KI]
    label = requote_label(key, vols, prev)
    row = [
        str(rank),
        " / ".join(tickers),
        " + ".join(x["bucket"] for x in names),
        " / ".join(f"{v*100:.0f}" for v in vols),
        f"{sum(pairs)/len(pairs):.2f}",
        f"{head['low']*100:.0f}-{head['high']*100:.0f}%",
        f"{head['p_ki']*100:.0f}%",
        category(names),
        label,
    ]
    record = {"key": key, "tickers": tickers, "vols": [round(v, 4) for v in vols],
              "avg_corr": round(sum(pairs) / len(pairs), 3),
              "coupon_headline_ki": [round(head["low"], 4), round(head["high"], 4)], "requote": label}
    return row, record


def ki_ladder_table(b: dict) -> str:
    rows, prev_mid, prev_ki = [], None, None
    for ki in TERMS.ki_levels:
        r = b["final"][ki]
        mid = (r["low"] + r["high"]) / 2 * 100
        if prev_mid is None:
            pickup, verdict = "-", "base protection"
        else:
            per_pt = (mid - prev_mid) / ((ki - prev_ki) * 100)
            pickup = f"{per_pt:.2f}% p.a."
            verdict = "prefer lower KI" if per_pt < 0.25 else ("balanced" if per_pt <= 0.60 else "strong pickup")
        rows.append([f"{ki*100:.0f}%", f"{r['low']*100:.1f}-{r['high']*100:.1f}%", f"{r['p_ki']*100:.1f}%", pickup, verdict])
        prev_mid, prev_ki = mid, ki
    return md_table(["KI", "Ballpark coupon p.a.", "P(loss at maturity)", "Pickup per KI pt", "Read"], rows)


def why_line(b: dict) -> str:
    parts = []
    for x in b["names"]:
        bits = [f"{x['ticker']}: {x['entry']}", f"{x['drawdown']:.0f}% vs 6M high", f"vol {x['vol']*100:.0f}% ({x['vol_src']})"]
        if x.get("earnings"):
            bits.append(f"next earnings {x['earnings']}")
        parts.append(", ".join(bits))
    return "; ".join(parts)


def generate(market: dict, now_utc: dt.datetime, prev: dict, manual: dict | None = None,
             manual_override: bool = False, manual_notes: list[str] | None = None) -> tuple[str, dict]:
    watchlist = load_watchlist()
    today = now_utc.astimezone(HKT).date()
    manual = manual or {}
    analysed = [analyse_name(row, market["names"].get(row["ticker"], {}), today,
                             manual.get(row["ticker"]), manual_override) for row in watchlist]
    with_data = [x for x in analysed if "vol" in x]
    with_opts = [x for x in with_data if x.get("iv3") or x.get("iv6")]
    n_api = sum(1 for x in with_data if "ORATS" in x["vol_src"])
    n_straddle = sum(1 for x in with_data if "straddle" in x["vol_src"])
    n_manual = sum(1 for x in with_data if x["vol_src"].startswith("manual"))
    n_rv = sum(1 for x in with_data if x["vol_src"].startswith("RV20"))
    tradier = market.get("tradier") or {}
    if n_manual:
        vol_sentence = (f"Vols: manual override for {n_manual} names (local run), otherwise Tradier/ORATS listed IV where available, "
                        "else Nasdaq ATM straddles")
    elif n_api:
        vol_sentence = "Vols come from Tradier/ORATS smoothed ATM implied vol, falling back to Nasdaq ATM straddles"
    else:
        vol_sentence = "Vols come from listed ATM straddles (Nasdaq)"
    eligible = sorted([x for x in with_data if x["status"] == "eligible"], key=lambda x: -x["score"])
    conditional = [x for x in with_data if x["status"] == "conditional"]

    coverage = len(with_data) / max(1, len(watchlist))
    opt_cov = len(with_opts) / max(1, len(watchlist))
    if coverage >= 0.8 and opt_cov >= 0.6:
        status = "GREEN"
    elif coverage >= 0.4:
        status = "AMBER"
    else:
        status = "RED"

    hk = now_utc.astimezone(HKT)
    asof = max((x["asof"] for x in with_data), default="n/a")
    lines = [
        "# FCN Daily Screen",
        "",
        f"**Generated:** {hk:%Y-%m-%d %H:%M} HKT  |  **US close used:** {asof}  |  **Data status:** {status}",
        "",
        f"> {LABEL}",
        "> Public/delayed data, used only to decide what to RFQ. Issuer RFQ levels override everything below.",
        "",
    ]

    record = {"generated_hkt": hk.isoformat(), "us_close": asof, "status": status, "baskets": []}
    if status == "RED":
        lines += [
            "## Data problem: no picks today",
            "",
            f"Only {len(with_data)} of {len(watchlist)} names returned usable data, so this run does not rank baskets.",
            "Re-run the workflow later or ask Claude for a live screen in chat.",
        ]
        return "\n".join(lines) + "\n", record

    pool = eligible[:POOL_SIZE]
    pool += [x for x in sorted(eligible[POOL_SIZE:], key=lambda x: -ENTRY_MULT[x['entry']]) if x['vol'] < 0.5][:10]
    pairs = build_baskets(pool, 2, PAIR_MIX, PAIRS_TO_PRICE)
    trios = build_baskets(pool, 3, TRIO_MIX, TRIOS_TO_PRICE)
    anchor = pick_anchor_pair(eligible, {frozenset(x["ticker"] for x in b["names"]) for b in pairs})

    header = ["#", "Basket", "Themes", "Vol % (legs)", "Avg corr", f"6M KI{HEADLINE_KI*100:.0f} ballpark", "P(loss)", "Profile", "Requote"]
    lines += [
        "## How to read this",
        "",
        f"Structure assumed for the ballpark: USD worst-of FCN, {TERMS.tenor_months}M, KO 100% monthly from month 1, "
        f"KI {HEADLINE_KI*100:.0f}% observed at maturity, strike 100%, RO 100, monthly fixed coupon. "
        f"{vol_sentence}; correlation from 90-day realized returns. "
        "The ballpark ignores skew, dividends and issuer-specific funding, so treat it as a sanity check for issuer levels, not a forecast. "
        "Every basket mixes different themes on purpose; same-sector pairs are pseudo-diversification.",
        "",
        "## Two-stock picks",
        "",
    ]
    rows = []
    for i, b in enumerate(pairs, 1):
        row, rec = basket_row(i, b, prev)
        rows.append(row)
        record["baskets"].append(rec)
    lines.append(md_table(header, rows) if rows else "_No eligible pair passed today's gates._")
    lines += ["", "## Three-stock picks", ""]
    rows = []
    for i, b in enumerate(trios, 1):
        row, rec = basket_row(i, b, prev)
        rows.append(row)
        record["baskets"].append(rec)
    lines.append(md_table(header, rows) if rows else "_No eligible trio passed today's gates._")
    if anchor:
        row, rec = basket_row(1, anchor, prev)
        record["baskets"].append(rec)
        lines += ["", "## Familiar-name anchor (for conservative clients)", "", md_table(header, [row]),
                  "", "Deep listed liquidity, lower vol, easy to explain. Expect a lower coupon."]

    lines += ["", "## Why these names", ""]
    for b in pairs[:3] + trios[:2]:
        lines.append(f"- **{' / '.join(x['ticker'] for x in b['names'])}**: {why_line(b)}")

    if pairs:
        lines += ["", f"## KI ladder: {' / '.join(x['ticker'] for x in pairs[0]['names'])} (top pair)", "",
                  ki_ladder_table(pairs[0]), "",
                  "Pickup per KI point thresholds: below 0.25% p.a. keep the lower KI; 0.25-0.60% balanced; above 0.60% the higher KI may be worth it. "
                  "Model pickup is smooth by construction; the real decision uses the issuer's KI ladder."]

    lines += ["", "## Conditional / watch only", ""]
    if conditional:
        crow = []
        for x in sorted(conditional, key=lambda x: -x["vol"]):
            crow.append([x["ticker"], fmt_pct(x["move_1d"], 1, True), fmt_pct(x["drawdown"], 0), f"{x['vol']*100:.0f}%", "; ".join(x["flags"])])
        lines.append(md_table(["Ticker", "1D", "vs 6M high", "Vol", "Why held back"], crow))
    else:
        lines.append("_None today._")

    lines += ["", "## Full screen (eligible names, by score)", ""]
    def vpct(v):
        return f"{v*100:.0f}%" if v else "n/a"

    show_api = any(x.get("iv_api") for x in with_data)
    show_manual = any(x.get("manual") for x in with_data)
    eheader = ["Ticker", "Theme", "Last", "1D", "vs 6M high", "Vol used", "Vol src"]
    if show_api:
        eheader += ["Straddle IV", "6M skew 80-ATM"]
    if show_manual:
        eheader += ["Manual IV30"]
    eheader += ["RV20", "ATM OI", "Next earnings"]
    erow = []
    for x in eligible:
        r = [x["ticker"], x["bucket"], f"{x['spot']:.2f}", fmt_pct(x["move_1d"], 1, True), fmt_pct(x["drawdown"], 0),
             f"{x['vol']*100:.0f}%", x["vol_src"]]
        if show_api:
            r += [vpct(x.get("iv_nasdaq")), f"{x['skew80']*100:+.0f} pts" if x.get("skew80") is not None else "n/a"]
        if show_manual:
            r += [vpct((x.get("manual") or {}).get("iv30"))]
        r += [f"{x['rv20']*100:.0f}%" if not math.isnan(x["rv20"]) else "n/a",
              f"{x['oi']:,}" if x.get("oi") else "n/a", x.get("earnings") or "n/a"]
        erow.append(r)
    lines.append(md_table(eheader, erow))
    cross = [x for x in with_data if any(f.startswith(("IV sources disagree", "manual IV30")) for f in x["flags"])]
    if cross:
        lines += ["", "**IV cross-check flags** (not blocking; check the chain before RFQ): "
                  + "; ".join(f"{x['ticker']} ({next(f for f in x['flags'] if f.startswith(('IV sources', 'manual IV30')))})" for x in cross)]

    missing = [x["ticker"] for x in analysed if "vol" not in x]
    lines += [
        "",
        "## Before you send an RFQ",
        "",
        "1. Check live spot; never strike off a fresh heavy down day (2-session stabilization rule).",
        "2. Check earnings / FDA / launch dates inside the tenor (`reference/event-calendar.md`) and option expiry quirks (`reference/option-expiry-quirks.md`).",
        "3. Ask for a KI ladder, not a single KI. Choose by coupon pickup per KI point.",
        "4. Compare issuer quotes like-for-like: tenor, KO level/observation, KI level/observation, strike, RO, coupon frequency.",
        "",
        "```text",
        "Please quote a USD worst-of FCN on [TICKERS], 3M and 6M, KO 100% monthly (also 98/102 if available),",
        "fixed monthly coupon, strike 100%, RO 100 (and requested RO). Coupon p.a. across KI 50/55/59/65/70",
        "at maturity, with estimated value, bid/offer and key assumptions.",
        "```",
        "",
        "## Data notes",
        "",
        f"- Names with usable data: {len(with_data)}/{len(watchlist)}; with listed-options read: {len(with_opts)}/{len(watchlist)}.",
        f"- Vol source used: Tradier/ORATS {n_api}, Nasdaq straddle {n_straddle}, realized-vol fallback {n_rv}"
        + (f", manual override {n_manual}" if n_manual else "") + ".",
        "- Tradier/ORATS: " + (
            f"configured, but stopped: {tradier['error']}. Regenerate the token and update the `TRADIER_TOKEN` secret." if tradier.get("error")
            else "configured (15-min delayed sandbox data unless TRADIER_BASE_URL points to production)." if tradier.get("configured")
            else "not configured. Add a `TRADIER_TOKEN` repository secret to use ORATS IV (see `research/data-sources.md`)."),
        *[f"- {note}" for note in (manual_notes or [])],
        f"- Missing today: {', '.join(missing) if missing else 'none'}.",
        f"- Model rate assumption {TERMS.rate*100:.2f}% + {TERMS.funding_spread*100:.2f}% funding; ballpark low end = ATM vol and 1.5% issuer margin, high end = ATM vol +3 pts and 0.75% margin.",
        "- Crypto-linked names are excluded by default.",
        "",
        f"_{LABEL}_",
    ]
    record["names"] = [
        {
            "ticker": x["ticker"], "theme": x["theme"], "bucket": x["bucket"], "status": x["status"],
            "spot": round(x["spot"], 4), "move_1d": round(x["move_1d"], 2), "drawdown": round(x["drawdown"], 2),
            "vol": round(x["vol"], 4), "vol_src": x["vol_src"],
            "iv_api": None if not x.get("iv_api") else round(x["iv_api"], 4),
            "iv_straddle": None if not x.get("iv_nasdaq") else round(x["iv_nasdaq"], 4),
            "skew80": None if x.get("skew80") is None else round(x["skew80"], 4),
            "rv20": None if math.isnan(x["rv20"]) else round(x["rv20"], 4),
            "oi": x.get("oi", 0), "earnings": x.get("earnings"), "entry": x["entry"], "flags": x["flags"],
        }
        for x in with_data
    ]
    return "\n".join(lines) + "\n", record


def update_index(daily: Path, archive: Path) -> None:
    files = sorted(archive.glob("*.md"), reverse=True)[:120]
    rows = [[p.stem, f"[open](archive/{p.name})"] for p in files]
    text = "# FCN Daily Screen Archive\n\n- [Latest](latest.md)\n\n" + md_table(["Run (HKT)", "Report"], rows) + "\n"
    (daily / "index.md").write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", help="Load market data from a JSON file instead of the network")
    parser.add_argument("--save-fixture", help="Save fetched market data to this JSON file")
    parser.add_argument("--out", default=None,
                        help="Output folder (default: daily/, or local/daily/ when a manual IV file is loaded)")
    parser.add_argument("--manual-iv", default=str(MANUAL_IV_PATH),
                        help="Hand-filled IV file for cross-checks (default: iv_inputs/manual_iv.csv; ignored if missing)")
    parser.add_argument("--manual-iv-override", action="store_true",
                        help="Use the manual IV as the model vol (iv_6m if given, else iv30). Local runs only.")
    args = parser.parse_args()

    now_utc = dt.datetime.now(dt.timezone.utc)
    today = now_utc.astimezone(HKT).date()
    manual, manual_notes = load_manual_iv(Path(args.manual_iv), today)
    if args.manual_iv_override and not manual:
        parser.error("--manual-iv-override needs a manual IV file with fresh rows")
    if args.fixture:
        market = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    else:
        market = collect_market(load_watchlist(), today)
        if args.save_fixture:
            Path(args.save_fixture).write_text(json.dumps(market), encoding="utf-8")

    if args.out:
        daily = Path(args.out)
    elif manual:
        # Manual IV usually comes from a site whose terms allow personal display only
        # (e.g. Market Chameleon). Keep reports that contain it out of the public repo.
        daily = LOCAL_OUT
        print(f"Manual IV loaded: writing to {daily} (git-ignored), not daily/.")
    else:
        daily = REPO_ROOT / "daily"
    if manual and daily.resolve() == (REPO_ROOT / "daily").resolve():
        print("WARNING: report contains manual IV and is going to the published daily/ folder. Do not commit it.")
    archive = daily / "archive"
    archive.mkdir(parents=True, exist_ok=True)
    prev_path = daily / "latest.json"
    prev = previous_baskets(prev_path if prev_path.exists() else REPO_ROOT / "daily" / "latest.json")
    report, record = generate(market, now_utc, prev, manual, args.manual_iv_override, manual_notes)
    (daily / "latest.md").write_text(report, encoding="utf-8")
    (daily / "latest.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    (archive / now_utc.astimezone(HKT).strftime("%Y-%m-%d-%H%M-HKT.md")).write_text(report, encoding="utf-8")
    update_index(daily, archive)
    print(f"Report written: status {record['status']}, {len(record['baskets'])} baskets")


if __name__ == "__main__":
    main()
