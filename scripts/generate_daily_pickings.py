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


TICKERS = ["MSTR", "COIN", "AMD", "SMCI", "NVDA", "TSLA", "PLTR", "HOOD", "SNDK", "GOOGL"]
KI_LADDER = [50, 55, 59, 65, 70]
NASDAQ_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.nasdaq.com",
    "Referer": "https://www.nasdaq.com/",
}

BASKETS = [
    {
        "rank": 1,
        "basket": ("MSTR", "COIN"),
        "category": "RFQ first",
        "terms": "3M/6M, KO 100 monthly, RFQ KI ladder 50/55/59/65/70",
        "risk": "Concentrated crypto-beta; BTC selloff can hit both names.",
    },
    {
        "rank": 2,
        "basket": ("AMD", "SMCI"),
        "category": "Balanced candidate",
        "terms": "3M tactical or 6M if client accepts event risk; optimize KI ladder",
        "risk": "SMCI can dominate worst-of downside; financing and jump risk matter.",
    },
    {
        "rank": 3,
        "basket": ("MSTR", "SMCI"),
        "category": "Aggressive candidate",
        "terms": "Prefer 3M; consider lower KI if coupon still works",
        "risk": "Two unstable high-vol names; severe gap and worst-of risk.",
    },
    {
        "rank": 4,
        "basket": ("COIN", "SMCI"),
        "category": "Aggressive candidate",
        "terms": "3M/6M; compare coupon pickup per KI point across ladder",
        "risk": "Crypto regulation plus SMCI financing/event risk.",
    },
    {
        "rank": 5,
        "basket": ("SNDK", "GOOGL"),
        "category": "Quote-check candidate",
        "terms": "Use issuer quote evidence; compare KO 98/100/102 and RO 97/100",
        "risk": "SanDisk idiosyncratic risk plus lower-vol mega-cap anchor; quote may be issuer-specific.",
    },
    {
        "rank": 6,
        "basket": ("AMD", "SNDK"),
        "category": "Quote-check candidate",
        "terms": "Use issuer quote evidence; normalize RO, KO, KI, and strike before ranking",
        "risk": "Semiconductor/event risk; SanDisk quote behavior may diverge from public vol screen.",
    },
    {
        "rank": 7,
        "basket": ("GOOGL", "AMD"),
        "category": "Watch only",
        "terms": "RFQ only if client wants familiar names; do not assume high coupon",
        "risk": "Lower actual coupon possible despite recognizable names; quote must drive decision.",
    },
]

RISK_TAGS = {
    "MSTR": "BTC beta, leverage, gap risk",
    "COIN": "Crypto flow, regulation, BTC/ETH sentiment",
    "AMD": "AI expectations, valuation, product cycle",
    "SMCI": "Financing/dilution, order-cycle risk, jump risk",
    "NVDA": "AI capex cycle, valuation, export controls",
    "TSLA": "Deliveries, margins, CEO/event risk",
    "PLTR": "Valuation, AI software sentiment, earnings risk",
    "HOOD": "Retail activity, crypto revenue, regulation",
    "SNDK": "Storage cycle, post-separation history, idiosyncratic gap risk",
    "GOOGL": "AI/search capex, antitrust, ad-cycle and mega-cap valuation risk",
}


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


def vol_read(ticker: str, move: float | None) -> str:
    base = {
        "MSTR": "Very high",
        "SMCI": "Very high",
        "COIN": "High",
        "TSLA": "High",
        "PLTR": "High",
        "HOOD": "High",
        "AMD": "Medium-high",
        "NVDA": "Medium-high",
        "SNDK": "High",
        "GOOGL": "Medium",
    }.get(ticker, "Medium")

    if move is not None and abs(move) >= 7:
        return f"{base}; elevated daily move"
    if move is not None and abs(move) >= 4:
        return f"{base}; active daily move"
    return base


def basket_coupon_direction(basket: tuple[str, str]) -> str:
    names = set(basket)
    if names == {"MSTR", "COIN"}:
        return "Screens for RFQ because both names carry crypto-beta and high volatility; actual coupon must come from issuer levels."
    if names == {"AMD", "SMCI"}:
        return "Screens as an AI-infrastructure candidate, but do not rank coupon value until issuer quotes are normalized."
    if names == {"MSTR", "SMCI"}:
        return "Screens as aggressive due to jump risk; use only after issuer RFQ confirms compensation."
    if names == {"COIN", "SMCI"}:
        return "Screens as aggressive; actual value depends on issuer correlation, skew, and hedge assumptions."
    if names == {"SNDK", "GOOGL"}:
        return "User quote evidence shows this can price strongly; treat issuer quote as calibration, not public-screen output."
    if names == {"AMD", "SNDK"}:
        return "User quote evidence suggests headline coupon is not enough; normalize RO 97, KO 102, KI 58, and strike terms."
    if names == {"GOOGL", "AMD"}:
        return "User quote evidence shows this may price weakly; avoid assuming popular names produce attractive coupon."
    return "RFQ interest depends on current issuer quote evidence after normalizing RO, KO, KI, strike, and tenor."


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


def generate_report() -> str:
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
        market_rows.append([ticker, last, when, move_text, vol_read(ticker, move), RISK_TAGS[ticker]])

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
**Source caveat:** {source_note}

## Market Snapshot

{md_table(market_rows)}

## Listed Options Vol Proxy

**Source caveat:** {option_source_note}

{md_table(option_rows)}

Use this section to judge relative listed-option richness and liquidity only. It is not an issuer FCN coupon, not a volatility surface, not an autocall model, and not enough to predict which basket will have the best actual coupon.

## Issuer Quote Calibration

Real issuer RFQs override this public-data screen. If a real quote contradicts the basket ranking, use the real quote as current calibration evidence and ask what drove the difference: RO, KO, KI, strike/reference, skew, correlation, borrow, dividends, funding, issuer inventory, or margin.

For rough comparison when RO differs:

```text
Approx annualized RO accretion = ((100 - RO) / RO) * (12 / tenor_months)
Approx annualized gross carry = coupon p.a. + annualized RO accretion
```

Example: for a 3M note at RO 97, the rough annualized RO accretion is about 12.4% before considering path risk, autocall timing, issuer bid/offer, and downside redemption risk. Keep headline coupon and RO accretion separate in client discussion.

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
"""


def main() -> None:
    output_dir = Path("daily")
    output_dir.mkdir(exist_ok=True)
    report = generate_report()
    (output_dir / "latest.md").write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
