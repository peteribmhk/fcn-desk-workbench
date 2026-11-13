# FCN Daily Screen

**Generated:** 2026-11-13 10:36 HKT  |  **US close used:** 2026-11-12  |  **Data status:** GREEN

> Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
> Public/delayed data, used only to decide what to RFQ. Issuer RFQ levels override everything below.

## How to read this

Structure assumed for the ballpark: USD worst-of FCN, 6M, KO 100% monthly from month 1, KI 59% observed at maturity, strike 100%, RO 100, monthly fixed coupon. Vols come from listed ATM straddles (Nasdaq); correlation from 90-day realized returns. The ballpark ignores skew, dividends and issuer-specific funding, so treat it as a sanity check for issuer levels, not a forecast. Every basket mixes different themes on purpose; same-sector pairs are pseudo-diversification.

## Two-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AVGO / TSLA | Semis/AI HW + EV/Auto | 48 / 46 | 0.49 | 15-21% | 10% | Balanced | fresh |
| 2 | AVGO / DXCM | Semis/AI HW + Biotech/Health | 48 / 43 | -0.07 | 15-21% | 11% | Balanced | fresh |
| 3 | RIVN / STX | EV/Auto + Semis/AI HW | 64 / 72 | 0.07 | 43-49% | 28% | Higher coupon | fresh |
| 4 | STX / ENPH | Semis/AI HW + Solar/Clean | 72 / 71 | 0.17 | 46-52% | 29% | Higher coupon | fresh |
| 5 | APLD / VKTX | AI Cloud/DC + Biotech/Health | 98 / 66 | 0.24 | 59-64% | 34% | Aggressive | fresh |

## Three-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AVGO / TSLA / DXCM | Semis/AI HW + EV/Auto + Biotech/Health | 48 / 46 / 43 | 0.17 | 19-26% | 15% | Balanced | fresh |
| 2 | VKTX / STX / ENPH | Biotech/Health + Semis/AI HW + Solar/Clean | 66 / 72 / 71 | 0.20 | 55-61% | 39% | Higher coupon | fresh |
| 3 | APLD / ASTS / DKNG | AI Cloud/DC + Space/Defense + Cyclical/Consumer | 98 / 96 / 58 | 0.16 | 69-74% | 46% | Aggressive | fresh |

## Why these names

- **AVGO / TSLA**: AVGO: sweet spot (-20% to -50%), -24% vs 6M high, vol 48% (6M straddle), next earnings 2026-12-09; TSLA: mild pullback, -10% vs 6M high, vol 46% (6M straddle)
- **AVGO / DXCM**: AVGO: sweet spot (-20% to -50%), -24% vs 6M high, vol 48% (6M straddle), next earnings 2026-12-09; DXCM: mild pullback, -12% vs 6M high, vol 43% (6M straddle), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%)
- **RIVN / STX**: RIVN: sweet spot (-20% to -50%), -36% vs 6M high, vol 64% (6M straddle); STX: deep drawdown (>50%), -50% vs 6M high, vol 72% (6M straddle), thesis check needed (no valuation data)
- **AVGO / TSLA / DXCM**: AVGO: sweet spot (-20% to -50%), -24% vs 6M high, vol 48% (6M straddle), next earnings 2026-12-09; TSLA: mild pullback, -10% vs 6M high, vol 46% (6M straddle); DXCM: mild pullback, -12% vs 6M high, vol 43% (6M straddle), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%)
- **VKTX / STX / ENPH**: VKTX: sweet spot (-20% to -50%), -35% vs 6M high, vol 66% (6M straddle); STX: deep drawdown (>50%), -50% vs 6M high, vol 72% (6M straddle), thesis check needed (no valuation data); ENPH: deep drawdown (>50%), -63% vs 6M high, vol 71% (6M straddle), thesis check needed (no valuation data)

## Valuation cross-check (legs in today's picks)

Would you be happy to own the worst leg at the strike? Cheap against its own 10-year range, an analyst target above the price and growing revenue make a sturdier floor. Not blocking: it informs the RFQ, it does not remove names. Data: `fundamentals/valuation.csv`.

| Ticker | vs 6M high | Valuation read | Caveat |
| --- | --- | --- | --- |
| ASTS | -74% | **no data: thesis check before RFQ** |  |
| APLD | -66% | **no data: thesis check before RFQ** |  |
| ENPH | -63% | **no data: thesis check before RFQ** |  |
| STX | -50% | **no data: thesis check before RFQ** |  |
| RIVN | -36% | no data |  |
| DKNG | -35% | no data |  |
| VKTX | -35% | no data |  |
| AVGO | -24% | no data |  |
| DXCM | -12% | supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%) |  |
| TSLA | -10% | no data |  |

