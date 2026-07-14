#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate an indicative FCN daily screening report.

This script is intentionally dependency-free so it can run on GitHub Actions
without package installation. It uses public quote and listed-option data as
rough screening inputs only. Outputs are indicative only and not firm quotes.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import math
import urllib.parse
import urllib.request
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WATCHLIST_PATH = REPO_ROOT / "watchlist.csv"
DEFAULT_WATCHLIST = [
    {
        "ticker": "AMD",
        "theme": "AI semiconductors",
        "volatility_role": "Medium-high coupon driver",
        "primary_risks": "AI expectations, valuation, product cycle",
    },
    {
        "ticker": "SMCI",
        "theme": "AI servers",
        "volatility_role": "Very high coupon driver",
        "primary_risks": "Financing/dilution, governance history, order-cycle risk, jump risk",
    },
    {
        "ticker": "NVDA",
        "theme": "AI semiconductors",
        "volatility_role": "Medium-high coupon driver",
        "primary_risks": "AI capex cycle, valuation, export controls",
    },
    {
        "ticker": "TSLA",
        "theme": "EV/AI/robotics",
        "volatility_role": "High coupon driver",
        "primary_risks": "Deliveries, margins, valuation, CEO/event risk",
    },
    {
        "ticker": "PLTR",
        "theme": "AI software",
        "volatility_role": "High coupon driver",
        "primary_risks": "Valuation, AI software sentiment, earnings risk",
    },
]


def load_watchlist() -> list[dict[str, str]]:
    if not WATCHLIST_PATH.exists():
        return DEFAULT_WATCHLIST
    rows: list[dict[str, str]] = []
    with WATCHLIST_PATH.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            ticker = (row.get("ticker") or "").strip().upper()
            if not ticker:
                continue
            cleaned = {key: (value or "").strip() for key, value in row.items()}
            cleaned["ticker"] = ticker
            rows.append(cleaned)
    return rows or DEFAULT_WATCHLIST


WATCHLIST = load_watchlist()
WATCHLIST_BY_TICKER = {row["ticker"]: row for row in WATCHLIST}
TICKERS = list(WATCHLIST_BY_TICKER)
KI_LADDER = [50, 55, 59, 65, 70]
CRYPTO_LINKED_TICKERS = {
    "MSTR",
    "COIN",
    "MARA",
    "RIOT",
    "CLSK",
    "HUT",
    "BTBT",
    "BITF",
    "IREN",
    "WGMI",
}
NASDAQ_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.nasdaq.com",
    "Referer": "https://www.nasdaq.com/",
}

