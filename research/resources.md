# Further resources

Open-source code, learning material and regulation relevant to FCN / worst-of autocallable work. Compiled 2026-10-12. Third-party code is listed for study: review it before use, and none of it is an issuer pricer.

## Open-source pricers and examples

| Project | What it shows |
|---|---|
| [ShrishDhuria/autocallable-pricer](https://github.com/ShrishDhuria/autocallable-pricer) | Worst-of Phoenix autocallable; Heston calibrated to the live SPY surface; correlated Monte Carlo; fair-coupon solver; quantifies the skew premium; tests that the PV rises with correlation |
| [Nicolas8330/structured-products-pricer](https://github.com/Nicolas8330/structured-products-pricer) | Monte Carlo for autocalls, reverse convertibles, shark notes and CLNs, with autocall probabilities and greeks |
| [chedi24/autocall-pricing](https://github.com/chedi24/autocall-pricing) | Autocall pricing example |
| [SalimEM04/autocall-snowball](https://github.com/SalimEM04/autocall-snowball) | Memory-coupon autocall in Python |
| [yshi34/autocallable-note-monte-carlo](https://github.com/yshi34/autocallable-note-monte-carlo) | Single-underlying autocall under GBM, with convergence analysis |
| [QuantLib-Python: Heston MC for an autocallable memory coupon note](http://mikejuniperhill.blogspot.com/2019/11/quantlib-python-heston-monte-carlo.html) | Walk-through with QuantLib |

## Libraries

- **QuantLib / QuantLib-Python**: term structures, vol surfaces, Heston and Monte Carlo engines.
- **py_vollib / py_vollib_vectorized**: fast implied vol and greeks (LetsBeRational).
- **pysabr, SSVI implementations**: smile and surface fitting.
- **arch**: GARCH-family realized-vol forecasting.
- **OpenBB Platform** ([openbb.co](https://openbb.co/products/platform)): open-source data layer that wraps many free and paid providers, including options chains.
- Curated list: [awesome-options-analytics](https://github.com/FlashAlpha-lab/awesome-options-analytics).

## Learning material

- Arta Finance, [levers for higher FCN yields](https://artafinance.com/global/insights/custom-fixed-coupon-notes-understanding-the-levers-for-higher-yields)
- Tiger Brokers Academy, [FCN risk and return](https://www.itiger.com/sg/learn/detail/risk-return-fcn-fixed-coupon-note-explained)
- DBS Private Bank HK, [FCN product page](https://www.dbs.com.hk/private-banking/investments/product-suite/structured-investments/fixed-coupon-notes) (Asian conventions: strike, daily KI, physical delivery)
- Standard Chartered, [FCN page](https://www.sc.com/sg/wealth/investment/fixed-coupon-notes/)
- Acadifi, [knock-in barrier pricing](https://acadifi.com/community/autocallable-structured-products-knock-in-barrier-pricing)
- The Journal of Derivatives (Spring 2015), *Autocallable Structured Products* (paywalled)
- Gatheral & Jacquier (2014), *Arbitrage-free SVI volatility surfaces* (arXiv)
- Cboe, [VIX methodology](https://cdn.cboe.com/resources/vix/VIX_Methodology.pdf)

## Market and risk history

- Risk.net, [Sliding HSCEI threatens fresh autocallable losses](https://www.risk.net/derivatives/structured-products/2441772/sliding-hscei-threatens-fresh-autocallable-losses): what happens when many notes sit on the same underlying
- Structured Retail Products, [Decrement indices and autocallables](https://www.structuredretailproducts.com/academy/selected-insight/77768/decrement-indices-and-autocallable-structures-the-good-the-bad-and-the-ugly): dividend and vega risk on issuer books

## Regulation (Hong Kong and US)

- **Hong Kong SFC, complex products** ([IFEC summary](https://www.ifec.org.hk/web/en/financial-products/financial-market/investor-protection/complex-products.html)): since July 2019, intermediaries must assess suitability for complex products even when the client orders them unsolicited, and must provide key product information and warning statements. Non-exchange-traded structured products such as FCNs fall under this. See also HKIB, [Suitability obligations on complex products distribution](https://www.hkib.org/pdf/1653990210_HDCPDCOMP220701%20Suitability%20Obligations%20on%20Complex%20Products%20Distribution.pdf).
- **FINRA (US), 2026 targeted sweep on structured notes** ([Seward & Kissel](https://www.sewkis.com/publications/finra-announces-targeted-sweep-on-structured-notes/)): covers 2022–2025 and focuses on customer **concentration** in non-principal-protected worst-of notes, Reg BI, surveillance alerts, training and compensation conflicts. The concentration lesson applies equally in Hong Kong.

Everything in this repo stays a screening aid. Product approval, suitability and disclosures follow your firm's process.
