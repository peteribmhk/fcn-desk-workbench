# How an FCN coupon is built

A practical reference for reading issuer quotes and designing better RFQs. Compiled 2026-10-12 from public sources (listed at the end) and from tests with `scripts/fcn_model.py`.

> Indicative only. Not a firm quote. Not investment advice.

## 1. What the investor is actually selling

A worst-of FCN is a package of three parts:

| Part | Who holds it | What it means |
|---|---|---|
| Zero-coupon bond at the issuer's **internal funding rate** | Investor | The issuer funds itself cheaply through the note; part of that funding advantage goes into the coupon. |
| Short **worst-of put** (down-and-in at the KI, or a plain put at the strike for strike-only FCNs) | Investor sells it to the issuer | The main source of the coupon. Its value rises with volatility, skew, lower correlation, more names, a higher KI/strike, longer tenor and higher dividends. |
| **Autocall (KO)** feature | Issuer benefits | It ends the note early when markets go up, which caps how many coupons get paid. It shortens the expected life but barely changes the *annualized* coupon. |

The issuer solves for the coupon that makes the package worth par after costs:

```text
100% − issuer margin and costs = PV(coupons paid while alive) + PV(redemption)
```

This is the equation `scripts/fcn_model.py` solves by Monte Carlo.

**How big the costs are.** US-registered notes must disclose an *estimated value*. For example, a 2026 Citigroup 2-year worst-of autocallable on SPX/RTY/EFA (11% p.a. contingent coupon, 65% final barrier) disclosed an estimated value of 98.79% of issue price. That puts total structuring, hedging and selling costs at about 1.2%, and the estimate uses Citi's internal funding rate. Private-bank FCNs in Asia usually have a similar or larger margin, plus distribution fees.

## 2. The levers and which way they move the coupon

Example with model numbers: 2 names, vols 50% / 40%, correlation 0.3, 6M, KO 100% monthly, rate 3.9%. The levels are indicative; what matters is the direction and rough size.

| Lever | Change | Coupon | Rough size (example) |
|---|---|---|---|
| KI level (at maturity) | 50 → 70 | ↑ | 6–11% → 27–33% p.a., about +1% p.a. per KI point |
| KI observation | at maturity → daily close | ↑ | A daily KI is triggered more often, so it pays more for the same level |
| Strike (strike-only FCN) | 80 → 90 | ↑ | 20–25% → 30–35% p.a., about +1% p.a. per strike point |
| Implied vol | +3 vol points on each leg | ↑ | about +3–5% p.a. |
| Correlation | lower | ↑ | Low correlation is also where real diversification lives, but correlation **rises in a sell-off**. Worst-of pricing assumes it won't. |
| Number of names | 2 → 3 | ↑↑ | Often +5–10% p.a.; the chance that one name breaks rises just as fast |
| Tenor | 4M → 6M (deep KI) | ↑ annualized | For deep KIs, the breach probability grows faster than time, so longer tenors annualize higher. For near-the-money strikes, shorter tenors can annualize higher |
| KO level | 100 → 97 | ≈ same or slightly ↑ p.a. | Expected life shrinks (≈3.8 → 3.4 months), so **total** coupon received falls. Useful for limiting time at risk |
| Non-call period (KO start) | month 1 → month 3 | ↓ p.a. | The investor keeps collecting in up-markets, which is worth more to them, so the p.a. coupon falls (example 15.8% → 14.6% at KI 59) even though total coupon tends to rise. More callable = higher p.a. coupon |
| Coupon type | fixed → conditional/memory (Phoenix) | ↑ headline | Fixed coupons are worth more to the investor, so they quote lower |
| Dividends | higher | ↑ | Higher dividends lower the forward and make the put worth more. This matters little for growth tech |
| Rates and issuer funding | higher | ↑ | The Sept 2026 Fed hike to 3.75–4.00% supports coupons |
| Issuer credit spread | wider | ↑ | You are paid for issuer credit risk |
| Borrow cost (hard-to-borrow names) | higher | ↑ quote, worse hedge | Issuers pass the cost through, or decline the name |
| Issuer margin, fees, RO | higher | ↓ | Compare RO below 100 separately (PLAYBOOK §6) |

## 3. Know which convention your quote uses

| | US-registered autocallables (SEC 424B2) | Asian private-bank FCN (e.g. DBS, SC) | This repo's screen |
|---|---|---|---|
| Coupon | Usually contingent (coupon barrier), quarterly | Fixed, usually monthly | Fixed, monthly |
| Downside | Final barrier at maturity (e.g. 60–70%), cash loss 1:1 below it | **Strike** (e.g. 80–95%) with physical delivery; KI optional, often **daily close** | KI at maturity, strike 100% |
| KO | Quarterly, from month 3 | Monthly, often from month 1 | Monthly from month 1 |
| Tenor | 1–5 years | 1–12 months typical | 6M (configurable) |

Example from DBS's public FCN page: 6M, strike 95%, KO 100% monthly, KI 90% daily close, 12% p.a. paid monthly, physical delivery of the worst performer at the strike.

