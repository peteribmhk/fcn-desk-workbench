# Quote Calibration Template

Use this template to compare Codex's indicative ballpark against the user's firm pricing-system result.

**Status:** Indicative only. Not a firm quote. Do not store issuer names, client details, or firm-confidential pricing assumptions in the public repo.

## Calibration Row

| Field | Value |
|---|---|
| Date / time | [YYYY-MM-DD HKT] |
| Basket | [TICKER 1] / [TICKER 2] |
| Tenor | [3M / 6M / 12M] |
| Strike / reference | [level or %] |
| KI | [level or %] |
| KI observation | [maturity / daily close / continuous] |
| KO | [level or %] |
| KO observation | [monthly / other] |
| RO / issue price | [100 / 97 / other] |
| Coupon frequency | [monthly / quarterly / other] |
| Codex ballpark coupon p.a. | [range] |
| Pricing-system coupon p.a. | [user input] |
| Difference | [pricing-system result minus midpoint of ballpark] |
| Calibration note | [too high / too low / useful / structural mismatch] |

## Rule

Use pricing-system numbers to recalibrate future ballparks in the current session. Store actual issuer quotes only in ignored/private storage such as `actual-quotes/`, not in the public repo.
