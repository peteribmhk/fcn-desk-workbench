# FCN Daily Screen

**Generated:** 2026-11-06 13:06 HKT  |  **US close used:** 2026-11-05  |  **Data status:** GREEN

> Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
> Public/delayed data, used only to decide what to RFQ. Issuer RFQ levels override everything below.

## How to read this

Structure assumed for the ballpark: USD worst-of FCN, 6M, KO 100% monthly from month 1, KI 59% observed at maturity, strike 100%, RO 100, monthly fixed coupon. Vols come from listed ATM straddles (Nasdaq); correlation from 90-day realized returns. The ballpark ignores skew, dividends and issuer-specific funding, so treat it as a sanity check for issuer levels, not a forecast. Every basket mixes different themes on purpose; same-sector pairs are pseudo-diversification.

## Two-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BABA / UAL | China ADR + Cyclical/Consumer | 45 / 49 | 0.14 | 16-22% | 11% | Balanced | repeat, same rationale |
| 2 | UAL / DXCM | Cyclical/Consumer + Biotech/Health | 49 / 43 | 0.07 | 15-21% | 11% | Balanced | fresh |
| 3 | RIVN / DKNG | EV/Auto + Cyclical/Consumer | 63 / 57 | 0.17 | 33-39% | 21% | Higher coupon | fresh |
| 4 | RIVN / TDOC | EV/Auto + Biotech/Health | 63 / 60 | 0.02 | 35-41% | 23% | Higher coupon | fresh |

## Three-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | BABA / UAL / DXCM | China ADR + Cyclical/Consumer + Biotech/Health | 45 / 49 / 43 | 0.16 | 20-26% | 16% | Balanced | fresh |
| 2 | RIVN / DKNG / TDOC | EV/Auto + Cyclical/Consumer + Biotech/Health | 63 / 57 / 60 | 0.17 | 41-48% | 31% | Higher coupon | fresh |

## Why these names

- **BABA / UAL**: BABA: sweet spot (-20% to -50%), -26% vs 6M high, vol 45% (6M straddle), next earnings 2026-11-24; UAL: mild pullback, -19% vs 6M high, vol 49% (6M straddle)
- **UAL / DXCM**: UAL: mild pullback, -19% vs 6M high, vol 49% (6M straddle); DXCM: near 6M high, -9% vs 6M high, vol 43% (6M straddle), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%)
- **RIVN / DKNG**: RIVN: sweet spot (-20% to -50%), -34% vs 6M high, vol 63% (6M straddle); DKNG: sweet spot (-20% to -50%), -22% vs 6M high, vol 57% (6M straddle)
- **BABA / UAL / DXCM**: BABA: sweet spot (-20% to -50%), -26% vs 6M high, vol 45% (6M straddle), next earnings 2026-11-24; UAL: mild pullback, -19% vs 6M high, vol 49% (6M straddle); DXCM: near 6M high, -9% vs 6M high, vol 43% (6M straddle), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%)
- **RIVN / DKNG / TDOC**: RIVN: sweet spot (-20% to -50%), -34% vs 6M high, vol 63% (6M straddle); DKNG: sweet spot (-20% to -50%), -22% vs 6M high, vol 57% (6M straddle); TDOC: near 6M high, -3% vs 6M high, vol 60% (6M straddle)

## Valuation cross-check (legs in today's picks)

Would you be happy to own the worst leg at the strike? Cheap against its own 10-year range, an analyst target above the price and growing revenue make a sturdier floor. Not blocking: it informs the RFQ, it does not remove names. Data: `fundamentals/valuation.csv`.

| Ticker | vs 6M high | Valuation read | Caveat |
| --- | --- | --- | --- |
| RIVN | -34% | no data |  |
| BABA | -26% | no data |  |
| DKNG | -22% | no data |  |
| UAL | -19% | no data |  |
| DXCM | -9% | supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%) |  |
| TDOC | -3% | no data |  |

## KI ladder: BABA / UAL (top pair)

| KI | Ballpark coupon p.a. | P(loss at maturity) | Pickup per KI pt | Read |
| --- | --- | --- | --- | --- |
| 50% | 6.7-11.7% | 4.2% | - | base protection |
| 55% | 11.6-17.3% | 7.6% | 1.04% p.a. | strong pickup |
| 59% | 16.4-22.2% | 11.4% | 1.22% p.a. | strong pickup |
| 65% | 23.9-30.0% | 18.2% | 1.28% p.a. | strong pickup |
| 70% | 30.0-35.9% | 24.5% | 1.19% p.a. | strong pickup |

