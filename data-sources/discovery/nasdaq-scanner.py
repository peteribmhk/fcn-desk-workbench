#!/usr/bin/env python3
"""
Nasdaq Public Quote & Option Chain Scanner
Fetches spot data and ATM option straddle proxy from Nasdaq public endpoints.
No API key required. Delayed/public data only.
"""
import json
import urllib.request
import urllib.error
from datetime import datetime

HEADERS = {"User-Agent": "FCN-Desk-Workbench/1.0 (peteribmhk)"}


def fetch_quote(ticker):
    """Fetch spot quote from Nasdaq public API."""
    url = f"https://api.nasdaq.com/api/quote/{ticker}/info?assetclass=stocks"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            body = data.get("data", {})
            return {
                "ticker": ticker,
                "spot": body.get("primaryData", {}).get("lastSalePrice"),
                "change_pct": body.get("primaryData", {}).get("percentageChange"),
                "bid": body.get("primaryData", {}).get("bidPrice"),
                "ask": body.get("primaryData", {}).get("askPrice"),
                "volume": body.get("primaryData", {}).get("volume"),
                "market_status": body.get("marketStatus"),
                "timestamp": datetime.now().isoformat(),
                "source": "nasdaq-public-quote",
                "caveat": "Delayed/public. Not firm real-time.",
            }
    except Exception as e:
        return {"ticker": ticker, "error": str(e), "source": "nasdaq-public-quote"}


def fetch_option_chain(ticker):
    """Fetch option chain and compute ATM straddle proxy."""
    url = f"https://api.nasdaq.com/api/quote/{ticker}/option-chain"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            body = data.get("data", {})
            tables = body.get("table", {}).get("rows", [])
            if not tables:
                return {"ticker": ticker, "error": "No option data", "source": "nasdaq-public-options"}

            # Find ATM strike (closest to spot)
            spot = body.get("lastTrade", 0)
            atm_row = min(tables, key=lambda r: abs(float(r.get("strike", 0)) - spot))
            strike = atm_row.get("strike")
            call_mid = _mid(atm_row.get("c_Last", "0"), atm_row.get("c_Bid", "0"), atm_row.get("c_Ask", "0"))
            put_mid = _mid(atm_row.get("p_Last", "0"), atm_row.get("p_Bid", "0"), atm_row.get("p_Ask", "0"))
            straddle = call_mid + put_mid

            return {
                "ticker": ticker,
                "spot": spot,
                "atm_strike": strike,
                "expiry": atm_row.get("expirygroup"),
                "call_mid": call_mid,
                "put_mid": put_mid,
                "straddle_mid": straddle,
                "call_oi": atm_row.get("c_Openinterest"),
                "put_oi": atm_row.get("p_Openinterest"),
                "timestamp": datetime.now().isoformat(),
                "source": "nasdaq-public-options",
                "caveat": "Public option chain. ATM straddle proxy only. Not IV surface.",
            }
    except Exception as e:
        return {"ticker": ticker, "error": str(e), "source": "nasdaq-public-options"}


def _mid(last, bid, ask):
    """Compute mid price. Fallback to last if bid/ask unavailable."""
    try:
        b, a = float(bid), float(ask)
        if b > 0 and a > b:
            return round((b + a) / 2, 4)
    except (ValueError, TypeError):
        pass
    try:
        return float(last)
    except (ValueError, TypeError):
        return 0.0


def main():
    import sys
    tickers = sys.argv[1:] if len(sys.argv) > 1 else ["AAPL", "TSLA", "NVDA"]
    for t in tickers:
        print(json.dumps(fetch_quote(t), indent=2))
        print(json.dumps(fetch_option_chain(t), indent=2))


if __name__ == "__main__":
    main()
