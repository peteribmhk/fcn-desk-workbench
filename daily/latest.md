# FCN Daily Screen

**Generated:** 2026-11-23 10:42 HKT  |  **US close used:** 2026-11-20  |  **Data status:** GREEN

> Indicative only. Not a firm quote. Not investment advice. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.
> Public/delayed data, used only to decide what to RFQ. Issuer RFQ levels override everything below.

## How to read this

Structure assumed for the ballpark: USD worst-of FCN, 6M, KO 100% monthly from month 1, KI 59% observed at maturity, strike 100%, RO 100, monthly fixed coupon. Vols come from listed ATM straddles (Nasdaq); correlation from 90-day realized returns. The ballpark ignores skew, dividends and issuer-specific funding, so treat it as a sanity check for issuer levels, not a forecast. Every basket mixes different themes on purpose; same-sector pairs are pseudo-diversification.

## Two-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | UAL / DXCM | Cyclical/Consumer + Biotech/Health | 50 / 43 | 0.12 | 16-22% | 11% | Balanced | repeat, same rationale |
| 2 | UAL / PDD | Cyclical/Consumer + China ADR | 50 / 40 | 0.04 | 14-20% | 10% | Balanced | fresh |
| 3 | TDOC / PDD | Biotech/Health + China ADR | 61 / 40 | 0.19 | 22-28% | 15% | Higher coupon | fresh |
| 4 | OKLO / TDOC | Nuclear/Power + Biotech/Health | 89 / 61 | -0.10 | 52-57% | 33% | Aggressive | fresh |

## Three-stock picks

| # | Basket | Themes | Vol % (legs) | Avg corr | 6M KI59 ballpark | P(loss) | Profile | Requote |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | UAL / DXCM / PDD | Cyclical/Consumer + Biotech/Health + China ADR | 50 / 43 / 40 | 0.11 | 18-24% | 14% | Balanced | fresh |
| 2 | TDOC / UAL / PDD | Biotech/Health + Cyclical/Consumer + China ADR | 61 / 50 / 40 | 0.12 | 28-34% | 22% | Higher coupon | fresh |

## Why these names

- **UAL / DXCM**: UAL: sweet spot (-20% to -50%), -26% vs 6M high, vol 50% (6M straddle); DXCM: mild pullback, -14% vs 6M high, vol 43% (6M straddle), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%)
- **UAL / PDD**: UAL: sweet spot (-20% to -50%), -26% vs 6M high, vol 50% (6M straddle); PDD: mild pullback, -13% vs 6M high, vol 40% (6M straddle)
- **TDOC / PDD**: TDOC: sweet spot (-20% to -50%), -23% vs 6M high, vol 61% (6M straddle); PDD: mild pullback, -13% vs 6M high, vol 40% (6M straddle)
- **UAL / DXCM / PDD**: UAL: sweet spot (-20% to -50%), -26% vs 6M high, vol 50% (6M straddle); DXCM: mild pullback, -14% vs 6M high, vol 43% (6M straddle), valuation supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%); PDD: mild pullback, -13% vs 6M high, vol 40% (6M straddle)
- **TDOC / UAL / PDD**: TDOC: sweet spot (-20% to -50%), -23% vs 6M high, vol 61% (6M straddle); UAL: sweet spot (-20% to -50%), -26% vs 6M high, vol 50% (6M straddle); PDD: mild pullback, -13% vs 6M high, vol 40% (6M straddle)

## Valuation cross-check (legs in today's picks)

Would you be happy to own the worst leg at the strike? Cheap against its own 10-year range, an analyst target above the price and growing revenue make a sturdier floor. Not blocking: it informs the RFQ, it does not remove names. Data: `fundamentals/valuation.csv`.

| Ticker | vs 6M high | Valuation read | Caveat |
| --- | --- | --- | --- |
| OKLO | -73% | **no data: thesis check before RFQ** |  |
| UAL | -26% | no data |  |
| TDOC | -23% | no data |  |
| DXCM | -14% | supported (fwd EV/EBITDA p10-p25 of 10Y, target +14%) |  |
| PDD | -13% | no data |  |

## KI ladder: UAL / DXCM (top pair)

| KI | Ballpark coupon p.a. | P(loss at maturity) | Pickup per KI pt | Read |
| --- | --- | --- | --- | --- |
| 50% | 6.5-11.2% | 4.0% | - | base protection |
| 55% | 11.1-16.6% | 7.3% | 1.01% p.a. | strong pickup |
| 59% | 15.8-21.8% | 11.1% | 1.23% p.a. | strong pickup |
| 65% | 23.4-29.3% | 17.9% | 1.26% p.a. | strong pickup |
| 70% | 29.2-35.0% | 23.9% | 1.15% p.a. | strong pickup |

Pickup per KI point thresholds: below 0.25% p.a. keep the lower KI; 0.25-0.60% balanced; above 0.60% the higher KI may be worth it. Model pickup is smooth by construction; the real decision uses the issuer's KI ladder.

## Conditional / watch only

