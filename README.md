# FCN Desk Workbench

A shared toolkit for screening **worst-of Fixed Coupon Notes (FCNs) on US stocks**: desk rules, a daily data-driven basket screen, a ballpark coupon model, and ready-to-use RFQ and client-explanation templates.

> **Indicative only. Not a firm quote. Not investment advice.** Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems. This repo is public: never commit client details, actual issuer quotes or firm-confidential material.

## Start here

| You want to… | Open |
|---|---|
| See today's screened baskets on your phone | [`daily/latest.md`](daily/latest.md) |
| Learn the desk rules (entry quality, KI ladder, event holds, quote comparison) | [`PLAYBOOK.md`](PLAYBOOK.md) |
| Send an RFQ | [`templates/rfq-template.md`](templates/rfq-template.md) |
| Explain an idea to a client (EN / 中文) | [`templates/client-explanation.md`](templates/client-explanation.md) |
| Choose a KI level from an issuer ladder | [`templates/ki-optimization.md`](templates/ki-optimization.md) |
| Check an idea you suggested before | [`templates/requote-checklist.md`](templates/requote-checklist.md) |
| Compare a quote with the ballpark | [`templates/quote-calibration.md`](templates/quote-calibration.md) |
| See the candidate universe | [`watchlist.csv`](watchlist.csv) and [`watchlist-changelog.md`](watchlist-changelog.md) |

## The daily screen

A GitHub Action runs every weekday at about **08:30 Hong Kong time**, after the US close, and publishes [`daily/latest.md`](daily/latest.md). Past runs are kept in [`daily/archive/`](daily/index.md).

What it does, using free public data:

1. For every watchlist name: last price, 1-day move, distance from the 6-month high, 20-day realized vol, implied vol from listed ATM straddles, option open interest, next earnings date.
2. Holds back names that fail a gate: fresh heavy drop (falling-knife rule), earnings within two weeks, thin options, or extreme vol.
3. Builds **cross-theme 2-stock and 3-stock baskets**, using real correlation from price history, across risk profiles (balanced / higher coupon / aggressive), plus a familiar-name anchor.
4. Prices each basket with the ballpark model (6M, KO 100% monthly, KI ladder 50/55/59/65/70 at maturity), shows the KI pickup per point, and labels repeats versus the previous run.

The **Data status** line tells you whether to trust a run: GREEN means good coverage, AMBER means partial data (use with care), and RED means no picks were produced.

To refresh manually: GitHub → **Actions** → **FCN Daily Screen** → **Run workflow**.

## Using it with Claude (or another AI assistant)

Point the assistant at this repo or paste the relevant file. It works best as **reference material**: the assistant should still pull today's market data itself and use its own judgment. [`CLAUDE.md`](CLAUDE.md) tells AI assistants how to use the repo without letting it override your own instructions.

Example prompt:

```text
Using the FCN Desk Workbench playbook (github.com/peteribmhk/fcn-desk-workbench), give me today's FCN picks
on US stocks: 2–3 names per basket, across risk profiles, with ballpark coupons, KI ladder view, risks and RFQ wording.
```

## Ballpark model

```bash
python scripts/fcn_model.py --vols 0.55 0.45 --corr 0.4 --tenor 6
```

The model prints a coupon range, the KO probability, the probability of loss at maturity, and the expected life for each KI level. It has no dependencies and works with plain Python 3.10+. Its limits are listed in `PLAYBOOK.md` §10.

## Folder map

```text
PLAYBOOK.md                 desk rules (the core of the repo)
CLAUDE.md / AGENTS.md       guidance for AI assistants
watchlist.csv               candidate pool (living, see PLAYBOOK §11)
watchlist-changelog.md      every add / freeze / removal with reason
reference/                  option-expiry quirks, event calendar
templates/                  RFQ, client explanation, KI ladder, requote, calibration
scripts/fcn_model.py        ballpark worst-of FCN coupon model
scripts/generate_daily_pickings.py   daily screen (run by GitHub Actions)
daily/                      latest report, JSON record, archive
```

## Contributing

- Improve the rules in `PLAYBOOK.md`; keep it short and practical.
- Log watchlist changes in `watchlist-changelog.md` with a reason.
- To edit the screen's thresholds, change the settings block at the top of `scripts/generate_daily_pickings.py`, then test it without network:
  `python scripts/generate_daily_pickings.py --fixture your_saved_data.json --out /tmp/test`
- Keep anything confidential out. The `actual-quotes/`, `client-notes/` and `suitability-records/` folders are git-ignored for local use only.

The pre-restructure version of this repo is preserved under the branch `legacy-2026-10-08`.