BASKETS = [
    {
        "rank": 1,
        "basket": ("SMCI", "AMD"),
        "category": "RFQ first",
        "terms": "3M/6M, KO 100 monthly, RFQ KI ladder 50/55/59/65/70",
        "risk": "SMCI can dominate worst-of downside; financing, governance, and gap risk matter.",
    },
    {
        "rank": 2,
        "basket": ("PLTR", "TSLA"),
        "category": "Balanced candidate",
        "terms": "3M tactical or 6M if client accepts valuation/event risk; optimize KI ladder",
        "risk": "High-beta momentum pair; earnings, deliveries, valuation, and sentiment can gap.",
    },
    {
        "rank": 3,
        "basket": ("HIMS", "MRNA"),
        "category": "Quote-check candidate",
        "terms": "3M/6M; require issuer availability, liquidity check, and event-risk review",
        "risk": "Healthcare/biotech headlines, trial/regulatory outcomes, and valuation reset risk.",
    },
    {
        "rank": 4,
        "basket": ("IONQ", "RKLB"),
        "category": "Aggressive candidate",
        "terms": "Prefer 3M; use lower KI unless pickup per KI point is compelling",
        "risk": "Speculative emerging-technology pair; funding, execution, and severe gap risk.",
    },
    {
        "rank": 5,
        "basket": ("ENPH", "FSLR"),
        "category": "Balanced candidate",
        "terms": "3M/6M; compare coupon pickup per KI point across ladder",
        "risk": "Rates, policy, demand cycle, and margin risk can dominate the clean-energy story.",
    },
    {
        "rank": 6,
        "basket": ("BABA", "PDD"),
        "category": "Quote-check candidate",
        "terms": "3M/6M; normalize ADR/geopolitical risk and issuer correlation assumptions",
        "risk": "China macro, regulation, geopolitics, and ADR sentiment.",
    },
    {
        "rank": 7,
        "basket": ("SNDK", "AMD"),
        "category": "Quote-check candidate",
        "terms": "Use issuer quote evidence; compare KO 98/100/102 and RO 97/100",
        "risk": "Storage/semiconductor cycle and SanDisk idiosyncratic quote behavior.",
    },
    {
        "rank": 8,
        "basket": ("GOOGL", "NVDA"),
        "category": "Watch only",
        "terms": "RFQ only if client wants familiar names; do not assume high coupon",
        "risk": "Recognizable names may dilute coupon; valuation and AI capex cycle still matter.",
    },
    {
        "rank": 9,
        "basket": ("RIVN", "TSLA"),
        "category": "Aggressive candidate",
        "terms": "Prefer short tenor; require issuer eligibility, lower KI ladder, and event-risk check",
        "risk": "EV delivery, cash burn, production ramp, margins, and sentiment risk.",
    },
    {
        "rank": 10,
        "basket": ("UAL", "TSLA"),
        "category": "Watch only",
        "terms": "Use only to broaden cyclicals; compare against cleaner same-sector alternatives",
        "risk": "Airline macro/fuel/labor risk plus Tesla event risk; mixed-theme explainability.",
    },
]

RISK_TAGS = {ticker: row.get("primary_risks", "Review issuer and event risk") for ticker, row in WATCHLIST_BY_TICKER.items()}


def clean_number(value: str | None) -> str:
    if value is None:
        return ""
    return value.replace("$", "").replace(",", "").replace("%", "").strip()


def parse_float(value: str) -> float:
    try:
        if value in {"", "N/D", "N/A", "-", "--"}:
            return float("nan")
        return float(value)
    except ValueError:
        return float("nan")


def parse_int(value: str | None) -> int:
    number = clean_number(value)
    if number in {"", "N/D", "N/A", "-", "--"}:
        return 0
    try:
        return int(float(number))
    except ValueError:
        return 0


def fetch_nasdaq_quotes(tickers: list[str]) -> dict[str, dict[str, str]]:
    rows = {}
    for ticker in tickers:
        url = f"https://api.nasdaq.com/api/quote/{ticker}/info?assetclass=stocks"
        request = urllib.request.Request(url, headers=NASDAQ_HEADERS)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8", errors="replace"))
        except Exception:
            continue

        data = payload.get("data") or {}
        primary = data.get("primaryData") or {}
        price = clean_number(primary.get("lastSalePrice"))
        if not price:
            continue

        rows[ticker] = {
            "Symbol": ticker,
            "Date": primary.get("lastTradeTimestamp") or "N/A",
            "Time": f"{data.get('marketStatus', 'N/A')} delayed",
            "Open": "",
            "High": "",
            "Low": "",
            "Close": price,
            "Volume": clean_number(primary.get("volume")),
            "PctChange": clean_number(primary.get("percentageChange")),
            "RealTime": str(primary.get("isRealTime", False)),
        }
    if not rows:
        raise RuntimeError("No public quote rows returned from Nasdaq public quote endpoint")
    return rows


def parse_expiry(value: str) -> dt.date | None:
    try:
        return dt.datetime.strptime(value, "%B %d, %Y").date()
    except (TypeError, ValueError):
        return None


def option_mid(bid: float, ask: float) -> float:
    if math.isnan(bid) and math.isnan(ask):
        return float("nan")
    if math.isnan(bid):
        return ask
    if math.isnan(ask):
        return bid
    return (bid + ask) / 2


