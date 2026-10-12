# FCN Desk Playbook

The desk rules for screening worst-of Fixed Coupon Notes (FCNs) on US equities, preparing issuer RFQs, and explaining ideas to clients. Everything in this repo serves this file.

> Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.

---

## 1. Ground rules

1. **Issuer RFQ levels decide.** Public data, the daily screen and any model ballpark only decide *what is worth asking for*. Once a real quote arrives (and terms are normalized, see §6), it overrides every screen.
2. **Public data is screening evidence.** Free quotes and option chains are delayed and unofficial. Never present them as live or firm.
3. **Crypto-linked names are excluded by default** (MSTR, COIN, BTC miners, crypto exchanges, crypto-beta baskets) unless the user explicitly opts in.
4. **Diversify the universe.** Do not let the screen collapse into one theme because that theme is volatile this week. Cover AI/semis, software, EV, biotech/healthcare, power/nuclear, space/defense, quantum, fintech, China ADRs, cyclicals.
5. **Never put confidential material in this public repo:** client names or details, suitability records, actual issuer quotes or screenshots, firm pricing-system outputs, channel calibration levels. Record the *method*, never the numbers.

## 2. What makes a good FCN underlying

**Entry quality: "deep drawdown, vol not dispersed."**

| Position vs 6-month high | Read |
|---|---|
| Within 10% of the high, vol already crushed | Avoid. Coupon rarely compensates and you strike near a top. |
| 10–20% below | Acceptable. |
| **20–50% below with 20-day realized vol still elevated** | **Sweet spot.** Coupon screens rich without buying a fresh top. |
| More than 50% below | Caution: check whether the thesis is broken. |

**Falling-knife rule.** Never strike on a fresh heavy down day. Wait for **two consecutive stabilization sessions** (price holds, no new low) before activating a basket on a falling name. Conditional ideas stay conditional until the test passes, and the output must say so.

**Never anchor to a spike.** Do not set strikes against a parabolic or immediately post-event print.

**Listed-options sanity.** Usable open interest near the money, and verify which expiries actually exist before quoting a 3M/6M proxy. Many mid-caps skip monthly cycles (see `reference/option-expiry-quirks.md`). When comparing vol day over day, compare the **same expiry**, otherwise you create false vol spikes or crushes.

## 3. Building the basket

- **Cross-theme beats same-sector.** Lower correlation raises the worst-of coupon *and* gives real diversification. Same-sector pairs (correlation often 0.8+) fall together in a sector shock; they are pseudo-diversification. Prefer pairs like AI infra + nuclear, semis + software, biotech + China ADR.
- **The worst leg drives everything.** One very high-vol name dominates both the coupon and the downside. Check that the client understands and accepts *that* name.
- **2 vs 3 names.** A third name raises the coupon but also the chance that something breaks. Use three only when each leg is independently acceptable.
- **Give a spread of risk profiles** when suggesting picks: balanced (no leg above ~50% vol), higher-coupon (legs ~50–75%), aggressive (any leg above ~75%), plus a familiar-name anchor for conservative clients.

## 4. Event discipline

- Before locking any tenor, map **earnings, FDA/trial dates, launches, macro prints** (FOMC, CPI, payrolls) inside it.
- An **earnings date inside the first couple of weeks** is an **event hold**: do not RFQ into it.
- **Post-earnings clearance window**: often the best entry. The event risk is gone, implied/realized vol is still rich, and the next print falls outside a 3M tenor. Re-mark the morning after; if the reaction was sharply negative, apply the 2-session stabilization rule.
- A known mid-tenor **macro** event is a one-time shock to absorb inside the KI buffer, not a reason to abandon the structure.

## 5. Structure: tenor, KO, KI

