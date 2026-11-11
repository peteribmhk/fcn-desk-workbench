# FCN Daily Screen

**Generated:** 2026-11-11 09:54 HKT  |  **US close used:** 2026-11-10  |  **Data status:** AMBER

> Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
> Public/delayed data, used only to decide what to RFQ. Issuer RFQ levels override everything below.

## How to read this

Structure assumed for the ballpark: USD worst-of FCN, 6M, KO 100% monthly from month 1, KI 59% observed at maturity, strike 100%, RO 100, monthly fixed coupon. Vols come from listed ATM straddles (Nasdaq); correlation from 90-day realized returns. The ballpark ignores skew, dividends and issuer-specific funding, so treat it as a sanity check for issuer levels, not a forecast. Every basket mixes different themes on purpose; same-sector pairs are pseudo-diversification.

## Two-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FSLR / ISRG | Solar/Clean + Biotech/Health | 48 / 45 | 0.07 | 16-22% | 11% | Balanced | fresh |
| 2 | FSLR / NIO | Solar/Clean + China ADR | 48 / 39 | 0.20 | 12-18% | 9% | Balanced | fresh |
| 3 | DELL / TDOC | Semis/AI HW + Biotech/Health | 105 / 103 | -0.19 | 83-87% | 50% | Aggressive | fresh |

## Three-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FSLR / NIO / ISRG | Solar/Clean + China ADR + Biotech/Health | 48 / 39 / 45 | 0.16 | 18-24% | 14% | Balanced | fresh |
| 2 | DELL / SMR / TDOC | Semis/AI HW + Nuclear/Power + Biotech/Health | 105 / 107 / 103 | 0.03 | 98-102% | 65% | Aggressive | fresh |

## Why these names

- **FSLR / ISRG**: FSLR: sweet spot (-20% to -50%), -43% vs 6M high, vol 48% (RV20 (no options)); ISRG: near 6M high, -7% vs 6M high, vol 45% (RV20 (no options)), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +7%)
- **FSLR / NIO**: FSLR: sweet spot (-20% to -50%), -43% vs 6M high, vol 48% (RV20 (no options)); NIO: sweet spot (-20% to -50%), -48% vs 6M high, vol 39% (RV20 (no options))
- **DELL / TDOC**: DELL: sweet spot (-20% to -50%), -41% vs 6M high, vol 105% (RV20 (no options)); TDOC: near 6M high, -8% vs 6M high, vol 103% (RV20 (no options))
- **FSLR / NIO / ISRG**: FSLR: sweet spot (-20% to -50%), -43% vs 6M high, vol 48% (RV20 (no options)); NIO: sweet spot (-20% to -50%), -48% vs 6M high, vol 39% (RV20 (no options)); ISRG: near 6M high, -7% vs 6M high, vol 45% (RV20 (no options)), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +7%)
- **DELL / SMR / TDOC**: DELL: sweet spot (-20% to -50%), -41% vs 6M high, vol 105% (RV20 (no options)); SMR: deep drawdown (>50%), -61% vs 6M high, vol 107% (RV20 (no options)), thesis check needed (no valuation data); TDOC: near 6M high, -8% vs 6M high, vol 103% (RV20 (no options))

## Valuation cross-check (legs in today's picks)

Would you be happy to own the worst leg at the strike? Cheap against its own 10-year range, an analyst target above the price and growing revenue make a sturdier floor. Not blocking: it informs the RFQ, it does not remove names. Data: `fundamentals/valuation.csv`.

| Ticker | vs 6M high | Valuation read | Caveat |
| --- | --- | --- | --- |
| SMR | -61% | **no data: thesis check before RFQ** |  |
| NIO | -48% | no data |  |
| FSLR | -43% | no data |  |
| DELL | -41% | no data |  |
| TDOC | -8% | no data |  |
| ISRG | -7% | supported (fwd EV/EBITDA p10-p25 of 10Y, target +7%) |  |

## KI ladder: FSLR / ISRG (top pair)

| KI | Ballpark coupon p.a. | P(loss at maturity) | Pickup per KI pt | Read |
| --- | --- | --- | --- | --- |
| 50% | 6.5-11.1% | 4.1% | - | base protection |
| 55% | 11.3-16.7% | 7.5% | 1.03% p.a. | strong pickup |
| 59% | 15.9-21.8% | 11.3% | 1.22% p.a. | strong pickup |
| 65% | 23.6-29.6% | 18.2% | 1.29% p.a. | strong pickup |
| 70% | 29.5-35.4% | 24.5% | 1.18% p.a. | strong pickup |

Pickup per KI point thresholds: below 0.25% p.a. keep the lower KI; 0.25-0.60% balanced; above 0.60% the higher KI may be worth it. Model pickup is smooth by construction; the real decision uses the issuer's KI ladder.

## Conditional / watch only