def format_option_point(point: dict[str, object] | None) -> str:
    if not point:
        return "N/A"
    expiry = point["expiry"]
    strike = point["strike"]
    straddle_pct = point["straddle_pct"]
    return f"{expiry} {strike:.0f} ATM straddle {straddle_pct:.1f}%"


def option_liquidity_read(volume: int, open_interest: int) -> str:
    if open_interest >= 10000 and volume >= 1000:
        return "Deep listed options liquidity"
    if open_interest >= 3000:
        return "Usable listed options liquidity"
    if open_interest > 0:
        return "Thin listed options liquidity"
    return "N/A"


def fetch_nasdaq_option_snapshot(
    tickers: list[str], quotes: dict[str, dict[str, str]], today: dt.date
) -> dict[str, dict[str, str]]:
    snapshots = {}
    targets = {"3M": 90, "6M": 180}
    for ticker in tickers:
        spot = parse_float(quotes.get(ticker, {}).get("Close", ""))
        if math.isnan(spot):
            continue

        query = urllib.parse.urlencode({"assetclass": "stocks", "fromdate": "all", "limit": "10000"})
        url = f"https://api.nasdaq.com/api/quote/{ticker}/option-chain?{query}"
        request = urllib.request.Request(url, headers=NASDAQ_HEADERS)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8", errors="replace"))
        except Exception:
            continue

        table = ((payload.get("data") or {}).get("table") or {})
        raw_rows = table.get("rows") or []
        chain = []
        current_expiry = None
        for raw in raw_rows:
            if raw.get("expirygroup"):
                current_expiry = parse_expiry(raw.get("expirygroup"))
                continue
            strike = parse_float(clean_number(raw.get("strike")))
            if math.isnan(strike) or current_expiry is None:
                continue
            c_bid = parse_float(clean_number(raw.get("c_Bid")))
            c_ask = parse_float(clean_number(raw.get("c_Ask")))
            p_bid = parse_float(clean_number(raw.get("p_Bid")))
            p_ask = parse_float(clean_number(raw.get("p_Ask")))
            call_mid = option_mid(c_bid, c_ask)
            put_mid = option_mid(p_bid, p_ask)
            if math.isnan(call_mid) or math.isnan(put_mid):
                continue
            chain.append(
                {
                    "expiry": current_expiry,
                    "strike": strike,
                    "straddle_pct": ((call_mid + put_mid) / spot) * 100,
                    "volume": parse_int(raw.get("c_Volume")) + parse_int(raw.get("p_Volume")),
                    "open_interest": parse_int(raw.get("c_Openinterest")) + parse_int(raw.get("p_Openinterest")),
                }
            )

        if not chain:
            continue

        ticker_snapshot: dict[str, str] = {}
        total_volume = 0
        total_open_interest = 0
        for label, target_days in targets.items():
            expiries = sorted({row["expiry"] for row in chain if row["expiry"] > today})
            if not expiries:
                continue
            target_expiry = min(expiries, key=lambda expiry: abs((expiry - today).days - target_days))
            expiry_rows = [row for row in chain if row["expiry"] == target_expiry]
            atm = min(expiry_rows, key=lambda row: abs(float(row["strike"]) - spot))
            total_volume += int(atm["volume"])
            total_open_interest += int(atm["open_interest"])
            ticker_snapshot[label] = format_option_point(
                {
                    "expiry": target_expiry.strftime("%b %d"),
                    "strike": float(atm["strike"]),
                    "straddle_pct": float(atm["straddle_pct"]),
                }
            )

        ticker_snapshot["Liquidity"] = option_liquidity_read(total_volume, total_open_interest)
        snapshots[ticker] = ticker_snapshot
    return snapshots


