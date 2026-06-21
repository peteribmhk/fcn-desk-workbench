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

Use this prompt in Codex:

```text
Refresh FCN market data using the FCN Desk Workbench. Screen the watchlist, rank the best high-coupon baskets, suggest tenor/KI/KO/airbag positioning, prepare issuer RFQ wording, and draft client explanation. Label everything indicative only.
```

Expected output:

1. Market snapshot with timestamp and source caveats.
2. High-coupon basket ranking.
3. Coupon driver explanation.
4. Suggested tenor, KO, KI, and airbag positioning.
5. Key downside risks.
6. Issuer RFQ wording.
7. Short Chinese/English client explanation.

## Project Files

- `watchlist.csv`: default high-volatility ticker universe and basket ideas.
- `methodology.md`: decision rules for ranking FCN baskets and judging structure terms.
- `templates/daily-pickings.md`: daily output template.
- `templates/rfq-template.md`: issuer RFQ template.
- `templates/client-explanation.md`: bilingual client explanation blocks.
- `samples/sample-daily-pickings.md`: example output format using qualitative assumptions.
- `mobile-cloud-workflow.md`: how to use this project from phone/ChatGPT when the laptop is off.

## GitHub Upload

Current repo setting: **public**.

Because this first version is Markdown/CSV only, upload the `fcn-desk-workbench` folder directly through GitHub web UI if you are recreating it:

1. Create a new GitHub repository named `fcn-desk-workbench`.
2. Upload all files and folders from this directory.
3. Commit with message: `Initial FCN desk workbench`.
4. Keep client names, account details, actual issuer quotes, and suitability records out of the repo, especially when the repo is public.
