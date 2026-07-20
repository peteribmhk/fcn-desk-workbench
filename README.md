# FCN Desk Workbench

Public-safe working repository for daily Fixed Coupon Note (FCN) screening, issuer RFQ preparation, and client explanation drafts.

This project is a sales workflow aid, not a tradable pricing system. It uses public or manually entered market context to help judge which baskets may produce higher coupons and whether the structure terms are reasonable. Do not store client-specific information, actual issuer quotes, suitability records, or firm-confidential materials in this public repository.

## Core Disclaimer

All outputs from this workbench are **indicative only, not firm quotes, not investment advice, and not a substitute for an issuer pricer or firm-approved market-data system**.

Before using any result with a client, validate:

- live spot and bid/ask levels,
- issuer pricing and final coupon,
- volatility, dividend, borrow, rate, and funding assumptions,
- product documentation and term sheet,
- suitability, risk disclosure, and internal compliance requirements.

## Continuity And Universe Policy

This repository is the persistent source of truth for future Codex, ChatGPT, Claude, or other AI-assisted work on the FCN desk workflow. Improvements should be committed back into the project files instead of living only in a chat thread.

The workbench should accumulate memory through GitHub:

- `desk-memory.md` stores durable user preferences and workflow rules.
- `SYNC_PROTOCOL.md` defines GitHub as the master copy and Codex as a local cache.
- `daily/latest.md` stores the phone-readable latest refresh.
- `daily/index.md` lists timestamped refresh history.
- `daily/archive/` stores each refresh as a public-safe historical snapshot.

Before giving picks or client-facing wording, the assistant should sync from GitHub when possible and reread the repo memory from scratch instead of relying only on chat memory.

Default screening is **non-crypto**. Do not suggest crypto-linked tickers or baskets unless the user explicitly opts in. The watchlist should stay open-minded and diversified across high-volatility sectors such as AI/semis, software, EV, healthcare/biotech, emerging technology, clean energy, China ADRs, cyclicals, and other liquid names where issuer RFQs may show worthwhile coupon.

Before repeating a ticker or basket from an earlier run, cross-check today's spot, listed-options proxy, liquidity, event risk, and exact requested structure against the prior rationale. If the structure differs by tenor, KI, KO, strike/reference, RO, coupon frequency, or issuer basis, treat it as a structural mismatch until normalized.

## Daily Workflow

Morning readiness hint:

```text
FCN Morning Bell
```

Expected assistant response:

- `FCN Morning Bell: GREEN` means today's Hong Kong-date report is current/refreshed and the assistant has reloaded the project rules.
- `FCN Morning Bell: AMBER` means the repo is readable but the report is stale, refresh access is missing, or market data could not be refreshed.
- `FCN Morning Bell: RED` means the assistant cannot access the project instructions/report or cannot safely separate public screens from issuer quote evidence.

Before giving any picks, the assistant must state the Hong Kong date, `daily/latest.md` timestamp, public-data caveat, and that issuer RFQ levels override public-data screens.

Use this prompt in Codex:

```text
Use `AGENTS.md` and `assistant-operating-instructions.md` first, then refresh FCN market data using the FCN Desk Workbench. Screen the non-crypto diversified watchlist for RFQ candidates, use listed-options vol proxy only as a public screening input, compare any real issuer quotes after normalizing RO/KO/KI/strike/tenor, cross-check repeat tickers against prior rationale, optimize KI by coupon pickup per KI point, prepare issuer RFQ wording, and draft client explanation. Label everything indicative only.
```

Expected output:

1. Profile verification gate: user preference, evidence quality, issuer quote override, structure normalization, KI value discipline, repeat discipline, and persistence.
2. Market snapshot with timestamp and source caveats.
3. RFQ candidate screen, not a coupon prediction.
4. Listed-options vol/liquidity proxy read.
5. Ballpark annualized coupon range for each idea, clearly labeled as indicative.
6. Pricing-system verified number field for user calibration.
7. Coupon driver explanation, with issuer quote evidence overriding public-data screens.
8. Suggested tenor, KO, KI, and airbag positioning.
9. KI ladder optimization view.
10. Requote rationale check for any repeated ticker or basket.
11. Key downside risks.
12. Issuer RFQ wording.
13. Short Chinese/English client explanation.

