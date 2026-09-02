# Data Source Infrastructure

This directory manages public market data discovery, health checking, and calculation for the FCN Desk Workbench.

## Philosophy

- **Discover, don't hardcode.** Data source endpoints and availability change. The workbench actively discovers and validates sources.
- **Health is transparent.** Every source has a health status in `registry.json`. AI assistants and GitHub Actions can read it.
- **Fallback is automatic.** If a primary source is down, the system falls back to the next source in the chain.
- **Calculations are isolated.** Each calculator is a standalone module with clear inputs and outputs.

## Directory Structure

```
data-sources/
├── README.md                 # This file
├── registry.json             # Live source registry with health status
├── discovery/
│   ├── nasdaq-scanner.py     # Nasdaq public quote/option scanner
│   ├── yahoo-fallback.py     # Yahoo Finance fallback fetcher
│   ├── fred-proxy.py         # FRED rate data fetcher
│   ├── sec-events.py         # SEC EDGAR earnings/event fetcher
│   └── source-validator.py   # Generic source health validator
├── calculators/
│   ├── iv_surface.py         # Implied vol surface from option chains
│   ├── correlation_proxy.py  # Historical correlation proxy
│   ├── rate_proxy.py         # Risk-free rate and term structure
│   └── fcn_indicative_pricer.py  # Public-data FCN indicative pricer
└── health-check.yml          # GitHub Action workflow (in .github/workflows/)
```

## Registry Format

`registry.json` is the single source of truth for data source status. It is updated by:
- `data-source-health-check.yml` (every 4 hours)
- `discover-data-sources.py` (weekly scan)
- Manual updates when a source changes

## Adding a New Source

1. Add the source to `registry.json` with `status: UNKNOWN`.
2. Write a fetcher in `discovery/`.
3. Add it to the fallback chain in `registry.json`.
4. Update `source-validator.py` to include the new endpoint.
5. Test via GitHub Actions or local run.
6. Update `06-data-policy.md` if the source changes the priority order.
