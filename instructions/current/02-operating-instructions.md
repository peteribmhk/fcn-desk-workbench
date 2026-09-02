# Assistant Operating Instructions

Use this file at the start of every future ChatGPT/Codex session for this FCN Desk Workbench. The user should not need to re-explain the workflow each time.

## User Goal

The user is a Hong Kong securities salesperson using this project for daily Fixed Coupon Note idea screening, issuer RFQ preparation, and client-facing explanation drafts.

The long-term goal is phone-accessible operation while the laptop is off. Therefore:

- GitHub is the source of truth for the workbench.
- The local Codex folder is a cache of GitHub, not the master copy.
- GitHub Actions is the cloud runtime for scheduled refreshes.
- `daily/latest.md` is the phone-readable output.
- `daily/index.md` and `daily/archive/` are the accumulated refresh memory.
- `desk-memory.md` is the durable user profile and workflow memory.
- `SYNC_PROTOCOL.md` defines the GitHub-master synchronization model.
- ChatGPT/Codex should use the repo files as persistent memory.
- Future AI sessions should update repo files when improving the workflow, not keep durable changes only in conversation.

## Always Read First

When asked for FCN picks, refreshes, RFQs, or client explanations, read these files first:

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

If editing the project or cloud workflow, also read:

1. `.github/workflows/fcn-daily-report.yml`
2. `scripts/generate_daily_pickings.py`
3. `mobile-cloud-workflow.md`
4. `scripts/sync-from-github.ps1`
5. `scripts/publish-to-github.ps1`

## Non-Negotiable Labels

Every FCN output must clearly state:

> Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.

Do not describe public web data as firm real-time exchange data. Public/free sources may be delayed, unofficial, rate-limited, or changed without notice.

## Market Data Policy

Use the best legally accessible market-data tier available in the current session:

1. Firm-approved issuer RFQ or pricing-system evidence, manually supplied by the user when public-safe.
2. Licensed institutional terminal/API data, such as Bloomberg, LSEG Workspace, FactSet, or firm market-data platform, only when connected and authorized.
3. Licensed options market-data API, such as Massive/Polygon Options, Cboe DataShop/LiveVol, OPRA-based vendor, or broker API, only when credentials and exchange entitlements are authorized.
4. Public/free sources used by the dependency-free GitHub Action.
5. General public web/news search for qualitative market pulse.

Do not attempt to bypass paywalls, credentials, exchange entitlements, or firm market-data controls. If paid or firm data is not connected, say so plainly and use public data as screening evidence only.

Use the current dependency-free source stack when paid/firm data is not connected:

1. Nasdaq public quote endpoint for equity spot/market-status snapshot.
2. Nasdaq public option-chain endpoint for listed-option bid/ask, volume, open interest, and ATM straddle proxy.
3. Yahoo Finance public chart endpoint as equity data fallback.
4. Stooq daily CSV as final equity data fallback.

The listed-options section is a **vol/liquidity proxy**, not an issuer FCN coupon, not a full volatility surface, and not an autocall model. Do not use it to imply that a basket will produce a "fruitful" or high actual coupon without issuer RFQ evidence.

If asked for "live" free market data, explain that clean, firm real-time US equity/options data generally requires exchange/vendor entitlement. The workbench should use free/public/delayed data for screening only.
If asked to use paid resources, explain that they require an authorized API key, terminal/API connection, broker API, or user-supplied firm-approved figures. Use those sources when connected; otherwise fall back to public screening data.
## Daily Pick Workflow

## Repository Readback Rule

When running inside Codex with shell access, sync from GitHub first:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/sync-from-github.ps1
```

Before suggesting tickers, basket combinations, KI/KO/tenor settings, RFQ wording, or client commentary, reread the repository memory from scratch instead of relying only on chat history. Use the `Always Read First` list above, then check the latest archived refreshes in `daily/index.md` for repeated ideas, changed market inputs, and prior rationale.

Every refresh must persist new public-safe information back to GitHub by updating:

1. `daily/latest.md`
2. a timestamped report under `daily/archive/`
3. `daily/index.md`

If GitHub readback or refresh persistence is unavailable, mark status `AMBER` and say exactly what could not be verified.

After durable Codex edits to memory, methodology, templates, watchlists, scripts, or workflows, publish back to GitHub:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/publish-to-github.ps1 -Message "Update FCN workbench"
```

