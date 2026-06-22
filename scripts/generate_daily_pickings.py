#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate an indicative FCN daily picking report.

This script is intentionally dependency-free so it can run on GitHub Actions
without package installation. It uses public Stooq quote CSV data as a rough
screening input. Outputs are indicative only and not firm quotes.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import math
import urllib.parse
import urllib.request
from pathlib import Path


TICKERS = ["MSTR", "COIN", "AMD", "SMCI", "NVDA", "TSLA", "PLTR", "HOOD"]
KI_LADDER = [50, 55, 59, 65, 70]

BASKETS = [
    {
        "rank": 1,
        "basket": ("MSTR", "COIN"),
        "category": "Max coupon",
        "terms": "3M/6M, KO 100 monthly, RFQ KI ladder 50/55/59/65/70",
        "risk": "Concentrated crypto-beta; BTC selloff can hit both names.",
    },
    {
        "rank": 2,
        "basket": ("AMD", "SMCI"),
        "category": "Balanced high coupon",
        "terms": "3M tactical or 6M if client accepts event risk; optimize KI ladder",
        "risk": "SMCI can dominate worst-of downside; financing and jump risk matter.",
    },
    {
        "rank": 3,
        "basket": ("MSTR", "SMCI"),
        "category": "Aggressive alternative",
        "terms": "Prefer 3M; consider lower KI if coupon still works",
        "risk": "Two unstable high-vol names; severe gap and worst-of risk.",
    },
    {
        "rank": 4,
        "basket": ("COIN", "SMCI"),
        "category": "Aggressive alternative",
        "terms": "3M/6M; compare coupon pickup per KI point across ladder",
        "risk": "Crypto regulation plus SMCI financing/event risk.",
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
}


def clean_number(value: str | None) -> str:
    if value is None:
        return ""
    return value.replace("$", "").replace(",", "").replace("%", "").strip()


def fetch_nasdaq_quotes(tickers: list[str]) -> dict[str, dict[str, str]]:
    rows = {}
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.nasdaq.com",
        "Referer": "https://www.nasdaq.com/",
    }
    for ticker in tickers:
        url = f"https://api.nasdaq.com/api/quote/{ticker}/info?assetclass=stocks"
        request = urllib.request.Request(url, headers=headers)
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


def parse_float(value: str) -> float:
    try:
        if value in {"", "N/D", "N/A", "-"}:
            return float("nan")
        return float(value)
    except ValueError:
        return float("nan")


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
    }.get(ticker, "Medium")

    if move is not None and abs(move) >= 7:
        return f"{base}; elevated daily move"
    if move is not None and abs(move) >= 4:
        return f"{base}; active daily move"
    return base


def basket_coupon_direction(basket: tuple[str, str]) -> str:
    names = set(basket)
    if names == {"MSTR", "COIN"}:
        return "Likely highest among core pairs because both names carry crypto-beta and high volatility."
    if names == {"AMD", "SMCI"}:
        return "Likely strong coupon with a clearer AI infrastructure story."
    if names == {"MSTR", "SMCI"}:
        return "Potentially very high, but risk is severe because both names can gap."
    if names == {"COIN", "SMCI"}:
        return "High coupon; avoids MSTR-specific leverage while keeping crypto plus SMCI risk."
    return "High coupon potential depends on current vol, correlation, and issuer assumptions."


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

    basket_rows = [["Rank", "Basket", "Category", "Coupon direction", "Suggested terms", "Key risk", "Action"]]
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
                "RFQ if client prioritizes coupon; validate final terms with issuer.",
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

## Basket Pickings

{md_table(basket_rows)}

## Default Structure For RFQ

- Product: worst-of FCN / autocallable FCN.
- Currency: USD.
- Tenor: compare 3M and 6M first; add 12M only if client accepts longer event risk.
- KO: 100%, monthly observation.
- KI / airbag: request ladder 50 / 55 / 59 / 65 / 70, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment.
- RO: no RO economics unless specifically requested.

## KI Optimization

{md_table(ki_optimization_rows())}

Decision rule: do not choose KI by habit. Compare the coupon pickup against the airbag sacrificed. If the pickup is flat, keep the lower KI. If a higher KI gives a sharply better coupon pickup per KI point, flag that level as the best-value candidate subject to client risk appetite.

## RFQ Wording

```text
Please quote indicative and firm levels for a USD worst-of FCN on [TICKER 1] / [TICKER 2], 3M and 6M tenor, KO 100 monthly, fixed monthly coupon, no RO economics. Please show coupon p.a. across KI 50 / 55 / 59 / 65 / 70 at maturity, plus coupon pickup per KI point, issuer estimated value, bid/offer, assumptions, and early unwind policy.
```

## Client Explanation

English:

> The higher coupon comes from the volatility of the underlyings. This is not a risk-free yield. The investor is compensated for taking worst-of downside risk. If the note does not autocall and the worst-performing stock finishes below the KI level, redemption may be linked to that stock's negative performance.

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
