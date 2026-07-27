#!/usr/bin/env python3
"""
FRED Rate Proxy Fetcher
Fetches SOFR and Treasury yields from FRED API.
Requires FRED_API_KEY as environment variable or falls back to desk assumptions.
"""
import os
import json
import urllib.request
from datetime import datetime

FRED_API_KEY = os.environ.get("FRED_API_KEY", "")
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

SERIES = {
    "SOFR": "SOFR",
    "DGS3MO": "3M Treasury",
    "DGS6MO": "6M Treasury",
    "DGS1": "1Y Treasury",
}


def fetch_series(series_id):
    if not FRED_API_KEY:
        return {"series": series_id, "error": "FRED_API_KEY not set", "fallback": "desk-assumption-rates"}

    url = f"{BASE_URL}?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json&sort_order=desc&limit=1"
    req = urllib.request.Request(url, headers={"User-Agent": "FCN-Desk-Workbench/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            obs = data.get("observations", [{}])[0]
            return {
                "series": series_id,
                "description": SERIES.get(series_id, series_id),
                "value": obs.get("value"),
                "date": obs.get("date"),
                "timestamp": datetime.now().isoformat(),
                "source": "fred-api",
                "caveat": "FRED data. May be delayed 1 business day.",
            }
    except Exception as e:
        return {"series": series_id, "error": str(e), "source": "fred-api", "fallback": "desk-assumption-rates"}


def main():
    for sid in SERIES:
        print(json.dumps(fetch_series(sid), indent=2))


if __name__ == "__main__":
    main()
