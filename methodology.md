# Methodology

Use this methodology when Codex prepares FCN pickings from public market data. The goal is to identify RFQ candidates and compare issuer quotes, not to produce firm tradable coupons or predict actual issuer pricing from public data.

## Required Labels

Every output must state:

> Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.

## Inputs To Collect

- Underlyings and market.
- Spot price and timestamp.
- Recent price trend: 1D, 1W, 1M if available.
- Implied volatility or public options-chain proxy if available.
- Liquidity and bid/ask quality.
- Event risks: earnings, financing, regulation, product launch, macro, sector stress, geopolitical or idiosyncratic catalysts.
- Structure terms: tenor, KO, KI, coupon frequency, observation frequency, airbag level, and KI observation style.
- RO / issue price and whether headline coupon or total economics are being compared.

## Ticker Universe Policy

Crypto-linked ideas are excluded by default. Do not screen MSTR, COIN, BTC miners, crypto exchanges, or crypto-beta baskets unless the user explicitly asks to opt in.

The default watchlist should remain diversified across industries. Do not let the workflow collapse into one theme just because one sector currently has high public volatility. At minimum, consider AI/semis, software, EV, healthcare/biotech, emerging technology, clean energy, China ADRs, cyclicals, and other liquid high-volatility names.

Use public data to decide what is worth RFQ, not to declare which basket has the best coupon. A lower-volatility but issuer-favored basket can beat a higher-volatility public screen once skew, correlation, funding, borrow, dividends, inventory, and margin are included.

## Profile Verification Gate

Run this gate before daily picks, ticker suggestions, basket combinations, RFQ wording, or client-facing commentary:

| Gate | Pass condition | If it fails |
|---|---|---|
| User preference | Crypto-linked names are excluded unless the user explicitly opts in. | Remove crypto names and rebuild the screen. |
| Evidence quality | Public/free data is labeled as delayed/public screening only. | Do not call the output live, firm, or issuer-priced. |
| Issuer quote override | Real issuer RFQ or firm pricing-system evidence overrides public-data ranking once normalized. | Re-rank from issuer evidence, not from public vol proxy. |
| Structure normalization | Tenor, strike/reference, KI, KI observation, KO, KO observation, RO, coupon frequency, issuer, bid/offer, dividends, borrow, funding, correlation, skew, and autocall assumptions are checked. | Mark comparison as structural mismatch. |
| KI value discipline | KI is optimized by coupon pickup per KI point of airbag sacrificed. | Do not recommend the lowest KI or highest headline coupon mechanically. |
| Repeat discipline | Repeated tickers/baskets are classified as same rationale, changed inputs, structural mismatch, or calibration drift. | Use the requote checklist before suggesting again. |
| Persistence | Reusable user corrections are written into repo instructions/templates. | Update the project files before relying on the memory later. |

## Issuer Quote Override

Issuer RFQ levels are the controlling evidence. Public quotes, listed-option straddles, and volatility labels can explain why a name may be worth asking about, but they cannot rank actual FCN coupon value by themselves.

If the user provides actual issuer quote examples, update the desk view immediately:

- Treat those quotes as calibration evidence for current issuer appetite.
- Do not keep an old basket ranking if the real quote contradicts it.
- Compare only like-for-like structures, or clearly list the structural differences.
- Separate headline coupon from RO/discount economics.
- Avoid saying a basket is "likely highest coupon" unless issuer quote evidence supports it.

Before comparing two quotes, normalize these fields:

| Field | Why it matters |
|---|---|
| Tenor | Annualized coupon can hide different path risk and autocall probability. |
| Underlyings | One high-vol name can dominate, but issuer correlation/skew assumptions matter. |
| Strike/reference | Different strike/reference conventions change downside and option value. |
| KI level and observation | Maturity KI, daily close KI, and continuous KI are not comparable. |
| KO level and observation | KO 98, 100, and 102 can change expected life and coupon materially. |
| RO / issue price | RO below par adds discount accretion if redeemed at par, separate from coupon. |
| Coupon frequency/memory | Payment mechanics change client economics. |
| Issuer/bid-offer | Issuer inventory, funding, margin, and hedge cost can dominate the screen. |

## Why Issuer Pricing Can Diverge

Differences versus UBS, JPM, Marex, Leonteq, or another issuer are usually not just "bad data." They can come from:

- different spot/reference timing and live bid/ask,
- issuer volatility surface, skew, and forward/dividend assumptions,
- worst-of correlation assumptions and autocall path modeling,
- borrow, financing, funding curve, issuer credit, and balance-sheet inventory,
- term-sheet details such as KI observation style, KO start date, coupon memory, strike convention, RO, fees, and settlement,
- issuer margin, bid/offer, and appetite for the exact underlyings.

Therefore, optimize the workbench as a screening and calibration tool. It should ask better RFQs, normalize real quotes more carefully, and learn from pricing-system feedback, but it should not pretend to replicate a bank issuer pricer from free public data.

## Requote Discipline

Before quoting or suggesting a ticker or basket that appeared before, classify the idea:

