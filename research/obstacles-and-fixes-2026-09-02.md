# Obstacles & Fixes — 2026-09-02 Review

Monthly review of the FCN desk workbench: what is blocking us, and the fix for each.

## 1. Watchlist coverage gap (FIXED by this package)

- Problem: `watchlist.csv` had 17 names, but the validated screening universe is now ~60 names across four batches. MU — the anchor of the top-ranked basket for multiple sessions — was not even on the watchlist.
- Fix: append `watchlist-additions.csv` (20 new rows: MU, GLW, MRVL, COHR, ALAB, ARM, VRT, APP, AMAT, CRDO, NBIS, OKLO, ASTS, RGTI, APLD, AVAV, NTLA, TDOC, ISRG, LLY).

## 2. Repo data is structurally one session behind

- Problem: GitHub Actions refresh runs on its schedule; by HK morning the repo's daily screen reflects older data. The morning bell cannot rely on it for pricing.
- Fix: accept the division of labor — the repo is the durable KNOWLEDGE base (methodology, memory, watchlist, templates); the live pricing refresh happens chat-side each morning. Optionally move the Actions cron to ~05:30 HKT (just after US close) so the archive lands before the bell.

## 3. Expiry-assumption fragility in the daily generator

- Problem: `scripts/generate_daily_pickings.py` assumes standard monthly option cycles. Mid-caps skip months (APLD has no 2026-11-20 at all; OKLO/COHR/ALAB/ARM/VRT lack 2027-02-19; RKLB/AVAV lack 2026-11-20) — producing empty chains or silently wrong tenors.
- Fix: `reference/option-expiry-quirks.md` (this package) + a verify-expiries-first step in the fetch routine. Re-verify monthly.

## 4. Stale pairing notes

- Problem: older notes still reference pairings and entry habits that predate the hard lessons (parabolic-print anchoring, fresh falling-knife entries).
- Fix: `desk-memory-addendum.md` (this package) codifies the accumulated rules: entry-quality framework, 2-session stabilization, post-earnings clearance window, correlation tradeoff, requote taxonomy, like-for-like vol comparison.

## 5. No push access from the analysis sandbox

- Problem: the sandbox has no `gh` CLI and no credentials, so repo updates cannot be pushed directly.
- Fix: updates are delivered as this file package. Apply locally (see COMMIT-GUIDE.md) using your existing `setup-git-gh-and-push.md` / `push-to-github.ps1` flow.

## 6. Confidential calibration material must stay out of the public repo

- Problem: issuer/channel calibration prints are marked internal-only; they are essential to our coupon expectations but can never be committed.
- Fix: the repo records the METHOD (calibrate → classify drift → requote), never the levels. This is now explicit in the desk-memory addendum. Not really an obstacle — a guardrail worth keeping visible.

## Not obstacles (by design)

- `/tmp` wiping between sessions: fetch scripts are regenerated each bell; GitHub remains the persistent store. This is the architecture working as intended.
