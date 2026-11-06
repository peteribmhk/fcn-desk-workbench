# Valuation cross-check

`valuation.csv` feeds the **Valuation cross-check** in the daily screen (PLAYBOOK §2, "Valuation floor check"). It answers one question: if a note is struck and the client receives the worst leg, is that a price we would be happy to own?

The check is **non-blocking**. It labels names; it never removes them from the screen.

## Columns

| Column | Meaning |
|---|---|
| `ticker` | Must match `watchlist.csv` |
| `as_of` | Date of the figures (YYYY-MM-DD). Rows older than 45 days are marked `[stale]` |
| `metric` | Forward multiple used: P/E for profitable names, P/S for loss-making, EV/EBITDA for capital-intensive |
| `current` | Current forward multiple |
| `p10`, `p25`, `median` | 10th / 25th / 50th percentile of the name's own 10-year range for that multiple |
| `price`, `target_median` | Price on `as_of` and median analyst target |
| `rev_g_next`, `rev_g_next2` | Consensus revenue growth (%), next year and the year after |
| `caveat` | Anything that weakens the read (short history, unclear basis). Shown as `*` in the report |
| `source` | Where the figures came from. Public or consensus data only |

## Labels

| Label | Rule |
|---|---|
| supported | Below its own p25, target above price, revenue growing |
| target below price | Median analyst target at or below the price: weak floor |
| rich vs own history | Above its own 10-year median |
| neutral | Anything else |

A name more than 50% below its 6-month high that is not `supported` is flagged **thesis check** in the report.

## Keeping it fresh

Update the rows at least monthly and after each earnings print. This repo is public: only public or consensus figures, never firm research, pricing-system outputs or client material.
