# Sample Daily FCN Pickings

**Date:** 2026-06-21  
**Prepared by:** Codex + FCN Desk Workbench  
**Data timestamp:** Example only. Replace with latest public market data before use.  
**Status:** Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.

## Market Snapshot

This sample demonstrates the output format. It does not embed live prices. Before sending any RFQ, refresh spot, volatility, event risk, and liquidity context.

| Ticker | Current role in FCN screen | Volatility read | Main risk |
|---|---|---|---|
| MSTR | Strong coupon engine | Very high | BTC beta, balance-sheet leverage, gap risk |
| COIN | Strong coupon engine | High | Crypto flow, regulation, BTC/ETH sentiment |
| AMD | Explainable AI-theme anchor | Medium-high | AI expectations, valuation, competition |
| SMCI | Strong coupon engine | Very high | Financing/dilution, AI server order cycle, jump risk |

## Basket Pickings

| Rank | Basket | Category | Coupon direction | Suggested terms | Key risk | Action |
|---:|---|---|---|---|---|---|
| 1 | MSTR / COIN | Max coupon | Likely highest among listed pairs due to crypto-beta and high volatility | Start with 3M and 6M, KO 100 monthly, KI 59 maturity, monthly coupon | Concentrated crypto exposure; BTC selloff can hit both names | RFQ first if client prioritizes coupon |
| 2 | AMD / SMCI | Balanced high coupon | Likely strong coupon with clearer AI infrastructure story | 3M for tactical view; 6M if client accepts event risk; KO 100, KI 59 | SMCI may dominate downside; dilution and financing risk | RFQ as preferred balanced high-coupon idea |
| 3 | MSTR / SMCI | Aggressive alternative | Potentially very high because both names are jumpy and theme-divergent | 3M only unless client is very risk-tolerant; consider lower KI if coupon allows | Two unstable worst-of candidates; severe gap risk | Use only for aggressive accounts |
| 4 | COIN / SMCI | Aggressive alternative | High coupon; avoids MSTR-specific leverage but keeps crypto plus SMCI risk | 3M or 6M; ask issuer to compare KI 55 vs KI 59 | Crypto regulation plus SMCI financing/event risk | RFQ if client wants high coupon without MSTR |

## Suggested RFQs

### RFQ 1: Max Coupon

```text
Please quote indicative and firm levels for a USD worst-of FCN on MSTR / COIN, 3M and 6M tenor, KO 100 monthly, KI 59 at maturity, fixed monthly coupon, no RO economics. Please show coupon p.a., issuer estimated value, bid/offer, assumptions, and early unwind policy.
```

### RFQ 2: Balanced High Coupon

```text
Please quote indicative and firm levels for a USD worst-of FCN on AMD / SMCI, 3M and 6M tenor, KO 100 monthly, KI 59 at maturity, fixed monthly coupon, no RO economics. Please also show coupon sensitivity for KI 55.
```

## Client Explanation Draft

English:

> The higher coupon comes from the volatility of the underlyings. This is not a risk-free yield. The investor is compensated for taking worst-of downside risk. If the note does not autocall and the worst-performing stock finishes below the KI level, redemption may be linked to that stock's negative performance.

中文:

> 较高票息来自相关股票较高的波动率，并不是无风险收益。投资者收取票息的同时，也承担最差表现股票的下行风险。如果产品没有提前赎回，并且到期时最差表现股票低于 KI 水平，本金赎回可能会跟随该股票的下跌表现。

## Desk Notes

- If issuer quote is much lower than expected, ask whether the driver is volatility, correlation, dividends, borrow, funding, margin, or autocall assumptions.
- If client wants more protection, compare KI 50 / 55 / 59 and show coupon give-up.
- If the basket is MSTR-related, explicitly explain BTC sensitivity.
- If the basket includes SMCI, explicitly explain financing/dilution and jump risk.

