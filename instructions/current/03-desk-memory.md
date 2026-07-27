# 03 — Desk Memory

**Version:** v1.0.0  
**Last Updated:** 2026-07-27  
**Read Order:** 3rd

---

This file stores durable, public-safe instructions learned from the user's FCN workflow. Future ChatGPT/Codex sessions should reread it before daily picks, refreshes, RFQs, or client explanation drafts.

## Core User Profile

- The user is a Hong Kong securities salesperson using this repo for FCN idea screening, issuer RFQ preparation, and client-facing explanation drafts.
- The goal is a phone-accessible workflow that still works when the laptop is off.
- GitHub is the persistent source of truth. GitHub Actions is the cloud refresh runtime.
- Codex local folders are caches of GitHub, not the master copy.
- Codex should run `scripts/sync-from-github.ps1` before FCN work and `scripts/publish-to-github.ps1` after durable repo changes.
- The repo is public-safe. Do not store client data, suitability records, actual issuer quotes, firm pricing-system screenshots, or confidential issuer assumptions here.

## Durable Preferences

- Exclude crypto-linked names by default. Do not suggest MSTR, COIN, BTC miners, crypto exchanges, or crypto-beta baskets unless the user explicitly opts in.
- Prefer diversified high-volatility US-listed equities where issuer RFQs may show worthwhile FCN coupons.
- Treat public/free market data as screening evidence only. It is not a firm quote, not guaranteed real time, and not a replacement for issuer pricing.
- Real issuer RFQ or firm-approved pricing-system levels override public-data rankings after structure terms are normalized.

## KI Value Discipline

The user does not want the lowest KI level by habit. The preferred method is value optimization:

1. Request KI ladder levels such as 50 / 55 / 59 / 65 / 70.
2. Compare coupon pickup per KI point of airbag sacrificed.
3. Keep the lower KI if coupon pickup is flat or weak.
4. Accept a higher KI if the coupon pickup is meaningfully better and the risk trade-off is clear.
5. Explain the chosen level as a balance between downside protection, coupon sacrificed, and client risk appetite.

## Refresh Memory Rule

Every refresh should save new information back to GitHub:

- `daily/latest.md` remains the phone-readable latest report.
- `daily/archive/YYYY-MM-DD-HHMM-HKT.md` stores each refresh as timestamped history.
- `daily/index.md` lists recent archived refreshes.
- `data-sources/registry.json` should be updated if source health changed.
- `issuer-mimicry/calibration/drift-tracker.md` should be updated if calibration data changed.

Before suggesting tickers, baskets, KI levels, RFQ wording, or client commentary, future sessions should reread the repo from scratch:

01. `instructions/current/01-agents.md`
02. `instructions/current/02-operating-instructions.md`
03. `instructions/current/03-desk-memory.md` (this file)
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

If these files cannot be read, mark the morning status `AMBER` or `RED` rather than giving confident picks.

## Verification Loop

Every daily output should include a profile verification gate covering:

- user preference: crypto excluded unless explicitly opted in,
- evidence quality: public data is only screening,
- paid-source access: use licensed paid or firm-approved sources when connected, but do not bypass paywalls, credentials, exchange entitlements, or firm controls,
- issuer quote override: normalized issuer RFQ controls,
- structure normalization: tenor, strike/reference, KI, KI observation, KO, KO observation, RO/issue price, coupon frequency, issuer, bid/offer, dividends, borrow, funding, correlation, skew, and autocall assumptions,
- KI value discipline: coupon pickup per KI point,
- repeat discipline: fresh idea versus repeated rationale, changed inputs, structural mismatch, or calibration drift,
- persistence: reusable corrections should update the repo instead of staying only in chat.

## What To Save

Save public-safe workflow improvements, watchlist logic, methodology changes, daily public-data screens, and non-confidential lessons learned from the user's preferences.

## What Not To Save

Do not save actual client information, suitability assessments, account details, issuer quote screenshots, firm pricing-system outputs, confidential bank levels, compliance notes, or any non-public information in this public repo.
