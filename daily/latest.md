# FCN Daily Report

**Report date:** 2026-07-01  
**Generated:** 2026-07-01 19:47 HKT / 2026-07-01 11:47 UTC  
**Status:** Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.  
**Source caveat:** Public quote source: Nasdaq public quote endpoint. Data is delayed/public and not a firm exchange feed.
**Universe policy:** Crypto-linked tickers are excluded by default. This report screens a diversified non-crypto watchlist across technology, healthcare/biotech, EV, clean energy, China ADRs, cyclicals, and other high-volatility sectors.

## Profile Verification Gate

This gate must pass before using the report for ticker suggestions or basket combinations.

| Gate | Status | Verification | Required behavior |
| --- | --- | --- | --- |
| User preference | PASS | Crypto-linked tickers excluded | Do not suggest crypto baskets unless the user explicitly opts in. |
| Evidence quality | PASS | Public quote and option-chain inputs are marked as delayed/public screening data. | Never present public data as firm real-time market data or issuer pricing. |
| Issuer quote override | PASS | Report states that issuer RFQs override public-data screens. | Use real issuer/pricing-system quotes as controlling evidence once terms are normalized. |
| Structure normalization | PASS | RFQ wording asks for tenor, KO, KI, strike/reference, RO, coupon frequency, issuer assumptions, and bid/offer. | Do not compare headline coupon unless RO/KO/KI/tenor/strike/frequency/issuer basis match. |
| KI value discipline | PASS | KI ladder 50 / 55 / 59 / 65 / 70 is required. | Choose the KI where incremental coupon pickup compensates for airbag sacrificed. |
| Ticker repeat discipline | PASS | Requote rationale check is required before repeating a ticker or basket. | Classify repeat ideas as same rationale, changed inputs, structural mismatch, or calibration drift. |
| Current data source | PASS | Public quote source: Nasdaq public quote endpoint. Data is delayed/public and not a firm exchange feed. | If quote refresh fails, treat the report as a template and do not provide data-driven picks. |
| Options proxy source | PASS | Nasdaq public option-chain endpoint. Listed option data is delayed/public and used only as an indicative vol/liquidity proxy. | Use listed-options proxy only to prioritize RFQs, not to predict actual FCN coupons. |

## Market Snapshot

| Ticker | Last | Date/Time | Daily move | Volatility read | Main risk |
| --- | --- | --- | --- | --- | --- |
| AMD | 574.46 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -1.11% | High | AI expectations, valuation, product cycle, competition with NVDA |
| SMCI | 29.10 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -0.78% | Very high | Financing/dilution, governance history, order-cycle risk, jump risk |
| NVDA | 198.85 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -0.62% | High | AI capex cycle, valuation, export controls, crowded positioning |
| TSLA | 419.56 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -0.25% | High | Deliveries, margins, valuation, CEO/event risk, China exposure |
| PLTR | 119.60 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | +2.51% | High | Valuation, government/commercial growth, sentiment, earnings risk |
| SNDK | 2194.80 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -3.47% | Quote-check coupon driver | Storage cycle, post-separation trading history, idiosyncratic gap risk |
| GOOGL | 356.93 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -0.12% | Lower-vol | AI capex, search/ads cycle, antitrust, valuation |
| HIMS | 34.98 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | +0.89% | High | Valuation, regulation, telehealth growth, product headline risk |
| MRNA | 69.80 | Jul 1, 2026 7:45 AM ET Pre-Market delayed | -0.33% | High | Pipeline risk, trial/regulatory outcomes, revenue reset, event gap risk |
| IONQ | 53.30 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | +0.08% | Very high | Speculative technology, valuation, contract credibility, capital raising, gap risk |
| RKLB | 101.20 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -0.45% | High | Launch execution, contract timing, funding, sector sentiment |
| ENPH | 49.00 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -0.49% | High | Rates, residential solar demand, inventory cycle, margin reset |
| FSLR | 236.02 | Jul 1, 2026 7:44 AM ET Pre-Market delayed | +0.03% | High | Policy/tariffs, project timing, margin, clean-energy sentiment |
| BABA | 95.60 | Jul 1, 2026 7:46 AM ET Pre-Market delayed | -0.40% | High | China macro/regulation, ADR/geopolitical risk, RMB/sentiment |
| PDD | 76.40 | Jul 1, 2026 7:42 AM ET Pre-Market delayed | +0.16% | High | China consumer demand, competition, regulatory/geopolitical risk, earnings gap |
| RIVN | 17.27 | Jul 1, 2026 7:47 AM ET Pre-Market delayed | -0.44% | Very high | Cash burn, deliveries, production ramp, funding/dilution risk |
| UAL | 136.99 | Jul 1, 2026 7:46 AM ET Pre-Market delayed | +0.74% | High | Fuel, labor, travel demand, macro sensitivity, event shocks |