| Ticker | 1D | vs 6M high | Vol | Why held back |
| --- | --- | --- | --- | --- |
| LITE | +10.7% | -47% | 137% | no listed-options read; vol too high for a core leg |
| LUNR | +15.0% | -74% | 132% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| CRDO | +10.3% | -56% | 130% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| ALAB | +13.7% | -55% | 129% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| APLD | +7.5% | -66% | 128% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| COHR | -4.7% | -50% | 128% | no listed-options read; vol too high for a core leg |
| SNDK | +6.2% | -62% | 126% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| NBIS | +9.2% | -51% | 124% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| BE | +11.9% | -44% | 123% | no listed-options read; vol too high for a core leg |
| CRWV | +5.6% | -61% | 123% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| APP | +4.8% | -33% | 122% | no listed-options read; vol too high for a core leg |
| IONQ | +8.3% | -51% | 122% | no listed-options read; vol too high for a core leg |
| MRVL | -0.1% | -51% | 121% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| OKLO | +14.0% | -64% | 120% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| AMD | +1.3% | -21% | 117% | no listed-options read; vol too high for a core leg |
| ASTS | +14.1% | -72% | 117% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| LEU | -6.4% | -45% | 115% | no listed-options read; falling knife: wait 2 stable sessions; vol too high for a core leg |
| RGTI | +10.5% | -52% | 114% | no listed-options read; thesis check: >50% off high without valuation support; vol too high for a core leg |
| VRT | +9.6% | -47% | 114% | no listed-options read; vol too high for a core leg |
| DKNG | +1.0% | -38% | 97% | no listed-options read; falling knife: wait 2 stable sessions |
| HIMS | -11.8% | -40% | 90% | no listed-options read; falling knife: wait 2 stable sessions |
| ZS | +0.7% | -24% | 67% | no listed-options read; falling knife: wait 2 stable sessions |
| AFRM | -0.1% | -21% | 63% | no listed-options read; falling knife: wait 2 stable sessions |
| MELI | -2.8% | -26% | 60% | no listed-options read; falling knife: wait 2 stable sessions |
| NVDA | -5.5% | -29% | 51% | no listed-options read; falling knife: wait 2 stable sessions |

## Full screen (eligible names, by score)

