# FCN Daily Report

**Report date:** 2026-06-23  
**Generated:** 2026-06-23 20:15 HKT / 2026-06-23 12:15 UTC  
**Status:** Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.  
**Source caveat:** Public quote source: Nasdaq public quote endpoint. Data is delayed/public and not a firm exchange feed.

## Market Snapshot

| Ticker | Last | Date/Time | Daily move | Volatility read | Main risk |
| --- | --- | --- | --- | --- | --- |
| MSTR | 106.22 | Jun 23, 2026 8:15 AM ET Pre-Market delayed | -2.96% | Very high | BTC beta, leverage, gap risk |
| COIN | 159.03 | Jun 23, 2026 8:15 AM ET Pre-Market delayed | -3.52% | High | Crypto flow, regulation, BTC/ETH sentiment |
| AMD | 517.45 | Jun 23, 2026 8:15 AM ET Pre-Market delayed | -6.20% | Medium-high; active daily move | AI expectations, valuation, product cycle |
| SMCI | 33.51 | Jun 23, 2026 8:15 AM ET Pre-Market delayed | -5.50% | Very high; active daily move | Financing/dilution, order-cycle risk, jump risk |
| NVDA | 203.39 | Jun 23, 2026 8:15 AM ET Pre-Market delayed | -2.52% | Medium-high | AI capex cycle, valuation, export controls |
| TSLA | 394.55 | Jun 23, 2026 8:15 AM ET Pre-Market delayed | -2.59% | High | Deliveries, margins, CEO/event risk |
| PLTR | 119.42 | Jun 23, 2026 8:15 AM ET Pre-Market delayed | -0.07% | High | Valuation, AI software sentiment, earnings risk |
| HOOD | 101.08 | Jun 23, 2026 8:15 AM ET Pre-Market delayed | -4.38% | High; active daily move | Retail activity, crypto revenue, regulation |

## Basket Pickings

| Rank | Basket | Category | Coupon direction | Suggested terms | Key risk | Action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | MSTR / COIN | Max coupon | Likely highest among core pairs because both names carry crypto-beta and high volatility. | 3M/6M, KO 100 monthly, RFQ KI ladder 50/55/59/65/70 | Concentrated crypto-beta; BTC selloff can hit both names. | RFQ if client prioritizes coupon; validate final terms with issuer. |
| 2 | AMD / SMCI | Balanced high coupon | Likely strong coupon with a clearer AI infrastructure story. | 3M tactical or 6M if client accepts event risk; optimize KI ladder | SMCI can dominate worst-of downside; financing and jump risk matter. | RFQ if client prioritizes coupon; validate final terms with issuer. |
| 3 | MSTR / SMCI | Aggressive alternative | Potentially very high, but risk is severe because both names can gap. | Prefer 3M; consider lower KI if coupon still works | Two unstable high-vol names; severe gap and worst-of risk. | RFQ if client prioritizes coupon; validate final terms with issuer. |
| 4 | COIN / SMCI | Aggressive alternative | High coupon; avoids MSTR-specific leverage while keeping crypto plus SMCI risk. | 3M/6M; compare coupon pickup per KI point across ladder | Crypto regulation plus SMCI financing/event risk. | RFQ if client prioritizes coupon; validate final terms with issuer. |

## Default Structure For RFQ

- Product: worst-of FCN / autocallable FCN.
- Currency: USD.
- Tenor: compare 3M and 6M first; add 12M only if client accepts longer event risk.
- KO: 100%, monthly observation.
- KI / airbag: request ladder 50 / 55 / 59 / 65 / 70, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment.
- RO: no RO economics unless specifically requested.

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
Please quote indicative and firm levels for a USD worst-of FCN on [TICKER 1] / [TICKER 2], 3M and 6M tenor, KO 100 monthly, fixed monthly coupon, no RO economics. Please show coupon p.a. across KI 50 / 55 / 59 / 65 / 70 at maturity, plus coupon pickup per KI point, issuer estimated value, bid/offer, assumptions, and early unwind policy.
```

## Client Explanation

English:

> The higher coupon comes from the volatility of the underlyings. This is not a risk-free yield. The investor is compensated for taking worst-of downside risk. If the note does not autocall and the worst-performing stock finishes below the KI level, redemption may be linked to that stock's negative performance.

中文:

> 较高票息来自相关股票较高的波动率，并不是无风险收益。投资者收取票息的同时，也承担最差表现股票的下行风险。如果产品没有提前赎回，并且到期时最差表现股票低于 KI 水平，本金赎回可能会跟随该股票的下跌表现。

## Phone Workflow

Open this file on your phone:

```text
https://github.com/peteribmhk/fcn-desk-workbench/blob/main/daily/latest.md
```

Then ask ChatGPT mobile to use this report together with `methodology.md` and `watchlist.csv` for follow-up RFQ or client-explanation drafting.
