# FCN Daily Screen

**Generated:** 2026-11-24 13:58 HKT  |  **US close used:** 2026-11-23  |  **Data status:** GREEN

> Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
> Public/delayed data, used only to decide what to RFQ. Issuer RFQ levels override everything below.

## How to read this

Structure assumed for the ballpark: USD worst-of FCN, 6M, KO 100% monthly from month 1, KI 59% observed at maturity, strike 100%, RO 100, monthly fixed coupon. Vols come from listed ATM straddles (Nasdaq); correlation from 90-day realized returns. The ballpark ignores skew, dividends and issuer-specific funding, so treat it as a sanity check for issuer levels, not a forecast. Every basket mixes different themes on purpose; same-sector pairs are pseudo-diversification.

## Two-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TSLA / DXCM | EV/Auto + Biotech/Health | 48 / 44 | 0.17 | 15-21% | 11% | Balanced | fresh |
| 2 | TSLA / TCOM | EV/Auto + China ADR | 48 / 41 | -0.11 | 14-19% | 10% | Balanced | fresh |
| 3 | VKTX / AMD | Biotech/Health + Semis/AI HW | 68 / 66 | 0.23 | 40-46% | 26% | Higher coupon | fresh |
| 4 | AMD / TDOC | Semis/AI HW + Biotech/Health | 66 / 64 | -0.17 | 40-45% | 27% | Higher coupon | fresh |
| 5 | COHR / NTLA | Semis/AI HW + Biotech/Health | 87 / 86 | 0.32 | 61-66% | 35% | Aggressive | fresh |

## Three-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TSLA / DXCM / TCOM | EV/Auto + Biotech/Health + China ADR | 48 / 44 / 41 | 0.12 | 18-24% | 14% | Balanced | fresh |
| 2 | AMD / TDOC / UAL | Semis/AI HW + Biotech/Health + Cyclical/Consumer | 66 / 64 / 50 | 0.13 | 43-49% | 32% | Higher coupon | fresh |
| 3 | NTLA / LUNR / ALAB | Biotech/Health + Space/Defense + Semis/AI HW | 86 / 89 / 87 | 0.44 | 70-75% | 43% | Aggressive | fresh |

## Why these names

- **TSLA / DXCM**: TSLA: mild pullback, -13% vs 6M high, vol 48% (6M straddle); DXCM: mild pullback, -11% vs 6M high, vol 44% (6M straddle), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%)
- **TSLA / TCOM**: TSLA: mild pullback, -13% vs 6M high, vol 48% (6M straddle); TCOM: mild pullback, -15% vs 6M high, vol 41% (6M straddle)
- **VKTX / AMD**: VKTX: sweet spot (-20% to -50%), -34% vs 6M high, vol 68% (6M straddle); AMD: sweet spot (-20% to -50%), -30% vs 6M high, vol 66% (6M straddle)
- **TSLA / DXCM / TCOM**: TSLA: mild pullback, -13% vs 6M high, vol 48% (6M straddle); DXCM: mild pullback, -11% vs 6M high, vol 44% (6M straddle), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%); TCOM: mild pullback, -15% vs 6M high, vol 41% (6M straddle)
- **AMD / TDOC / UAL**: AMD: sweet spot (-20% to -50%), -30% vs 6M high, vol 66% (6M straddle); TDOC: sweet spot (-20% to -50%), -21% vs 6M high, vol 64% (6M straddle); UAL: sweet spot (-20% to -50%), -20% vs 6M high, vol 50% (6M straddle)

## Valuation cross-check (legs in today's picks)

Would you be happy to own the worst leg at the strike? Cheap against its own 10-year range, an analyst target above the price and growing revenue make a sturdier floor. Not blocking: it informs the RFQ, it does not remove names. Data: `fundamentals/valuation.csv`.

