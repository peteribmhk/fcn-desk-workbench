# FCN Desk Memory

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

Before suggesting tickers, baskets, KI levels, RFQ wording, or client commentary, future sessions should reread the repo from scratch:

1. `AGENTS.md`
2. `assistant-operating-instructions.md`
3. `desk-memory.md`
4. `SYNC_PROTOCOL.md`
5. `README.md`
6. `methodology.md`
7. `watchlist.csv`
8. `daily/latest.md`
9. `daily/index.md`
10. Relevant recent files under `daily/archive/`
11. `templates/ki-optimization.md`
12. `templates/requote-checklist.md`
13. `research/free-market-data-sources.md`
14. `research/market-data-source-hierarchy.md`

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

---

Append this section to `desk-memory.md`. All items are public-safe: no client data, no issuer/channel quote levels, no firm-confidential material.

## Entry-Quality Framework ("deep drawdown + vol not dispersed")

- Prefer underlyings roughly 20–50% below their 6-month high where 20-day realized vol is still elevated. This is where worst-of coupons screen richest without buying a fresh uptrend top.
- Never anchor KI/strike levels to parabolic or immediately post-event prints. A strike set against a spike high bakes in a reference price the market has already abandoned.
- Conversely, avoid names sitting AT their 6-month high with vol already crushed — the coupon rarely compensates.

## Falling-Knife Rule (2-session stabilization)

- Never anchor strikes on a fresh heavy down day. Wait for two consecutive stabilization sessions (price holds a level, no new low) before activating a basket on a falling name.
- Conditional baskets stay conditional until the stabilization test passes; say so explicitly in the daily output rather than silently re-sending them.

## Post-Earnings Clearance Window

- The best entry is often right AFTER a binary event clears: event risk removed, implied/realized vol residual still pricing rich, and the next scheduled event falls outside a 3M tenor.
- Discipline: hold RFQs into the event ("event hold"), re-mark strikes the morning after ("event cleared"), then apply the stabilization rule if the reaction was sharply negative.

## Worst-of Correlation Tradeoff

- Lower inter-leg correlation raises the worst-of coupon AND delivers genuine diversification.
- Same-sector pairs (correlation often 0.8+) are pseudo-diversification: both legs fall together in a sector shock. Prefer cross-theme pairs (e.g., AI infra + nuclear, semis + software, healthcare high-vol + anchor).

## Event Calendar Discipline

- Before locking any 3M tenor, map earnings, FDA/trial dates, launches, and macro prints (FOMC, payrolls, CPI) falling inside the tenor.
- Treat a known mid-tenor macro event as a one-time shock assumption when sizing KI, not as a reason to abandon the structure.

## Requote Classification Taxonomy

Classify every repeated idea instead of silently re-sending it:

- fresh — new idea or new inputs
- repeat-same-rationale — thesis unchanged, levels re-marked
- repeat-changed-inputs — same names, materially different spot/vol
- structural mismatch — quoted structure differs from screen assumptions
- calibration drift — issuer levels drifting from public-data screen
- event hold — paused into a binary event
- event cleared — resumed after the event, levels re-marked

## Like-for-Like Vol Comparison

- When comparing implied vol day over day, compare the SAME expiry. Switching expiries between readings creates false vol-spike or vol-crush signals.

## Option Expiry Quirks

- Mid-caps frequently skip standard monthly cycles. Always verify available expiries before fetching chains or sending an RFQ. See `reference/option-expiry-quirks.md`.

## Data Hygiene

- Public/free market data is screening evidence only — never present it as a firm quote.
- Free datasources are slow and occasionally drop calls; batch fetches in the background with retry loops, and verify file counts before computing.

## Internal Calibration Sources

- Firm-permitted internal/channel calibration material may be used as a negotiation ruler for what a fair coupon looks like.
- Its actual levels are confidential: never commit them to this public repo. Record only the METHOD (calibrate, classify drift, requote), never the numbers.
