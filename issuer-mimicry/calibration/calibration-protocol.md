# Calibration Protocol

## When to Calibrate

- After every real issuer RFQ response.
- When the mimicry output diverges > 20% from issuer quotes consistently.
- When market regime changes (VIX > 30, rates shift > 50bp, etc.).
- Weekly, even without new quotes, to check for model drift.

## Calibration Steps

### Step 1: Normalize the Quote

Ensure the issuer quote and mimicry inputs match on:

| Field | Action |
|-------|--------|
| Tenor | Same months |
| Basket | Same tickers |
| Strike/Reference | Same convention |
| KI level | Same % |
| KI observation | Maturity / Daily / Continuous |
| KO level | Same % |
| KO observation | Monthly / Quarterly |
| RO | Same issue price |
| Coupon frequency | Monthly / Quarterly |
| Memory | Yes / No |

### Step 2: Run Mimicry Pricer

```bash
python data-sources/calculators/fcn_indicative_pricer.py
# or via GitHub Actions
```

Use current `default.json` assumptions.

### Step 3: Compare

| Metric | Acceptable | Action if exceeded |
|--------|-----------|-------------------|
| Mimicry vs. Issuer (same structure) | ±15% | Note and monitor |
| Mimicry vs. Issuer (same structure) | ±20-30% | Adjust issuer_spread in default.json |
| Mimicry vs. Issuer (same structure) | > ±30% | Investigate: wrong vol? wrong correlation? event risk? |

### Step 4: Adjust Assumptions

In `issuer-mimicry/assumptions/default.json`, adjust:

- `funding_spread`: if mimicry is consistently low/high across issuers.
- `skew_markup`: if single-name baskets diverge more than indices.
- `correlation_haircut`: if worst-of baskets diverge systematically.
- `profit_margin`: if one issuer is consistently tighter/wider.

### Step 5: Log

Update `drift-tracker.md` with:

- Date
- Basket
- Issuer (anonymized if public repo: "Issuer A", "Issuer B")
- Mimicry output
- Actual quote (normalized)
- Divergence %
- Adjustment made
- Notes

## Public Repo Safety

- Do NOT log actual issuer names if repo is public.
- Do NOT log actual quote ladders with timestamps that could identify trades.
- Use anonymized labels: "Major Swiss issuer", "US Bulge Bracket", "European Structured House".
- Store detailed quote history in private repo or firm system.