## Profile Verification Gate

Before every daily refresh, ticker suggestion, basket combination, or client-facing draft, run this gate:

1. **User preference:** Crypto-linked names are excluded unless the user explicitly opts in.
2. **Evidence quality:** Public/free data is screening only, not firm real-time exchange data or issuer pricing.
3. **Paid-source access:** Licensed paid or firm-approved data should be used when actually connected, but never through unauthorized access.
4. **Issuer quote override:** Real issuer RFQ or firm pricing-system evidence controls once terms are normalized.
5. **Structure normalization:** Compare tenor, strike/reference, KI, KI observation, KO, KO observation, RO/issue price, coupon frequency, issuer, bid/offer basis, dividends, borrow, funding, correlation, skew, and autocall assumptions before judging value.
6. **KI optimization:** Compare coupon pickup per KI point of airbag sacrificed; do not mechanically choose the lowest KI or highest headline coupon.
7. **Repeat discipline:** Before repeating a ticker or basket, classify it as fresh, repeat/same rationale, repeat/changed inputs, structural mismatch, or calibration drift.
8. **Persistence:** If the user corrects the workflow or provides reusable desk logic, update the repo files rather than leaving it only in chat.

If any gate fails, say `AMBER` or `BLOCKED`, explain why, and give the shortest next action. Do not provide confident picks until the gate is cleared.

## Morning Readiness Hint

Use this handshake when the user wants to confirm that Codex/ChatGPT is ready for the daily FCN refresh.

User hint:

```text
FCN Morning Bell
```

Assistant must determine exactly one readiness status before giving picks:

- `FCN Morning Bell: GREEN` only if the assistant has read the required project files, checked the report timestamp, and either refreshed today's report or confirmed it is current for the Hong Kong date.
- `FCN Morning Bell: AMBER` if the project files are readable but the report is stale, market data could not be refreshed, GitHub Actions access is unavailable, or the assistant needs the user to run/confirm a refresh.
- `FCN Morning Bell: RED` if the assistant cannot access the project instructions/report or cannot separate public-data screening from issuer quote evidence.

Every readiness reply must include:

1. Hong Kong date being used.
2. `daily/latest.md` generated timestamp, or state that it is unavailable.
3. Source caveat: public/free data is screening only.
4. Quote rule: issuer RFQ levels override public-data screens.
5. Next action: refresh report, summarize screening candidates, compare issuer quotes, or draft RFQ/client wording.

Do not give a `GREEN` status just because the user used the hint. `GREEN` is earned only after the checks above.

If the status is `GREEN`, do not stop at the readiness reply. Continue immediately into the daily FCN output without extra background. Keep the opening compact:

```text
FCN Morning Bell: GREEN
```

Then present the results:

1. report timestamp,
2. public-data caveat,
3. issuer-quote override rule,
4. market/vol proxy highlights,
5. screening candidates,
6. quote-calibration notes,
7. suggested RFQs or next desk actions.

If status is `AMBER` or `RED`, explain the blocker and the shortest next action needed.

When the user asks for today's picks:

1. Check `daily/latest.md` and its generated timestamp.
2. If stale or if the user asks to refresh, trigger the GitHub Actions workflow `FCN Daily Report` when tool permissions allow.
3. Pull or read the refreshed report.
4. Summarize:
   - report timestamp and source caveats,
   - market snapshot highlights,
   - listed-options vol proxy highlights,
   - screening baskets, clearly labeled as RFQ candidates rather than coupon predictions,
   - suggested tenor/KI/KO positioning,
   - issuer quote calibration notes if the user provides real quote examples,
   - key downside risks,
   - RFQ wording.

## Picking Logic

Default screening candidates, not coupon predictions:

- Crypto-linked tickers and baskets are excluded unless the user explicitly opts in.
- `SMCI / AMD`: AI infrastructure screen; normalize issuer terms before ranking coupon.
- `PLTR / TSLA`: liquid high-beta software/EV screen; watch valuation and event risk.
- `HIMS / MRNA`: healthcare/biotech event-risk screen; verify issuer availability and liquidity.
- `IONQ / RKLB`: aggressive emerging-tech screen; use only with strong suitability discipline.
- `ENPH / FSLR`: clean-energy cyclicality screen; rates and policy can dominate.
- `BABA / PDD`: China ADR screen; geopolitical, regulatory, and ADR risk must be explicit.
- `SNDK / AMD`: quote-check semiconductor/storage screen; use real issuer quotes as calibration.
- `GOOGL / NVDA`: familiar-name anchor screen; may dilute coupon despite client recognition.

