# Changelog

## 2026-11-06: Valuation floor check

- **Valuation cross-check in the daily screen.** New `fundamentals/valuation.csv` holds each name's forward multiple against its own 10-year range, the median analyst target and consensus revenue growth. The screen labels every leg (supported / target below price / rich vs own history / neutral), adds a "Valuation cross-check" section for the legs in today's picks and a `Valuation` column in the full screen, and flags names more than 50% off their high with no valuation support for a thesis check. Non-blocking: no name is removed. Missing file = old behaviour. Guide: `fundamentals/README.md`.
- **Watchlist round 3:** DXCM, ZBH, ZS, BE (see `watchlist-changelog.md`). DXCM and ZBH give the screen mid-vol medtech defensive legs; the health bucket previously held only high-vol biotech.
- PLAYBOOK §2 gains the "Valuation floor check"; §11 asks for a valuation read when adding names.

## 2026-11-04: Implied vol sources

- **Tradier/ORATS IV in the daily screen.** When a `TRADIER_TOKEN` secret is set (a free sandbox token works), the screen takes ORATS smoothed ATM implied vol for the ~3M and ~6M expiries, ATM open interest, and a 6M skew read (80% put minus ATM). Nasdaq straddle IV is still fetched as the fallback and shown as a cross-check; gaps above 10 vol points are flagged. Without a token the screen behaves exactly as before. Setup: `research/data-sources.md`.
- **Manual IV cross-check (local only).** `iv_inputs/manual_iv.csv` takes IV you read yourself, such as Market Chameleon IV30. Market Chameleon is display-only and forbids scraping, so the screen never fetches it. The file is git-ignored, and a run that loads it writes to `local/daily/` (also git-ignored). `--manual-iv-override` uses those values as the model vol. Guide: `iv_inputs/README.md`.
- Full screen table gains `Vol src` (plus `Straddle IV`, `6M skew 80-ATM` and `Manual IV30` when available); Data notes count names by vol source and report Tradier status.
- `research/data-sources.md`: Tradier setup, Market Chameleon terms, Massive Basic has no IV snapshot.

## 2026-10-12: Research pack and model conventions

- Added `research/fcn-pricing-logic.md` (how the coupon is built, lever directions with model examples, US vs Asian conventions, why issuers differ, RFQ best practices), `research/data-sources.md` (free, keyed, paid and institutional data; SEC EDGAR 424B2 as a public calibration source) and `research/resources.md` (open-source pricers, libraries, learning, SFC/FINRA regulation).
- `scripts/fcn_model.py` now supports a strike below 100%, a daily-close KI and strike-only FCNs (`--strike`, `--ki-style`, `--ladder`, `--ko-start`).
- PLAYBOOK: §5 conventions, §10 model usage, new §12 screening requirements (risk-controlled default, tech-growth template, exclusion switches), new §13 pricing logic summary. Corrected the non-call period effect: a longer non-call period lowers the p.a. coupon.
- Daily screen: runs at 06:17 HKT, lists every held-back name, and saves per-name metrics in `daily/latest.json`.

## 2026-10-08: Restructure for team use

- **Daily screen rebuilt.** The old generator published the same 10 hard-coded baskets every day. The new one ranks cross-theme 2- and 3-stock baskets from that day's data: drawdown, realized vol, listed-options implied vol, open interest, real correlation, and earnings dates. It applies the falling-knife and event-hold gates, prices a ballpark coupon and KI ladder, and labels repeats against the previous run. Data status (GREEN/AMBER/RED) is computed, not hard-coded.
- **New `scripts/fcn_model.py`.** A dependency-free Monte Carlo ballpark for worst-of FCN coupons. It replaces `issuer-mimicry/` and `data-sources/calculators/`.
- **One rulebook.** `desk-memory.md`, `methodology.md`, `assistant-operating-instructions.md`, `SYNC_PROTOCOL.md` and the duplicate `instructions/` tree are merged into `PLAYBOOK.md`. All the desk rules are kept: entry quality, falling knife, post-earnings window, correlation trade-off, KI value discipline, quote normalization, requote taxonomy, living watchlist.
- **AI guidance slimmed.** `CLAUDE.md` / `AGENTS.md` now treat the repo as reference material behind the user's own instructions and live data. The 14-file read ritual and the "Morning Bell" protocol are removed.
- **Removed:** PowerShell sync/publish scripts, Codex/ChatGPT setup guides, the data-source health-check workflow (it committed noise daily), committed `__pycache__`, old archive reports.
- The previous version is preserved under the branch `legacy-2026-10-08`.