Pickup per KI point thresholds: below 0.25% p.a. keep the lower KI; 0.25-0.60% balanced; above 0.60% the higher KI may be worth it. Model pickup is smooth by construction; the real decision uses the issuer's KI ladder.

## Conditional / watch only

| Ticker | 1D | vs 6M high | Vol | Why held back |
| --- | --- | --- | --- | --- |
| APLD | -14.7% | -71% | 103% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| ASTS | -15.2% | -77% | 100% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-09 |
| CRWV | -9.8% | -65% | 99% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-10 |
| NBIS | -14.9% | -58% | 98% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-12; thin listed options |
| LUNR | -13.2% | -81% | 93% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-12; thin listed options |
| CRDO | -17.7% | -63% | 89% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| OKLO | -13.2% | -75% | 89% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-06 |
| NTLA | -9.8% | -38% | 88% | falling knife: wait 2 stable sessions |
| ALAB | -19.6% | -63% | 88% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| SMR | -14.8% | -69% | 87% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| BE | -16.4% | -52% | 87% | falling knife: wait 2 stable sessions |
| QBTS | -12.8% | -70% | 86% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-10 |
| MRNA | -6.5% | -7% | 83% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-06; thin listed options |
| RKLB | -12.2% | -69% | 82% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-09 |
| LEU | -3.8% | -58% | 81% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| SNDK | -22.3% | -65% | 81% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| HIMS | -9.8% | -37% | 81% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-09; thin listed options |
| RGTI | -12.1% | -64% | 80% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-10 |
| COHR | -13.0% | -60% | 80% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| SMCI | -8.5% | -46% | 79% | falling knife: wait 2 stable sessions |
| IONQ | -10.5% | -63% | 79% | falling knife: wait 2 stable sessions |
| DELL | -14.9% | -46% | 76% | falling knife: wait 2 stable sessions; thin listed options |
| STX | -16.3% | -57% | 76% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| AVAV | -9.8% | -52% | 75% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| QUBT | -12.4% | -55% | 74% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-09 |
| WDC | -17.4% | -64% | 74% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| ENPH | -8.2% | -60% | 73% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| LITE | -18.7% | -55% | 72% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| ARM | -13.1% | -62% | 72% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| NET | -8.3% | -32% | 70% | falling knife: wait 2 stable sessions; thin listed options |
| MRVL | -16.4% | -58% | 70% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| KTOS | -7.1% | -49% | 67% | falling knife: wait 2 stable sessions; thin listed options |
| VKTX | -7.8% | -39% | 67% | falling knife: wait 2 stable sessions; thin listed options |
| VRT | -14.0% | -53% | 66% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| DDOG | -7.5% | -40% | 66% | falling knife: wait 2 stable sessions |
| APP | +31.0% | -42% | 65% | thin listed options |
| ZS | -9.2% | -22% | 65% | falling knife: wait 2 stable sessions; thin listed options |
| AFRM | -7.8% | -19% | 64% | falling knife: wait 2 stable sessions; thin listed options |
| ORCL | -6.9% | -54% | 63% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| MU | -17.5% | -46% | 63% | falling knife: wait 2 stable sessions; thin listed options |
| GLW | -12.9% | -60% | 63% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| SNOW | -7.2% | -27% | 61% | falling knife: wait 2 stable sessions; thin listed options |
| AMAT | -13.6% | -56% | 61% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-12 |
| AMD | -17.3% | -38% | 61% | falling knife: wait 2 stable sessions |
| TLN | -3.2% | -28% | 59% | falling knife: wait 2 stable sessions; thin listed options |
| ANET | -10.8% | -27% | 57% | falling knife: wait 2 stable sessions |
| XPEV | -2.5% | -46% | 57% | event hold: earnings 2026-11-16 |
| PLTR | -9.7% | -26% | 57% | falling knife: wait 2 stable sessions |
| CRSP | -6.2% | -22% | 57% | falling knife: wait 2 stable sessions |
| GEV | -7.5% | -34% | 54% | falling knife: wait 2 stable sessions; thin listed options |
| SOFI | -7.7% | -16% | 54% | falling knife: wait 2 stable sessions |
| VST | -6.2% | -33% | 54% | falling knife: wait 2 stable sessions |
| AVGO | -10.4% | -39% | 49% | falling knife: wait 2 stable sessions |
| TSLA | -10.8% | -23% | 49% | falling knife: wait 2 stable sessions |
| BIDU | -1.2% | -47% | 46% | event hold: earnings 2026-11-16 |
| NVDA | -9.3% | -24% | 46% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-17 |
| MELI | -12.0% | -24% | 42% | falling knife: wait 2 stable sessions; thin listed options |
| PDD | +2.2% | -16% | 40% | event hold: earnings 2026-11-17 |
| JD | +3.3% | -15% | 38% | event hold: earnings 2026-11-17 |
| LLY | -3.8% | -4% | 37% | thin listed options |
| ISRG | -2.8% | -3% | 36% | thin listed options |
| TCOM | +2.6% | -17% | 36% | event hold: earnings 2026-11-16 |
| ZBH | -3.0% | -3% | 32% | thin listed options |