| Ticker | vs 6M high | Valuation read | Caveat |
| --- | --- | --- | --- |
| LUNR | -79% | **no data: thesis check before RFQ** |  |
| ALAB | -54% | **no data: thesis check before RFQ** |  |
| COHR | -49% | no data |  |
| NTLA | -43% | no data |  |
| VKTX | -34% | no data |  |
| AMD | -30% | no data |  |
| TDOC | -21% | no data |  |
| UAL | -20% | no data |  |
| TCOM | -15% | no data |  |
| TSLA | -13% | no data |  |
| DXCM | -11% | supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%) |  |

## KI ladder: TSLA / DXCM (top pair)

| KI | Ballpark coupon p.a. | P(loss at maturity) | Pickup per KI pt | Read |
| --- | --- | --- | --- | --- |
| 50% | 6.2-10.7% | 3.9% | - | base protection |
| 55% | 10.8-16.3% | 7.1% | 1.01% p.a. | strong pickup |
| 59% | 15.3-21.2% | 10.7% | 1.18% p.a. | strong pickup |
| 65% | 22.8-28.8% | 17.3% | 1.26% p.a. | strong pickup |
| 70% | 28.8-34.6% | 23.5% | 1.18% p.a. | strong pickup |

Pickup per KI point thresholds: below 0.25% p.a. keep the lower KI; 0.25-0.60% balanced; above 0.60% the higher KI may be worth it. Model pickup is smooth by construction; the real decision uses the issuer's KI ladder.

## Conditional / watch only

| Ticker | 1D | vs 6M high | Vol | Why held back |
| --- | --- | --- | --- | --- |
| NBIS | +20.3% | -66% | 109% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| APLD | +20.3% | -72% | 107% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| ASTS | +10.3% | -81% | 104% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| SMR | +5.1% | -75% | 103% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| CRWV | +22.3% | -61% | 96% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| IONQ | +12.6% | -68% | 94% | falling knife: wait 2 stable sessions |
| QBTS | +12.1% | -76% | 93% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| CRDO | +22.6% | -60% | 92% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-12-01 |
| RGTI | +13.1% | -70% | 91% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| SNDK | +10.7% | -70% | 91% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| QUBT | +7.4% | -62% | 90% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| BE | +18.1% | -51% | 90% | falling knife: wait 2 stable sessions |
| SMCI | +13.3% | -51% | 87% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| ENPH | +6.3% | -71% | 86% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| HIMS | +3.2% | -61% | 85% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| LEU | +6.6% | -56% | 83% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| MRNA | +8.8% | -21% | 83% | falling knife: wait 2 stable sessions |
| RKLB | +9.3% | -67% | 82% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| LITE | +18.2% | -52% | 79% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| AVAV | +4.5% | -58% | 78% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-12-08; thin listed options |
| STX | +13.8% | -52% | 77% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| DELL | +20.5% | -43% | 76% | falling knife: wait 2 stable sessions; thin listed options |
| WDC | +13.8% | -60% | 76% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| KTOS | +6.0% | -56% | 75% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| MRVL | +18.4% | -54% | 74% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-12-01 |
| ARM | +16.1% | -60% | 73% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| RIVN | +8.6% | -44% | 70% | falling knife: wait 2 stable sessions |
| NET | +5.9% | -19% | 69% | thin listed options |
| VRT | +12.1% | -48% | 68% | falling knife: wait 2 stable sessions; thin listed options |
| APP | +7.4% | -39% | 67% | thin listed options |
| GLW | +14.8% | -58% | 67% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| MU | +19.0% | -42% | 66% | falling knife: wait 2 stable sessions |
| DDOG | +7.4% | -42% | 66% | falling knife: wait 2 stable sessions; thin listed options |
| DKNG | -0.3% | -48% | 66% | falling knife: wait 2 stable sessions |
| ORCL | +12.3% | -54% | 63% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| AFRM | +8.2% | -32% | 62% | falling knife: wait 2 stable sessions; thin listed options |
| SNOW | +6.5% | -26% | 62% | falling knife: wait 2 stable sessions; event hold: earnings 2026-12-02; thin listed options |
| XPEV | +7.4% | -51% | 61% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| ZS | +17.7% | -12% | 61% | event hold: earnings 2026-12-02; thin listed options |
| AMAT | +14.6% | -52% | 61% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| NIO | +4.9% | -57% | 60% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-12-01 |
| SOFI | +4.9% | -32% | 60% | falling knife: wait 2 stable sessions |
| PLTR | +11.1% | -24% | 58% | falling knife: wait 2 stable sessions |
| CRSP | +10.7% | -30% | 58% | thin listed options |
| FSLR | +6.5% | -54% | 57% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| TLN | +9.6% | -17% | 56% | thin listed options |
| GEV | +8.2% | -36% | 55% | falling knife: wait 2 stable sessions; thin listed options |
| VST | +7.5% | -27% | 51% | thin listed options |
| NVDA | +31.5% | -31% | 50% | falling knife: wait 2 stable sessions |
| BIDU | +5.5% | -52% | 48% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| BABA | +6.1% | -35% | 46% | falling knife: wait 2 stable sessions |
| MELI | +5.2% | -29% | 43% | falling knife: wait 2 stable sessions; thin listed options |
| GOOGL | +6.3% | -28% | 39% | falling knife: wait 2 stable sessions |
| ISRG | +4.3% | -14% | 38% | falling knife: wait 2 stable sessions; thin listed options |
| LLY | +1.3% | -5% | 37% | thin listed options |
| NVO | +3.5% | -24% | 37% | falling knife: wait 2 stable sessions |
| JD | +1.6% | -24% | 37% | falling knife: wait 2 stable sessions |
| ZBH | +4.8% | -4% | 32% | thin listed options |