def fetch_yahoo_quotes(tickers: list[str]) -> dict[str, dict[str, str]]:
    rows = {}
    for ticker in tickers:
        query = urllib.parse.urlencode({"range": "5d", "interval": "1d"})
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?{query}"
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8", errors="replace"))

        result = (payload.get("chart", {}).get("result") or [None])[0]
        if not result:
            continue

        timestamps = result.get("timestamp") or []
        quote = ((result.get("indicators", {}).get("quote") or [{}])[0])
        closes = quote.get("close") or []
        opens = quote.get("open") or []

        latest_index = None
        for idx in range(len(closes) - 1, -1, -1):
            if closes[idx] is not None:
                latest_index = idx
                break
        if latest_index is None:
            continue

        price = closes[latest_index]
        open_ = opens[latest_index] if latest_index < len(opens) else None
        timestamp = timestamps[latest_index] if latest_index < len(timestamps) else None
        when = "N/A"
        time_text = "close"
        if timestamp:
            stamp = dt.datetime.fromtimestamp(int(timestamp), tz=dt.timezone.utc)
            when = stamp.strftime("%Y-%m-%d")
            time_text = stamp.strftime("%H:%M UTC")
        volumes = quote.get("volume") or []
        volume = volumes[latest_index] if latest_index < len(volumes) else ""
        rows[ticker] = {
            "Symbol": ticker,
            "Date": when,
            "Time": time_text,
            "Open": "" if open_ is None else str(open_),
            "High": "",
            "Low": "",
            "Close": str(price),
            "Volume": str(volume),
        }
    if not rows:
        raise RuntimeError("No public quote rows returned from Yahoo Finance chart endpoint")
    return rows


def fetch_stooq_quotes(tickers: list[str]) -> dict[str, dict[str, str]]:
    rows = {}
    for ticker in tickers:
        query = urllib.parse.urlencode({"s": f"{ticker.lower()}.us", "i": "d"})
        url = f"https://stooq.com/q/d/l/?{query}"
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                text = response.read().decode("utf-8", errors="replace")
        except Exception:
            continue

        history = list(csv.DictReader(text.splitlines()))
        if not history:
            continue
        latest = history[-1]
        latest["Symbol"] = f"{ticker}.US"
        latest["Time"] = "close"
        rows[ticker] = latest
    if not rows:
        raise RuntimeError("No public quote rows returned from Stooq daily CSV endpoint")
    return rows


def pct_change(close: float, open_: float) -> float | None:
    if not open_ or math.isnan(open_) or math.isnan(close):
        return None
    return (close / open_ - 1.0) * 100.0


def row_pct_change(row: dict[str, str], close: float, open_: float) -> float | None:
    quoted_change = parse_float(row.get("PctChange", ""))
    if not math.isnan(quoted_change):
        return quoted_change
    return pct_change(close, open_)


def watchlist_field(ticker: str, field: str, default: str = "") -> str:
    return WATCHLIST_BY_TICKER.get(ticker, {}).get(field, default) or default


def base_vol_label(ticker: str) -> str:
    role = watchlist_field(ticker, "volatility_role", "Medium")
    for label in ["Very high", "High", "Medium-high", "Medium", "Lower-vol"]:
        if label.lower() in role.lower():
            return label
    return role


def vol_read(ticker: str, move: float | None) -> str:
    base = base_vol_label(ticker)

    if move is not None and abs(move) >= 7:
        return f"{base}; elevated daily move"
    if move is not None and abs(move) >= 4:
        return f"{base}; active daily move"
    return base


