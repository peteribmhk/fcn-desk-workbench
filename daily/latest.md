# FCN Daily Report

**Report date:** 2026-06-27
**Generated:** 2026-06-27 10:14 HKT / 2026-06-27 02:14 UTC
**Status:** Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.  
**Source caveat:** Policy refresh only. Public market data was not refreshed in the local sandbox. Trigger the GitHub Actions workflow to overwrite this file with the latest public quote and listed-options proxy data.
**Universe policy:** Crypto-linked tickers are excluded by default. This report uses the diversified non-crypto watchlist.

## Market Snapshot

Current public quotes were not fetched in this local update. Use the GitHub Actions refresh before relying on spot, move, or listed-options proxy fields.

| Ticker | Theme | Volatility role | Main risk |
| --- | --- | --- | --- |
| AMD | AI semiconductors | Medium-high coupon driver | AI expectations, valuation, product cycle, competition with NVDA |
| SMCI | AI servers | Very high coupon driver | Financing/dilution, governance history, order-cycle risk, jump risk |
| NVDA | AI semiconductors | Medium-high coupon driver | AI capex cycle, valuation, export controls, crowded positioning |
| TSLA | EV/AI/robotics | High coupon driver | Deliveries, margins, valuation, CEO/event risk, China exposure |
| PLTR | AI software | High coupon driver | Valuation, government/commercial growth, sentiment, earnings risk |
| SNDK | Storage/semiconductors | Quote-check coupon driver | Storage cycle, post-separation trading history, idiosyncratic gap risk |
| GOOGL | Mega-cap AI/search | Lower-vol anchor | AI capex, search/ads cycle, antitrust, valuation |
| HIMS | Digital health | High coupon driver | Valuation, regulation, telehealth growth, product headline risk |
| MRNA | Biotech | High coupon driver | Pipeline risk, trial/regulatory outcomes, revenue reset, event gap risk |
| IONQ | Quantum computing | Very high coupon driver | Speculative technology, valuation, contract credibility, capital raising, gap risk |
| RKLB | Space/aerospace | High coupon driver | Launch execution, contract timing, funding, sector sentiment |
| ENPH | Solar technology | High coupon driver | Rates, residential solar demand, inventory cycle, margin reset |
| FSLR | Solar manufacturing | Medium-high coupon driver | Policy/tariffs, project timing, margin, clean-energy sentiment |
| BABA | China internet ADR | Medium-high coupon driver | China macro/regulation, ADR/geopolitical risk, RMB/sentiment |
| PDD | China e-commerce ADR | High coupon driver | China consumer demand, competition, regulatory/geopolitical risk, earnings gap |
| RIVN | EV manufacturer | Very high coupon driver | Cash burn, deliveries, production ramp, funding/dilution risk |
| UAL | Airlines/cyclicals | Medium-high coupon driver | Fuel, labor, travel demand, macro sensitivity, event shocks |

## Listed Options Vol Proxy

Not refreshed in this local update. The cloud generator should fetch Nasdaq public option-chain data and use it only as an indicative vol/liquidity proxy. It is not an issuer FCN coupon, not a volatility surface, and not an autocall model.

## Issuer Quote Calibration

Real issuer RFQs override this public-data screen. If a real quote from UBS, JPM, Marex, Leonteq, or another issuer contradicts the basket ranking, use the real quote as current calibration evidence after normalizing tenor, strike/reference, KI, KO, RO, coupon frequency, issuer basis, bid/offer, dividends, borrow, funding, skew, correlation, margin, and autocall assumptions.

The public screen is not expected to match issuer pricing. Use this report to ask better RFQs and normalize quotes, not to replace a bank issuer pricer.

## Requote Rationale Check

Before repeating any ticker or basket from a previous report or chat, classify it as fresh, repeat/same rationale, repeat/changed inputs, structural mismatch, or calibration drift. Cross-check today's spot/reference, 3M/6M listed-options proxy, liquidity, event risk, tenor, KI, KO, strike/reference, RO, coupon frequency, issuer basis, and prior calibration note.

Use `templates/requote-checklist.md` for the full comparison. Do not store actual issuer quotes, issuer names, client details, or firm-confidential pricing assumptions in this public repo.

## Standing Screening Map

These are standing RFQ candidates, not today's ranked coupon predictions. Refresh public market data and compare issuer quotes before using them.