- **Fresh idea:** no recent prior rationale.
- **Repeat, same rationale:** same basket and structure, with today's refreshed market data.
- **Repeat, changed inputs:** same ticker/basket but spot, listed-options proxy, liquidity, event risk, or structure changed.
- **Structural mismatch:** tenor, KI, KO, strike/reference, RO, coupon frequency, issuer, or observation style differs.
- **Calibration drift:** today's issuer/pricing-system result contradicts the old public-data screen.

Use `templates/requote-checklist.md` for the comparison. If real quote evidence contradicts the old view, the real quote wins for current calibration.

Quick RO normalization for a rough desk comparison:

```text
Approx annualized RO accretion = ((100 - RO) / RO) * (12 / tenor_months)
Approx annualized gross carry = coupon p.a. + annualized RO accretion
```

This is not a valuation model. It is only a way to avoid comparing a 97 RO note against a 100 RO note by headline coupon alone.

## Ranking Logic

For public-data reports, rank baskets as RFQ screening candidates, not as coupon predictions. Use this order:

1. **Issuer quote evidence**: real RFQ levels override public-data intuition.
2. **Structure-normalized economics**: compare tenor, RO, KO, KI, strike, and coupon mechanics before judging value.
3. **Volatility and jump risk**: higher vol generally supports higher coupon only when terms and issuer assumptions are comparable.
4. **Worst-of risk**: the weakest or most volatile name usually drives coupon and downside.
5. **Correlation and skew**: issuer correlation/skew assumptions can make actual quotes diverge from simple vol screens.
6. **Tenor**: longer tenor usually supports higher annualized coupon but increases time-at-risk.
7. **KI and airbag**: lower KI / deeper airbag reduces downside trigger risk and lowers coupon; higher KI raises coupon and risk.
8. **KO level and observation**: lower/easier KO usually increases early redemption probability and can reduce total carry opportunity.
9. **Liquidity, borrow, dividends, and hedge cost**: issuer hedge economics can dominate public listed-option screens.
10. **Client explainability**: a slightly lower coupon basket can be preferable if the story and risks are easier to explain.

## Structure Guidance

### Tenor

- **3M**: cleaner short-risk expression; coupon usually lower than 6M/12M.
- **6M**: practical balance for high-vol baskets; common starting point for RFQ.
- **12M**: higher coupon potential but higher path and event risk.

### KO

- **KO 100**: standard reference point; easier to explain.
- Monthly observation is the default unless otherwise specified.
- Later autocall start can increase coupon but adds exposure.

### KI / Airbag

Use "airbag" as the downside protection buffer between initial level and KI.

- Do not assume one fixed KI level is optimal.
- Request a **KI ladder** from issuers for the same basket, tenor, KO, observation schedule, and coupon frequency.
- Default ladder: **KI 50 / 55 / 59 / 65 / 70**, observed at maturity unless specified otherwise.
- Lower KI gives more protection and lower coupon.
- Higher KI gives higher coupon but makes downside redemption more realistic.
- Always state whether KI is observed at maturity, daily close, or continuously.

## KI Optimization

The objective is not "lowest KI" or "highest coupon" by itself. The objective is best value: how much extra coupon is received for each point of airbag sacrificed.

For each issuer quote matrix, calculate:

```text
Airbag = 100 - KI
Coupon pickup = Higher-KI coupon - Lower-KI coupon
Airbag sacrificed = Higher KI - Lower KI
Pickup per KI point = Coupon pickup / Airbag sacrificed
```

Decision guide:

- If pickup is small, keep the lower KI.
- If pickup is meaningful and the client accepts the extra downside risk, move up the KI ladder.
- If pickup accelerates sharply at a higher KI, flag that level as a potential value point.
- If pickup is flat between two KI levels, choose the lower KI.

Suggested desk thresholds, to be adjusted with experience:

| Pickup per 1 KI point | Interpretation | Action |
|---:|---|---|
| Below 0.25% p.a. | Weak compensation | Prefer lower KI |
| 0.25%-0.60% p.a. | Balanced tradeoff | Compare client risk appetite |
| Above 0.60% p.a. | Strong compensation | Higher KI may be worth considering |

Always compare KI levels using the same tenor, KO, basket, issuer, and observation assumptions.

## Coupon Language

Avoid false precision. Prefer screening language:

- "This basket screens as worth RFQ, but issuer levels are needed before ranking coupon value."
- "Public vol/liquidity suggests coupon potential; actual terms may differ because of RO, KO, KI, skew, correlation, funding, borrow, dividends, and issuer margin."
- "The real issuer quote contradicts the screen, so the quote should override the public-data ranking."
- "If issuer quote is far below or above the screen, ask which input is driving the difference: RO, KO, KI, vol, skew, correlation, funding, borrow, dividends, or margin."
- "The best KI is where incremental coupon pickup justifies the extra loss-trigger risk."

## Output Ranking Categories

Use these labels:

- **RFQ first**: strongest current reason to request issuer levels, not a coupon prediction.
- **Quote-supported high coupon**: attractive actual issuer quote after normalizing terms.
- **Balanced candidate**: potentially useful coupon/story tradeoff, pending issuer RFQ.
- **Aggressive candidate**: high-risk basket that may be unsuitable for conservative clients.
- **Watch only**: interesting but not preferred due to event risk, liquidity, or crowded exposure.
