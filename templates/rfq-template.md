# Issuer RFQ Template

Use this template when asking issuers for indicative or firm FCN terms.

```text
Please quote indicative and firm levels for:

Product: Worst-of Fixed Coupon Note / Autocallable FCN
Underlyings: [TICKER 1] / [TICKER 2]
Currency: USD
Tenor: [3M / 6M / 12M]
Initial fixing: [live level / close / specified fixing date]
Coupon: fixed coupon, paid [monthly / quarterly]
KO: [100%], observed [monthly], autocall from [month 1 / month 2 / month 3]
KI: [59%], observed [at maturity / daily close / continuously]
Airbag: [41% buffer if KI is 59%]
Redemption: if KI event applies and final worst-of is below strike, redemption follows worst-of performance
Notional: [amount]
Settlement: [cash / physical / issuer standard]
No RO economics included unless otherwise specified

Please show:
- coupon p.a.,
- payment frequency,
- issuer estimated value,
- bid/offer,
- settlement convention,
- fee/margin assumptions,
- key risk notes,
- early unwind policy.
```

## Quick Variants

### Max Coupon RFQ

```text
Please maximize coupon for a USD worst-of FCN on [TICKER 1] / [TICKER 2], KO 100 monthly, KI 59 at maturity, monthly coupon, no RO economics. Show 3M, 6M, and 12M levels.
```

### Safer Airbag RFQ

```text
Please compare KI 50 / 55 / 59 for the same basket and tenor. Show coupon give-up and explain which input drives the difference.
```

### Quote Challenge

```text
Your coupon appears below my indicative screen. Please clarify whether the difference is mainly driven by vol, correlation, dividends, borrow, funding, issuer margin, or autocall assumptions.
```