## KI ladder: AVGO / TSLA (top pair)

| KI | Ballpark coupon p.a. | P(loss at maturity) | Pickup per KI pt | Read |
| --- | --- | --- | --- | --- |
| 50% | 6.5-11.1% | 3.9% | - | base protection |
| 55% | 10.9-16.4% | 6.9% | 0.96% p.a. | strong pickup |
| 59% | 15.3-21.3% | 10.0% | 1.15% p.a. | strong pickup |
| 65% | 22.3-28.5% | 15.8% | 1.19% p.a. | strong pickup |
| 70% | 28.0-33.8% | 21.2% | 1.09% p.a. | strong pickup |

Pickup per KI point thresholds: below 0.25% p.a. keep the lower KI; 0.25-0.60% balanced; above 0.60% the higher KI may be worth it. Model pickup is smooth by construction; the real decision uses the issuer's KI ladder.

## Conditional / watch only

| Ticker | 1D | vs 6M high | Vol | Why held back |
| --- | --- | --- | --- | --- |
| SMR | -7.8% | -65% | 94% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| NBIS | -16.8% | -55% | 92% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| CRDO | -1.1% | -54% | 89% | thesis check: >50% off high without valuation support; thin listed options |
| NTLA | -7.5% | -41% | 87% | falling knife: wait 2 stable sessions |
| CRWV | -6.9% | -55% | 87% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| QBTS | -7.6% | -67% | 86% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| SMCI | -11.3% | -46% | 85% | falling knife: wait 2 stable sessions |
| MRNA | -7.0% | -14% | 83% | falling knife: wait 2 stable sessions; thin listed options |
| LEU | -7.4% | -48% | 80% | falling knife: wait 2 stable sessions; thin listed options |
| SNDK | -4.1% | -60% | 79% | thesis check: >50% off high without valuation support; thin listed options |
| RGTI | -7.0% | -62% | 77% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| IONQ | -9.4% | -57% | 76% | falling knife: wait 2 stable sessions |
| HIMS | +8.8% | -46% | 75% | falling knife: wait 2 stable sessions |
| DELL | +11.8% | -36% | 72% | event hold: earnings 2026-11-24; thin listed options |
| AVAV | -2.9% | -44% | 70% | thin listed options |
| LITE | +10.7% | -43% | 68% | thin listed options |
| KTOS | -5.3% | -47% | 65% | thin listed options |
| APP | -2.7% | -36% | 64% | thin listed options |
| ZS | -0.3% | -26% | 64% | falling knife: wait 2 stable sessions; thin listed options |
| DDOG | +0.0% | -37% | 62% | thin listed options |
| VRT | +1.5% | -43% | 62% | thin listed options |
| AFRM | -2.9% | -23% | 60% | falling knife: wait 2 stable sessions; thin listed options |
| XPEV | -3.8% | -47% | 57% | event hold: earnings 2026-11-16 |
| CRSP | -6.8% | -31% | 55% | falling knife: wait 2 stable sessions; thin listed options |
| TLN | +2.1% | -12% | 54% | thin listed options |
| NIO | -5.9% | -50% | 53% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-24 |
| GEV | +1.4% | -31% | 52% | thin listed options |
| VST | +0.8% | -20% | 48% | thin listed options |
| NVDA | -4.3% | -31% | 47% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-17 |
| BIDU | -2.7% | -44% | 46% | event hold: earnings 2026-11-16 |
| UAL | -6.0% | -18% | 46% | falling knife: wait 2 stable sessions |
| BABA | -7.1% | -30% | 45% | falling knife: wait 2 stable sessions; event hold: earnings 2026-11-19 |
| MELI | -2.4% | -26% | 41% | falling knife: wait 2 stable sessions; thin listed options |
| JD | -1.6% | -17% | 37% | event hold: earnings 2026-11-17 |
| PDD | -1.9% | -21% | 37% | event hold: earnings 2026-11-17 |
| ISRG | -2.1% | -9% | 36% | thin listed options |
| LLY | -0.7% | -1% | 36% | thin listed options |
| TCOM | -0.9% | -13% | 35% | event hold: earnings 2026-11-16 |
| ZBH | -2.7% | -5% | 31% | thin listed options |

## Full screen (eligible names, by score)

