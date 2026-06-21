# Mobile And Cloud Workflow

Goal: keep the FCN Desk Workbench usable from a phone or ChatGPT even when the laptop is off.

## Key Point

GitHub stores the project. It does not, by itself, run the project.

If the laptop is off, use one of these cloud paths:

1. **ChatGPT mobile + GitHub repo context** for manual refresh and discussion.
2. **ChatGPT scheduled tasks** for recurring market checks and reminders, if available on the account.
3. **GitHub Actions** for scheduled cloud runs that update files in the repo.
4. **GitHub Codespaces** for a browser-based cloud development environment.

## Recommended V1 Setup

Use this project as a private GitHub repo and access it from ChatGPT mobile:

1. Upload the repo to GitHub as private.
2. In ChatGPT mobile, start a project or chat called `FCN Desk Workbench`.
3. Add or paste the key files:
   - `README.md`
   - `methodology.md`
   - `watchlist.csv`
   - `templates/daily-pickings.md`
   - `templates/rfq-template.md`
   - `templates/client-explanation.md`
4. Use this prompt:

```text
Use my FCN Desk Workbench. Refresh latest public market data for the watchlist, rank high-coupon FCN baskets, suggest tenor/KI/KO/airbag positioning, prepare issuer RFQ wording, and draft bilingual client explanation. Everything must be indicative only, not a firm quote.
```

This works from phone because ChatGPT does the reasoning and live data lookup in the cloud. The laptop does not need to be on.

## What Codex Remote Access Means

Remote Codex access from phone is useful for continuing work on a connected host. However, if the host machine is the source of the files, shell, and local context, that host must remain awake and online.

So for this project's laptop-off goal, do not rely only on local Codex remote access. Put the source files in GitHub and use ChatGPT/cloud execution.

## Optional V2: GitHub Actions Automation

Use GitHub Actions if you want the repo itself to update on schedule.

Possible workflow:

1. A scheduled GitHub Actions job runs after the US close.
2. It fetches public market data from approved/free sources or an API key stored in GitHub Secrets.
3. It writes a new Markdown file under `daily/YYYY-MM-DD.md`.
4. It commits the file back to the private repo.

This requires adding scripts and a workflow file later. It is not part of V1 because the current repo intentionally has no runtime dependency.

## Optional V3: Codespaces

Use GitHub Codespaces if you want an online development environment in the browser. This is useful when you want to edit files, add scripts, or run checks without the laptop.

For phone-only usage, ChatGPT mobile is usually easier than Codespaces. Codespaces is better for editing and running a real project environment.

## Operating Rule

For client-facing use, always keep three layers separate:

1. **Public-data screen**: useful for idea generation.
2. **Issuer RFQ**: source of actual tradable coupon.
3. **Compliance/suitability process**: required before client use.

