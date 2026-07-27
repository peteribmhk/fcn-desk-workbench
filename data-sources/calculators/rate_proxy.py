#!/usr/bin/env python3
"""
Rate Proxy Calculator
Fetches or estimates risk-free rates and term structure for FCN pricing.
Prefers FRED API, falls back to desk assumptions.
"""
import os
import json
import urllib.request
from datetime import datetime

FRED_API_KEY = os.environ.get("FRED_API_KEY", "")


def fetch_fred_rate(series_id):
    if not FRED_API_KEY:
        return None
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json&sort_order=desc&limit=1"
    req = urllib.request.Request(url, headers={"User-Agent": "FCN-Desk-Workbench/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            obs = data.get("observations", [{}])[0]
            val = obs.get("value")
            return float(val) / 100.0 if val and val != "." else None
    except Exception:
        return None


def get_rate_curve():
    """Get rate curve. Try FRED first, then desk assumptions."""
    sofr = fetch_fred_rate("SOFR")
    d3m = fetch_fred_rate("DGS3MO")
    d6m = fetch_fred_rate("DGS6MO")
    d1y = fetch_fred_rate("DGS1")

    # Desk assumptions (update monthly)
    DESK_ASSUMPTIONS = {
        "SOFR": 0.0525,
        "3M": 0.0535,
        "6M": 0.0540,
        "1Y": 0.0545,
    }

    curve = {
        "SOFR": sofr if sofr is not None else DESK_ASSUMPTIONS["SOFR"],
        "3M": d3m if d3m is not None else DESK_ASSUMPTIONS["3M"],
        "6M": d6m if d6m is not None else DESK_ASSUMPTIONS["6M"],
        "1Y": d1y if d1y is not None else DESK_ASSUMPTIONS["1Y"],
        "source": "fred-api" if FRED_API_KEY else "desk-assumption",
        "timestamp": datetime.now().isoformat(),
        "caveat": "FRED data may be delayed 1 day. Desk assumptions are conservative estimates.",
    }
    return curve


def main():
    print(json.dumps(get_rate_curve(), indent=2))


if __name__ == "__main__":
    main()
