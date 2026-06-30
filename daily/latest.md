# FCN Daily Report

**Report date:** 2026-06-30  
**Generated:** 2026-06-30 19:32 HKT / 2026-06-30 11:32 UTC  
**Status:** Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.  
**Source caveat:** Public quote source: Nasdaq public quote endpoint. Data is delayed/public and not a firm exchange feed.

## Market Snapshot

| Ticker | Last | Date/Time | Daily move | Volatility read | Main risk |
| --- | --- | --- | --- | --- | --- |
| MSTR | 89.54 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | -3.39% | Very high | BTC beta, leverage, gap risk |
| COIN | 148.67 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | -1.97% | High | Crypto flow, regulation, BTC/ETH sentiment |
| AMD | 542.99 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | +0.65% | Medium-high | AI expectations, valuation, product cycle |
| SMCI | 28.57 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | +1.49% | Very high | Financing/dilution, order-cycle risk, jump risk |
| NVDA | 196.86 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | +0.97% | Medium-high | AI capex cycle, valuation, export controls |
| TSLA | 408.00 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | -0.93% | High | Deliveries, margins, CEO/event risk |
| PLTR | 116.70 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | +0.86% | High | Valuation, AI software sentiment, earnings risk |
| HOOD | 102.31 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | +0.47% | High | Retail activity, crypto revenue, regulation |
| SNDK | 2098.93 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | +2.37% | High | Storage cycle, post-separation history, idiosyncratic gap risk |
| GOOGL | 355.06 | Jun 30, 2026 7:32 AM ET Pre-Market delayed | +0.40% | Medium | AI/search capex, antitrust, ad-cycle and mega-cap valuation risk |

## Listed Options Vol Proxy

**Source caveat:** Nasdaq public option-chain endpoint. Listed option data is delayed/public and used only as an indicative vol/liquidity proxy.

| Ticker | 3M ATM straddle proxy | 6M ATM straddle proxy | Listed options liquidity |
| --- | --- | --- | --- |
| MSTR | Sep 18 90 ATM straddle 35.0% | Dec 18 90 ATM straddle 49.8% | Deep listed options liquidity |
| COIN | Sep 18 150 ATM straddle 28.2% | Dec 18 150 ATM straddle 40.8% | Usable listed options liquidity |
| AMD | Sep 18 540 ATM straddle 27.9% | Dec 18 540 ATM straddle 39.3% | Thin listed options liquidity |
| SMCI | Sep 18 29 ATM straddle 34.6% | Dec 18 29 ATM straddle 48.9% | Usable listed options liquidity |
| NVDA | Sep 18 195 ATM straddle 15.3% | Dec 18 195 ATM straddle 22.7% | Deep listed options liquidity |
| TSLA | Sep 18 410 ATM straddle 17.5% | Dec 18 410 ATM straddle 26.2% | Deep listed options liquidity |
| PLTR | Sep 18 115 ATM straddle 20.7% | Dec 18 115 ATM straddle 30.2% | Deep listed options liquidity |
| HOOD | Sep 18 100 ATM straddle 26.0% | Dec 18 100 ATM straddle 37.6% | Usable listed options liquidity |
| SNDK | Sep 18 2100 ATM straddle 41.9% | Dec 18 2100 ATM straddle 60.0% | Thin listed options liquidity |
| GOOGL | Sep 18 355 ATM straddle 13.6% | Dec 18 355 ATM straddle 19.9% | Usable listed options liquidity |

Use this section to judge relative listed-option richness and liquidity only. It is not an issuer FCN coupon, not a volatility surface, not an autocall model, and not enough to predict which basket will have the best actual coupon.

## Issuer Quote Calibration

Real issuer RFQs override this public-data screen. If a real quote contradicts the basket ranking, use the real quote as current calibration evidence and ask what drove the difference: RO, KO, KI, strike/reference, skew, correlation, borrow, dividends, funding, issuer inventory, or margin.

For rough comparison when RO differs:

```text
Approx annualized RO accretion = ((100 - RO) / RO) * (12 / tenor_months)
Approx annualized gross carry = coupon p.a. + annualized RO accretion
```

Example: for a 3M note at RO 97, the rough annualized RO accretion is about 12.4% before considering path risk, autocall timing, issuer bid/offer, and downside redemption risk. Keep headline coupon and RO accretion separate in client discussion.

## Screening Baskets

| Rank | Basket | Category | Screening read | Suggested terms | Key risk | Action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | MSTR / COIN | RFQ first | Screens for RFQ because both names carry crypto-beta and high volatility; actual coupon must come from issuer levels. | 3M/6M, KO 100 monthly, RFQ KI ladder 50/55/59/65/70 | Concentrated crypto-beta; BTC selloff can hit both names. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 2 | AMD / SMCI | Balanced candidate | Screens as an AI-infrastructure candidate, but do not rank coupon value until issuer quotes are normalized. | 3M tactical or 6M if client accepts event risk; optimize KI ladder | SMCI can dominate worst-of downside; financing and jump risk matter. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 3 | MSTR / SMCI | Aggressive candidate | Screens as aggressive due to jump risk; use only after issuer RFQ confirms compensation. | Prefer 3M; consider lower KI if coupon still works | Two unstable high-vol names; severe gap and worst-of risk. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 4 | COIN / SMCI | Aggressive candidate | Screens as aggressive; actual value depends on issuer correlation, skew, and hedge assumptions. | 3M/6M; compare coupon pickup per KI point across ladder | Crypto regulation plus SMCI financing/event risk. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 5 | SNDK / GOOGL | Quote-check candidate | User quote evidence shows this can price strongly; treat issuer quote as calibration, not public-screen output. | Use issuer quote evidence; compare KO 98/100/102 and RO 97/100 | SanDisk idiosyncratic risk plus lower-vol mega-cap anchor; quote may be issuer-specific. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 6 | AMD / SNDK | Quote-check candidate | User quote evidence suggests headline coupon is not enough; normalize RO 97, KO 102, KI 58, and strike terms. | Use issuer quote evidence; normalize RO, KO, KI, and strike before ranking | Semiconductor/event risk; SanDisk quote behavior may diverge from public vol screen. | Request/compare issuer RFQ; do not rank by public screen alone. |
| 7 | GOOGL / AMD | Watch only | User quote evidence shows this may price weakly; avoid assuming popular names produce attractive coupon. | RFQ only if client wants familiar names; do not assume high coupon | Lower actual coupon possible despite recognizable names; quote must drive decision. | Request/compare issuer RFQ; do not rank by public screen alone. |

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