**Rule:** a 20% coupon on a strike-80 FCN and a 20% coupon on a KI-55-at-maturity FCN are different risks. Run the model in the same convention as your quote system before comparing:

```bash
python scripts/fcn_model.py --vols 0.55 0.45 --corr 0.3 --ki-style none --ladder 80 85 90            # strike-only
python scripts/fcn_model.py --vols 0.55 0.45 --corr 0.3 --ki-style daily --strike 90 --ladder 60 65  # daily KI
python scripts/fcn_model.py --vols 0.55 0.45 --corr 0.3                                               # KI at maturity
```

## 4. Why two issuers quote the same basket differently

- **Vol surface and skew.** The investor sells an out-of-the-money put, so the issuer prices it off the *downside* skew, not ATM vol. A flat-vol model under-prices that put. In open-source tests, a skew-calibrated model moves the fair coupon by tens of basis points or more, so a public ATM-vol screen tends to *understate* deep-KI coupons. Our ballpark's high end adds 3 vol points for this reason.
- **Correlation.** Each desk uses its own correlation estimates and stresses, and it is the dominant risk in worst-of pricing.
- **Existing book (axes).** Desks build up vega, skew, dividend and correlation exposure from what they have already sold. A name or pair that offsets the book prices better at that bank. One famous example: banks that sold heavy HSCEI and Euro Stoxx autocallables ended up long vol and long dividends and lost money when those moved (Risk.net, SRP).
- **Funding and credit.** A higher internal funding spread leaves more budget for the coupon.
- **Margin and appetite.** Some issuers will not quote small caps, recent IPOs, hard-to-borrow names or names with binary events at all.
- **Term details.** KI observation style, KO start, coupon memory, strike convention, settlement, and reference time and price.

When a quote differs a lot from the screen, ask the issuer which input drives it (templates/rfq-template.md has the wording), then log the driver in `templates/quote-calibration.md`.

## 5. Best practices that follow from the pricing logic

1. **Send the same RFQ to several issuers at the same reference time.** Reference timing alone moves coupons on high-vol names.
2. **Always ask for a ladder** (KI or strike), never a single level. Choose by pickup per point (PLAYBOOK §5).
3. **State the KI observation style** in every RFQ and every comparison.
4. **Ask for the estimated value or issuer margin** where the issuer will give it. It is the cleanest measure of what you pay.
5. **Look at total coupon received, not only the p.a. figure.** A lower KO raises the chance of early exit and lowers total carry.
6. **Low correlation is double-edged.** It raises the coupon and diversifies, but correlation goes to 1 in a crash. Size positions assuming it will.
7. **Avoid striking into a binary event,** and prefer the post-earnings window (PLAYBOOK §4).
8. **Watch concentration.** Regulators see worst-of notes as higher risk; FINRA ran a targeted 2026 sweep on customer concentration in non-principal-protected worst-of notes. Spread clients across baskets and issuers.
9. **Use public filings as a calibration ruler.** SEC 424B2 pricing supplements show real coupons, barriers and estimated values for single-stock worst-of notes (see `research/data-sources.md`). Normalize the convention before comparing.
10. **Never treat the model as a quote.** It has flat vol per leg, no dividends or borrow, constant correlation and no issuer appetite.

## Sources

- Arta Finance, [Custom FCNs: understanding the levers for higher yields](https://artafinance.com/global/insights/custom-fixed-coupon-notes-understanding-the-levers-for-higher-yields)
- Acadifi, [Autocallable structured products and knock-in barrier pricing](https://acadifi.com/community/autocallable-structured-products-knock-in-barrier-pricing)
- DBS Private Bank HK, [Fixed Coupon Notes](https://www.dbs.com.hk/private-banking/investments/product-suite/structured-investments/fixed-coupon-notes)
- Standard Chartered SG, [Fixed coupon notes](https://www.sc.com/sg/wealth/investment/fixed-coupon-notes/)
- Tiger Brokers, [FCN risk and return explained](https://www.itiger.com/sg/learn/detail/risk-return-fcn-fixed-coupon-note-explained)
- SEC EDGAR, [Citigroup worst-of autocallable pricing supplement (Feb 2026)](https://www.sec.gov/Archives/edgar/data/200245/000191870426004883/form424b2.htm)
- GitHub, [ShrishDhuria/autocallable-pricer](https://github.com/ShrishDhuria/autocallable-pricer): Heston-calibrated worst-of Phoenix, skew premium, correlation as the dominant risk
- Structured Retail Products, [Decrement indices and autocallable structures](https://www.structuredretailproducts.com/academy/selected-insight/77768/decrement-indices-and-autocallable-structures-the-good-the-bad-and-the-ugly)
- Risk.net, [Sliding HSCEI threatens fresh autocallable losses](https://www.risk.net/derivatives/structured-products/2441772/sliding-hscei-threatens-fresh-autocallable-losses)
- Seward & Kissel, [FINRA announces targeted sweep on structured notes (2026)](https://www.sewkis.com/publications/finra-announces-targeted-sweep-on-structured-notes/)
