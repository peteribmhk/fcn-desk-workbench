# FCN Desk Memory

This file stores durable, public-safe instructions learned from the user's FCN workflow. Future ChatGPT/Codex sessions should reread it before daily picks, refreshes, RFQs, or client explanation drafts.

## Core User Profile

- The user is a Hong Kong securities salesperson using this repo for FCN idea screening, issuer RFQ preparation, and client-facing explanation drafts.
- The goal is a phone-accessible workflow that still works when the laptop is off.
- GitHub is the persistent source of truth. GitHub Actions is the cloud refresh runtime.
- Codex local folders are caches of GitHub, not the master copy.
- Codex should run `scripts/sync-from-github.ps1` before FCN work and `scripts/publish-to-github.ps1` after durable repo changes.
- The repo is public-safe. Do not store client data, suitability records, actual issuer quotes, firm pricing-system screenshots, or confidential issuer assumptions here.

## Durable Preferences

- Exclude crypto-linked names by default. Do not suggest MSTR, COIN, BTC miners, crypto exchanges, or crypto-beta baskets unless the user explicitly opts in.
- Prefer diversified high-volatility US-listed equities where issuer RFQs may show worthwhile FCN coupons.
- Treat public/free market data as screening evidence only. It is not a firm quote, not guaranteed real time, and not a replacement for issuer pricing.
- Real issuer RFQ or firm-approved pricing-system levels override public-data rankings after structure terms are normalized.

## KI Value Discipline

The user does not want the lowest KI level by habit. The preferred method is value optimization:

1. Request KI ladder levels such as 50 / 55 / 59 / 65 / 70.
2. Compare coupon pickup per KI point of airbag sacrificed.
3. Keep the lower KI if coupon pickup is flat or weak.
4. Accept a higher KI if the coupon pickup is meaningfully better and the risk trade-off is clear.
5. Explain the chosen level as a balance between downside protection, coupon sacrificed, and client risk appetite.

## Refresh Memory Rule

Every refresh should save new information back to GitHub:

- `daily/latest.md` remains the phone-readable latest report.
- `daily/archive/YYYY-MM-DD-HHMM-HKT.md` stores each refresh as timestamped history.
- `daily/index.md` lists recent archived refreshes.

Before suggesting tickers, baskets, KI levels, RFQ wording, or client commentary, future sessions should reread the repo from scratch:

1. `AGENTS.md`
2. `assistant-operating-instructions.md`
3. `desk-memory.md`
4. `SYNC_PROTOCOL.md`
5. `README.md`
6. `methodology.md`
7. `watchlist.csv`
8. `daily/latest.md`
9. `daily/index.md`
10. Relevant recent files under `daily/archive/`
11. `templates/ki-optimization.md`
12. `templates/requote-checklist.md`
13. `research/free-market-data-sources.md`
14. `research/market-data-source-hierarchy.md`

If these files cannot be read, mark the morning status `AMBER` or `RED` rather than giving confident picks.

## Verification Loop

Every daily output should include a profile verification gate covering:

- user preference: crypto excluded unless explicitly opted in,
- evidence quality: public data is only screening,
- paid-source access: use licensed paid or firm-approved sources when connected, but do not bypass paywalls, credentials, exchange entitlements, or firm controls,
- issuer quote override: normalized issuer RFQ controls,
- structure normalization: tenor, strike/reference, KI, KI observation, KO, KO observation, RO/issue price, coupon frequency, issuer, bid/offer, dividends, borrow, funding, correlation, skew, and autocall assumptions,
- KI value discipline: coupon pickup per KI point,
- repeat discipline: fresh idea versus repeated rationale, changed inputs, structural mismatch, or calibration drift,
- persistence: reusable corrections should update the repo instead of staying only in chat.

## What To Save

Save public-safe workflow improvements, watchlist logic, methodology changes, daily public-data screens, and non-confidential lessons learned from the user's preferences.

## What Not To Save

Do not save actual client information, suitability assessments, account details, issuer quote screenshots, firm pricing-system outputs, confidential bank levels, compliance notes, or any non-public information in this public repo.

---

Append this section to `desk-memory.md`. All items are public-safe: no client data, no issuer/channel quote levels, no firm-confidential material.

## Entry-Quality Framework ("deep drawdown + vol not dispersed")

- Prefer underlyings roughly 20–50% below their 6-month high where 20-day realized vol is still elevated. This is where worst-of coupons screen richest without buying a fresh uptrend top.
- Never anchor KI/strike levels to parabolic or immediately post-event prints. A strike set against a spike high bakes in a reference price the market has already abandoned.
- Conversely, avoid names sitting AT their 6-month high with vol already crushed — the coupon rarely compensates.

## Falling-Knife Rule (2-session stabilization)

- Never anchor strikes on a fresh heavy down day. Wait for two consecutive stabilization sessions (price holds a level, no new low) before activating a basket on a falling name.
- Conditional baskets stay conditional until the stabilization test passes; say so explicitly in the daily output rather than silently re-sending them.

## Post-Earnings Clearance Window

