#!/usr/bin/env python3
"""
Yahoo Finance Fallback Fetcher
Used when Nasdaq public endpoints are down or rate-limited.
Unofficial endpoint — can break or throttle without notice.
"""
import json
import urllib.request
from datetime import datetime

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; FCN-Desk-Workbench/1.0)"}


def fetch_chart(ticker):
    """Fetch historical prices and latest spot from Yahoo chart endpoint."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1mo"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            result = data.get("chart", {}).get("result", [{}])[0]
            meta = result.get("meta", {})
            timestamps = result.get("timestamp", [])
            closes = result.get("indicators", {}).get("quote", [{}])[0].get("close", [])

            if not timestamps or not closes:
                return {"ticker": ticker, "error": "No data", "source": "yahoo-chart"}

            latest_close = closes[-1]
            prev_close = closes[-2] if len(closes) > 1 else latest_close
            change_pct = round((latest_close - prev_close) / prev_close * 100, 2) if prev_close else None

            return {
                "ticker": ticker,
                "spot": latest_close,
                "prev_close": prev_close,
                "change_pct": change_pct,
                "currency": meta.get("currency"),
                "exchange": meta.get("exchangeName"),
                "timestamp": datetime.now().isoformat(),
                "source": "yahoo-chart",
                "caveat": "Unofficial endpoint. Delayed. Can break without notice.",
            }
    except Exception as e:
        return {"ticker": ticker, "error": str(e), "source": "yahoo-chart"}


def main():
    import sys
    tickers = sys.argv[1:] if len(sys.argv) > 1 else ["AAPL"]
    for t in tickers:
        print(json.dumps(fetch_chart(t), indent=2))


if __name__ == "__main__":
    main()