| Term | Default | Notes |
|---|---|---|
| Tenor | Compare 3M and 6M first | 12M only if the client accepts longer event risk. |
| KO | 100%, monthly | Also ask 97/98/102. A lower KO or earlier KO start shortens expected life (less time at risk, fewer coupons in total). A non-call period lowers the p.a. coupon but keeps coupons flowing in up-markets. |
| KI | Ask for a **ladder**: 50 / 55 / 59 / 65 / 70 | Always state the observation style: at maturity, daily close, or continuous. They are not comparable. A daily-close KI pays more because it triggers more often. |
| Strike | 100% (US style) | Asian FCNs often use a strike of 80–95% with physical delivery and no KI, or a daily KI. Quote and model in the **same convention** (`research/fcn-pricing-logic.md` §3). |
| RO | 100, plus requested RO | Compare RO separately from headline coupon (§6). |
| Coupon | Fixed, monthly | Note memory vs non-memory. |

### KI value discipline

Do not pick the lowest KI by habit, and do not chase the highest headline coupon. Pick the KI where the extra coupon pays for the airbag given up.

```text
Airbag              = 100 - KI
Pickup per KI point = (coupon at higher KI - coupon at lower KI) / (higher KI - lower KI)
```

| Pickup per 1 KI point | Read | Action |
|---:|---|---|
| below 0.25% p.a. | Weak | Keep the lower KI |
| 0.25–0.60% p.a. | Balanced | Decide by client risk appetite |
| above 0.60% p.a. | Strong | The higher KI may be worth it; flag any level where pickup jumps |

Use `templates/ki-optimization.md` with the issuer's actual ladder.

## 6. Comparing quotes like-for-like

Before comparing two coupons, align: tenor, underlyings, strike/reference, KI level **and** observation, KO level, start and observation, RO/issue price, coupon frequency and memory, issuer and bid/offer basis. If anything differs, call it a **structural mismatch** and list the differences instead of ranking.

Quick RO normalization (desk shorthand, not valuation):

```text
Annualized RO accretion ≈ ((100 - RO) / RO) × (12 / tenor_months)
Gross carry ≈ coupon p.a. + annualized RO accretion
```

**Why issuer levels differ from a public screen** (ask which input is driving it): reference timing and live bid/ask, the issuer's vol surface and skew, dividends/forwards, correlation assumptions, autocall path modeling, borrow, funding curve and credit, inventory and appetite for those names, term-sheet details, margin.

## 7. Repeated ideas (requote taxonomy)

Never silently re-send an earlier idea. Label it:

| Label | Meaning |
|---|---|
| fresh | New idea, or no recent rationale |
| repeat, same rationale | Thesis unchanged; levels re-marked |
| repeat, changed inputs | Same names, materially different spot/vol/event picture |
| structural mismatch | Quoted terms differ from what the screen assumed |
| calibration drift | Issuer levels now contradict the old screen; the quote wins |
| event hold | Paused into a binary event |
| event cleared | Resumed after the event, levels re-marked |

Use `templates/requote-checklist.md` when the answer is not obvious.

## 8. Calibrating against real quotes

When a pricing-system or issuer number is available, compare it with the ballpark using `templates/quote-calibration.md`: record the gap and its likely driver (vol, skew, correlation, funding, margin, structure). Adjust expectations for the session. **Keep the actual numbers in private storage** (the `actual-quotes/` folder is git-ignored), never in this repo.

## 9. What a good picks answer looks like

1. Date and data timestamp, with the public-data caveat.
2. A short market read: what moved and which themes are in or out of favour.
3. **2–3-stock baskets across risk profiles**, each with: why these names now (entry quality, vol, catalyst), correlation/theme mix, suggested tenor/KO/KI, a **ballpark coupon range clearly labeled indicative**, the main downside risk, and the requote label.
4. Conditional / watch-only names and what would activate them.
5. Ready-to-send RFQ wording (`templates/rfq-template.md`), and client wording if asked (`templates/client-explanation.md`, EN/中文).
6. The indicative-only label.

Prefer plain screening language: "worth RFQ", "screens rich", "the quote overrides the screen". Avoid false precision and "this will pay X%".

## 10. Ballpark model

