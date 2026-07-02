# FCN Desk Memory

This file stores durable, public-safe instructions learned from the user's FCN workflow. Future ChatGPT/Codex sessions should reread it before daily picks, refreshes, RFQs, or client explanation drafts.

## Core User Profile

- The user is a Hong Kong securities salesperson using this repo for FCN idea screening, issuer RFQ preparation, and client-facing explanation drafts.
- The goal is a phone-accessible workflow that still works when the laptop is off.
- GitHub is the persistent source of truth. GitHub Actions is the cloud refresh runtime.
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

Before suggesting tickers, baskets, KI levels, RFQ wording, or client commentary, future sessions should reread the repo from scratch:

1. `AGENTS.md`
2. `assistant-operating-instructions.md`
3. `desk-memory.md`
4. `README.md`
5. `methodology.md`
6. `watchlist.csv`
7. `daily/latest.md`
8. `daily/index.md`
9. Relevant recent files under `daily/archive/`
10. `templates/ki-optimization.md`
11. `templates/requote-checklist.md`
12. `research/free-market-data-sources.md`

If these files cannot be read, mark the morning status `AMBER` or `RED` rather than giving confident picks.

## Verification Loop

Every daily output should include a profile verification gate covering:

- user preference: crypto excluded unless explicitly opted in,
- evidence quality: public data is only screening,
- issuer quote override: normalized issuer RFQ controls,
- structure normalization: tenor, strike/reference, KI, KI observation, KO, KO observation, RO/issue price, coupon frequency, issuer, bid/offer, dividends, borrow, funding, correlation, skew, and autocall assumptions,
- KI value discipline: coupon pickup per KI point,
- repeat discipline: fresh idea versus repeated rationale, changed inputs, structural mismatch, or calibration drift,
- persistence: reusable corrections should update the repo instead of staying only in chat.

## What To Save

Save public-safe workflow improvements, watchlist logic, methodology changes, daily public-data screens, and non-confidential lessons learned from the user's preferences.

## What Not To Save

Do not save actual client information, suitability assessments, account details, issuer quote screenshots, firm pricing-system outputs, confidential bank levels, compliance notes, or any non-public information in this public repo.