def basket_coupon_direction(basket: tuple[str, str]) -> str:
    names = set(basket)
    if names == {"AMD", "SMCI"}:
        return "Screens as an AI-infrastructure candidate, but do not rank coupon value until issuer quotes are normalized."
    if names == {"PLTR", "TSLA"}:
        return "Screens as a liquid high-beta software/EV candidate; actual coupon depends on issuer skew, correlation, and autocall assumptions."
    if names == {"HIMS", "MRNA"}:
        return "Screens as a healthcare/biotech event-risk candidate; verify issuer availability and liquidity before ranking."
    if names == {"IONQ", "RKLB"}:
        return "Screens as an aggressive emerging-tech candidate; use issuer RFQ to confirm whether coupon compensates for severe gap risk."
    if names == {"ENPH", "FSLR"}:
        return "Screens as a clean-energy cyclicality candidate; rates, policy, and margins may drive quote dispersion."
    if names == {"BABA", "PDD"}:
        return "Screens as a China ADR candidate; normalize geopolitical, ADR, and correlation assumptions before comparison."
    if names == {"AMD", "SNDK"}:
        return "Quote-check semiconductor/storage candidate; normalize RO, KO, KI, tenor, strike/reference, and issuer basis before ranking."
    if names == {"GOOGL", "NVDA"}:
        return "Familiar-name anchor candidate; useful for explainability, but public popularity does not guarantee attractive coupon."
    if names == {"RIVN", "TSLA"}:
        return "Aggressive EV candidate; check issuer eligibility, funding risk, and whether lower KI still gives enough coupon."
    if names == {"UAL", "TSLA"}:
        return "Broader cyclicals check; use only if mixed-theme explainability and issuer quote quality are acceptable."

    themes = " / ".join(watchlist_field(ticker, "theme", ticker) for ticker in basket)
    vol_roles = " / ".join(watchlist_field(ticker, "volatility_role", "Review") for ticker in basket)
    return (
        f"RFQ interest depends on current issuer quote evidence for {themes}. "
        f"Public screen roles: {vol_roles}. Normalize RO, KO, KI, strike, tenor, and issuer basis."
    )


def md_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    header = "| " + " | ".join(rows[0]) + " |"
    sep = "| " + " | ".join("---" for _ in rows[0]) + " |"
    body = ["| " + " | ".join(row) + " |" for row in rows[1:]]
    return "\n".join([header, sep, *body])


def ki_optimization_rows() -> list[list[str]]:
    rows = [
        [
            "KI",
            "Airbag",
            "Coupon p.a.",
            "Pickup vs prior KI",
            "Pickup per KI point",
            "Desk decision",
        ]
    ]
    for index, ki in enumerate(KI_LADDER):
        rows.append(
            [
                f"{ki}%",
                f"{100 - ki}%",
                "Issuer RFQ",
                "-" if index == 0 else "Calculate",
                "-" if index == 0 else "Calculate",
                "Base protection"
                if index == 0
                else "Move up only if pickup justifies airbag sacrificed",
            ]
        )
    return rows


def profile_verification_rows(source_note: str, option_source_note: str) -> list[list[str]]:
    crypto_hits = sorted(set(TICKERS) & CRYPTO_LINKED_TICKERS)
    rows = [
        ["Gate", "Status", "Verification", "Required behavior"],
        [
            "User preference",
            "PASS" if not crypto_hits else "BLOCKED",
            "Crypto-linked tickers excluded" if not crypto_hits else f"Crypto-linked tickers found: {', '.join(crypto_hits)}",
            "Do not suggest crypto baskets unless the user explicitly opts in.",
        ],
        [
            "Evidence quality",
            "PASS",
            "Public quote and option-chain inputs are marked as delayed/public screening data.",
            "Never present public data as firm real-time market data or issuer pricing.",
        ],
        [
            "Paid-source access",
            "PASS",
            "No licensed paid or firm-approved feed is connected in this dependency-free GitHub Action run.",
            "Use paid/firm data first when authorized; otherwise state public fallback and do not bypass paywalls or exchange entitlements.",
        ],
        [
            "Issuer quote override",
            "PASS",
            "Report states that issuer RFQs override public-data screens.",
            "Use real issuer/pricing-system quotes as controlling evidence once terms are normalized.",
        ],
        [
            "Structure normalization",
            "PASS",
            "RFQ wording asks for tenor, KO, KI, strike/reference, RO, coupon frequency, issuer assumptions, and bid/offer.",
            "Do not compare headline coupon unless RO/KO/KI/tenor/strike/frequency/issuer basis match.",
        ],
        [
            "KI value discipline",
            "PASS",
            "KI ladder 50 / 55 / 59 / 65 / 70 is required.",
            "Choose the KI where incremental coupon pickup compensates for airbag sacrificed.",
        ],
        [
            "Ticker repeat discipline",
            "PASS",
            "Requote rationale check is required before repeating a ticker or basket.",
            "Classify repeat ideas as same rationale, changed inputs, structural mismatch, or calibration drift.",
        ],
        [
            "Current data source",
            "PASS" if "failed" not in source_note.lower() else "AMBER",
            source_note,
            "If quote refresh fails, treat the report as a template and do not provide data-driven picks.",
        ],
        [
            "Options proxy source",
            "PASS" if "failed" not in option_source_note.lower() else "AMBER",
            option_source_note,
            "Use listed-options proxy only to prioritize RFQs, not to predict actual FCN coupons.",
        ],
    ]
    return rows


