#!/usr/bin/env python3
"""
Correlation Proxy Calculator
Computes historical Pearson correlation from Yahoo/Stooq daily returns.
Used as a proxy for worst-of basket correlation in FCN screening.
"""
import json
import urllib.request
import math
from datetime import datetime

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; FCN-Desk-Workbench/1.0)"}


def fetch_returns(ticker, days=90):
    """Fetch daily closes and compute daily returns."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=6mo"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            result = data.get("chart", {}).get("result", [{}])[0]
            closes = result.get("indicators", {}).get("quote", [{}])[0].get("close", [])
            closes = [c for c in closes if c is not None]
            if len(closes) < days + 1:
                return None
            recent = closes[-(days + 1):]
            returns = [(recent[i] - recent[i-1]) / recent[i-1] for i in range(1, len(recent))]
            return returns
    except Exception:
        return None


def pearson_correlation(x, y):
    """Compute Pearson correlation coefficient."""
    n = len(x)
    if n != len(y) or n < 2:
        return None
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    den_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
    if den_x == 0 or den_y == 0:
        return None
    return num / (den_x * den_y)


def compute_correlation(ticker_a, ticker_b, days=90):
    """Compute historical correlation proxy for two tickers."""
    ret_a = fetch_returns(ticker_a, days)
    ret_b = fetch_returns(ticker_b, days)
    if ret_a is None or ret_b is None:
        return {
            "ticker_a": ticker_a,
            "ticker_b": ticker_b,
            "correlation": None,
            "status": "FAILED",
            "caveat": "Could not fetch sufficient historical data.",
        }

    # Align lengths
    min_len = min(len(ret_a), len(ret_b))
    ret_a = ret_a[-min_len:]
    ret_b = ret_b[-min_len:]

    corr = pearson_correlation(ret_a, ret_b)
    return {
        "ticker_a": ticker_a,
        "ticker_b": ticker_b,
        "correlation": round(corr, 4) if corr is not None else None,
        "lookback_days": min_len,
        "status": "OK" if corr is not None else "FAILED",
        "caveat": "Historical Pearson correlation from public daily returns. Not issuer implied correlation. Tends to 1 in stress.",
        "timestamp": datetime.now().isoformat(),
    }


def main():
    import sys
    if len(sys.argv) >= 3:
        a, b = sys.argv[1], sys.argv[2]
    else:
        a, b = "AAPL", "MSFT"
    print(json.dumps(compute_correlation(a, b), indent=2))


if __name__ == "__main__":
    main()