## Listed Options Vol Proxy

**Source caveat:** Nasdaq public option-chain endpoint. Listed option data is delayed/public and used only as an indicative vol/liquidity proxy.

| Ticker | 3M ATM straddle proxy | 6M ATM straddle proxy | Listed options liquidity |
| --- | --- | --- | --- |
| AMD | Sep 18 570 ATM straddle 28.5% | Dec 18 570 ATM straddle 40.2% | Thin listed options liquidity |
| SMCI | Sep 18 29 ATM straddle 34.6% | Dec 18 29 ATM straddle 49.0% | Usable listed options liquidity |
| NVDA | Sep 18 200 ATM straddle 15.4% | Dec 18 200 ATM straddle 22.9% | Deep listed options liquidity |
| TSLA | Sep 18 420 ATM straddle 17.1% | Dec 18 420 ATM straddle 25.9% | Deep listed options liquidity |
| PLTR | Sep 18 120 ATM straddle 20.4% | Dec 18 120 ATM straddle 30.0% | Deep listed options liquidity |
| SNDK | Sep 18 2190 ATM straddle 42.6% | Dec 18 2190 ATM straddle 61.0% | Thin listed options liquidity |
| GOOGL | Sep 18 355 ATM straddle 13.1% | Dec 18 355 ATM straddle 19.7% | Usable listed options liquidity |
| HIMS | Sep 18 35 ATM straddle 37.2% | Dec 18 35 ATM straddle 50.7% | Usable listed options liquidity |
| MRNA | Sep 18 70 ATM straddle 33.4% | Dec 18 70 ATM straddle 46.8% | Usable listed options liquidity |
| IONQ | Sep 18 55 ATM straddle 38.0% | Dec 18 55 ATM straddle 53.5% | Usable listed options liquidity |
| RKLB | Sep 18 100 ATM straddle 34.6% | Dec 18 100 ATM straddle 49.6% | Usable listed options liquidity |
| ENPH | Sep 18 50 ATM straddle 35.3% | Dec 18 50 ATM straddle 48.4% | Usable listed options liquidity |
| FSLR | Sep 18 240 ATM straddle 25.4% | Dec 18 240 ATM straddle 35.9% | Thin listed options liquidity |
| BABA | Sep 18 95 ATM straddle 17.5% | Dec 18 95 ATM straddle 25.4% | Deep listed options liquidity |
| PDD | Sep 18 75 ATM straddle 16.1% | Dec 18 75 ATM straddle 23.0% | Usable listed options liquidity |
| RIVN | Sep 18 17 ATM straddle 26.0% | Dec 18 18 ATM straddle 39.5% | Deep listed options liquidity |
| UAL | Sep 18 135 ATM straddle 19.1% | Dec 18 135 ATM straddle 27.4% | Thin listed options liquidity |

Use this section to judge relative listed-option richness and liquidity only. It is not an issuer FCN coupon, not a volatility surface, not an autocall model, and not enough to predict which basket will have the best actual coupon.

## Issuer Quote Calibration

Real issuer RFQs override this public-data screen. If a real quote from UBS, JPM, Marex, Leonteq, or another issuer contradicts the basket ranking, use the real quote as current calibration evidence and ask what drove the difference: RO, KO, KI, strike/reference, skew, correlation, borrow, dividends, funding, issuer inventory, margin, or exact autocall assumptions.

The public screen is not expected to match issuer pricing. Issuers use their own spot/reference timing, vol surface, skew, correlation, forward/dividend, borrow, funding, credit, inventory, margin, settlement, and autocall-path assumptions. Use this report to ask better RFQs and normalize quotes, not to replace a bank pricer.

For rough comparison when RO differs:

```text
Approx annualized RO accretion = ((100 - RO) / RO) * (12 / tenor_months)
Approx annualized gross carry = coupon p.a. + annualized RO accretion
```

Example: for a 3M note at RO 97, the rough annualized RO accretion is about 12.4% before considering path risk, autocall timing, issuer bid/offer, and downside redemption risk. Keep headline coupon and RO accretion separate in client discussion.

## Requote Rationale Check

Before repeating any ticker or basket from a previous report or chat, classify it as fresh, repeat/same rationale, repeat/changed inputs, structural mismatch, or calibration drift. Cross-check today's spot/reference, 3M/6M listed-options proxy, liquidity, event risk, tenor, KI, KO, strike/reference, RO, coupon frequency, issuer basis, and prior calibration note.

