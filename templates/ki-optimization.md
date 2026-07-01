# KI Optimization Template

Use this when comparing issuer quotes across KI levels. The goal is to find the best value point, not mechanically choose the lowest KI or highest coupon.

**Status:** Indicative only. Not a firm quote. Final terms must be validated by issuer RFQ and firm-approved systems.

## Quote Inputs

| Field | Value |
|---|---|
| Basket | [TICKER 1] / [TICKER 2] |
| Tenor | [3M / 6M / 12M] |
| KO | 100%, monthly |
| Coupon frequency | Monthly |
| KI observation | Maturity / daily close / continuous |
| RO | No RO unless specified |
| Issuer | [Issuer name] |

## KI Ladder

| KI | Airbag | Coupon p.a. | Coupon pickup vs prior KI | Airbag sacrificed | Pickup per KI point | Decision |
|---:|---:|---:|---:|---:|---:|---|
| 50 | 50 | TBD | - | - | - | Base protection |
| 55 | 45 | TBD | TBD | 5 | TBD | Keep lower KI / move up |
| 59 | 41 | TBD | TBD | 4 | TBD | Keep lower KI / move up |
| 65 | 35 | TBD | TBD | 6 | TBD | Keep lower KI / move up |
| 70 | 30 | TBD | TBD | 5 | TBD | Use only if pickup is strong |

## Decision Rules

- If pickup per KI point is below 0.25% p.a., prefer the lower KI.
- If pickup per KI point is 0.25%-0.60% p.a., treat it as a balanced tradeoff.
- If pickup per KI point is above 0.60% p.a., the higher KI may be worth considering.
- If pickup is flat, choose the lower KI.
- If pickup accelerates sharply, flag that KI as a value point.

## Client-Friendly Summary

English:

> We are comparing how much extra coupon the investor receives for accepting a higher KI level. The best value is not necessarily the lowest KI or the highest coupon; it is the point where the extra coupon reasonably compensates for the extra downside trigger risk.

中文:

> 我们比较的是：投资者接受更高 KI 后，能多拿多少票息。最佳选择不一定是最低 KI，也不一定是最高票息，而是多拿的票息是否足以补偿额外的下行触发风险。