| Ticker | Theme | Last | 1D | vs 6M high | Vol used | Vol src | RV20 | ATM OI | Next earnings | Valuation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APLD | AI Cloud/DC | 16.95 | -5.4% | -66% | 98% | 6M straddle | 129% | 10,471 | 2027-01-06 | n/a |
| BE | Nuclear/Power | 201.93 | -3.6% | -42% | 83% | 6M straddle | 129% | 3,922 | n/a | supported* |
| ASTS | Space/Defense | 34.50 | -5.8% | -74% | 96% | 6M straddle | 116% | 7,089 | n/a | n/a |
| COHR | Semis/AI HW | 232.08 | -1.0% | -46% | 78% | 6M straddle | 128% | 1,008 | n/a | n/a |
| LUNR | Space/Defense | 13.03 | +7.0% | -71% | 89% | 6M straddle | 127% | 1,591 | n/a | n/a |
| OKLO | Nuclear/Power | 24.45 | -5.5% | -67% | 82% | 6M straddle | 120% | 9,353 | n/a | n/a |
| ALAB | Semis/AI HW | 227.79 | -1.4% | -53% | 82% | 6M straddle | 130% | 1,446 | n/a | n/a |
| MRVL | Semis/AI HW | 164.45 | -2.6% | -48% | 66% | 6M straddle | 125% | 2,970 | 2026-12-01 | n/a |
| VKTX | Biotech/Health | 27.58 | -3.0% | -35% | 66% | 6M straddle | 74% | 2,470 | n/a | n/a |
| RKLB | Space/Defense | 64.07 | -3.1% | -57% | 76% | 6M straddle | 107% | 16,986 | n/a | n/a |
| RIVN | EV/Auto | 12.80 | -5.5% | -36% | 64% | 6M straddle | 61% | 17,611 | n/a | n/a |
| STX | Semis/AI HW | 545.14 | -1.2% | -50% | 72% | 6M straddle | 108% | 1,044 | n/a | n/a |
| ENPH | Solar/Clean | 26.78 | -5.4% | -63% | 71% | 6M straddle | 94% | 2,841 | n/a | n/a |
| QUBT | Quantum | 5.82 | -5.7% | -53% | 70% | 6M straddle | 93% | 7,149 | n/a | n/a |
| MU | Semis/AI HW | 798.44 | -1.6% | -34% | 60% | 6M straddle | 106% | 2,907 | 2026-12-16 | n/a |
| ORCL | Software | 127.11 | -1.0% | -49% | 59% | 6M straddle | 78% | 5,155 | 2026-12-09 | n/a |
| NET | Software | 318.50 | +1.1% | -12% | 64% | 6M straddle | 86% | 1,432 | n/a | n/a |
| ARM | Semis/AI HW | 199.78 | -1.8% | -55% | 67% | 6M straddle | 99% | 1,379 | n/a | n/a |
| WDC | Semis/AI HW | 311.21 | -0.7% | -58% | 67% | 6M straddle | 111% | 1,149 | n/a | n/a |
| DKNG | Cyclical/Consumer | 19.64 | +1.4% | -35% | 58% | 6M straddle | 96% | 11,310 | n/a | n/a |
| AMAT | Semis/AI HW | 380.95 | -3.6% | -47% | 57% | 6M straddle | 91% | 1,916 | n/a | n/a |
| TDOC | Biotech/Health | 8.69 | -2.8% | -11% | 60% | 6M straddle | 104% | 3,810 | n/a | n/a |
| SNOW | Software | 298.70 | -0.8% | -19% | 59% | 6M straddle | 64% | 1,527 | 2026-12-02 | n/a |
| FSLR | Solar/Clean | 172.30 | -3.3% | -46% | 51% | 6M straddle | 47% | 7,192 | n/a | n/a |
| GLW | Semis/AI HW | 120.46 | +7.4% | -53% | 59% | 6M straddle | 83% | 2,116 | n/a | n/a |
| PLTR | Software | 171.58 | -0.5% | -18% | 55% | 6M straddle | 63% | 3,336 | n/a | n/a |
| AMD | Semis/AI HW | 585.30 | +5.9% | -10% | 60% | 6M straddle | 120% | 8,929 | n/a | n/a |
| SOFI | Fintech | 15.63 | -3.9% | -19% | 53% | 6M straddle | 68% | 3,275 | n/a | n/a |
| AVGO | Semis/AI HW | 364.36 | +5.5% | -24% | 48% | 6M straddle | 70% | 3,363 | 2026-12-09 | n/a |
| ANET | Semis/AI HW | 206.63 | +5.1% | -5% | 55% | 6M straddle | 86% | 3,563 | n/a | n/a |
| TSLA | EV/Auto | 397.45 | +1.7% | -10% | 46% | 6M straddle | 61% | 1,779 | n/a | n/a |
| DXCM | Biotech/Health | 81.39 | +1.3% | -12% | 43% | 6M straddle | 50% | 3,896 | n/a | supported |
| GOOGL | Mega-cap | 298.70 | +1.8% | -25% | 36% | 6M straddle | 55% | 6,995 | n/a | n/a |
| NVO | Biotech/Health | 40.65 | -1.1% | -21% | 34% | 6M straddle | 32% | 59,064 | n/a | n/a |

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
