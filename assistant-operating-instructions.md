# Assistant Operating Instructions

Use this file at the start of every future ChatGPT/Codex session for this FCN Desk Workbench. The user should not need to re-explain the workflow each time.

## User Goal

The user is a Hong Kong securities salesperson using this project for daily Fixed Coupon Note idea screening, issuer RFQ preparation, and client-facing explanation drafts.

The long-term goal is phone-accessible operation while the laptop is off. Therefore:

- GitHub is the source of truth for the workbench.
- GitHub Actions is the cloud runtime for scheduled refreshes.
- `daily/latest.md` is the phone-readable output.
- ChatGPT/Codex should use the repo files as persistent memory.

## Always Read First

When asked for FCN picks, refreshes, RFQs, or client explanations, read these files first:

1. `README.md`
2. `methodology.md`
3. `watchlist.csv`
4. `daily/latest.md`
5. `templates/ki-optimization.md`
6. `research/free-market-data-sources.md`

If editing the project or cloud workflow, also read:

1. `.github/workflows/fcn-daily-report.yml`
2. `scripts/generate_daily_pickings.py`
3. `mobile-cloud-workflow.md`

## Non-Negotiable Labels

Every FCN output must clearly state:

> Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.

Do not describe public web data as firm real-time exchange data. Public/free sources may be delayed, unofficial, rate-limited, or changed without notice.

## Market Data Policy

Use the current dependency-free source stack:

1. Nasdaq public quote endpoint for equity spot/market-status snapshot.
2. Nasdaq public option-chain endpoint for listed-option bid/ask, volume, open interest, and ATM straddle proxy.
3. Yahoo Finance public chart endpoint as equity data fallback.
4. Stooq daily CSV as final equity data fallback.

The listed-options section is a **vol/liquidity proxy**, not an issuer FCN coupon, not a full volatility surface, and not an autocall model.

If asked for "live" free market data, explain that clean, firm real-time US equity/options data generally requires exchange/vendor entitlement. The workbench should use free/public/delayed data for screening only.

## Daily Pick Workflow

When the user asks for today's picks:

1. Check `daily/latest.md` and its generated timestamp.
2. If stale or if the user asks to refresh, trigger the GitHub Actions workflow `FCN Daily Report` when tool permissions allow.
3. Pull or read the refreshed report.
4. Summarize:
   - report timestamp and source caveats,
   - market snapshot highlights,
   - listed-options vol proxy highlights,
   - ranked baskets,
   - suggested tenor/KI/KO positioning,
   - key downside risks,
   - RFQ wording.

## Picking Logic

Default high-coupon candidates:

- `MSTR / COIN`: max coupon, crypto beta, concentrated risk.
- `AMD / SMCI`: balanced high-coupon AI infrastructure story.
- `MSTR / SMCI`: very high potential coupon, severe gap/worst-of risk.
- `COIN / SMCI`: aggressive alternative, crypto plus SMCI event risk.

Use listed-options ATM straddle proxies to refine the ranking. Higher 3M/6M straddle proxy and usable/deep listed-options liquidity generally support stronger coupon-screening interest, subject to issuer RFQ.

## KI Optimization Rule

Do not default to KI around 55 or 59 by habit.

Always request and compare a KI ladder:

```text
KI 50 / 55 / 59 / 65 / 70
```

For each issuer coupon matrix:

```text
Airbag = 100 - KI
Coupon pickup = Higher-KI coupon - Lower-KI coupon
Airbag sacrificed = Higher KI - Lower KI
Pickup per KI point = Coupon pickup / Airbag sacrificed
```

Decision rule:

- If pickup is flat, keep the lower KI.
- If pickup per KI point is weak, prefer the lower KI.
- If pickup accelerates sharply at a higher KI, flag that KI as a possible best-value point.
- The best KI is the level where extra coupon reasonably compensates for the airbag sacrificed, subject to client risk appetite.

## RFQ Default

Use this RFQ wording unless the user specifies different terms:

```text
Please quote indicative and firm levels for a USD worst-of FCN on [TICKER 1] / [TICKER 2], 3M and 6M tenor, KO 100 monthly, fixed monthly coupon, no RO economics. Please show coupon p.a. across KI 50 / 55 / 59 / 65 / 70 at maturity, plus coupon pickup per KI point, issuer estimated value, bid/offer, assumptions, and early unwind policy.
```

## Phone And Cloud Behavior

GitHub Actions can refresh and commit `daily/latest.md` while the laptop is off.

Normal ChatGPT mobile can read, discuss, and reason from the repo/report, but it does not automatically update GitHub unless the session has GitHub/Codex-style tools with write/run permissions.

For urgent manual refresh from phone:

1. Open GitHub repo.
2. Go to **Actions**.
3. Select **FCN Daily Report**.
4. Tap **Run workflow**.
5. Open `daily/latest.md`.

## Public Repo Hygiene

This repo is currently public-safe. Do not commit:

- client names,
- account details,
- suitability records,
- actual issuer quotes,
- firm-confidential pricing assumptions,
- private compliance notes.

If real issuer quote ladders are stored later, move that data to a private repo or another approved confidential storage location.