## Full screen (eligible names, by score)

| Ticker | Theme | Last | 1D | vs 6M high | Vol used | Vol src | RV20 | ATM OI | Next earnings | Valuation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COHR | Semis/AI HW | 215.81 | +15.3% | -49% | 87% | 6M straddle | 139% | 1,168 | n/a | n/a |
| NTLA | Biotech/Health | 10.15 | +1.5% | -43% | 86% | 6M straddle | 91% | 5,982 | n/a | n/a |
| LUNR | Space/Defense | 9.75 | +11.1% | -79% | 89% | 6M straddle | 145% | 1,970 | n/a | n/a |
| ALAB | Semis/AI HW | 222.12 | +23.2% | -54% | 87% | 6M straddle | 160% | 1,756 | n/a | n/a |
| OKLO | Nuclear/Power | 20.77 | +4.6% | -72% | 86% | 6M straddle | 121% | 3,526 | n/a | n/a |
| VKTX | Biotech/Health | 27.69 | +11.8% | -34% | 68% | 6M straddle | 82% | 3,144 | n/a | n/a |
| AMD | Semis/AI HW | 453.46 | +6.8% | -30% | 66% | 6M straddle | 136% | 9,678 | n/a | n/a |
| TDOC | Biotech/Health | 7.68 | +3.1% | -21% | 64% | 6M straddle | 106% | 31,071 | n/a | n/a |
| ANET | Semis/AI HW | 178.31 | +6.4% | -18% | 59% | 6M straddle | 98% | 2,100 | n/a | n/a |
| AVGO | Semis/AI HW | 313.55 | +3.0% | -35% | 52% | 6M straddle | 87% | 4,059 | 2026-12-09 | n/a |
| UAL | Cyclical/Consumer | 108.71 | +7.6% | -20% | 50% | 6M straddle | 64% | 3,455 | n/a | n/a |
| TSLA | EV/Auto | 385.46 | +11.5% | -13% | 48% | 6M straddle | 74% | 1,519 | n/a | n/a |
| DXCM | Biotech/Health | 82.42 | +3.9% | -11% | 44% | 6M straddle | 47% | 2,718 | n/a | supported |
| TCOM | China ADR | 41.10 | +1.4% | -15% | 41% | 6M straddle | 32% | 3,932 | n/a | n/a |
| PDD | China ADR | 87.14 | +4.1% | -6% | 40% | 6M straddle | 50% | 13,377 | n/a | n/a |

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
