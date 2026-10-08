# Changelog

## 2026-10-08: Restructure for team use

- **Daily screen rebuilt.** The old generator published the same 10 hard-coded baskets every day. The new one ranks cross-theme 2- and 3-stock baskets from that day's data: drawdown, realized vol, listed-options implied vol, open interest, real correlation, and earnings dates. It applies the falling-knife and event-hold gates, prices a ballpark coupon and KI ladder, and labels repeats against the previous run. Data status (GREEN/AMBER/RED) is computed, not hard-coded.
- **New `scripts/fcn_model.py`.** A dependency-free Monte Carlo ballpark for worst-of FCN coupons. It replaces `issuer-mimicry/` and `data-sources/calculators/`.
- **One rulebook.** `desk-memory.md`, `methodology.md`, `assistant-operating-instructions.md`, `SYNC_PROTOCOL.md` and the duplicate `instructions/` tree are merged into `PLAYBOOK.md`. All the desk rules are kept: entry quality, falling knife, post-earnings window, correlation trade-off, KI value discipline, quote normalization, requote taxonomy, living watchlist.
- **AI guidance slimmed.** `CLAUDE.md` / `AGENTS.md` now treat the repo as reference material behind the user's own instructions and live data. The 14-file read ritual and the "Morning Bell" protocol are removed.
- **Removed:** PowerShell sync/publish scripts, Codex/ChatGPT setup guides, the data-source health-check workflow (it committed noise daily), committed `__pycache__`, old archive reports.
- The previous version is preserved under the branch `legacy-2026-10-08`.
