# FCN Daily Screen

**Generated:** 2026-11-16 09:59 HKT  |  **US close used:** 2026-11-13  |  **Data status:** GREEN

> Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
> Public/delayed data, used only to decide what to RFQ. Issuer RFQ levels override everything below.

## How to read this

Structure assumed for the ballpark: USD worst-of FCN, 6M, KO 100% monthly from month 1, KI 59% observed at maturity, strike 100%, RO 100, monthly fixed coupon. Vols come from listed ATM straddles (Nasdaq); correlation from 90-day realized returns. The ballpark ignores skew, dividends and issuer-specific funding, so treat it as a sanity check for issuer levels, not a forecast. Every basket mixes different themes on purpose; same-sector pairs are pseudo-diversification.

## Two-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AVGO / UAL | Semis/AI HW + Cyclical/Consumer | 49 / 47 | 0.34 | 17-23% | 11% | Balanced | fresh |
| 2 | AVGO / TSLA | Semis/AI HW + EV/Auto | 49 / 46 | 0.48 | 16-22% | 10% | Balanced | repeat, same rationale |
| 3 | VKTX / ENPH | Biotech/Health + Solar/Clean | 72 / 73 | 0.17 | 47-53% | 30% | Higher coupon | fresh |
| 4 | VKTX / RKLB | Biotech/Health + Space/Defense | 72 / 73 | 0.24 | 47-53% | 29% | Higher coupon | fresh |
| 5 | APLD / DKNG | AI Cloud/DC + Cyclical/Consumer | 97 / 60 | -0.17 | 57-62% | 36% | Aggressive | fresh |

## Three-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AVGO / UAL / TSLA | Semis/AI HW + Cyclical/Consumer + EV/Auto | 49 / 47 / 46 | 0.37 | 21-27% | 16% | Balanced | fresh |
| 2 | VKTX / ENPH / WDC | Biotech/Health + Solar/Clean + Semis/AI HW | 72 / 73 / 70 | 0.18 | 58-64% | 41% | Higher coupon | fresh |
| 3 | APLD / VKTX / DKNG | AI Cloud/DC + Biotech/Health + Cyclical/Consumer | 97 / 72 / 60 | 0.01 | 67-72% | 48% | Aggressive | fresh |

## Why these names

- **AVGO / UAL**: AVGO: sweet spot (-20% to -50%), -28% vs 6M high, vol 49% (6M straddle), next earnings 2026-12-09; UAL: mild pullback, -20% vs 6M high, vol 47% (6M straddle)
- **AVGO / TSLA**: AVGO: sweet spot (-20% to -50%), -28% vs 6M high, vol 49% (6M straddle), next earnings 2026-12-09; TSLA: mild pullback, -12% vs 6M high, vol 46% (6M straddle)
- **VKTX / ENPH**: VKTX: sweet spot (-20% to -50%), -31% vs 6M high, vol 72% (6M straddle); ENPH: deep drawdown (>50%), -64% vs 6M high, vol 73% (6M straddle), thesis check needed (no valuation data)
- **AVGO / UAL / TSLA**: AVGO: sweet spot (-20% to -50%), -28% vs 6M high, vol 49% (6M straddle), next earnings 2026-12-09; UAL: mild pullback, -20% vs 6M high, vol 47% (6M straddle); TSLA: mild pullback, -12% vs 6M high, vol 46% (6M straddle)
- **VKTX / ENPH / WDC**: VKTX: sweet spot (-20% to -50%), -31% vs 6M high, vol 72% (6M straddle); ENPH: deep drawdown (>50%), -64% vs 6M high, vol 73% (6M straddle), thesis check needed (no valuation data); WDC: deep drawdown (>50%), -60% vs 6M high, vol 70% (6M straddle), thesis check needed (no valuation data)

## Valuation cross-check (legs in today's picks)

Would you be happy to own the worst leg at the strike? Cheap against its own 10-year range, an analyst target above the price and growing revenue make a sturdier floor. Not blocking: it informs the RFQ, it does not remove names. Data: `fundamentals/valuation.csv`.

| Ticker | vs 6M high | Valuation read | Caveat |
| --- | --- | --- | --- |
| APLD | -68% | **no data: thesis check before RFQ** |  |
| ENPH | -64% | **no data: thesis check before RFQ** |  |
| WDC | -60% | **no data: thesis check before RFQ** |  |
| RKLB | -59% | **no data: thesis check before RFQ** |  |
| DKNG | -37% | no data |  |
| VKTX | -31% | no data |  |
| AVGO | -28% | no data |  |
| UAL | -20% | no data |  |
| TSLA | -12% | no data |  |