| Ticker | Theme | Last | 1D | vs 6M high | Vol used | Vol src | RV20 | ATM OI | Next earnings | Valuation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DELL | Semis/AI HW | 346.31 | +5.4% | -41% | 105% | RV20 (no options) | 105% | n/a | n/a | n/a |
| MU | Semis/AI HW | 725.11 | -1.1% | -40% | 97% | RV20 (no options) | 97% | n/a | n/a | n/a |
| QUBT | Quantum | 6.86 | +8.4% | -45% | 96% | RV20 (no options) | 96% | n/a | n/a | n/a |
| RKLB | Space/Defense | 58.86 | +10.9% | -61% | 110% | RV20 (no options) | 110% | n/a | n/a | n/a |
| DDOG | Software | 179.62 | +0.3% | -39% | 94% | RV20 (no options) | 94% | n/a | n/a | n/a |
| QBTS | Quantum | 11.47 | +7.4% | -62% | 109% | RV20 (no options) | 109% | n/a | n/a | n/a |
| SMR | Nuclear/Power | 5.44 | +7.1% | -61% | 107% | RV20 (no options) | 107% | n/a | n/a | n/a |
| WDC | Semis/AI HW | 289.20 | -0.2% | -61% | 106% | RV20 (no options) | 106% | n/a | n/a | n/a |
| VST | Nuclear/Power | 133.92 | +7.3% | -21% | 91% | RV20 (no options) | 91% | n/a | n/a | supported* |
| AVAV | Space/Defense | 123.50 | -2.7% | -42% | 89% | RV20 (no options) | 89% | n/a | n/a | n/a |
| AMAT | Semis/AI HW | 372.53 | +0.5% | -48% | 88% | RV20 (no options) | 88% | n/a | n/a | n/a |
| SMCI | Semis/AI HW | 27.79 | -2.8% | -45% | 87% | RV20 (no options) | 87% | n/a | n/a | n/a |
| STX | Semis/AI HW | 501.62 | -0.9% | -54% | 101% | RV20 (no options) | 101% | n/a | n/a | n/a |
| MRNA | Biotech/Health | 269.00 | +5.8% | 0% | 105% | RV20 (no options) | 105% | n/a | n/a | n/a |
| TDOC | Biotech/Health | 8.98 | +2.4% | -8% | 103% | RV20 (no options) | 103% | n/a | n/a | n/a |
| ENPH | Solar/Clean | 29.08 | +2.1% | -60% | 97% | RV20 (no options) | 97% | n/a | n/a | n/a |
| VKTX | Biotech/Health | 28.99 | +8.0% | -31% | 82% | RV20 (no options) | 82% | n/a | n/a | n/a |
| GEV | Nuclear/Power | 829.34 | +7.1% | -29% | 80% | RV20 (no options) | 80% | n/a | n/a | supported |
| NET | Software | 293.75 | +9.3% | -19% | 87% | RV20 (no options) | 87% | n/a | n/a | n/a |
| NTLA | Biotech/Health | 12.11 | +6.7% | -32% | 79% | RV20 (no options) | 79% | n/a | n/a | n/a |
| ARM | Semis/AI HW | 186.30 | +6.7% | -58% | 91% | RV20 (no options) | 91% | n/a | n/a | n/a |
| ANET | Semis/AI HW | 186.17 | +9.0% | -14% | 86% | RV20 (no options) | 86% | n/a | n/a | n/a |
| KTOS | Space/Defense | 36.72 | -2.6% | -44% | 76% | RV20 (no options) | 76% | n/a | n/a | n/a |
| GLW | Semis/AI HW | 112.13 | -3.3% | -56% | 79% | RV20 (no options) | 79% | n/a | n/a | n/a |
| ORCL | Software | 117.98 | -1.5% | -52% | 79% | RV20 (no options) | 79% | n/a | n/a | n/a |
| AVGO | Semis/AI HW | 331.98 | +3.9% | -31% | 67% | RV20 (no options) | 67% | n/a | n/a | n/a |
| SOFI | Fintech | 16.75 | +3.3% | -13% | 74% | RV20 (no options) | 74% | n/a | n/a | n/a |
| SNOW | Software | 291.14 | +5.5% | -21% | 66% | RV20 (no options) | 66% | n/a | n/a | n/a |
| TLN | Nuclear/Power | 363.13 | +7.2% | -17% | 71% | RV20 (no options) | 71% | n/a | n/a | n/a |
| RIVN | EV/Auto | 14.01 | +2.9% | -30% | 58% | RV20 (no options) | 58% | n/a | n/a | n/a |
| PLTR | Software | 169.20 | +5.5% | -19% | 63% | RV20 (no options) | 63% | n/a | n/a | n/a |
| TSLA | EV/Auto | 379.78 | +0.5% | -15% | 61% | RV20 (no options) | 61% | n/a | n/a | n/a |
| XPEV | China ADR | 10.22 | -0.2% | -43% | 55% | RV20 (no options) | 55% | n/a | n/a | n/a |
| UAL | Cyclical/Consumer | 120.56 | +0.1% | -11% | 58% | RV20 (no options) | 58% | n/a | n/a | n/a |
| GOOGL | Mega-cap | 287.38 | -0.3% | -29% | 53% | RV20 (no options) | 53% | n/a | n/a | n/a |
| DXCM | Biotech/Health | 79.92 | -1.4% | -13% | 53% | RV20 (no options) | 53% | n/a | n/a | supported |
| FSLR | Solar/Clean | 180.98 | -5.5% | -43% | 48% | RV20 (no options) | 48% | n/a | n/a | n/a |
| CRSP | Biotech/Health | 50.04 | -0.1% | -19% | 50% | RV20 (no options) | 50% | n/a | n/a | n/a |
| ZBH | Biotech/Health | 107.32 | -0.9% | -3% | 54% | RV20 (no options) | 54% | n/a | n/a | supported* |
| NIO | China ADR | 3.41 | +0.6% | -48% | 39% | RV20 (no options) | 39% | n/a | n/a | n/a |
| ISRG | Biotech/Health | 450.04 | -2.3% | -7% | 45% | RV20 (no options) | 45% | n/a | n/a | supported |
| BABA | China ADR | 105.38 | -3.7% | -28% | 35% | RV20 (no options) | 35% | n/a | n/a | n/a |
| NVO | Biotech/Health | 40.70 | -1.6% | -21% | 33% | RV20 (no options) | 33% | n/a | n/a | n/a |
| LLY | Biotech/Health | 1432.29 | +1.4% | 0% | 40% | RV20 (no options) | 40% | n/a | n/a | n/a |
| BIDU | China ADR | 79.71 | -1.6% | -47% | 30% | RV20 (no options) | 30% | n/a | n/a | n/a |
| PDD | China ADR | 80.50 | -3.0% | -19% | 30% | RV20 (no options) | 30% | n/a | n/a | n/a |
| JD | China ADR | 28.38 | -2.5% | -16% | 29% | RV20 (no options) | 29% | n/a | n/a | n/a |
| TCOM | China ADR | 44.08 | +0.1% | -16% | 27% | RV20 (no options) | 27% | n/a | n/a | n/a |

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

- Names with usable data: 73/73; with listed-options read: 0/73.
- Vol source used: Tradier/ORATS 0, Nasdaq straddle 0, realized-vol fallback 73.
- Tradier/ORATS: not configured. Add a `TRADIER_TOKEN` repository secret to use ORATS IV (see `research/data-sources.md`).
- Valuation file: 9 names from `fundamentals/valuation.csv` (oldest row 2026-11-06).
- Missing today: none.
- Model rate assumption 3.90% + 0.50% funding; ballpark low end = ATM vol and 1.5% issuer margin, high end = ATM vol +3 pts and 0.75% margin.
- Crypto-linked names are excluded by default.

_Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems._