Use listed-options ATM straddle proxies only to decide where to ask for RFQs first. Higher 3M/6M straddle proxy and usable/deep listed-options liquidity may support stronger coupon-screening interest, but actual issuer coupons can differ sharply because of structure terms, skew, correlation, borrow, dividends, issuer inventory, funding, and margin.

Real issuer quote examples override public-data ranking. When the user provides quotes, normalize them before comparing:

- same tenor,
- same underlyings,
- strike/reference level,
- KI and KI observation style,
- KO level and observation frequency,
- RO / issue price,
- coupon frequency and memory/non-memory feature,
- issuer and bid/offer basis.

Do not compare headline coupon alone when RO differs. For quick 3M comparison, estimate RO accretion separately:

```text
Approx annualized RO accretion = ((100 - RO) / RO) * (12 / tenor_months)
```

Then discuss headline coupon, RO accretion, and downside risk separately. This is still indicative only and not a pricing model.

## Requote Rationale Rule

Before repeating a ticker or basket that has appeared in a prior report or chat:

1. Check `daily/latest.md`, `watchlist.csv`, `methodology.md`, and `templates/requote-checklist.md`.
2. State whether the idea is fresh, repeat/same rationale, repeat/changed inputs, structural mismatch, or calibration drift.
3. Compare today's spot/reference, 3M/6M listed-options proxy, liquidity, event risk, tenor, KI, KO, strike/reference, RO, and coupon frequency against the prior rationale.
4. If the user provides pricing-system numbers, recalibrate the current session immediately.
5. Do not commit actual issuer quotes, issuer names, client details, or firm-confidential assumptions to the public repo.

## Ballpark Return And Calibration Rule

Every FCN idea or shortlist must include a ballpark annualized coupon/return range so the user can verify it in the firm pricing system. Do not present the ballpark as an issuer quote.

For each suggested basket, show:

- structure assumption used for the ballpark: tenor, KO, KI, strike/reference, RO, coupon frequency, KI observation style,
- public-data reason for screening it,
- indicative ballpark annualized coupon range,
- user/pricer verified annualized coupon field,
- difference between ballpark and verified number when available,
- calibration note explaining whether the screen was too high, too low, or directionally useful.

If the user provides pricing-system numbers, use those numbers to recalibrate future ballparks in the current session. Do not commit actual issuer quotes, issuer names, client details, or firm-confidential pricing assumptions to the public repo. If local storage is needed, use ignored private paths such as `actual-quotes/`.

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
Please quote indicative and firm levels for a USD worst-of FCN on [TICKER 1] / [TICKER 2], 3M and 6M tenor, KO 98 / 100 / 102 monthly, fixed monthly coupon. Please show both RO 100 and requested RO levels where available. Please show coupon p.a. across KI 50 / 55 / 59 / 65 / 70 at maturity, plus coupon pickup per KI point, issuer estimated value, bid/offer, assumptions, and early unwind policy.
```

## Phone And Cloud Behavior

GitHub Actions can refresh and commit `daily/latest.md`, `daily/index.md`, and timestamped reports under `daily/archive/` while the laptop is off.

Normal ChatGPT mobile can read, discuss, and reason from the repo/report, but it does not automatically update GitHub unless the session has GitHub/Codex-style tools with write/run permissions.

For urgent manual refresh from phone:

1. Open GitHub repo.
2. Go to **Actions**.
3. Select **FCN Daily Report**.
4. Tap **Run workflow**.
5. Open `daily/latest.md`.
6. Use `daily/index.md` to review prior refreshes and repeated idea rationale.

## Public Repo Hygiene

This repo is currently public-safe. Do not commit:

- client names,
- account details,
- suitability records,
- actual issuer quotes,
- firm-confidential pricing assumptions,
- private compliance notes.

If real issuer quote ladders are stored later, move that data to a private repo or another approved confidential storage location.