## KI ladder: AVGO / UAL (top pair)

| KI | Ballpark coupon p.a. | P(loss at maturity) | Pickup per KI pt | Read |
| --- | --- | --- | --- | --- |
| 50% | 7.3-12.0% | 4.4% | - | base protection |
| 55% | 12.0-17.6% | 7.6% | 1.04% p.a. | strong pickup |
| 59% | 16.8-22.8% | 11.3% | 1.25% p.a. | strong pickup |
| 65% | 24.2-30.3% | 17.6% | 1.24% p.a. | strong pickup |
| 70% | 30.0-35.7% | 23.3% | 1.11% p.a. | strong pickup |

Pickup per KI point thresholds: below 0.25% p.a. keep the lower KI; 0.25-0.60% balanced; above 0.60% the higher KI may be worth it. Model pickup is smooth by construction; the real decision uses the issuer's KI ladder.

## Conditional / watch only

| Ticker | 1D | vs 6M high | Vol | Why held back |
| --- | --- | --- | --- | --- |
| NBIS | -9.9% | -60% | 95% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| CRWV | -6.1% | -57% | 91% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| CRDO | -5.9% | -57% | 89% | thesis check: >50% off high without valuation support; thin listed options |
| NTLA | -8.1% | -46% | 87% | falling knife: wait 2 stable sessions |
| RGTI | -6.9% | -64% | 87% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| SMCI | -0.5% | -46% | 86% | falling knife: wait 2 stable sessions |
| MRNA | -3.4% | -17% | 83% | thin listed options |
| IONQ | -6.4% | -60% | 83% | falling knife: wait 2 stable sessions; thin listed options |
| LEU | -0.1% | -48% | 82% | thin listed options |
| QUBT | -4.5% | -55% | 82% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| SNDK | -5.6% | -62% | 80% | thesis check: >50% off high without valuation support; thin listed options |
| COHR | -6.0% | -49% | 79% | falling knife: wait 2 stable sessions; thin listed options |
| DELL | -7.2% | -41% | 74% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-24; thin listed options |
| LITE | -4.5% | -47% | 74% | thin listed options |
| STX | -3.1% | -52% | 73% | thesis check: >50% off high without valuation support; thin listed options |
| AVAV | -2.7% | -45% | 71% | thin listed options |
| KTOS | -2.4% | -48% | 67% | thin listed options |
| NET | -4.0% | -15% | 65% | thin listed options |
| APP | +3.9% | -33% | 65% | thin listed options |
| ZS | -0.4% | -26% | 64% | falling knife: wait 2 stable sessions; thin listed options |
| VRT | -3.6% | -44% | 64% | thin listed options |
| DDOG | -0.2% | -37% | 62% | thin listed options |
| NIO | -4.9% | -52% | 62% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-24 |
| AMD | -8.8% | -18% | 61% | falling knife: wait 2 stable sessions |
| SNOW | -2.6% | -21% | 60% | thin listed options |
| AFRM | -1.1% | -24% | 59% | falling knife: wait 2 stable sessions; thin listed options |
| AMAT | -2.7% | -49% | 57% | thin listed options |
| CRSP | -0.9% | -32% | 57% | falling knife: wait 2 stable sessions; thin listed options |
| XPEV | -1.0% | -48% | 55% | event hold: earnings 2026-11-16 |
| TLN | -2.8% | -14% | 53% | thin listed options |
| GEV | -1.9% | -32% | 52% | thin listed options |
| VST | -1.1% | -21% | 49% | thin listed options |
| NVDA | -2.0% | -32% | 48% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-17 |
| BIDU | +0.7% | -43% | 48% | event hold: earnings 2026-11-16 |
| JD | +1.5% | -17% | 44% | event hold: earnings 2026-11-17 |
| BABA | +0.0% | -30% | 44% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-19 |
| MELI | +1.1% | -26% | 41% | falling knife: wait 2 stable sessions |
| PDD | +1.9% | -20% | 37% | event hold: earnings 2026-11-19 |
| ISRG | +0.8% | -8% | 37% | thin listed options |
| LLY | +1.1% | 0% | 36% | thin listed options |
| TCOM | +0.9% | -12% | 34% | event hold: earnings 2026-11-16 |
| ZBH | -1.3% | -6% | 31% | thin listed options |

## Full screen (eligible names, by score)

