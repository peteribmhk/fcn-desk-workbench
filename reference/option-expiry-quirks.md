# Option Expiry Quirks — Verified Reference Table

Public-data observation (Yahoo Finance option chains), verified 2026-09-01. Standard assumption: 3M tenor ≈ nearest monthly ~3 months out, 6M ≈ ~6 months out. Many mid-caps do NOT list the expected months — verify before fetching chains or sending an RFQ.

## Standard cycle (3M = 2026-11-20, 6M = 2027-02-19 available)

MU, SNDK, SMCI, AMD, TSLA, NVDA, GLW, INTC, BABA, ENPH, HIMS, GOOGL, NBIS, ASTS, RGTI, MRVL, CRDO, APP, AMAT

## No 2027-02-19 — use 2027-03-19 for ~6M

IONQ, PDD, FSLR, OKLO, COHR, ALAB, ARM, VRT, RKLB

## No 2026-11-20 — use 2026-12-18 for ~3M

RKLB, AVAV

## Missing BOTH 2026-11-20 and 2027-02-19 — use 2027-01-15

TDOC, NTLA, CRSP, APLD

(APLD skips 2026-11-20 entirely; its chain jumps from October to January.)

## Working rules

1. Call the expiration-dates endpoint FIRST for any new ticker; never assume the standard monthly ladder.
2. When comparing straddle/implied-vol proxies across days, use the same expiry per ticker (like-for-like).
3. A missing expiry is also a liquidity signal: sparser chains usually mean wider bid/ask and thinner open interest — factor that into issuer RFQ expectations.
4. Re-verify monthly; exchanges add cycles as open interest builds.
