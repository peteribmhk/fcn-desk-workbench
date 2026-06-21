# Daily FCN Pickings

**Date:** YYYY-MM-DD  
**Prepared by:** Codex + FCN Desk Workbench  
**Data timestamp:** [source and time]  
**Status:** Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.

## Market Snapshot

| Ticker | Spot | 1D | 1W | 1M | Volatility read | Event / news risk | Source |
|---|---:|---:|---:|---:|---|---|---|
| MSTR | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| COIN | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| AMD | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| SMCI | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| NVDA | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| TSLA | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| PLTR | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| HOOD | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |

## Basket Pickings

| Rank | Basket | Category | Coupon direction | Suggested terms | Key risk | Action |
|---:|---|---|---|---|---|---|
| 1 | TBD | Max coupon | TBD | TBD | TBD | RFQ / watch |
| 2 | TBD | Balanced high coupon | TBD | TBD | TBD | RFQ / watch |
| 3 | TBD | Aggressive alternative | TBD | TBD | TBD | RFQ / watch |
| 4 | TBD | Watch only | TBD | TBD | TBD | RFQ / watch |

## Structure View

Default structure to compare:

- Product: worst-of FCN / autocallable FCN.
- Tenor: 3M, 6M, and 12M comparison if time allows.
- KO: 100%, monthly observation.
- KI / airbag: 59% KI, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment unless requested otherwise.
- Data: public data for screening only.

## RFQ To Send

```text
Please quote indicative and firm levels for:
Product: Worst-of Fixed Coupon Note / Autocallable FCN
Underlyings: [TICKER 1] / [TICKER 2]
Currency: USD
Tenor: [3M / 6M / 12M]
Initial fixing: [live level / today close / specified date]
Coupon: fixed coupon, paid monthly
KO: 100%, observed monthly, autocall from [month 1 / month 2 / month 3]
KI: 59%, observed at maturity
No RO economics included unless otherwise specified
Notional: [amount]
Please show coupon p.a., issuer estimated value, bid/offer, settlement convention, fee/margin assumptions, and early unwind policy.
```

## Client Explanation Draft

English:

> This is an indicative high-coupon FCN idea. The coupon is higher because the underlyings are volatile, and the investor is taking worst-of downside risk. If the note does not autocall and the worst-performing stock finishes below the KI level, redemption may be linked to that downside performance.

中文:

> 这是一个仅供参考的高票息 FCN 想法。票息较高，是因为相关股票波动较大，投资者承担最差表现股票的下行风险。如果产品没有提前赎回，并且到期时最差表现股票低于 KI 水平，本金赎回可能会跟随该股票的下跌表现。

