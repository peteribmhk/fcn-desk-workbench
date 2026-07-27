# 01 — AI Continuity Rules

**Version:** v1.0.0  
**Last Updated:** 2026-07-27  
**Read Order:** 1st (always read this first)

---

## Source Of Truth

- Treat GitHub as the persistent source of truth for this workbench.
- Treat the local Codex folder as a cache of GitHub, not as the master copy.
- At the start of a Codex session, run `powershell -ExecutionPolicy Bypass -File scripts/sync-from-github.ps1` before FCN work when shell access is available.
- After durable Codex changes, run `powershell -ExecutionPolicy Bypass -File scripts/publish-to-github.ps1 -Message "Update FCN workbench"` so ChatGPT and future Codex sessions see the same workbench.
- Follow `04-sync-protocol.md` for the GitHub-master sync model.
- When you improve the workflow, instructions, templates, or generator, update the repository files rather than leaving the improvement only in chat.
- Keep `daily/latest.md` phone-readable and public-safe.
- Keep `daily/index.md` and `daily/archive/` as accumulated refresh memory.
- Read `03-desk-memory.md` before FCN picks, refreshes, RFQs, or client explanations.

## Repository Readback And Memory

Before suggesting tickers, basket combinations, KI/KO/tenor settings, RFQ wording, or client commentary, reread the repository memory from scratch:

01. `instructions/current/01-agents.md` (this file)
02. `instructions/current/02-operating-instructions.md`
03. `instructions/current/03-desk-memory.md`
04. `instructions/current/04-sync-protocol.md`
05. `instructions/current/05-methodology.md`
06. `instructions/current/06-data-policy.md`
07. `README.md`
08. `watchlist.csv`
09. `daily/latest.md`
10. `daily/index.md`
11. Relevant recent files under `daily/archive/`
12. `templates/ki-optimization.md`
13. `templates/requote-checklist.md`
14. `templates/pricing-comparison.md`
15. `data-sources/registry.json`
16. `issuer-mimicry/assumptions/default.json`
17. `issuer-mimicry/README.md`

If any required memory file cannot be read, mark the FCN Morning Bell status `AMBER` or `RED` before giving picks.

Every refresh should commit both the latest report and a timestamped archive report to GitHub. Durable user corrections should be saved in public-safe repo files, not left only in the chat.

## User Preference

- Crypto-linked ideas are excluded by default. Do not suggest MSTR, COIN, BTC miners, crypto exchanges, or crypto-beta baskets unless the user explicitly asks to opt in.
- Build a diversified FCN screening universe across AI/semis, software, EV, healthcare/biotech, emerging technology, clean energy, China ADRs, cyclicals, and other high-volatility sectors.
- Treat all output as RFQ screening, not firm pricing or investment advice.

## Profile Verification Gate

Run this gate before every daily refresh, ticker suggestion, basket combination, or client-facing draft:

1. Confirm crypto-linked names are excluded unless the user explicitly opts in.
2. Confirm public/free data is only a screening input, not firm real-time data or issuer pricing.
3. Confirm licensed paid or firm-approved data is used when actually connected, but never by bypassing paywalls, credentials, exchange entitlements, or firm controls.
4. Confirm issuer RFQ or firm pricing-system evidence overrides public-data rankings once terms are normalized.
5. Confirm comparisons normalize tenor, strike/reference, KI, KI observation, KO, KO observation, RO/issue price, coupon frequency, issuer, bid/offer basis, dividends, borrow, funding, correlation, skew, and autocall assumptions.
6. Confirm KI is optimized by coupon pickup per KI point of airbag sacrificed, not by mechanically choosing the lowest KI.
7. Confirm repeat tickers/baskets are checked against prior rationale and classified as fresh, same rationale, changed inputs, structural mismatch, or calibration drift.
8. If any gate fails, say `AMBER` or `BLOCKED` and explain the shortest next action instead of giving confident picks.

## Pricing Discipline

- Public spot and listed-option data are screening inputs only.
- Issuer RFQ levels from UBS, JPM, Marex, Leonteq, or any other issuer override public-data ranking once terms are normalized.
- Before comparing coupon levels, normalize tenor, strike/reference, KI level, KI observation, KO level, KO observation, RO/issue price, coupon frequency, issuer, bid/offer basis, dividends, borrow, funding, correlation, skew, and autocall assumptions.
- Do not store actual issuer quotes, client details, suitability records, or firm-confidential pricing assumptions in this public repo.

## Requote Rule

Before repeating a ticker or basket on a later day:

- Check `daily/latest.md`, `watchlist.csv`, `methodology.md`, `templates/quote-calibration.md`, `templates/requote-checklist.md`, and `issuer-mimicry/calibration/drift-tracker.md`.
- State whether the idea is fresh, repeated with the same rationale, repeated with changed market inputs, or structurally different.
- Compare today's spot/reference, 3M/6M listed-options proxy, liquidity, event risk, tenor, KI, KO, strike/reference, RO, and coupon frequency against the prior rationale.
- If the user provides pricing-system numbers, use them for session calibration, but keep actual quote records in ignored/private storage such as `actual-quotes/`.

## Required Label

Every FCN output must say:

> Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