def generate_report(now_utc: dt.datetime | None = None) -> str:
    if now_utc is None:
        now_utc = dt.datetime.now(dt.timezone.utc)
    hk_time = now_utc.astimezone(dt.timezone(dt.timedelta(hours=8)))

    try:
        quotes = fetch_nasdaq_quotes(TICKERS)
        source_note = "Public quote source: Nasdaq public quote endpoint. Data is delayed/public and not a firm exchange feed."
    except Exception as nasdaq_exc:  # noqa: BLE001 - report should still be created
        try:
            quotes = fetch_yahoo_quotes(TICKERS)
            source_note = "Public quote source: Yahoo Finance public chart endpoint fallback. Data may be delayed or unavailable."
        except Exception as yahoo_exc:  # noqa: BLE001 - report should still be created
            try:
                quotes = fetch_stooq_quotes(TICKERS)
                source_note = "Public quote source: Stooq daily CSV fallback. Data may be delayed or unavailable."
            except Exception as stooq_exc:  # noqa: BLE001 - report should still be created
                quotes = {}
                source_note = (
                    "Public quote fetch failed: "
                    f"nasdaq={nasdaq_exc!r}; yahoo={yahoo_exc!r}; stooq={stooq_exc!r}. "
                    "Use this report as a template only."
                )

    market_rows = [["Ticker", "Last", "Date/Time", "Daily move", "Volatility read", "Main risk"]]
    for ticker in TICKERS:
        row = quotes.get(ticker, {})
        close = parse_float(row.get("Close", ""))
        open_ = parse_float(row.get("Open", ""))
        move = row_pct_change(row, close, open_)
        last = "N/A" if math.isnan(close) else f"{close:.2f}"
        when = "N/A"
        if row:
            when = f"{row.get('Date', 'N/A')} {row.get('Time', '')}".strip()
        move_text = "N/A" if move is None else f"{move:+.2f}%"
        market_rows.append(
            [
                ticker,
                last,
                when,
                move_text,
                vol_read(ticker, move),
                RISK_TAGS.get(ticker, "Review issuer and event risk"),
            ]
        )

    option_source_note = "Nasdaq public option-chain endpoint. Listed option data is delayed/public and used only as an indicative vol/liquidity proxy."
    option_rows = [["Ticker", "3M ATM straddle proxy", "6M ATM straddle proxy", "Listed options liquidity"]]
    try:
        option_snapshot = fetch_nasdaq_option_snapshot(TICKERS, quotes, hk_time.date())
    except Exception as option_exc:  # noqa: BLE001 - report should still be created
        option_snapshot = {}
        option_source_note = f"Option-chain fetch failed: {option_exc!r}."
    for ticker in TICKERS:
        snapshot = option_snapshot.get(ticker, {})
        option_rows.append(
            [
                ticker,
                snapshot.get("3M", "N/A"),
                snapshot.get("6M", "N/A"),
                snapshot.get("Liquidity", "N/A"),
            ]
        )

    basket_rows = [["Rank", "Basket", "Category", "Screening read", "Suggested terms", "Key risk", "Action"]]
    for basket in BASKETS:
        names = basket["basket"]
        basket_rows.append(
            [
                str(basket["rank"]),
                " / ".join(names),
                basket["category"],
                basket_coupon_direction(names),
                basket["terms"],
                basket["risk"],
                "Request/compare issuer RFQ; do not rank by public screen alone.",
            ]
        )

    report_date = hk_time.strftime("%Y-%m-%d")
    return f"""# FCN Daily Report

**Report date:** {report_date}
**Generated:** {hk_time.strftime('%Y-%m-%d %H:%M')} HKT / {now_utc.strftime('%Y-%m-%d %H:%M')} UTC
**Status:** Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
**Data-access tier:** Public/free GitHub Action fallback. Use licensed paid or firm-approved data first when it is connected and authorized; do not bypass paywalls, credentials, exchange entitlements, or firm data controls.
**Source caveat:** {source_note}
**Universe policy:** Crypto-linked tickers are excluded by default. This report screens a diversified non-crypto watchlist across technology, healthcare/biotech, EV, clean energy, China ADRs, cyclicals, and other high-volatility sectors.

## Profile Verification Gate

This gate must pass before using the report for ticker suggestions or basket combinations.

{md_table(profile_verification_rows(source_note, option_source_note))}

## Market Snapshot

{md_table(market_rows)}

## Listed Options Vol Proxy

**Source caveat:** {option_source_note}

{md_table(option_rows)}

Use this section to judge relative listed-option richness and liquidity only. It is not an issuer FCN coupon, not a volatility surface, not an autocall model, and not enough to predict which basket will have the best actual coupon.

## Issuer Quote Calibration

Real issuer RFQs override this public-data screen. If a real quote from UBS, JPM, Marex, Leonteq, or another issuer contradicts the basket ranking, use the real quote as current calibration evidence and ask what drove the difference: RO, KO, KI, strike/reference, skew, correlation, borrow, dividends, funding, issuer inventory, margin, or exact autocall assumptions.

The public screen is not expected to match issuer pricing. Issuers use their own spot/reference timing, vol surface, skew, correlation, forward/dividend, borrow, funding, credit, inventory, margin, settlement, and autocall-path assumptions. Use this report to ask better RFQs and normalize quotes, not to replace a bank pricer.

For rough comparison when RO differs:

```text
Approx annualized RO accretion = ((100 - RO) / RO) * (12 / tenor_months)
Approx annualized gross carry = coupon p.a. + annualized RO accretion
```

Example: for a 3M note at RO 97, the rough annualized RO accretion is about 12.4% before considering path risk, autocall timing, issuer bid/offer, and downside redemption risk. Keep headline coupon and RO accretion separate in client discussion.

## Requote Rationale Check

Before repeating any ticker or basket from a previous report or chat, classify it as fresh, repeat/same rationale, repeat/changed inputs, structural mismatch, or calibration drift. Cross-check today's spot/reference, 3M/6M listed-options proxy, liquidity, event risk, tenor, KI, KO, strike/reference, RO, coupon frequency, issuer basis, and prior calibration note.

Use `templates/requote-checklist.md` for the full comparison. Do not store actual issuer quotes, issuer names, client details, or firm-confidential pricing assumptions in this public repo.

## Screening Baskets

{md_table(basket_rows)}

## Default Structure For RFQ

- Product: worst-of FCN / autocallable FCN.
- Currency: USD.
- Tenor: compare 3M and 6M first; add 12M only if client accepts longer event risk.
- KO: 100%, monthly observation.
- KI / airbag: request ladder 50 / 55 / 59 / 65 / 70, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment.
- RO: compare RO 100 and requested RO, such as RO 97, separately; do not compare headline coupon alone.

## KI Optimization

{md_table(ki_optimization_rows())}

Decision rule: do not choose KI by habit. Compare the coupon pickup against the airbag sacrificed. If the pickup is flat, keep the lower KI. If a higher KI gives a sharply better coupon pickup per KI point, flag that level as the best-value candidate subject to client risk appetite.

## RFQ Wording

```text
Please quote indicative and firm levels for a USD worst-of FCN on [TICKER 1] / [TICKER 2], 3M and 6M tenor, KO 98 / 100 / 102 monthly, fixed monthly coupon. Please show both RO 100 and requested RO levels where available. Please show coupon p.a. across KI 50 / 55 / 59 / 65 / 70 at maturity, plus coupon pickup per KI point, issuer estimated value, bid/offer, assumptions, and early unwind policy.
```

## Client Explanation

English:

> The coupon is set by issuer pricing for the exact terms, including underlyings, tenor, RO, KO, KI, strike/reference level, volatility, skew, correlation, dividends, borrow, funding, and issuer margin. It is not a risk-free yield. The investor is compensated for taking worst-of downside risk. If the note does not autocall and the worst-performing stock finishes below the KI level, redemption may be linked to that stock's negative performance.

中文:

> 较高票息来自相关股票较高的波动率，并不是无风险收益。投资者收取票息的同时，也承担最差表现股票的下行风险。如果产品没有提前赎回，并且到期时最差表现股票低于 KI 水平，本金赎回可能会跟随该股票的下跌表现。

## Phone Workflow

Open this file on your phone:

```text
https://github.com/peteribmhk/fcn-desk-workbench/blob/main/daily/latest.md
```

Then ask ChatGPT mobile to use this report together with `methodology.md` and `watchlist.csv` for follow-up RFQ or client-explanation drafting.

For refresh memory, also open:

```text
https://github.com/peteribmhk/fcn-desk-workbench/blob/main/daily/index.md
```
"""


