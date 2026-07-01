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
| Issuer/pricing source | [private user input; do not commit issuer-sensitive detail] |
| Codex ballpark coupon p.a. | [range] |
| Pricing-system coupon p.a. | [user input] |
| Difference | [pricing-system result minus midpoint of ballpark] |
| Difference driver | [vol / skew / correlation / dividends / borrow / funding / issuer inventory / margin / autocall assumption / structure] |
| Requote label | [fresh / repeat same rationale / repeat changed inputs / structural mismatch / calibration drift] |
| Calibration note | [too high / too low / useful / structural mismatch / issuer quote overrides screen] |

## Normalization Checklist

Do not compare coupon levels until these fields are aligned or explicitly explained:

- tenor,
- underlyings,
- strike/reference,
- KI level and observation style,
- KO level, KO start, and observation frequency,
- RO / issue price,
- coupon frequency and memory/non-memory feature,
- issuer and bid/offer basis,
- settlement convention,
- dividends, borrow, funding, skew, and correlation assumptions where known.

## Rule

Use pricing-system numbers to recalibrate future ballparks in the current session. Store actual issuer quotes only in ignored/private storage such as `actual-quotes/`, not in the public repo.