## Cloud Runtime And Phone Interface

This repo now includes a GitHub Actions cloud runtime:

- Workflow: `.github/workflows/fcn-daily-report.yml`
- Generator: `scripts/generate_daily_pickings.py`
- Codex sync script: `scripts/sync-from-github.ps1`
- Codex publish script: `scripts/publish-to-github.ps1`
- Phone-readable report: `daily/latest.md`
- Refresh archive index: `daily/index.md`
- Timestamped refresh history: `daily/archive/`

The workflow runs at **08:30 Hong Kong time, Monday-Friday**, and can also be started manually from the GitHub **Actions** tab. It does not require your laptop to be on.

The generator tries free/public delayed quote sources in this order: Nasdaq public quote endpoint, Yahoo Finance public chart endpoint, then Stooq daily CSV fallback. It also uses Nasdaq public option-chain data for an indicative ATM straddle/liquidity proxy. These are not firm real-time exchange feeds.

If licensed paid or firm-approved data is connected later, the workbench should use that higher-quality source first and state the source/timestamp clearly. Paid resources must be accessed only through authorized API keys, terminal/API connections, broker APIs, or user-supplied firm-approved figures. Do not bypass paywalls, credentials, exchange entitlements, or firm data controls.

Phone link:

```text
https://github.com/peteribmhk/fcn-desk-workbench/blob/main/daily/latest.md
```
## Project Files

- `AGENTS.md`: first-read continuity rules for future AI assistants.
- `assistant-operating-instructions.md`: persistent instructions for future ChatGPT/Codex sessions.
- `desk-memory.md`: durable user preferences, verification loop, and public-safe memory rules.
- `SYNC_PROTOCOL.md`: GitHub-master synchronization protocol for Codex and ChatGPT usage.
- `watchlist.csv`: default high-volatility ticker universe and basket ideas.
- `methodology.md`: decision rules for ranking FCN baskets and judging structure terms.
- `templates/daily-pickings.md`: daily output template.
- `templates/rfq-template.md`: issuer RFQ template.
- `templates/client-explanation.md`: bilingual client explanation blocks.
- `templates/ki-optimization.md`: KI ladder and coupon-pickup comparison template.
- `templates/requote-checklist.md`: repeat-ticker/rationale cross-check template.
- `samples/sample-daily-pickings.md`: example output format using qualitative assumptions.
- `mobile-cloud-workflow.md`: how to use this project from phone/ChatGPT when the laptop is off.
- `.github/workflows/fcn-daily-report.yml`: cloud runtime for scheduled reports.
- `scripts/generate_daily_pickings.py`: dependency-free report generator.
- `scripts/sync-from-github.ps1`: align local Codex workspace to GitHub master copy.
- `scripts/publish-to-github.ps1`: publish durable Codex changes back to GitHub.
- `daily/latest.md`: phone-readable latest report.
- `daily/index.md`: archive index generated by the refresh workflow.
- `daily/archive/`: timestamped refresh reports generated by the refresh workflow.
- `research/free-market-data-sources.md`: GitHub/open-source and free-data source review.
- `research/market-data-source-hierarchy.md`: paid/public/firm data-source priority rule for future refreshes.

## GitHub Upload

Current repo setting: **public**.

Because this first version is Markdown/CSV only, upload the `fcn-desk-workbench` folder directly through GitHub web UI if you are recreating it:

1. Create a new GitHub repository named `fcn-desk-workbench`.
2. Upload all files and folders from this directory.
3. Commit with message: `Initial FCN desk workbench`.
4. Keep client names, account details, actual issuer quotes, and suitability records out of the repo, especially when the repo is public.
allow reas and write