`scripts/fcn_model.py` gives a worst-of FCN coupon range by Monte Carlo: monthly coupon and KO, flat vol per leg from listed ATM straddles, realized correlation, a rate + funding assumption, and a low/high band for issuer margin and skew. It supports three downside conventions: KI at maturity (default), daily-close KI, and strike-only FCN with delivery at the strike. It ignores skew shape, dividends, borrow and issuer appetite. Use it to sanity-check issuer levels and to make ladder trade-offs concrete, never as a quote. How coupons are built and why issuers differ: `research/fcn-pricing-logic.md`.

```bash
python scripts/fcn_model.py --vols 0.55 0.45 --corr 0.4 --tenor 6                          # KI at maturity
python scripts/fcn_model.py --vols 0.55 0.45 --corr 0.4 --ki-style none --ladder 80 85 90  # strike-only FCN
python scripts/fcn_model.py --vols 0.55 0.45 --corr 0.4 --ki-style daily --strike 90       # daily KI
```

## 11. Living watchlist

`watchlist.csv` is a **candidate pool, not a fixed universe**. Every name is re-scored daily; none is guaranteed a pick.

- **Daily additions from the market** (whether or not a name is in the pool): overnight earnings/FDA/contract/M&A events with residual vol; liquid names whose realized vol jumps with real option depth; well-known names newly in the 20–50% drawdown zone; the two most liquid names in a theme seeing clear rotation; any name a client asks about (answer even if the answer is "not suitable").
- **To join the pool**, a name passes four gates: sensible drawdown position, enough realized vol, enough option open interest, event calendar mapped. Verify expiries and issuer eligibility first.
- **Freeze or remove** when the thesis breaks, vol is exhausted (within 10% of highs with RV collapsed), option liquidity dries up, or the name becomes off-limits. Log every change with a reason in `watchlist-changelog.md` so names do not resurface without memory.

## 12. Screening requirements (desk defaults)

These are the default filters for a picks request. A request that states its own terms overrides them.

**Risk-controlled profile (default: "good coupon, controlled risk")**
- Target coupon about **15–25% p.a.**, KI **55–59 at maturity** (or the equivalent strike-only level, checked with the model).
- Ballpark probability of loss at maturity about **12% or less**.
- 2–3 names from **different themes**; at most one leg with implied vol above ~65%.
- No leg reporting earnings before the first KO observation unless the event is deliberately accepted; prefer the post-earnings window.
- No falling knives (2-session rule) and no strikes on a spike day (roughly +7% or more in a day).
- Avoid names whose thesis is under fresh question until the news settles (e.g. October 2026, AI-cloud names after the OpenAI revenue report).

**Tech-growth template**
- Tenor 4M or 6M, KO 97–97.5% monthly, coupon **≥ 20% p.a.**, the deepest KI that still clears 20% (usually 50–55 on 6M).
- At 4M, 20%+ normally needs KI 59+ or a higher-vol leg; say so rather than stretching.

**Exclusion switches**
- Crypto-linked: excluded by default (§1).
- China ADRs: exclude when the user asks; then the defensive leg usually comes from healthcare or power instead.

## 13. Pricing logic in one screen

- The investor sells a worst-of put to the issuer; the coupon is that premium plus the issuer's funding benefit, minus margin, spread over the expected life.
- Coupon **rises** with: implied vol, downside skew, lower correlation, more names, a higher KI or strike, daily rather than maturity KI, higher rates/funding, a weaker issuer credit, more callability.
- Coupon **falls** with: issuer margin and fees, a longer non-call period, fixed rather than conditional coupons, and familiar low-vol names.
- Issuers differ because of their own vol/skew surfaces, correlation marks, existing book (axes), funding, appetite and term details. Ask which input drives a gap.
- Public calibration: SEC 424B2 pricing supplements disclose real worst-of coupons and estimated values (`research/data-sources.md`). Normalize the convention first.
- Concentration: spread clients across baskets and issuers. Regulators (SFC complex-product rules, FINRA 2026 sweep) focus on suitability and concentration in worst-of notes (`research/resources.md`).
