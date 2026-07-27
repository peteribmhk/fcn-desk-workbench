# 06 — Data Policy

**Version:** v1.0.0  
**Last Updated:** 2026-07-27  
**Read Order:** 6th

---

This file defines the market data hierarchy, source discovery protocol, and calculation rules for the FCN Desk Workbench.

## Standing Rule

Use the best legally accessible source available in the current session. Do not limit analysis to free sources when a licensed paid or firm-approved source is connected. Do not attempt to bypass paywalls, credentials, exchange entitlements, or firm market-data controls.

## Priority Order

| Priority | Source type | Best use | FCN desk treatment |
|----------|------------|----------|-------------------|
| 1 | Firm-approved issuer RFQ / pricing system | Actual coupon, RO, KI/KO ladder, issuer basis | Controlling evidence after terms are normalized |
| 2 | Licensed institutional terminal/API, such as Bloomberg, LSEG Workspace, FactSet, or firm market-data platform | Live spot, news, earnings, option surface, borrow/dividend/funding context | Use when licensed and connected; cite source and timestamp |
| 3 | Licensed options market-data API, such as Massive/Polygon Options, Cboe DataShop/LiveVol, OPRA-based vendor, or broker API | Option chain, NBBO, IV, Greeks, open interest, skew, term structure | Stronger screening input than public options pages |
| 4 | Public/free sources currently used by GitHub Actions | Nasdaq public quote, Nasdaq public option chain, Yahoo fallback, Stooq fallback, FRED rates, SEC EDGAR events | Public/delayed screening only; not firm real-time data |
| 5 | General web/news search | Market pulse, earnings narrative, sector sentiment, risk events | Qualitative context only; verify against market data and filings |

## Paid Source Access Boundary

Paid resources are usable only when one of these is true:

- an API key or token is provided through approved secrets or environment variables,
- a licensed terminal/API is connected in the current environment,
- the user manually provides non-confidential numbers from a firm-approved system,
- a broker or vendor API is authorized for the relevant market data and usage.

If none of these is true, the assistant must say that paid data is not connected and fall back to public screening data. It should still scan public web/news for market pulse, but it must not call that a live institutional feed.

## Public Source Discovery Protocol

The workbench maintains an active discovery and health-check system for public data sources. See `data-sources/registry.json` for the current source registry and `data-sources/README.md` for the discovery protocol.

### Source Registry

`data-sources/registry.json` tracks:
- source name and URL/endpoint
- last successful fetch timestamp
- health status: `HEALTHY`, `DEGRADED`, `DOWN`, `DEPRECATED`
- data type: `spot`, `options`, `rates`, `earnings`, `news`
- rate limit and throttling notes
- fallback chain

### Health Check

`.github/workflows/data-source-health-check.yml` runs every 4 hours to:
1. Probe each registered source endpoint.
2. Record response time, HTTP status, and data freshness.
3. Update `data-sources/registry.json` with health status.
4. Alert (via commit message) if a primary source is down and fallback is active.

### Discovery Scan

`scripts/discover-data-sources.py` (runs weekly via GitHub Actions) to:
1. Scan known public data source lists (Nasdaq, Cboe, FRED, SEC, etc.).
2. Check for new endpoints or API versions.
3. Test new sources against a small ticker sample.
4. Propose additions to `data-sources/registry.json` via PR or direct commit.

## Calculation Rules

### Volatility Proxy

From public option chains, compute:

1. **ATM Straddle Proxy**: Find the strike closest to spot. Compute mid-price straddle = call mid + put mid.
2. **Implied Volatility (rough)**: Use Black-Scholes inversion from ATM straddle mid. See `data-sources/calculators/iv_surface.py`.
3. **Term Structure Proxy**: Compare 1M, 3M, 6M ATM straddles if available.
4. **Skew Proxy**: Compare 90% and 110% moneyness straddles versus ATM.

Label all computed vols as "public-options proxy, indicative only."

### Correlation Proxy

For worst-of baskets, public data cannot directly compute issuer correlation assumptions. Use these proxies:

1. **Historical correlation**: 90-day Pearson correlation of daily returns from Yahoo/Stooq.
2. **Sector beta alignment**: if both names are in the same sector, flag higher implicit correlation.
3. **Market stress proxy**: during VIX spikes or sector selloffs, correlation tends toward 1.

See `data-sources/calculators/correlation_proxy.py`.

### Rate Proxy

For discounting and funding assumptions:

1. **SOFR proxy**: Use FRED `SOFR` series for USD risk-free rate.
2. **Term proxy**: Use FRED `DGS3MO`, `DGS6MO`, `DGS1` for approximate term structure.
3. **Spread assumption**: issuer funding spread is not observable publicly; use a conservative desk assumption (e.g., +50-150bp) and label it.

See `data-sources/calculators/rate_proxy.py`.

### FCN Indicative Pricing

The workbench now includes an issuer-mimicry indicative pricing module. See `issuer-mimicry/README.md` for details.

When public data is used for indicative pricing:

1. Use Black-Scholes + autocall adjustment as the base model.
2. Apply issuer-style adjustments: skew markup, correlation haircut, borrow/dividend drag, funding spread.
3. Run Monte Carlo worst-of simulation for basket path dependency.
4. Output a range, not a point estimate.
5. Always label: "Issuer-mimicry indicative range. Not an issuer quote. Calibrate with real RFQ."

## Daily Refresh Requirement

Every FCN Morning Bell should state:

1. which market-data tier was actually used,
2. timestamp and freshness,
3. whether paid/firm data was connected or unavailable,
4. whether issuer RFQ evidence was used,
5. whether issuer-mimicry pricing was calibrated,
6. that public data is screening only and issuer RFQ controls final coupon.

## Source Links

- Massive Options overview: https://massive.com/docs/rest/options/overview
- Cboe DataShop Option EOD Summary: https://datashop.cboe.com/option-eod-summary
- Nasdaq Data Link API page: https://data.nasdaq.com/tools/api
- FRED API: https://fred.stlouisfed.org/docs/api/api_key.html
- SEC EDGAR API: https://www.sec.gov/edgar/sec-api-documentation