## Full screen (eligible names, by score)

| Ticker | Theme | Last | 1D | vs 6M high | Vol used | Vol src | RV20 | ATM OI | Next earnings | Valuation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RIVN | EV/Auto | 13.29 | -5.5% | -34% | 63% | 6M straddle | 58% | 16,883 | n/a | n/a |
| DKNG | Cyclical/Consumer | 23.52 | +1.8% | -22% | 57% | 6M straddle | 40% | 4,487 | n/a | n/a |
| FSLR | Solar/Clean | 195.76 | +0.6% | -38% | 52% | 6M straddle | 40% | 2,068 | n/a | n/a |
| TDOC | Biotech/Health | 9.41 | -3.0% | -3% | 60% | 6M straddle | 98% | 3,787 | n/a | n/a |
| NIO | China ADR | 3.20 | -3.0% | -51% | 57% | 6M straddle | 39% | 21,119 | 2026-11-24 | n/a |
| BABA | China ADR | 108.07 | +2.6% | -26% | 45% | 6M straddle | 37% | 2,385 | 2026-11-24 | n/a |
| UAL | Cyclical/Consumer | 110.49 | -4.6% | -19% | 49% | 6M straddle | 55% | 3,457 | n/a | n/a |
| GOOGL | Mega-cap | 282.57 | -2.2% | -30% | 37% | 6M straddle | 53% | 6,235 | n/a | n/a |
| NVO | Biotech/Health | 40.30 | -4.5% | -22% | 35% | 6M straddle | 32% | 56,524 | n/a | n/a |
| DXCM | Biotech/Health | 84.46 | -4.5% | -9% | 43% | 6M straddle | 48% | 2,053 | n/a | supported |

## Before you send an RFQ

1. Check live spot; never strike off a fresh heavy down day (2-session stabilization rule).
2. Check earnings / FDA / launch dates inside the tenor (`reference/event-calendar.md`) and option expiry quirks (`reference/option-expiry-quirks.md`).
3. Ask for a KI ladder, not a single KI. Choose by coupon pickup per KI point.
4. Compare issuer quotes like-for-like: tenor, KO level/observation, KI level/observation, strike, RO, coupon frequency.

```text
Please quote a USD worst-of FCN on [TICKERS], 3M and 6M, KO 100% monthly (also 98/102 if available),
fixed monthly coupon, strike 100%, RO 100 (and requested RO). Coupon p.a. across KI 50/55/59/65/70
at maturity, with estimated value, bid/offer and key assumptions.
```

## Data notes

- Names with usable data: 73/73; with listed-options read: 73/73.
- Vol source used: Tradier/ORATS 0, Nasdaq straddle 73, realized-vol fallback 0.
- Tradier/ORATS: not configured. Add a `TRADIER_TOKEN` repository secret to use ORATS IV (see `research/data-sources.md`).
- Valuation file: 9 names from `fundamentals/valuation.csv` (oldest row 2026-11-06).
- Missing today: none.
- Model rate assumption 3.90% + 0.50% funding; ballpark low end = ATM vol and 1.5% issuer margin, high end = ATM vol +3 pts and 0.75% margin.
- Crypto-linked names are excluded by default.

_Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems._
