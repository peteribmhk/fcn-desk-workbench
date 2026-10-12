# Changelog

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
