# 04 — Sync Protocol

**Version:** v1.0.0  
**Last Updated:** 2026-07-27  
**Read Order:** 4th

---

## GitHub Master Sync Protocol

GitHub is the master copy for the FCN Desk Workbench. Codex, ChatGPT, and any other assistant should behave as clients of the same cloud workbench, not as separate sources of truth.

## Source Of Truth

- Master repo: `https://github.com/peteribmhk/fcn-desk-workbench`
- Master branch: `main`
- Local Codex folder: a cache of the GitHub repo, not the master copy.
- Durable user preferences and workflow rules belong in repo files such as `instructions/current/03-desk-memory.md`, `instructions/current/01-agents.md`, `instructions/current/02-operating-instructions.md`, `instructions/current/05-methodology.md`, and templates.
- Daily public-data refresh history belongs in `daily/latest.md`, `daily/index.md`, and `daily/archive/`.
- Data source health belongs in `data-sources/registry.json`.
- Issuer mimicry calibration belongs in `issuer-mimicry/calibration/`.

## Start Of Every Codex Session

Before FCN work, Codex should run:

```
powershell -ExecutionPolicy Bypass -File scripts/sync-from-github.ps1
```

Then reread the project memory:

01. `instructions/current/01-agents.md`
02. `instructions/current/02-operating-instructions.md`
03. `instructions/current/03-desk-memory.md`
04. `instructions/current/04-sync-protocol.md` (this file)
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

If sync or readback fails, mark the FCN Morning Bell status `AMBER` or `RED` before giving picks.

## After Codex Makes Durable Changes

If Codex changes workflow files, memory, templates, watchlists, scripts, or workflows, publish back to GitHub immediately:

```
powershell -ExecutionPolicy Bypass -File scripts/publish-to-github.ps1 -Message "Update FCN workbench"
```

Do not leave durable improvements only in the current chat or local Codex folder.

## Conflict Policy

- GitHub `main` wins as the master copy.
- `sync-from-github.ps1` preserves local uncommitted work in a Git stash before aligning to GitHub.
- `sync-from-github.ps1` preserves a local backup branch before moving local `main` to GitHub `main`.
- `publish-to-github.ps1` first tries normal Git push.
- If normal Git push fails because of Windows/GitHub transport resets, `publish-to-github.ps1` uses the GitHub API fallback to publish the same tracked local file state to GitHub.

## Public Repo Hygiene

Do not publish client names, account details, suitability records, actual issuer quote screenshots, firm pricing-system outputs, confidential issuer levels, or private compliance notes to this public repo.

Actual issuer/pricing-system numbers may be used for session calibration, but should not be committed here unless the repo is made private and approved for that data.