| Rank | Basket | Category | Screening read | Suggested terms | Key risk | Action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SMCI / AMD | RFQ first | AI-infrastructure candidate; issuer quotes must verify coupon value. | 3M/6M, KO 100 monthly, RFQ KI ladder 50/55/59/65/70 | SMCI can dominate worst-of downside. | Refresh data and request issuer RFQ. |
| 2 | PLTR / TSLA | Balanced candidate | Liquid high-beta software/EV candidate. | 3M tactical or 6M if client accepts valuation/event risk | Earnings, deliveries, valuation, and sentiment can gap. | Refresh data and request issuer RFQ. |
| 3 | HIMS / MRNA | Quote-check candidate | Healthcare/biotech event-risk candidate. | 3M/6M; require issuer availability and liquidity check | Healthcare headlines and trial/regulatory risk. | Quote only after liquidity check. |
| 4 | IONQ / RKLB | Aggressive candidate | Emerging-tech high-volatility candidate. | Prefer 3M; use lower KI unless pickup per KI point is compelling | Speculative valuation, funding, and severe gap risk. | Use only with strong suitability discipline. |
| 5 | ENPH / FSLR | Balanced candidate | Clean-energy cyclicality candidate. | 3M/6M; compare coupon pickup per KI point | Rates, policy, demand, and margin risk. | RFQ as diversified sector candidate. |
| 6 | BABA / PDD | Quote-check candidate | China ADR candidate. | 3M/6M; normalize ADR/geopolitical risk and issuer correlation assumptions | China macro, regulation, geopolitics, ADR sentiment. | RFQ only after risk disclosure is clear. |
| 7 | SNDK / AMD | Quote-check candidate | Semiconductor/storage candidate. | Compare KO 98/100/102 and RO 97/100 | SanDisk idiosyncratic quote behavior. | Use issuer quotes as calibration. |
| 8 | GOOGL / NVDA | Watch only | Familiar-name anchor candidate. | RFQ only if client wants recognizable names | May dilute coupon despite explainability. | Do not assume attractive coupon. |

## Default Structure For RFQ

- Product: worst-of FCN / autocallable FCN.
- Currency: USD.
- Tenor: compare 3M and 6M first; add 12M only if client accepts longer event risk.
- KO: 98 / 100 / 102, monthly observation.
- KI / airbag: request ladder 50 / 55 / 59 / 65 / 70, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment.
- RO: compare RO 100 and requested RO separately; do not compare headline coupon alone.

## KI Optimization

| KI | Airbag | Coupon p.a. | Pickup vs prior KI | Pickup per KI point | Desk decision |
| --- | --- | --- | --- | --- | --- |
| 50% | 50% | Issuer RFQ | - | - | Base protection |
| 55% | 45% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 59% | 41% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 65% | 35% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 70% | 30% | Issuer RFQ | Calculate | Calculate | Use only if pickup is strong |

Decision rule: do not choose KI by habit. Compare the coupon pickup against the airbag sacrificed. If the pickup is flat, keep the lower KI.

## RFQ Wording

```text
Please quote indicative and firm levels for a USD worst-of FCN on [TICKER 1] / [TICKER 2], 3M and 6M tenor, KO 98 / 100 / 102 monthly, fixed monthly coupon. Please show both RO 100 and requested RO levels where available. Please show coupon p.a. across KI 50 / 55 / 59 / 65 / 70 at maturity, plus coupon pickup per KI point, issuer estimated value, bid/offer, assumptions, and early unwind policy.
```

## Client Explanation

English:

> The coupon is set by issuer pricing for the exact terms, including underlyings, tenor, RO, KO, KI, strike/reference level, volatility, skew, correlation, dividends, borrow, funding, and issuer margin. It is not a risk-free yield. The investor is compensated for taking worst-of downside risk. If the note does not autocall and the worst-performing stock finishes below the KI level, redemption may be linked to that stock's negative performance.

中文:

> 较高票息来自相关股票较高的波动率，并不是无风险收益。投资者收取票息的同时，也承担最差表现股票的下行风险。如果产品没有提前赎回，并且到期时最差表现股票低于 KI 水平，本金赎回可能会跟随该股票的下跌表现。

## Phone Workflow

Open this file on your phone:

```text
https://github.com/peteribmhk/fcn-desk-workbench/blob/main/daily/latest.md
```

Then ask ChatGPT mobile to use this report together with `AGENTS.md`, `methodology.md`, `watchlist.csv`, and `templates/requote-checklist.md` for follow-up RFQ or client-explanation drafting.
