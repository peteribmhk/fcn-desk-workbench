# Watchlist Changelog — 常驻池进出记录

Per the Living Watchlist Protocol (see PLAYBOOK.md §11): every add / freeze / removal is logged here with a reason, so no name resurfaces memory-less two weeks later.

## 2026-09-02 — Round 1 additions (+20, pool 17 → 37)

Added: MU, GLW, MRVL, COHR, ALAB, ARM, VRT, APP, AMAT, CRDO, NBIS, OKLO, ASTS, RGTI, APLD, AVAV, NTLA, TDOC, ISRG, LLY.
Reason: validated through the 4-gate screen (entry quality / RV / option liquidity / event calendar) during Aug screening batches; MU had anchored the top basket for sessions without being on the list.

## 2026-09-02 — Round 2 additions (+32, pool 37 → 69)

Added: AVGO, ANET, WDC, STX, LITE, DELL, CRWV, ORCL, SNOW, NET, DDOG, SOFI, AFRM, JD, NIO, XPEV, BIDU, MELI, TCOM, CRSP, VKTX, NVO, LUNR, KTOS, SMR, LEU, GEV, VST, TLN, DKNG, QUBT, QBTS.
Reason: user directive — the pool is a living candidate base, not a fixed universe; broadened across AI infra, power, software, fintech, China ADR, biotech, space/defense, quantum.
Pending for round-2 names: option-expiry verification + issuer eligibility check before first RFQ.

## 2026-11-06 — Round 3 additions (+4, pool 69 → 73)

Added: DXCM, ZBH, ZS, BE.
Reason: sourced from an external valuation screen (forward multiple below the name's own 10-year 25th percentile, revenue still growing, market cap ≥ $10B, median analyst target above price). DXCM and ZBH fill a gap: the Biotech/Health bucket held only high-vol biotech, with no mid-vol medtech to act as a defensive non-tech leg. ZS adds a software leg; BE an aggressive power leg.
Considered and skipped: RMD, BAX, GEN (median analyst target below price, so a weak floor if struck); MDLN (2025 IPO, short valuation history, many issuers will not quote it); ABT, SYK, CARR (vol too low for a useful coupon).
Valuation reads for these and for NVDA, GEV, VST, ISRG, IONQ are in `fundamentals/valuation.csv`; the daily screen shows them as a non-blocking cross-check.
Pending: option-expiry verification + issuer eligibility before first RFQ.

## Frozen / Removed

(none yet — first weekly review due week of 2026-09-07)

## Standing exclusions

Crypto-linked names (MSTR, COIN, miners, exchanges) excluded by default unless the user explicitly opts in.
