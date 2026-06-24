# FCN Daily Report

**Report date:** 2026-06-24  
**Generated:** 2026-06-24 19:24 HKT / 2026-06-24 11:24 UTC  
**Status:** Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.  
**Source caveat:** Public quote source: Nasdaq public quote endpoint. Data is delayed/public and not a firm exchange feed.

## Market Snapshot

| Ticker | Last | Date/Time | Daily move | Volatility read | Main risk |
| --- | --- | --- | --- | --- | --- |
| MSTR | 104.10 | Jun 24, 2026 7:24 AM ET Pre-Market delayed | +0.25% | Very high | BTC beta, leverage, gap risk |
| COIN | 158.81 | Jun 24, 2026 7:24 AM ET Pre-Market delayed | +0.40% | High | Crypto flow, regulation, BTC/ETH sentiment |
| AMD | 524.06 | Jun 24, 2026 7:24 AM ET Pre-Market delayed | +0.81% | Medium-high | AI expectations, valuation, product cycle |
| SMCI | 33.89 | Jun 24, 2026 7:24 AM ET Pre-Market delayed | +1.71% | Very high | Financing/dilution, order-cycle risk, jump risk |
| NVDA | 201.06 | Jun 24, 2026 7:24 AM ET Pre-Market delayed | +0.51% | Medium-high | AI capex cycle, valuation, export controls |
| TSLA | 383.26 | Jun 24, 2026 7:24 AM ET Pre-Market delayed | +0.43% | High | Deliveries, margins, CEO/event risk |
| PLTR | 115.50 | Jun 24, 2026 7:24 AM ET Pre-Market delayed | -1.03% | High | Valuation, AI software sentiment, earnings risk |
| HOOD | 102.95 | Jun 24, 2026 7:24 AM ET Pre-Market delayed | -0.29% | High | Retail activity, crypto revenue, regulation |

## Listed Options Vol Proxy

**Source caveat:** Nasdaq public option-chain endpoint. Listed option data is delayed/public and used only as an indicative vol/liquidity proxy.

| Ticker | 3M ATM straddle proxy | 6M ATM straddle proxy | Listed options liquidity |
| --- | --- | --- | --- |
| MSTR | Sep 18 105 ATM straddle 31.7% | Dec 18 105 ATM straddle 45.8% | Usable listed options liquidity |
| COIN | Sep 18 160 ATM straddle 27.4% | Dec 18 160 ATM straddle 39.8% | Usable listed options liquidity |
| AMD | Sep 18 520 ATM straddle 29.3% | Dec 18 520 ATM straddle 40.5% | Thin listed options liquidity |
| SMCI | Sep 18 34 ATM straddle 35.0% | Dec 18 34 ATM straddle 49.1% | Usable listed options liquidity |
| NVDA | Sep 18 200 ATM straddle 15.9% | Dec 18 200 ATM straddle 23.5% | Deep listed options liquidity |
| TSLA | Sep 18 385 ATM straddle 17.8% | Dec 18 385 ATM straddle 26.3% | Usable listed options liquidity |
| PLTR | Sep 18 115 ATM straddle 21.2% | Dec 18 115 ATM straddle 30.9% | Usable listed options liquidity |
| HOOD | Sep 18 105 ATM straddle 26.6% | Dec 18 105 ATM straddle 38.1% | Usable listed options liquidity |

Use this section to judge relative listed-option richness and liquidity only. It is not an issuer FCN coupon, not a volatility surface, and not an autocall model.

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
