# Mobile And Cloud Workflow

Goal: keep the FCN Desk Workbench usable from a phone or ChatGPT even when the laptop is off.

## Key Point

GitHub stores the project. It does not, by itself, run the project.

If the laptop is off, use one of these cloud paths:

1. **ChatGPT mobile + GitHub repo context** for manual refresh and discussion.
2. **ChatGPT scheduled tasks** for recurring market checks and reminders, if available on the account.
3. **GitHub Actions** for scheduled cloud runs that update files in the repo.
4. **GitHub Codespaces** for a browser-based cloud development environment.

## Installed In This Repo

This repo includes the recommended cloud runtime and phone interface:

- **Cloud runtime:** GitHub Actions workflow `.github/workflows/fcn-daily-report.yml`
- **Report generator:** `scripts/generate_daily_pickings.py`
- **Codex sync:** `scripts/sync-from-github.ps1`
- **Codex publish:** `scripts/publish-to-github.ps1`
- **Phone-readable report:** `daily/latest.md`
- **Refresh memory:** `daily/index.md` and timestamped reports under `daily/archive/`
- **Durable profile:** `desk-memory.md`
- **Sync protocol:** `SYNC_PROTOCOL.md`

The workflow runs at 08:30 Hong Kong time, Monday-Friday, and can also be run manually from GitHub's **Actions** tab.

Open from phone:

```text
https://github.com/peteribmhk/fcn-desk-workbench/blob/main/daily/latest.md
```

Open refresh history from phone:

```text
https://github.com/peteribmhk/fcn-desk-workbench/blob/main/daily/index.md
```

## Recommended V1 Setup

Use this project as a GitHub repo and access it from ChatGPT mobile:

1. Upload the repo to GitHub. If it is public, keep it sanitized and template-only.
2. In ChatGPT mobile, start a project or chat called `FCN Desk Workbench`.
3. Add or paste the key files:
   - `assistant-operating-instructions.md`
   - `README.md`
   - `methodology.md`
   - `watchlist.csv`
   - `desk-memory.md`
   - `daily/latest.md`
   - `daily/index.md`
   - `templates/daily-pickings.md`
   - `templates/rfq-template.md`
   - `templates/client-explanation.md`
   - `templates/ki-optimization.md`
   - `research/free-market-data-sources.md`
4. Use this prompt:

```text
Use my FCN Desk Workbench and read assistant-operating-instructions.md, AGENTS.md, desk-memory.md, daily/latest.md, and daily/index.md first. Refresh latest public market data for the watchlist, save the refresh back to GitHub if you have write access, use the listed-options vol proxy only as a public screening input, screen RFQ candidates rather than predicting coupons, normalize any real issuer quotes by RO/KO/KI/strike/tenor, optimize KI by coupon pickup per KI point, suggest tenor/KI/KO/airbag positioning, prepare issuer RFQ wording, and draft bilingual client explanation. Everything must be indicative only, not a firm quote.
```

This works from phone because ChatGPT does the reasoning and live data lookup in the cloud. The laptop does not need to be on.

For Codex, use GitHub as the master copy. At the start of a Codex session, run `scripts/sync-from-github.ps1`; after durable Codex changes, run `scripts/publish-to-github.ps1`.

## Morning Readiness Hint

Use this quick prompt each morning:

```text
FCN Morning Bell
```

The assistant should reply with one of:

- `FCN Morning Bell: GREEN` - project rules loaded, Hong Kong date checked, latest report current/refreshed, and ready to proceed.
- `FCN Morning Bell: AMBER` - project readable but report/data refresh is stale or unavailable; proceed only with caveats or trigger refresh first.
- `FCN Morning Bell: RED` - project/report unavailable or rules cannot be verified; do not use for daily picks yet.

The reply must include the report timestamp, source caveat, and reminder that issuer RFQ levels override public-data screens.

## What Codex Remote Access Means

Remote Codex access from phone is useful for continuing work on a connected host. However, if the host machine is the source of the files, shell, and local context, that host must remain awake and online.

So for this project's laptop-off goal, do not rely only on local Codex remote access. Put the source files in GitHub and use ChatGPT/cloud execution.

## Optional V2: GitHub Actions Automation

Use GitHub Actions if you want the repo itself to update on schedule.

Possible workflow:

1. A scheduled GitHub Actions job runs after the US close.
2. It fetches public market data from approved/free sources or an API key stored in GitHub Secrets.
3. It writes a new Markdown file under `daily/archive/YYYY-MM-DD-HHMM-HKT.md`.
4. It updates `daily/latest.md` and `daily/index.md`.
5. It commits the files back to the repo.

The current repo already includes this basic GitHub Actions path using public/free sources only. Treat the output as screening, not issuer pricing.

## Optional V3: Codespaces

Use GitHub Codespaces if you want an online development environment in the browser. This is useful when you want to edit files, add scripts, or run checks without the laptop.

For phone-only usage, ChatGPT mobile is usually easier than Codespaces. Codespaces is better for editing and running a real project environment.

## Operating Rule

For client-facing use, always keep three layers separate:

1. **Public-data screen**: useful for idea generation.
2. **Issuer RFQ**: source of actual tradable coupon.
3. **Compliance/suitability process**: required before client use.
