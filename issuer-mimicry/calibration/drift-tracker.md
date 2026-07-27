# Drift Tracker

Logs all calibration events and model-vs-reality divergence.

## Format

```markdown
### YYYY-MM-DD — [Basket] — [Issuer Style]

- **Mimicry Output**: X% p.a. (assumptions: ...)
- **Actual Quote**: Y% p.a. (normalized structure: ...)
- **Divergence**: Z%
- **Adjustment**: [None / funding_spread ±Xbp / skew_markup ±X%]
- **Notes**: [Market conditions, event risks, etc.]
```

---

## Log

### 2026-07-27 — Initial Setup — Generic

- **Mimicry Output**: N/A (baseline)
- **Actual Quote**: N/A
- **Divergence**: N/A
- **Adjustment**: Set conservative defaults: funding_spread=80bp, skew_markup=3%, correlation_haircut=10%
- **Notes**: Initial model setup. Awaiting first real RFQ for calibration.