Use `templates/requote-checklist.md` for the full comparison. Do not store actual issuer quotes, issuer names, client details, or firm-confidential pricing assumptions in this public repo.

## Screening Baskets

| Rank | Basket | Category | Screening read | Suggested terms | Key risk | Action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SMCI / AMD | RFQ first | Screens as an AI-infrastructure candidate, but do not rank coupon value until issuer quotes are normalized. | 3M/6M, KO 100 monthly, RFQ KI ladder 50/55/59/65/70 | SMCI can dominate worst-of downside; financing, governance, and gap risk matter. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 2 | PLTR / TSLA | Balanced candidate | Screens as a liquid high-beta software/EV candidate; actual coupon depends on issuer skew, correlation, and autocall assumptions. | 3M tactical or 6M if client accepts valuation/event risk; optimize KI ladder | High-beta momentum pair; earnings, deliveries, valuation, and sentiment can gap. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 3 | HIMS / MRNA | Quote-check candidate | Screens as a healthcare/biotech event-risk candidate; verify issuer availability and liquidity before ranking. | 3M/6M; require issuer availability, liquidity check, and event-risk review | Healthcare/biotech headlines, trial/regulatory outcomes, and valuation reset risk. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 4 | IONQ / RKLB | Aggressive candidate | Screens as an aggressive emerging-tech candidate; use issuer RFQ to confirm whether coupon compensates for severe gap risk. | Prefer 3M; use lower KI unless pickup per KI point is compelling | Speculative emerging-technology pair; funding, execution, and severe gap risk. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 5 | ENPH / FSLR | Balanced candidate | Screens as a clean-energy cyclicality candidate; rates, policy, and margins may drive quote dispersion. | 3M/6M; compare coupon pickup per KI point across ladder | Rates, policy, demand cycle, and margin risk can dominate the clean-energy story. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 6 | BABA / PDD | Quote-check candidate | Screens as a China ADR candidate; normalize geopolitical, ADR, and correlation assumptions before comparison. | 3M/6M; normalize ADR/geopolitical risk and issuer correlation assumptions | China macro, regulation, geopolitics, and ADR sentiment. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 7 | SNDK / AMD | Quote-check candidate | Quote-check semiconductor/storage candidate; normalize RO, KO, KI, tenor, strike/reference, and issuer basis before ranking. | Use issuer quote evidence; compare KO 98/100/102 and RO 97/100 | Storage/semiconductor cycle and SanDisk idiosyncratic quote behavior. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 8 | GOOGL / NVDA | Watch only | Familiar-name anchor candidate; useful for explainability, but public popularity does not guarantee attractive coupon. | RFQ only if client wants familiar names; do not assume high coupon | Recognizable names may dilute coupon; valuation and AI capex cycle still matter. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 9 | RIVN / TSLA | Aggressive candidate | Aggressive EV candidate; check issuer eligibility, funding risk, and whether lower KI still gives enough coupon. | Prefer short tenor; require issuer eligibility, lower KI ladder, and event-risk check | EV delivery, cash burn, production ramp, margins, and sentiment risk. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 10 | UAL / TSLA | Watch only | Broader cyclicals check; use only if mixed-theme explainability and issuer quote quality are acceptable. | Use only to broaden cyclicals; compare against cleaner same-sector alternatives | Airline macro/fuel/labor risk plus Tesla event risk; mixed-theme explainability. | Request/compare issuer RFQ; do not rank by public screen alone. |

## Default Structure For RFQ

- Product: worst-of FCN / autocallable FCN.
- Currency: USD.
- Tenor: compare 3M and 6M first; add 12M only if client accepts longer event risk.
- KO: 100%, monthly observation.
- KI / airbag: request ladder 50 / 55 / 59 / 65 / 70, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment.
- RO: compare RO 100 and requested RO, such as RO 97, separately; do not compare headline coupon alone.

## KI Optimization

| KI | Airbag | Coupon p.a. | Pickup vs prior KI | Pickup per KI point | Desk decision |
| --- | --- | --- | --- | --- | --- |
| 50% | 50% | Issuer RFQ | - | - | Base protection |
| 55% | 45% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 59% | 41% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 65% | 35% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 70% | 30% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |

Decision rule: do not choose KI by habit. Compare the coupon pickup against the airbag sacrificed. If the pickup is flat, keep the lower KI. If a higher KI gives a sharply better coupon pickup per KI point, flag that level as the best-value candidate subject to client risk appetite.

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

Then ask ChatGPT mobile to use this report together with `methodology.md` and `watchlist.csv` for follow-up RFQ or client-explanation drafting.