| Ticker | Theme | Last | 1D | vs 6M high | Vol used | Vol src | RV20 | ATM OI | Next earnings | Valuation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ASTS | Space/Defense | 32.60 | -5.5% | -76% | 98% | 6M straddle | 113% | 7,098 | n/a | n/a |
| BE | Nuclear/Power | 191.99 | -4.9% | -44% | 84% | 6M straddle | 129% | 2,631 | n/a | supported* |
| APLD | AI Cloud/DC | 15.97 | -5.8% | -68% | 97% | 6M straddle | 123% | 1,430 | 2027-01-06 | n/a |
| HIMS | Biotech/Health | 19.73 | +0.0% | -48% | 77% | 6M straddle | 110% | 2,339 | n/a | n/a |
| SMR | Nuclear/Power | 4.66 | -3.3% | -67% | 89% | 6M straddle | 101% | 5,117 | n/a | n/a |
| LUNR | Space/Defense | 13.00 | -0.2% | -72% | 89% | 6M straddle | 124% | 1,622 | n/a | n/a |
| QBTS | Quantum | 9.56 | -2.8% | -68% | 86% | 6M straddle | 104% | 21,532 | n/a | n/a |
| VKTX | Biotech/Health | 29.22 | +5.9% | -31% | 72% | 6M straddle | 69% | 4,193 | n/a | n/a |
| ALAB | Semis/AI HW | 221.83 | -2.6% | -54% | 83% | 6M straddle | 129% | 1,465 | n/a | n/a |
| OKLO | Nuclear/Power | 23.92 | -2.2% | -67% | 82% | 6M straddle | 118% | 9,352 | n/a | n/a |
| RKLB | Space/Defense | 61.53 | -4.0% | -59% | 73% | 6M straddle | 103% | 12,343 | n/a | n/a |
| ENPH | Solar/Clean | 26.07 | -2.7% | -64% | 73% | 6M straddle | 94% | 2,847 | n/a | n/a |
| RIVN | EV/Auto | 12.18 | -4.8% | -40% | 62% | 6M straddle | 62% | 45,454 | n/a | n/a |
| ORCL | Software | 125.35 | -1.4% | -49% | 62% | 6M straddle | 77% | 5,202 | 2026-12-09 | n/a |
| MU | Semis/AI HW | 778.31 | -2.5% | -36% | 61% | 6M straddle | 104% | 1,396 | 2026-12-16 | n/a |
| WDC | Semis/AI HW | 295.65 | -5.0% | -60% | 70% | 6M straddle | 109% | 5,665 | n/a | n/a |
| DKNG | Cyclical/Consumer | 18.89 | -1.2% | -37% | 60% | 6M straddle | 96% | 11,463 | n/a | n/a |
| ARM | Semis/AI HW | 190.53 | -4.6% | -57% | 69% | 6M straddle | 97% | 2,760 | n/a | n/a |
| MRVL | Semis/AI HW | 156.76 | -4.7% | -50% | 67% | 6M straddle | 125% | 3,568 | 2026-12-01 | n/a |
| GLW | Semis/AI HW | 114.08 | -4.5% | -55% | 61% | 6M straddle | 83% | 2,279 | n/a | n/a |
| FSLR | Solar/Clean | 171.39 | -0.5% | -46% | 52% | 6M straddle | 45% | 7,212 | n/a | n/a |
| PLTR | Software | 167.99 | -2.1% | -20% | 56% | 6M straddle | 59% | 3,427 | n/a | n/a |
| TDOC | Biotech/Health | 8.80 | +1.3% | -9% | 60% | 6M straddle | 100% | 3,811 | n/a | n/a |
| AVGO | Semis/AI HW | 347.01 | -4.8% | -28% | 49% | 6M straddle | 71% | 3,885 | 2026-12-09 | n/a |
| SOFI | Fintech | 15.42 | -1.3% | -20% | 53% | 6M straddle | 67% | 4,715 | n/a | n/a |
| ANET | Semis/AI HW | 197.29 | -4.5% | -9% | 56% | 6M straddle | 86% | 3,427 | n/a | n/a |
| UAL | Cyclical/Consumer | 109.31 | -1.7% | -20% | 47% | 6M straddle | 58% | 3,509 | n/a | n/a |
| TSLA | EV/Auto | 390.22 | -1.8% | -12% | 46% | 6M straddle | 61% | 6,387 | n/a | n/a |
| GOOGL | Mega-cap | 295.77 | -1.0% | -25% | 36% | 6M straddle | 54% | 3,551 | n/a | n/a |
| DXCM | Biotech/Health | 83.33 | +2.4% | -10% | 42% | 6M straddle | 50% | 4,036 | n/a | supported |
| NVO | Biotech/Health | 41.63 | +2.4% | -19% | 35% | 6M straddle | 33% | 15,598 | n/a | n/a |

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
