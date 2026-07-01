# Daily FCN Pickings

**Date:** YYYY-MM-DD  
**Prepared by:** Codex + FCN Desk Workbench  
**Data timestamp:** [source and time]  
**Status:** Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
**Universe policy:** Crypto-linked tickers are excluded by default unless the user explicitly opts in.

## Market Snapshot

| Ticker | Spot | 1D | 1W | 1M | Volatility read | Event / news risk | Source |
|---|---:|---:|---:|---:|---|---|---|
| AMD | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| SMCI | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| NVDA | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| TSLA | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| PLTR | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| HIMS | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| MRNA | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| IONQ | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| RKLB | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| ENPH | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| FSLR | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| BABA | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |
| PDD | TBD | TBD | TBD | TBD | Very high / high / medium | TBD | TBD |

## Screening Baskets

| Rank | Basket | Category | Screening read | Suggested terms | Key risk | Action |
|---:|---|---|---|---|---|---|
| 1 | TBD | RFQ first | TBD | TBD | TBD | RFQ / watch |
| 2 | TBD | Balanced candidate | TBD | TBD | TBD | RFQ / watch |
| 3 | TBD | Quote-check candidate | TBD | TBD | TBD | RFQ / watch |
| 4 | TBD | Aggressive candidate | TBD | TBD | TBD | RFQ / watch |
| 5 | TBD | Watch only | TBD | TBD | TBD | RFQ / watch |

## Requote Rationale Check

Before repeating a ticker or basket from a previous report, classify it:

- Fresh idea.
- Repeat, same rationale.
- Repeat, changed market inputs.
- Structural mismatch.
- Calibration drift.

Use `templates/requote-checklist.md` and compare spot/reference, listed-options proxy, liquidity, event risk, tenor, KI, KO, strike/reference, RO, coupon frequency, issuer basis, and prior calibration note.

## Structure View

Default structure to compare:

- Product: worst-of FCN / autocallable FCN.
- Tenor: 3M, 6M, and 12M comparison if time allows.
- KO: 98 / 100 / 102, monthly observation.
- KI / airbag: request KI ladder 50 / 55 / 59 / 65 / 70, observed at maturity unless issuer specifies otherwise.
- Coupon: fixed coupon, monthly payment unless requested otherwise.
- RO: show RO 100 and requested RO levels separately.
- Data: public data for screening only.

## KI Optimization

| Basket | Tenor | KI | Airbag | Coupon p.a. | Coupon pickup vs prior KI | Pickup per KI point | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| [TICKER 1] / [TICKER 2] | 3M | 50 | 50 | TBD | - | - | Base protection |
| [TICKER 1] / [TICKER 2] | 3M | 55 | 45 | TBD | TBD | TBD | Keep / move up |
| [TICKER 1] / [TICKER 2] | 3M | 59 | 41 | TBD | TBD | TBD | Keep / move up |
| [TICKER 1] / [TICKER 2] | 3M | 65 | 35 | TBD | TBD | TBD | Keep / move up |
| [TICKER 1] / [TICKER 2] | 3M | 70 | 30 | TBD | TBD | TBD | Only if pickup is strong |

Decision rule: choose the KI where incremental coupon pickup is worth the airbag sacrificed. If coupon pickup is flat, prefer the lower KI.

## RFQ To Send

```text
Please quote indicative and firm levels for:
Product: Worst-of Fixed Coupon Note / Autocallable FCN
Underlyings: [TICKER 1] / [TICKER 2]
Currency: USD
Tenor: [3M / 6M / 12M]
Initial fixing: [live level / today close / specified date]
Coupon: fixed coupon, paid monthly
KO: 98 / 100 / 102, observed monthly, autocall from [month 1 / month 2 / month 3]
KI: please quote ladder 50 / 55 / 59 / 65 / 70, observed at maturity
Please show RO 100 and requested RO levels where available
Notional: [amount]
Please show coupon p.a., issuer estimated value, bid/offer, settlement convention, fee/margin assumptions, correlation/skew/funding/borrow drivers where possible, and early unwind policy.
```

## Client Explanation Draft

English:

> This is an indicative FCN idea. The coupon is set by issuer pricing for the exact terms, including underlyings, tenor, RO, KO, KI, strike/reference level, volatility, skew, correlation, dividends, borrow, funding, and issuer margin. The investor is taking worst-of downside risk. If the note does not autocall and the worst-performing stock finishes below the KI level, redemption may be linked to that downside performance.

中文:

> 这是一个仅供参考的 FCN 想法。票息由发行人根据具体条款定价，包括相关股票、期限、RO、KO、KI、行使价/参考价、波动率、偏斜、相关性、股息、借货成本、融资成本和发行人利润。投资者承担最差表现股票的下行风险。如果产品没有提前赎回，并且到期时最差表现股票低于 KI 水平，本金赎回可能会跟随该股票的下跌表现。
