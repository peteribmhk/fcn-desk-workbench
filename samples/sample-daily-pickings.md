# Sample Daily FCN Pickings

**Date:** 2026-06-27
**Prepared by:** Codex + FCN Desk Workbench  
**Data timestamp:** Example only. Replace with latest public market data before use.  
**Status:** Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
**Universe policy:** Crypto-linked tickers are excluded by default unless the user explicitly opts in.

## Market Snapshot

This sample demonstrates the output format. It does not embed live prices. Before sending any RFQ, refresh spot, volatility, event risk, liquidity context, and issuer quote evidence.

| Ticker | Current role in FCN screen | Volatility read | Main risk |
|---|---|---|---|
| SMCI | RFQ screening candidate | Very high | Financing/dilution, governance history, order-cycle risk, jump risk |
| AMD | AI semiconductor anchor | Medium-high | AI expectations, valuation, product cycle |
| PLTR | Momentum/software candidate | High | Valuation, commercial/government growth, earnings risk |
| TSLA | Familiar high-beta candidate | High | Deliveries, margins, valuation, CEO/event risk |
| HIMS | Healthcare/consumer growth candidate | High | Regulation, telehealth growth, product headline risk |
| IONQ | Emerging-tech aggressive candidate | Very high | Speculative valuation, funding, contract credibility, gap risk |
| ENPH | Clean-energy cyclicality candidate | High | Rates, demand cycle, inventory, margins |
| BABA | China ADR candidate | Medium-high | China macro, regulation, geopolitics, ADR sentiment |

## Screening Baskets

| Rank | Basket | Category | Screening read | Suggested terms | Key risk | Action |
|---:|---|---|---|---|---|---|
| 1 | SMCI / AMD | RFQ first | Screens as AI infrastructure, but coupon value must be issuer-verified | Start with 3M and 6M, KO 100 monthly, quote KI ladder 50/55/59/65/70 | SMCI can dominate worst-of downside | RFQ first, pending issuer quote evidence |
| 2 | PLTR / TSLA | Balanced candidate | Liquid high-beta software/EV screen | 3M tactical or 6M if client accepts event risk | Valuation and event risk can gap both names | RFQ as candidate |
| 3 | HIMS / MRNA | Quote-check candidate | Healthcare/biotech event-risk screen | 3M/6M; verify issuer availability and liquidity | Regulatory, trial, product headline, and revenue reset risk | RFQ only after liquidity check |
| 4 | IONQ / RKLB | Aggressive candidate | Emerging-tech high-volatility screen | Prefer 3M and lower KI unless pickup is compelling | Severe gap, funding, and execution risk | Use only for aggressive suitability |
| 5 | ENPH / FSLR | Balanced candidate | Clean-energy cyclicality screen | 3M/6M; compare coupon pickup per KI point | Rates, policy, demand, and margin risk | RFQ as diversified sector candidate |

## Requote Rationale Check

If any basket appeared before, do not reuse the old conclusion blindly. Classify it as fresh, repeat/same rationale, repeat/changed inputs, structural mismatch, or calibration drift. Compare spot/reference, listed-options proxy, liquidity, event risk, tenor, KI, KO, strike/reference, RO, coupon frequency, issuer basis, and any user-provided pricing-system calibration.

## KI Optimization

| KI | Airbag | Coupon p.a. | Pickup vs prior KI | Pickup per KI point | Desk decision |
|---:|---:|---:|---:|---:|---|
| 50% | 50% | Issuer RFQ | - | - | Base protection |
| 55% | 45% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 59% | 41% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 65% | 35% | Issuer RFQ | Calculate | Calculate | Move up only if pickup justifies airbag sacrificed |
| 70% | 30% | Issuer RFQ | Calculate | Calculate | Only if pickup is strong |

Decision rule: if coupon pickup is flat, keep the lower KI. If pickup accelerates sharply at a higher KI, that level may be the best-value candidate subject to client risk appetite.

## Suggested RFQs

### RFQ 1: Value RFQ

```text
Please quote indicative and firm levels for a USD worst-of FCN on SMCI / AMD, 3M and 6M tenor, KO 98 / 100 / 102 monthly, fixed monthly coupon. Please show both RO 100 and requested RO levels where available. Please show coupon p.a. across KI 50 / 55 / 59 / 65 / 70 at maturity, plus coupon pickup per KI point, issuer estimated value, bid/offer, assumptions, and early unwind policy.
```

### RFQ 2: Sector Diversification RFQ

```text
Please quote indicative and firm levels for a USD worst-of FCN on ENPH / FSLR, 3M and 6M tenor, KO 98 / 100 / 102 monthly, fixed monthly coupon. Please quote KI 50 / 55 / 59 / 65 / 70 and show the incremental coupon pickup per KI point.
```

## Client Explanation Draft

English:

> The coupon is set by issuer pricing for the exact terms, including underlyings, tenor, RO, KO, KI, strike/reference level, volatility, skew, correlation, dividends, borrow, funding, and issuer margin. It is not a risk-free yield. The investor is compensated for taking worst-of downside risk. If the note does not autocall and the worst-performing stock finishes below the KI level, redemption may be linked to that stock's negative performance.

中文:

> 较高票息来自相关股票较高的波动率，并不是无风险收益。投资者收取票息的同时，也承担最差表现股票的下行风险。如果产品没有提前赎回，并且到期时最差表现股票低于 KI 水平，本金赎回可能会跟随该股票的下跌表现。

## Desk Notes

- If issuer quote is much lower or higher than expected, ask whether the driver is volatility, skew, correlation, dividends, borrow, funding, inventory, margin, or autocall assumptions.
- Do not default to a mid-50s KI by habit. Compare KI 50 / 55 / 59 / 65 / 70 and show coupon pickup per KI point.
- If a ticker or basket is repeated, run the requote checklist before presenting it again.
- If terms differ by RO, KO, KI, strike, tenor, or observation style, call it a structural mismatch until normalized.
