# Requote Rationale Checklist

Use this before suggesting a ticker or basket that has appeared before.

**Status:** Indicative only. Not a firm quote. Do not store issuer names, client details, or firm-confidential pricing assumptions in the public repo.

## Same-Idea Check

| Field | Prior rationale | Today | Change / action |
|---|---|---|---|
| Date/time checked | [YYYY-MM-DD HKT] | [YYYY-MM-DD HKT] | Fresh / repeat / stale |
| Basket | [TICKER 1] / [TICKER 2] | [TICKER 1] / [TICKER 2] | Same / changed |
| Sector theme | [theme] | [theme] | Same / changed |
| Spot/reference | [prior] | [today] | Re-fix or quote from live level |
| 3M listed-options proxy | [prior] | [today] | Richer / flatter / unavailable |
| 6M listed-options proxy | [prior] | [today] | Richer / flatter / unavailable |
| Listed-options liquidity | [prior] | [today] | Better / worse / unchanged |
| Event/news risk | [prior] | [today] | New event risk? |
| Tenor | [3M/6M/12M] | [3M/6M/12M] | Normalize before comparing |
| KI and observation | [level/style] | [level/style] | Normalize before comparing |
| KO and observation | [level/style] | [level/style] | Normalize before comparing |
| Strike/reference | [level/%] | [level/%] | Normalize before comparing |
| RO / issue price | [RO] | [RO] | Separate RO accretion from coupon |
| Coupon frequency | [monthly/quarterly] | [monthly/quarterly] | Normalize before comparing |
| Prior calibration note | [public-safe summary] | [today note] | Recalibrate if contradicted |

## Decision Labels

- **Fresh idea:** no recent prior rationale; screen from current public data and ask issuer RFQ.
- **Repeat, same rationale:** market inputs and structure are broadly unchanged; reuse only with today's data timestamp.
- **Repeat, changed inputs:** same ticker/basket but spot, vol proxy, event risk, tenor, KO, KI, strike, or RO changed enough to refresh the rationale.
- **Structural mismatch:** do not compare coupon levels until terms are normalized.
- **Calibration drift:** today's issuer/pricing-system result contradicts the old public-data screen; update the session view and let real quote evidence override the screen.
