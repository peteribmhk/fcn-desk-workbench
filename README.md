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
Use `assistant-operating-instructions.md` first, then refresh FCN market data using the FCN Desk Workbench. Screen the watchlist for RFQ candidates, use listed-options vol proxy only as a public screening input, compare any real issuer quotes after normalizing RO/KO/KI/strike/tenor, optimize KI by coupon pickup per KI point, prepare issuer RFQ wording, and draft client explanation. Label everything indicative only.
```

Expected output:

1. Market snapshot with timestamp and source caveats.
2. RFQ candidate screen, not a coupon prediction.
3. Listed-options vol/liquidity proxy read.
4. Ballpark annualized coupon range for each idea, clearly labeled as indicative.
5. Pricing-system verified number field for user calibration.
6. Coupon driver explanation, with issuer quote evidence overriding public-data screens.
7. Suggested tenor, KO, KI, and airbag positioning.
8. KI ladder optimization view.
9. Key downside risks.
10. Issuer RFQ wording.
11. Short Chinese/English client explanation.

## Cloud Runtime And Phone Interface

This repo now includes a GitHub Actions cloud runtime:

- Workflow: `.github/workflows/fcn-daily-report.yml`
- Generator: `scripts/generate_daily_pickings.py`
- Phone-readable report: `daily/latest.md`

The workflow runs at **08:30 Hong Kong time, Monday-Friday**, and can also be started manually from the GitHub **Actions** tab. It does not require your laptop to be on.

The generator tries free/public delayed quote sources in this order: Nasdaq public quote endpoint, Yahoo Finance public chart endpoint, then Stooq daily CSV fallback. It also uses Nasdaq public option-chain data for an indicative ATM straddle/liquidity proxy. These are not firm real-time exchange feeds.

Phone link:

```text
https://github.com/peteribmhk/fcn-desk-workbench/blob/main/daily/latest.md
```

## Project Files

- `assistant-operating-instructions.md`: persistent instructions for future ChatGPT/Codex sessions.
- `watchlist.csv`: default high-volatility ticker universe and basket ideas.
- `methodology.md`: decision rules for ranking FCN baskets and judging structure terms.
- `templates/daily-pickings.md`: daily output template.
- `templates/rfq-template.md`: issuer RFQ template.
- `templates/client-explanation.md`: bilingual client explanation blocks.
- `templates/ki-optimization.md`: KI ladder and coupon-pickup comparison template.
- `samples/sample-daily-pickings.md`: example output format using qualitative assumptions.
- `mobile-cloud-workflow.md`: how to use this project from phone/ChatGPT when the laptop is off.
- `.github/workflows/fcn-daily-report.yml`: cloud runtime for scheduled reports.
- `scripts/generate_daily_pickings.py`: dependency-free report generator.
- `daily/latest.md`: phone-readable latest report.
- `research/free-market-data-sources.md`: GitHub/open-source and free-data source review.

## GitHub Upload

Current repo setting: **public**.

Because this first version is Markdown/CSV only, upload the `fcn-desk-workbench` folder directly through GitHub web UI if you are recreating it:

1. Create a new GitHub repository named `fcn-desk-workbench`.
2. Upload all files and folders from this directory.
3. Commit with message: `Initial FCN desk workbench`.
4. Keep client names, account details, actual issuer quotes, and suitability records out of the repo, especially when the repo is public.
