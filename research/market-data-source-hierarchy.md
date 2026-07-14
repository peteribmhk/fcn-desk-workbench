# FCN Market Data Source Hierarchy

**Status:** Indicative only. This note defines data-source priority for FCN screening and RFQ preparation. It is not a firm pricing model and not a market-data redistribution policy.

## Standing Rule

Use the best legally accessible source available in the current session. Do not limit analysis to free sources when a licensed paid or firm-approved source is connected. Do not attempt to bypass paywalls, credentials, exchange entitlements, or firm market-data controls.

## Priority Order

| Priority | Source type | Best use | FCN desk treatment |
|---:|---|---|---|
| 1 | Firm-approved issuer RFQ / pricing system | Actual coupon, RO, KI/KO ladder, issuer basis | Controlling evidence after terms are normalized |
| 2 | Licensed institutional terminal/API, such as Bloomberg, LSEG Workspace, FactSet, or firm market-data platform | Live spot, news, earnings, option surface, borrow/dividend/funding context | Use when licensed and connected; cite source and timestamp |
| 3 | Licensed options market-data API, such as Massive/Polygon Options, Cboe DataShop/LiveVol, OPRA-based vendor, or broker API | Option chain, NBBO, IV, Greeks, open interest, skew, term structure | Stronger screening input than public options pages |
| 4 | Public/free sources currently used by GitHub Actions | Nasdaq public quote, Nasdaq public option chain, Yahoo fallback, Stooq fallback | Public/delayed screening only; not firm real-time data |
| 5 | General web/news search | Market pulse, earnings narrative, sector sentiment, risk events | Qualitative context only; verify against market data and filings |

## Paid Source Access Boundary

Paid resources are usable only when one of these is true:

- an API key or token is provided through approved secrets or environment variables,
- a licensed terminal/API is connected in the current environment,
- the user manually provides non-confidential numbers from a firm-approved system,
- a broker or vendor API is authorized for the relevant market data and usage.

If none of these is true, the assistant must say that paid data is not connected and fall back to public screening data. It should still scan public web/news for market pulse, but it must not call that a live institutional feed.

## Best Upgrade Path For This Workbench

1. **Issuer RFQ calibration first:** real issuer coupon ladders beat any public-data model once tenor, strike/reference, KI, KO, RO, coupon frequency, issuer, and observation rules are normalized.
2. **Options data next:** for US equity FCNs, the biggest data upgrade is listed-options IV/Greeks/skew/term-structure from an authorized options data source.
3. **Market pulse third:** news and earnings context explain why vol or issuer appetite may change, but they do not price the FCN.
4. **Public fallback always:** keep Nasdaq/Yahoo/Stooq fallback so phone/GitHub refreshes still run when paid feeds are not connected.

## Provider Notes

- Massive/Polygon Options API publishes US options endpoints including chain snapshots with implied volatility, Greeks, open interest, latest quote/trade, and underlying price for supported plans.
- Cboe DataShop offers OPRA-based US listed-options data, including NBBO snapshots, bid/ask, volume, open interest, and optional implied-volatility/Greeks calculations for purchased products.
- Bloomberg, LSEG Workspace, FactSet, and firm platforms are valuable only when the user has licensed access and the usage is allowed by the firm's data policy.
- Nasdaq public quote/option endpoints remain useful fallback sources but can be delayed, unofficial for automation, rate-limited, or changed without notice.

## Daily Refresh Requirement

Every FCN Morning Bell should state:

1. which market-data tier was actually used,
2. timestamp and freshness,
3. whether paid/firm data was connected or unavailable,
4. whether issuer RFQ evidence was used,
5. that public data is screening only and issuer RFQ controls final coupon.

## Source Links Checked

- Massive Options overview: https://massive.com/docs/rest/options/overview
- Cboe DataShop Option EOD Summary: https://datashop.cboe.com/option-eod-summary
- Nasdaq Data Link API page: https://data.nasdaq.com/tools/api
