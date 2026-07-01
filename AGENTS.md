# AI Continuity Rules

Use this file as the first handoff note for any AI assistant working in this repository.

## Source Of Truth

- Treat GitHub as the persistent source of truth for this workbench.
- When you improve the workflow, instructions, templates, or generator, update the repository files rather than leaving the improvement only in chat.
- Keep `daily/latest.md` phone-readable and public-safe.

## User Preference

- Crypto-linked ideas are excluded by default. Do not suggest MSTR, COIN, BTC miners, crypto exchanges, or crypto-beta baskets unless the user explicitly asks to opt in.
- Build a diversified FCN screening universe across AI/semis, software, EV, healthcare/biotech, emerging technology, clean energy, China ADRs, cyclicals, and other high-volatility sectors.
- Treat all output as RFQ screening, not firm pricing or investment advice.

## Profile Verification Gate

Run this gate before every daily refresh, ticker suggestion, basket combination, or client-facing draft:

1. Confirm crypto-linked names are excluded unless the user explicitly opts in.
2. Confirm public/free data is only a screening input, not firm real-time data or issuer pricing.
3. Confirm issuer RFQ or firm pricing-system evidence overrides public-data rankings once terms are normalized.
4. Confirm comparisons normalize tenor, strike/reference, KI, KI observation, KO, KO observation, RO/issue price, coupon frequency, issuer, bid/offer basis, dividends, borrow, funding, correlation, skew, and autocall assumptions.
5. Confirm KI is optimized by coupon pickup per KI point of airbag sacrificed, not by mechanically choosing the lowest KI.
6. Confirm repeat tickers/baskets are checked against prior rationale and classified as fresh, same rationale, changed inputs, structural mismatch, or calibration drift.
7. If any gate fails, say `AMBER` or `BLOCKED` and explain the shortest next action instead of giving confident picks.

## Pricing Discipline

- Public spot and listed-option data are screening inputs only.
- Issuer RFQ levels from UBS, JPM, Marex, Leonteq, or any other issuer override public-data ranking once terms are normalized.
- Before comparing coupon levels, normalize tenor, strike/reference, KI level, KI observation, KO level, KO observation, RO/issue price, coupon frequency, issuer, bid/offer basis, dividends, borrow, funding, correlation, skew, and autocall assumptions.
- Do not store actual issuer quotes, client details, suitability records, or firm-confidential pricing assumptions in this public repo.

## Requote Rule

Before repeating a ticker or basket on a later day:

- Check `daily/latest.md`, `methodology.md`, `watchlist.csv`, `templates/quote-calibration.md`, and `templates/requote-checklist.md`.
- State whether the idea is fresh, repeated with the same rationale, repeated with changed market inputs, or structurally different.
- Compare today's spot, listed-options proxy, liquidity, event risk, and requested structure against the previous rationale.
- If the user provides private pricing-system numbers, use them for session calibration, but keep actual quote records in ignored/private storage such as `actual-quotes/`.

## Required Label

Every FCN output must say:

> Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
