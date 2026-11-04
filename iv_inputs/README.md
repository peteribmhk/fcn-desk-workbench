# Manual IV inputs (local only)

An optional cross-check for the daily screen: implied vol you read yourself from a site you are entitled to use, such as **Market Chameleon**.

## Why this is manual

Market Chameleon's free IV pages are "display only". Its developer page says there is no web/REST API, and that automated collection ("scraping") breaks its Terms of Use and is actively enforced. The only permitted bulk routes are metered CSV downloads for Premium subscribers and paid data feeds (licensed for personal, internal or redistribution use). So the screen **never fetches** Market Chameleon. You read the numbers in your browser (or download your Premium CSV) and put them in a file here.

This repo is public, so everything in this folder except the example is git-ignored, and a run that loads manual IV writes its report to `local/daily/` (also git-ignored) instead of `daily/`.

## How to use it

1. Copy `manual_iv.example.csv` to `manual_iv.csv` in this folder.
2. Fill one row per name you care about:

   | Column | Meaning |
   |---|---|
   | `ticker` | US ticker, e.g. `NVDA` |
   | `date` | The date you read the value, `YYYY-MM-DD`. Rows older than 5 days are ignored. |
   | `iv30` | 30-day IV, as `40.5`, `40.5%` or `0.405` |
   | `iv_6m` | Optional. IV for a ~6M expiry, if you can see a term-structure value |
   | `source` | e.g. `Market Chameleon` |
   | `notes` | Optional |

3. Run the screen on your own PC:

   ```bash
   # cross-check only: adds a "Manual IV30" column and flags gaps > 10 vol points vs the ~3M listed IV
   python scripts/generate_daily_pickings.py

   # use your numbers as the model vol (iv_6m if given, otherwise iv30)
   python scripts/generate_daily_pickings.py --manual-iv-override
   ```

   The report lands in `local/daily/latest.md`.

## Reading the cross-check

- **IV30 is a 30-day measure; the screen prices a 6M note.** A gap between IV30 and the 6M listed IV is often just term structure (for example, an earnings event inside 30 days lifts IV30). Treat a flag as "look at the chain", not "the screen is wrong".
- The override is useful when the listed-options read is missing or clearly broken for a name. For a 6M note, prefer `iv_6m` over `iv30`.
- Market Chameleon's IV30 percentile and 52-week range are a good read on whether a name's vol is rich or cheap compared with its own history. That context belongs in your notes, not in the model.