- The best entry is often right AFTER a binary event clears: event risk removed, implied/realized vol residual still pricing rich, and the next scheduled event falls outside a 3M tenor.
- Discipline: hold RFQs into the event ("event hold"), re-mark strikes the morning after ("event cleared"), then apply the stabilization rule if the reaction was sharply negative.

## Worst-of Correlation Tradeoff

- Lower inter-leg correlation raises the worst-of coupon AND delivers genuine diversification.
- Same-sector pairs (correlation often 0.8+) are pseudo-diversification: both legs fall together in a sector shock. Prefer cross-theme pairs (e.g., AI infra + nuclear, semis + software, healthcare high-vol + anchor).

## Event Calendar Discipline

- Before locking any 3M tenor, map earnings, FDA/trial dates, launches, and macro prints (FOMC, payrolls, CPI) falling inside the tenor.
- Treat a known mid-tenor macro event as a one-time shock assumption when sizing KI, not as a reason to abandon the structure.

## Requote Classification Taxonomy

Classify every repeated idea instead of silently re-sending it:

- fresh — new idea or new inputs
- repeat-same-rationale — thesis unchanged, levels re-marked
- repeat-changed-inputs — same names, materially different spot/vol
- structural mismatch — quoted structure differs from screen assumptions
- calibration drift — issuer levels drifting from public-data screen
- event hold — paused into a binary event
- event cleared — resumed after the event, levels re-marked

## Like-for-Like Vol Comparison

- When comparing implied vol day over day, compare the SAME expiry. Switching expiries between readings creates false vol-spike or vol-crush signals.

## Option Expiry Quirks

- Mid-caps frequently skip standard monthly cycles. Always verify available expiries before fetching chains or sending an RFQ. See `reference/option-expiry-quirks.md`.

## Data Hygiene

- Public/free market data is screening evidence only — never present it as a firm quote.
- Free datasources are slow and occasionally drop calls; batch fetches in the background with retry loops, and verify file counts before computing.

## Internal Calibration Sources

- Firm-permitted internal/channel calibration material may be used as a negotiation ruler for what a fair coupon looks like.
- Its actual levels are confidential: never commit them to this public repo. Record only the METHOD (calibrate, classify drift, requote), never the numbers.

---


Append to `desk-memory.md`. Principle: the watchlist is a **candidate pool, not a fixed universe**. What we observe each day is decided by the market, not by the list.

## 三层结构

### 第 1 层：常驻池（watchlist.csv）
- 已通过四道闸（入场质量 / RV / 期权流动性 / 事件日历）的标的，目前 69 只。
- 作用是"熟面孔档案库"：已知到期月怪癖、已知发行商覆盖、已知配对关系，定价快。
- 池内标的不保证每天被推荐——只保证每天被重新打分。

### 第 2 层：每日市场驱动的新增观察（最重要）
每天晨钟必须做一次"市场扫描"，以下任一触发条件命中即纳入当日观察，不论是否在池内：
1. **事件驱动**：隔夜财报、FDA/临床数据、发射/合同、并购、监管裁决——波动残留即票息机会（MRVL 剧本）。
2. **波动异动**：RV20 突然站上 60 且期权链有厚度（OI 充足）的标普 1500 / 纳斯达克 100 成分股。
3. **深度回撤新面孔**：任何新跌入"距 6 月高点 20–50% + 高 RV20"区间的知名美股。
4. **板块轮动**：当日资金明显流入/流出的主题（AI 电力、核电、量子、航天、生物科技、中概……），从该主题里挑流动性最好的两只。
5. **用户/客户现场提问**：柜台被问到的任何标的，当日必须给出评估（即使结论是"不适合"）。

### 第 3 层：冻结/移出
- 暂停观察：论点被破坏、波动被榨干（距高点 <10% 且 RV20 塌陷）、期权链流动性恶化、或进入"勿碰"状态（如加密关联，默认排除，除非用户明确选择加入）。
- 移出记录写明原因，留在档案里——防止同样的名字两周后被无记忆地重新提起。

## 每日流程（晨钟固定动作）

1. 先跑常驻池全量打分（价格、回撤、RV20、跨式、OI）。
2. 再跑第 2 层扫描：当日有没有"应该被观察的新东西"。
3. 新旧混合，统一排序出 Top 4–5，说明为什么这几个最好。
4. 任何新进入常驻池的名字：先验证到期月（reference/option-expiry-quirks.md 流程）+ 发行商资格，再进池。
5. 常驻池每周复盘一次：谁该进、谁该冻结、为什么——写回 GitHub。

## 入库/出库纪律

- 入库四道闸缺一不可：距高点位置合适、RV20 够、期权 OI 够、事件日历已绘制。
- 出库不丢人：市场环境变了就该走，记录原因即可。
- 名单规模没有上限和下限——69 只是今天的快照，不是目标数。

## 硬性红线（不随市场变化）

- 加密关联标的默认排除（MSTR、COIN、矿企、加密交易所），除非用户明确选择加入。
- 公开数据只是筛查证据，发行商 RFQ 才定价。
- 新鲜下跌日不锚定执行价；连续两日企稳才激活条件单。
- 渠道/发行商实际报价数字永不进公开仓库。
