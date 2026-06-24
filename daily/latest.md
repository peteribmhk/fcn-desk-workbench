# FCN Daily Report

**Report date:** 2026-06-24  
**Generated:** 2026-06-24 08:23 HKT / 2026-06-24 00:23 UTC  
**Status:** Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.  
**Source caveat:** Public quote source: Nasdaq public quote endpoint. Data is delayed/public and not a firm exchange feed.

## Market Snapshot

| Ticker | Last | Date/Time | Daily move | Volatility read | Main risk |
| --- | --- | --- | --- | --- | --- |
| MSTR | 109.46 | Jun 23, 2026 Closed delayed | -2.73% | Very high | BTC beta, leverage, gap risk |
| COIN | 164.84 | Jun 23, 2026 Closed delayed | +0.97% | High | Crypto flow, regulation, BTC/ETH sentiment |
| AMD | 551.63 | Jun 23, 2026 Closed delayed | +2.65% | Medium-high | AI expectations, valuation, product cycle |
| SMCI | 35.46 | Jun 23, 2026 Closed delayed | +15.66% | Very high; elevated daily move | Financing/dilution, order-cycle risk, jump risk |
| NVDA | 208.65 | Jun 23, 2026 Closed delayed | -0.97% | Medium-high | AI capex cycle, valuation, export controls |
| TSLA | 405.05 | Jun 23, 2026 Closed delayed | +1.14% | High | Deliveries, margins, CEO/event risk |
| PLTR | 119.50 | Jun 23, 2026 Closed delayed | -6.98% | High; active daily move | Valuation, AI software sentiment, earnings risk |
| HOOD | 105.71 | Jun 23, 2026 Closed delayed | -2.26% | High | Retail activity, crypto revenue, regulation |

## Listed Options Vol Proxy

**Source caveat:** Nasdaq public option-chain endpoint. Listed option data is delayed/public and used only as an indicative vol/liquidity proxy.

| Ticker | 3M ATM straddle proxy | 6M ATM straddle proxy | Listed options liquidity |
| --- | --- | --- | --- |
| MSTR | Sep 18 110 ATM straddle 30.9% | Dec 18 110 ATM straddle 44.5% | Usable listed options liquidity |
| COIN | Sep 18 165 ATM straddle 26.8% | Dec 18 165 ATM straddle 38.9% | Thin listed options liquidity |
| AMD | Sep 18 550 ATM straddle 28.9% | Dec 18 550 ATM straddle 39.7% | Thin listed options liquidity |
| SMCI | Sep 18 35 ATM straddle 34.1% | Dec 18 35 ATM straddle 47.6% | Deep listed options liquidity |
| NVDA | Sep 18 210 ATM straddle 15.8% | Dec 18 210 ATM straddle 23.2% | Deep listed options liquidity |
| TSLA | Sep 18 405 ATM straddle 17.7% | Dec 18 405 ATM straddle 25.6% | Usable listed options liquidity |
| PLTR | Sep 18 120 ATM straddle 20.9% | Dec 18 120 ATM straddle 30.3% | Deep listed options liquidity |
| HOOD | Sep 18 105 ATM straddle 25.9% | Dec 18 105 ATM straddle 37.1% | Usable listed options liquidity |

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