| Ticker | 1D | vs 6M high | Vol | Why held back |
| --- | --- | --- | --- | --- |
| NBIS | -16.1% | -72% | 113% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; vol too high for a core leg |
| QBTS | -10.8% | -78% | 109% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| APLD | -17.8% | -77% | 109% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| ASTS | -8.9% | -83% | 106% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| LUNR | -10.3% | -81% | 104% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| CRWV | -12.0% | -68% | 102% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| CRDO | -15.2% | -67% | 99% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-12-01; thin listed options |
| SMR | -11.8% | -76% | 96% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| RGTI | -11.2% | -74% | 95% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| BE | -15.3% | -59% | 94% | falling knife: wait 2 stable sessions |
| ALAB | -14.8% | -63% | 94% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| IONQ | -8.8% | -71% | 92% | falling knife: wait 2 stable sessions |
| SMCI | -9.2% | -57% | 92% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| SNDK | -16.1% | -73% | 91% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| LEU | -9.2% | -59% | 90% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| NTLA | +5.0% | -44% | 90% | falling knife: wait 2 stable sessions |
| HIMS | -8.9% | -62% | 89% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| COHR | -12.9% | -56% | 88% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| QUBT | -9.8% | -64% | 87% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| RKLB | -10.9% | -70% | 85% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| MRNA | -2.2% | -28% | 84% | falling knife: wait 2 stable sessions; thin listed options |
| LITE | -13.9% | -59% | 84% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| ENPH | -10.7% | -73% | 82% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| AVAV | -9.5% | -60% | 81% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| STX | -12.3% | -58% | 80% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| DELL | -11.0% | -53% | 80% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-11-24; thin listed options |
| WDC | -12.0% | -65% | 78% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| MRVL | -11.7% | -61% | 78% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-12-01 |
| ARM | -14.1% | -65% | 77% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| KTOS | -9.3% | -59% | 77% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| NET | -9.5% | -24% | 73% | falling knife: wait 2 stable sessions; thin listed options |
| VRT | -10.1% | -54% | 72% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| MU | -13.9% | -51% | 71% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; thin listed options |
| GLW | -10.9% | -63% | 71% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| AMD | -13.2% | -35% | 70% | falling knife: wait 2 stable sessions |
| ZS | -5.3% | -25% | 69% | event hold: earnings 2026-12-02; thin listed options |
| NIO | -7.9% | -59% | 69% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions; event hold: earnings 2026-12-01 |
| APP | -8.1% | -43% | 69% | falling knife: wait 2 stable sessions; thin listed options |
| VKTX | -4.1% | -41% | 68% | thin listed options |
| RIVN | -8.5% | -49% | 68% | falling knife: wait 2 stable sessions |
| ORCL | -8.5% | -59% | 68% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| DDOG | -5.5% | -46% | 67% | falling knife: wait 2 stable sessions; thin listed options |
| AFRM | -5.1% | -37% | 67% | falling knife: wait 2 stable sessions |
| DKNG | -6.1% | -47% | 66% | falling knife: wait 2 stable sessions |
| SNOW | -5.1% | -31% | 66% | falling knife: wait 2 stable sessions; event hold: earnings 2026-12-02; thin listed options |
| AMAT | -10.7% | -58% | 65% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| SOFI | -7.8% | -35% | 63% | falling knife: wait 2 stable sessions |
| CRSP | +0.4% | -37% | 63% | falling knife: wait 2 stable sessions |
| ANET | -11.6% | -23% | 63% | falling knife: wait 2 stable sessions |
| PLTR | -6.6% | -31% | 62% | falling knife: wait 2 stable sessions |
| FSLR | -9.5% | -57% | 59% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| TLN | -6.5% | -24% | 59% | falling knife: wait 2 stable sessions; thin listed options |
| XPEV | -13.9% | -55% | 59% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| GEV | -7.5% | -40% | 58% | falling knife: wait 2 stable sessions; thin listed options |
| NVDA | -14.0% | -48% | 58% | falling knife: wait 2 stable sessions |
| AVGO | -12.2% | -37% | 57% | falling knife: wait 2 stable sessions |
| VST | -7.2% | -32% | 54% | falling knife: wait 2 stable sessions; thin listed options |
| TSLA | -7.6% | -22% | 52% | falling knife: wait 2 stable sessions |
| BIDU | -6.7% | -55% | 49% | thesis check: >50% off high without valuation support; falling knife: wait 2 stable sessions |
| BABA | -2.7% | -39% | 49% | falling knife: wait 2 stable sessions |
| MELI | -0.0% | -32% | 46% | falling knife: wait 2 stable sessions; thin listed options |
| GOOGL | -2.7% | -32% | 42% | falling knife: wait 2 stable sessions |
| TCOM | -4.1% | -16% | 41% | event hold: earnings 2026-11-23 |
| JD | -2.9% | -26% | 39% | falling knife: wait 2 stable sessions |
| ISRG | -2.0% | -17% | 39% | falling knife: wait 2 stable sessions; thin listed options |
| LLY | -0.3% | -7% | 38% | thin listed options |
| NVO | -2.7% | -27% | 37% | falling knife: wait 2 stable sessions |
| ZBH | -0.4% | -8% | 34% | thin listed options |

## Full screen (eligible names, by score)

| Ticker | Theme | Last | 1D | vs 6M high | Vol used | Vol src | RV20 | ATM OI | Next earnings | Valuation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OKLO | Nuclear/Power | 19.85 | -4.8% | -73% | 89% | 6M straddle | 119% | 3,530 | n/a | n/a |
| TDOC | Biotech/Health | 7.45 | -4.4% | -23% | 61% | 6M straddle | 106% | 28,461 | n/a | n/a |
| UAL | Cyclical/Consumer | 101.03 | -4.3% | -26% | 50% | 6M straddle | 60% | 2,493 | n/a | n/a |
| DXCM | Biotech/Health | 79.32 | -1.1% | -14% | 43% | 6M straddle | 45% | 2,715 | n/a | supported |
| PDD | China ADR | 83.68 | -2.7% | -13% | 40% | 6M straddle | 48% | 13,459 | n/a | n/a |

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