def update_daily_index(output_dir: Path, archive_dir: Path) -> None:
    archive_files = sorted(archive_dir.glob("*.md"), reverse=True)
    rows = ["| Refresh timestamp | Report |", "|---|---|"]
    for path in archive_files[:120]:
        label = path.stem.replace("-", " ")
        rows.append(f"| {label} | [archive/{path.name}](archive/{path.name}) |")

    if len(rows) == 2:
        rows.append("| No archived refreshes yet | - |")

    index = f"""# FCN Daily Report Archive

**Status:** Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.

Use this page as the persistent refresh memory for the FCN Desk Workbench. Before suggesting tickers or basket combinations, read `latest.md`, this archive index, and the relevant recent archived reports so repeated ideas can be checked against prior rationale.

## Latest Report

- [latest.md](latest.md)

## Archived Refreshes

{chr(10).join(rows)}

## Memory Rule

Every refresh should commit both the latest report and a timestamped archive file to GitHub. If a future assistant cannot read this index or the latest report, it should mark the FCN Morning Bell status `AMBER` or `RED` rather than giving confident picks.
"""
    (output_dir / "index.md").write_text(index, encoding="utf-8")


def main() -> None:
    now_utc = dt.datetime.now(dt.timezone.utc)
    hk_time = now_utc.astimezone(dt.timezone(dt.timedelta(hours=8)))
    output_dir = REPO_ROOT / "daily"
    output_dir.mkdir(exist_ok=True)
    archive_dir = output_dir / "archive"
    archive_dir.mkdir(exist_ok=True)
    report = generate_report(now_utc)
    (output_dir / "latest.md").write_text(report, encoding="utf-8")
    archive_name = hk_time.strftime("%Y-%m-%d-%H%M-HKT.md")
    (archive_dir / archive_name).write_text(report, encoding="utf-8")
    update_daily_index(output_dir, archive_dir)


if __name__ == "__main__":
    main()
