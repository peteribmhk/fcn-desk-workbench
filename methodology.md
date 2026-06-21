# Methodology

Use this methodology when Codex prepares FCN pickings from public market data. The goal is to rank opportunities and prepare RFQs, not to produce firm tradable coupons.

## Required Labels

Every output must state:

> Indicative only. Not a firm quote. Final coupon and terms must be confirmed by issuer RFQ and firm-approved systems.

## Inputs To Collect

- Underlyings and market.
- Spot price and timestamp.
- Recent price trend: 1D, 1W, 1M if available.
- Implied volatility or public options-chain proxy if available.
- Liquidity and bid/ask quality.
- Event risks: earnings, financing, regulation, product launch, macro, crypto moves.
- Structure terms: tenor, KO, KI, coupon frequency, observation frequency, airbag level, and KI observation style.

## Ranking Logic

Rank baskets by the following order:

1. **Volatility and jump risk**: higher vol generally supports higher coupon.
2. **Worst-of risk**: the weakest or most volatile name usually drives coupon and downside.
3. **Correlation**: lower correlation can increase worst-of dispersion risk and support coupon; highly correlated baskets may gap together.
4. **Tenor**: longer tenor usually supports higher annualized coupon but increases time-at-risk.
5. **KI and airbag**: lower KI / deeper airbag reduces downside trigger risk and lowers coupon; higher KI raises coupon and risk.
6. **KO level and observation**: lower/easier KO usually increases early redemption probability and can reduce total carry opportunity.
7. **Liquidity and hedge cost**: wider hedge cost means issuer may retain more margin.
8. **Client explainability**: a slightly lower coupon basket can be preferable if the story and risks are easier to explain.

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

- **KI 59**: aggressive but meaningful downside buffer; common for high-vol names when chasing coupon.
- Lower KI gives more protection and lower coupon.
- Higher KI gives higher coupon but makes loss trigger more realistic.
- Always state whether KI is observed at maturity, daily close, or continuously.

## Coupon Language

Avoid false precision. Use ranges:

- "Likely highest coupon basket."
- "Coupon should screen above the semiconductor basket because volatility and jump risk are higher."
- "RFQ target range should be validated with issuer."
- "If issuer quote is far below this range, ask which input is driving the difference: vol, correlation, funding, borrow, or margin."

## Output Ranking Categories

Use these labels:

- **Max coupon**: highest expected coupon, highest downside risk.
- **Balanced high coupon**: attractive coupon with clearer client story.
- **Aggressive alternative**: high coupon but likely unsuitable for conservative clients.
- **Watch only**: interesting but not preferred due to event risk, liquidity, or crowded exposure.

