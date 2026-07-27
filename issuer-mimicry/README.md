# Issuer Mimicry Engine

This directory contains the FCN indicative pricing engine that attempts to
mimic how major issuers (UBS, JPM, Marex, Leonteq, etc.) price worst-of FCNs.

## Philosophy

- **Calibrate, don't guess.** The model starts with conservative assumptions
  and calibrates itself when you feed it real issuer quotes.
- **Every issuer is different.** We track issuer-style assumptions separately.
- **Public data has limits.** This engine gives you a *directionally useful*
  range, not an exact replica of a bank's pricer.

## Directory Structure

```
issuer-mimicry/
├── README.md
├── calibration/
│   ├── calibration-protocol.md      # How to calibrate the model
│   └── drift-tracker.md            # Tracks model vs. reality divergence
├── models/
│   ├── bs_autocall.py              # Black-Scholes + autocall adjustment
│   ├── mc_worst_of.py              # Monte Carlo worst-of simulator
│   └── skew_adjustment.py          # Issuer-style skew markup
└── assumptions/
    ├── default.json                # Current calibrated assumptions
    └── issuer-styles/
        ├── ubs-style.md
        ├── jpm-style.md
        └── marex-style.md
```

## How It Works

1. **Base Model**: Monte Carlo worst-of simulation using public vol/correlation data.
2. **Issuer Adjustment Layer**: Applies issuer-specific skew, correlation haircut,
   funding spread, and margin assumptions.
3. **Calibration Loop**: When you provide a real issuer quote, the model
   back-solves for the implied issuer spread and updates `default.json`.
4. **Output**: An indicative coupon range with explicit assumptions.

## Calibration Rule

Every time you receive a real issuer RFQ:

1. Normalize the quote (same tenor, KI, KO, basket, observation style).
2. Run the mimicry pricer with current assumptions.
3. Compare mimicry output vs. issuer quote.
4. If divergent > 20%, adjust issuer_spread or skew_markup in `default.json`.
5. Log the comparison in `calibration/drift-tracker.md`.

## Disclaimer

> This engine mimics issuer pricing using public data and conservative assumptions.
> It is NOT a substitute for an issuer pricer or firm-approved system.
> Real issuer quotes always override mimicry output.
