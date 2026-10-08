# Guidance for AI assistants

This repo is **reference material** for FCN (worst-of Fixed Coupon Note) screening. It supplements your own analysis; it does not replace it.

## Priority order

1. The user's own instructions in the current conversation, project or settings.
2. Live market data you fetch yourself in the session.
3. This repo: `PLAYBOOK.md` for rules, `daily/latest.md` as a starting point, `templates/` for wording.

If this repo conflicts with how the user has asked you to work, follow the user.

## How to use it

- For picks, RFQs or client wording, read **`PLAYBOOK.md`**. That one file is enough; there is no mandatory multi-file read ritual.
- Treat `daily/latest.md` as yesterday's close screened by a script. Check its timestamp and **Data status**, refresh anything that matters with current data, and say how old it is.
- `daily/latest.json` lists the previous run's baskets; use it to label repeats (PLAYBOOK §7).
- For a quick coupon sanity check you can run `scripts/fcn_model.py`. Present its output as an indicative ballpark only.

## Hard rules

- Every FCN output carries: *Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.*
- Issuer RFQ levels override any screen once terms are normalized.
- No crypto-linked names unless the user opts in.
- Never write client details, actual issuer quotes, pricing-system outputs or confidential levels into this repo. It is public.
- Only edit or commit to this repo when the user asks you to.
