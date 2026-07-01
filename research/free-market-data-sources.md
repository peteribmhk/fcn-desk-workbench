# Free/Public Market Data Source Review

**Status:** Indicative only. This note is for FCN screening workflow design, not firm pricing or client-facing market-data redistribution.

## Practical Ranking For This Workbench

| Rank | Source / Project | Best Use | Limitation |
|---:|---|---|---|
| 1 | Nasdaq public quote endpoint | Free/public US equity spot snapshot, pre-market/market-status text, percent move | Delayed/public; no firm exchange entitlement |
| 2 | Nasdaq public option-chain endpoint | Listed option bid/ask, volume, open interest, ATM straddle proxy by tenor | No direct IV surface; public endpoint can change without notice |
| 3 | Yahoo Finance public chart endpoint / `yfinance` ecosystem | Historical prices, fallback spot data, broad open-source examples | Unofficial; can break or throttle |
| 4 | Stooq daily CSV | Dependency-free daily fallback | End-of-day only; not suitable for intraday RFQ timing |
| 5 | OpenBB | Best open-source research platform if we later accept dependencies/API keys | Too heavy for the current dependency-free GitHub Action |
| 6 | Alpha Vantage / Finnhub / Twelve Data / Massive | Cleaner official API model with free tiers | Usually needs API key; real-time US equities/options may require paid plan or exchange entitlement |
| 7 | Cboe delayed quotes/options pages | Useful official delayed options reference | Cboe CDN/API can reject automated requests; not reliable enough as primary workflow source |

## GitHub Ecosystem Scan

- `ranaroussi/yfinance`: dominant free Yahoo Finance wrapper; very active and widely used.
- `dpguthrie/yahooquery`: useful Yahoo Finance wrapper with broad data access.
- `OpenBB-finance/OpenBB`: largest open-source financial data platform; powerful but heavier than this repo needs today.
- `vollib/py_vollib` and vectorized variants: useful for Black-Scholes implied-vol and Greeks if we later compute IV from option chain mid prices.

## Recommendation

Keep the GitHub Action dependency-free for phone reliability:

1. Use Nasdaq public quote data first.
2. Add Nasdaq public option-chain data as an indicative listed-options vol/liquidity proxy.
3. Keep Yahoo and Stooq as fallbacks.
4. Do not call this "real-time" or "firm"; label as public/delayed.
5. If production-grade live data becomes required, move to an approved vendor or firm market-data system.

## Issuer Pricing Gap

Public data will not replicate UBS, JPM, Marex, Leonteq, or other issuer pricing. The workbench sees public spot and listed-option proxies; issuers price exact autocall terms with their own volatility surface, skew, correlation, dividends, borrow, funding, inventory, credit, margin, settlement, and autocall-path assumptions.

Use public data to screen and prepare sharper RFQs. Use issuer quotes and firm-approved systems to rank real coupon value.

## Next Upgrade Ideas

- Compute rough Black-Scholes implied volatility from ATM option mids using a dependency-free solver.
- Add earnings-date/event-risk data from a key-based provider.
- Store issuer RFQ coupon ladders manually in a private file, then calculate best KI value from real quotes.
