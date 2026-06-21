# FCN Daily Report

**Report date:** 2026-06-21  
**Generated:** 2026-06-21 22:38 HKT / 2026-06-21 14:38 UTC  
**Status:** Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.  
**Source caveat:** Public quote fetch failed: RuntimeError('No public quote rows returned from Stooq daily CSV endpoint'). Use this report as a template only.

## Market Snapshot

| Ticker | Last | Date/Time | Daily move | Volatility read | Main risk |
| --- | --- | --- | --- | --- | --- |
| MSTR | N/A | N/A | N/A | Very high | BTC beta, leverage, gap risk |
| COIN | N/A | N/A | N/A | High | Crypto flow, regulation, BTC/ETH sentiment |
| AMD | N/A | N/A | N/A | Medium-high | AI expectations, valuation, product cycle |
| SMCI | N/A | N/A | N/A | Very high | Financing/dilution, order-cycle risk, jump risk |
| NVDA | N/A | N/A | N/A | Medium-high | AI capex cycle, valuation, export controls |
| TSLA | N/A | N/A | N/A | High | Deliveries, margins, CEO/event risk |
| PLTR | N/A | N/A | N/A | High | Valuation, AI software sentiment, earnings risk |
| HOOD | N/A | N/A | N/A | High | Retail activity, crypto revenue, regulation |

## Basket Pickings

| Rank | Basket | Category | Coupon direction | Suggested terms | Key risk | Action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | MSTR / COIN | Max coupon | Likely highest among core pairs because both names carry crypto-beta and high volatility. | 3M/6M, KO 100 monthly, KI 59 maturity, monthly coupon | Concentrated crypto-beta; BTC selloff can hit both names. | RFQ if client prioritizes coupon; validate final terms with issuer. |
| 2 | AMD / SMCI | Balanced high coupon | Likely strong coupon with a clearer AI infrastructure story. | 3M tactical or 6M if client accepts event risk; KO 100, KI 59 | SMCI can dominate worst-of downside; financing and jump risk matter. | RFQ if client prioritizes coupon; validate final terms with issuer. |
| 3 | MSTR / SMCI | Aggressive alternative | Potentially very high, but risk is severe because both names can gap. | Prefer 3M; consider lower KI if coupon still works | Two unstable high-vol names; severe gap and worst-of risk. | RFQ if client prioritizes coupon; validate final terms with issuer. |
| 4 | COIN / SMCI | Aggressive alternative | High coupon; avoids MSTR-specific leverage while keeping crypto plus SMCI risk. | 3M/6M; ask issuer to compare KI 55 vs KI 59 | Crypto regulation plus SMCI financing/event risk. | RFQ if client prioritizes coupon; validate final terms with issuer. |

## Default Structure For RFQ

- Product: worst-of FCN / autocallable FCN.
- Currency: USD.
- Tenor: compare 3M and 6M first; add 12M only if client accepts longer event risk.
- KO: 100%, monthly observation.
- KI / airbag: 59% KI, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment.
- RO: no RO economics unless specifically requested.

## RFQ Wording

```text
Please quote indicative and firm levels for a USD worst-of FCN on [TICKER 1] / [TICKER 2], 3M and 6M tenor, KO 100 monthly, KI 59 at maturity, fixed monthly coupon, no RO economics. Please show coupon p.a., issuer estimated value, bid/offer, assumptions, and early unwind policy.
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
