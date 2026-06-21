#!/usr/bin/env python3
"""Generate an indicative FCN daily picking report.

This script is intentionally dependency-free so it can run on GitHub Actions
without package installation. It uses public Stooq quote CSV data as a rough
screening input. Outputs are indicative only and not firm quotes.
"""

from __future__ import annotations

import csv
import datetime as dt
import math
import urllib.parse
import urllib.request
from pathlib import Path


TICKERS = ["MSTR", "COIN", "AMD", "SMCI", "NVDA", "TSLA", "PLTR", "HOOD"]

BASKETS = [
    {
        "rank": 1,
        "basket": ("MSTR", "COIN"),
        "category": "Max coupon",
        "terms": "3M/6M, KO 100 monthly, KI 59 maturity, monthly coupon",
        "risk": "Concentrated crypto-beta; BTC selloff can hit both names.",
    },
    {
        "rank": 2,
        "basket": ("AMD", "SMCI"),
        "category": "Balanced high coupon",
        "terms": "3M tactical or 6M if client accepts event risk; KO 100, KI 59",
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
        "terms": "3M/6M; ask issuer to compare KI 55 vs KI 59",
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


def fetch_stooq_quotes(tickers: list[str]) -> dict[str, dict[str, str]]:
    symbols = ",".join(f"{ticker.lower()}.us" for ticker in tickers)
    query = urllib.parse.urlencode({"s": symbols, "f": "sd2t2ohlcv", "h": "", "e": "csv"})
    url = f"https://stooq.com/q/l/?{query}"

    with urllib.request.urlopen(url, timeout=30) as response:
        text = response.read().decode("utf-8", errors="replace")

    rows = {}
    for row in csv.DictReader(text.splitlines()):
        symbol = row.get("Symbol", "").split(".")[0].upper()
        if symbol:
            rows[symbol] = row
    return rows


def pct_change(close: float, open_: float) -> float | None:
    if not open_ or math.isnan(open_) or math.isnan(close):
        return None
    return (close / open_ - 1.0) * 100.0


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


def generate_report() -> str:
    now_utc = dt.datetime.now(dt.timezone.utc)
    hk_time = now_utc.astimezone(dt.timezone(dt.timedelta(hours=8)))

    try:
        quotes = fetch_stooq_quotes(TICKERS)
        source_note = "Public quote source: Stooq CSV. Data may be delayed or unavailable."
    except Exception as exc:  # noqa: BLE001 - report should still be created
        quotes = {}
        source_note = f"Public quote fetch failed: {exc!r}. Use this report as a template only."

    market_rows = [["Ticker", "Last", "Date/Time", "Daily move", "Volatility read", "Main risk"]]
    for ticker in TICKERS:
        row = quotes.get(ticker, {})
        close = parse_float(row.get("Close", ""))
        open_ = parse_float(row.get("Open", ""))
        move = pct_change(close, open_)
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
- KI / airbag: 59% KI, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment.
- RO: no RO economics unless specifically requested.

## RFQ Wording

```text
Please quote indicative and firm levels for a USD worst-of FCN on [TICKER 1] / [TICKER 2], 3M and 6M tenor, KO 100 monthly, KI 59 at maturity, fixed monthly coupon, no RO economics. Please show coupon p.a., issuer estimated value, bid/offer, assumptions, and early unwind policy.
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

