# Market data sources for FCN screening

What is available, what it costs, and what each source is good for. Compiled 2026-10-12. Limits and prices change, so check the provider's own page before relying on a figure.

> Rule: use only data you are entitled to. Do not bypass paywalls, logins, exchange entitlements or firm controls. Many free tiers are **non-commercial**; using them for client business may need a commercial licence or firm approval.

## What an FCN screen needs

| Input | Why | Best free source | Better (paid / firm) |
|---|---|---|---|
| Spot and price history (6M+) | Drawdown, realized vol, correlation | Nasdaq public API, Yahoo chart, Stooq CSV | Licensed vendor or firm feed |
| Implied vol by expiry (3M/6M) | Coupon driver | Nasdaq option chain (ATM straddle → IV) | IV and greeks from Massive Starter, EODHD, ThetaData, OptionMetrics |
| Skew (25-delta put vs ATM) | Prices the KI put | Derive from the free chain (noisy) | Vendor IV surface; issuer is the real source |
| Option open interest | Hedgeability and liquidity | Nasdaq / Yahoo chains | OPRA-based vendor |
| Earnings and event dates | Event holds | Nasdaq earnings-date endpoint, Finnhub calendar | Vendor or firm calendar |
| USD rates | Discounting and funding | FRED (DGS3MO, SOFR), Treasury.gov yield curve | Firm curve |
| Real coupon levels | Calibration | **SEC EDGAR 424B2 pricing supplements** | Your issuer RFQs (keep private) |

## Free, no key (what the GitHub Action uses now)

| Source | Data | Notes |
|---|---|---|
| Nasdaq public API (`api.nasdaq.com`) | Quotes, daily history, full option chains, earnings date | Unofficial and undocumented; needs browser-like headers and may change without notice. Primary source of `scripts/generate_daily_pickings.py`. |
| Yahoo Finance chart endpoint | Daily history | Unofficial; fallback. The `yfinance` Python package wraps it (and chains). |
| Stooq | Daily OHLC CSV | Final fallback; history only. |
| Treasury.gov | Daily yield curve | Official, no key. |
| Cboe | Daily market statistics, VIX, put/call ratios; [VIX methodology](https://cdn.cboe.com/resources/vix/VIX_Methodology.pdf) | Index-level context. |
| SEC EDGAR | Filings, full-text search | Free; needs a User-Agent with contact details; about 10 requests per second. See below. |

## Free with a key (sign-up)

| Source | Free tier (as published) | Useful for |
|---|---|---|
| FRED | Free key, rate-limited | Rates (3M bill, SOFR), macro series |
| Finnhub | ~60 calls/min; commercial use restricted | Earnings calendar, option chain, news |
| Massive (formerly Polygon.io) Options Basic | $0, 5 calls/min, EOD, 2 years | Options EOD aggregates |
| Alpha Vantage | ~25 calls/day | Quotes, earnings, fundamentals |
| Twelve Data | ~800 calls/day, 8/min | Delayed prices |
| Tradier (sandbox) | Free sandbox | Chains with greeks |
| Alpaca | Free dev tier (IEX subset) | Stock and options data |
| Market Data App | Free tier | Chains and history |

## Low-cost paid (if the desk wants clean IV and greeks)

| Source | Price (as published) | What you get |
|---|---|---|
| Massive Options Starter | ~$29/month | 15-min delayed, IV, greeks, flat files |
| EODHD US Options add-on | ~$29.99/month | EOD chains for 6,000+ US stocks, IV, greeks, OI, 2 years of history |
| ThetaData | from ~$40/month | OPRA NBBO, chains, long history |
| Finnhub paid | from ~$49.99/month | Broader coverage |

## Institutional (through the firm)

OptionMetrics IvyDB (EOD IV surfaces, the academic standard), Cboe DataShop / LiveVol (files with IV and greeks), Databento (tick OPRA), Bloomberg / LSEG / FactSet. If the firm already licenses one, use it first. The repo's data hierarchy (PLAYBOOK §1) puts these above all public sources.

## SEC EDGAR as a public calibration ruler

US banks file a pricing supplement (form **424B2**) for every registered structured note. Many are **worst-of autocallables on single US stocks** (NVDA, TSLA, AMD and others), and each discloses the coupon, barriers, observation schedule and the issuer's **estimated value**. That makes them the best free record of where issuers actually price.

Full-text search endpoint (free, no key):

```text
GET https://efts.sec.gov/LATEST/search-index?q="worst performing" "contingent coupon" NVIDIA&forms=424B2&startdt=2026-09-01&enddt=2026-10-09
Header: User-Agent: fcn-desk-workbench your-name your-email@example.com
```

- The path is case-sensitive (`/LATEST/`). Results are JSON (`hits.hits[]._source` has the filer, form and file date). Stay under about 10 requests per second; going over leads to temporary IP blocks.
- How to use the results: read the coupon, barrier, tenor and estimated value; **normalize the convention** (US notes usually have contingent quarterly coupons, a final barrier and 1–2 year tenors); compare with `fcn_model.py` run on the same terms. Note the gap as calibration evidence, not as a quote for your own structure.
- The [web search UI](https://efts.sec.gov/LATEST/search-index) works too; filter on form 424B2.

## Access from where

| Where | Can reach market APIs? | Notes |
|---|---|---|
| GitHub Actions (this repo's daily screen) | Yes | Nasdaq, Yahoo, Stooq, SEC, FRED all reachable |
| Claude chat sandbox | Usually **no** (network allowlist) | Claude uses web search/fetch for news and reads the daily screen from GitHub |
| Your own PC | Yes | Subject to the firm's network policy |

## Sources

- QuantVPS, [Historical options data: free and paid sources (2026)](https://www.quantvps.com/blog/best-apis-for-historical-options-market-data-volatility)
- Qveris, [Free financial API comparison](https://qveris.ai/guides/free-financial-api-comparison/)
- FlashAlpha, [awesome-options-analytics](https://github.com/FlashAlpha-lab/awesome-options-analytics)
- EODHD, [US stock options API](https://eodhd.com/lp/us-stock-options-api)
- iVolatility, [API docs](https://www.ivolatility.com/api/docs)
- Market Data App, [Options data](https://www.marketdata.app/data/options/)
- Orthogonal, [SEC EDGAR full-text search API (efts)](https://orthogonal.info/sec-edgar-full-text-search-api-efts-python/)
- SEC EDGAR, [example worst-of pricing supplement](https://www.sec.gov/Archives/edgar/data/200245/000191870426004883/form424b2.htm)
