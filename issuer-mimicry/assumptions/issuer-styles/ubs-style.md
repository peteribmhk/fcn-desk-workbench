# UBS-Style Pricing Assumptions

**Status:** Inferred from market observation. Not official UBS documentation.

## Known Characteristics

- Tighter on large-cap single names (AAPL, MSFT, GOOGL)
- Conservative on China ADRs
- Moderate skew markup (~2.5-3.0%)
- Strong funding advantage (lower spread)
- Monthly KO observation standard

## Parameters (from default.json)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| skew_markup | 3.0% | Moderate skew adjustment |
| correlation_haircut | 10% | Conservative worst-of |
| funding_spread | 80bp | Strong balance sheet |
| profit_margin | 50bp | Competitive pricing |
| dividend_drag | 50bp | Standard adjustment |
| borrow_cost | 20bp | Low for liquid names |

## When to Use

- When RFQ to UBS or UBS-like major Swiss/European issuer
- When basket contains liquid large-caps
- When client prioritizes issuer credit quality
