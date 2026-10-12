#!/usr/bin/env python3
"""Ballpark worst-of FCN coupon model (dependency-free).

What it does
------------
Monte Carlo for a worst-of FCN with monthly coupon and KO observation:
  * fixed coupon paid every month the note is alive,
  * KO (autocall) when the worst leg closes >= KO level on an observation date,
  * downside at maturity (no KO) under one of three conventions:
      - "maturity": European KI (US-style default),
      - "daily":    KI observed on daily closes (common in Asian FCN term sheets),
      - "none":     strike-only FCN (delivery whenever the worst ends below strike);
    the investor then receives worst / strike, i.e. shares delivered at the strike.

The fair coupon is solved in closed form from the simulated paths:

    100% - issuer_margin = coupon/12 * E[sum of DF on paid months] + E[DF * redemption]

What it does NOT do
-------------------
Flat vol (no skew), no dividends or borrow, no issuer funding curve, no
inventory or appetite effects. It is a desk ballpark to sanity-check issuer
RFQ levels, never a quote. Issuer RFQ levels always override it.

Usage from the command line (example):

    python scripts/fcn_model.py --vols 0.55 0.48 --corr 0.45 --tenor 6
    python scripts/fcn_model.py --vols 0.55 0.48 --corr 0.45 --ki-style none --ladder 80 85 90
    python scripts/fcn_model.py --vols 0.55 0.48 --corr 0.45 --ki-style daily --strike 90 --ladder 60 65
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass, field


@dataclass
class FCNTerms:
    tenor_months: int = 6
    ko: float = 1.00
    ki_levels: list[float] = field(default_factory=lambda: [0.50, 0.55, 0.59, 0.65, 0.70])
    rate: float = 0.039  # USD short rate (Fed funds 3.75-4.00% after the 2026-09-16 hike); edit when it changes
    funding_spread: float = 0.005  # issuer funding over the rate, passed to the investor via discounting
    ko_start_month: int = 1
    strike: float = 1.00  # delivery/loss strike; Asian FCNs often use 80-95%
    ki_style: str = "maturity"  # "maturity" (European), "daily" (daily close), or "none" (strike-only FCN)


def _cholesky(matrix: list[list[float]]) -> list[list[float]] | None:
    n = len(matrix)
    low = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(low[i][k] * low[j][k] for k in range(j))
            if i == j:
                value = matrix[i][i] - s
                if value <= 1e-10:
                    return None
                low[i][j] = math.sqrt(value)
            else:
                low[i][j] = (matrix[i][j] - s) / low[j][j]
    return low


def safe_cholesky(corr: list[list[float]]) -> list[list[float]]:
    """Cholesky, shrinking toward a 0.5 flat matrix if the input is not PSD."""
    n = len(corr)
    for weight in (0.0, 0.1, 0.25, 0.5, 0.75, 1.0):
        blended = [
            [1.0 if i == j else (1 - weight) * corr[i][j] + weight * 0.5 for j in range(n)]
            for i in range(n)
        ]
        low = _cholesky(blended)
        if low is not None:
            return low
    raise ValueError("Correlation matrix could not be repaired")


def simulate_fcn(
    vols: list[float],
    corr: list[list[float]],
    terms: FCNTerms | None = None,
    n_paths: int = 20000,
    seed: int = 7,
) -> dict[float, dict[str, float]]:
    """Per ladder level stats: {"annuity", "pv_redemption", "p_ko", "p_ki", "exp_life_m"}.

    Ladder levels are KI levels for ki_style "maturity"/"daily", and STRIKE levels for
    ki_style "none" (strike-only FCN, the common Asian ladder 80/85/90...).
    Loss event at maturity (no KO): KI condition met AND worst < strike; the investor
    receives worst/strike (physical delivery at strike, valued at the final price).
    p_ki is the probability of that loss event. Use fair_coupon() to get a coupon.
    """
    terms = terms or FCNTerms()
    n = len(vols)
    low = safe_cholesky(corr)
    rng = random.Random(seed)
    steps = 21 if terms.ki_style == "daily" else 1  # sub-steps per month
    dt = 1.0 / 12.0 / steps
    months = terms.tenor_months
    month_dt = 1.0 / 12.0
    discount = [math.exp(-(terms.rate + terms.funding_spread) * month_dt * (m + 1)) for m in range(months)]
    drift = [(terms.rate - 0.5 * v * v) * dt for v in vols]
    shock = [v * math.sqrt(dt) for v in vols]

    annuity_sum = 0.0
    ko_red_sum = 0.0
    ko_count = 0
    life_sum = 0.0
    survivors: list[tuple[float, float]] = []  # (worst at maturity, path minimum of worst) for non-KO paths

    for path in range(n_paths):
        sign = 1.0 if path % 2 == 0 else -1.0  # antithetic pairs reduce noise
        if sign > 0:
            normals_cache = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(months * steps)]
        log_s = [0.0] * n
        path_min = 1.0
        knocked = False
        for m in range(months):
            for k in range(steps):
                z = normals_cache[m * steps + k]
                for i in range(n):
                    correlated = sum(low[i][j] * z[j] for j in range(i + 1)) * sign
                    log_s[i] += drift[i] + shock[i] * correlated
                if steps > 1:
                    path_min = min(path_min, math.exp(min(log_s)))
            annuity_sum += discount[m]
            worst = math.exp(min(log_s))
            path_min = min(path_min, worst)
            if m + 1 >= terms.ko_start_month and worst >= terms.ko:
                ko_red_sum += discount[m]
                ko_count += 1
                life_sum += m + 1
                knocked = True
                break
        if not knocked:
            life_sum += months
            survivors.append((math.exp(min(log_s)), path_min))

    df_t = discount[-1]
    out: dict[float, dict[str, float]] = {}
    for level in terms.ki_levels:
        if terms.ki_style == "none":
            ki, strike = None, level
        else:
            ki, strike = level, terms.strike
        red = ko_red_sum
        losses = 0
        for w, pmin in survivors:
            if terms.ki_style == "daily":
                triggered = pmin < ki
            elif terms.ki_style == "maturity":
                triggered = w < ki
            else:
                triggered = True
            if triggered and w < strike:
                red += df_t * (w / strike)
                losses += 1
            else:
                red += df_t
        out[level] = {
            "annuity": annuity_sum / n_paths,
            "pv_redemption": red / n_paths,
            "p_ko": ko_count / n_paths,
            "p_ki": losses / n_paths,
            "exp_life_m": life_sum / n_paths,
        }
    return out


def fair_coupon(stats: dict[str, float], issuer_margin: float) -> float:
    """Annualized coupon (decimal) that makes PV = 1 - issuer_margin."""
    monthly = (1.0 - issuer_margin - stats["pv_redemption"]) / stats["annuity"]
    return max(0.0, monthly * 12.0)


def ballpark_range(
    vols: list[float],
    corr: list[list[float]],
    terms: FCNTerms | None = None,
    n_paths: int = 20000,
    skew_bump: float = 0.03,
    margin_high: float = 0.015,
    margin_low: float = 0.0075,
    seed: int = 7,
) -> dict[float, dict[str, float]]:
    """Low/high ballpark per KI.

    Low end: ATM vol, 1.5% issuer margin. High end: ATM vol + 3 vol pts (rough
    stand-in for downside skew), 0.75% issuer margin. Real issuer levels can land
    outside this band.
    """
    terms = terms or FCNTerms()
    base = simulate_fcn(vols, corr, terms, n_paths, seed)
    bumped = simulate_fcn([v + skew_bump for v in vols], corr, terms, n_paths, seed)
    result = {}
    for ki in terms.ki_levels:
        result[ki] = {
            "low": fair_coupon(base[ki], margin_high),
            "high": fair_coupon(bumped[ki], margin_low),
            "p_ko": base[ki]["p_ko"],
            "p_ki": base[ki]["p_ki"],
            "exp_life_m": base[ki]["exp_life_m"],
        }
    return result


def _main() -> None:
    parser = argparse.ArgumentParser(description="Ballpark worst-of FCN coupon (indicative only).")
    parser.add_argument("--vols", type=float, nargs="+", required=True, help="Annual vols, e.g. 0.55 0.48")
    parser.add_argument("--corr", type=float, default=0.5, help="Flat pairwise correlation")
    parser.add_argument("--tenor", type=int, default=6, help="Tenor in months")
    parser.add_argument("--ko", type=float, default=100, help="KO level in percent")
    parser.add_argument("--ko-start", type=int, default=1, help="First KO observation month (non-call period)")
    parser.add_argument("--strike", type=float, default=100, help="Strike in percent (ignored for --ki-style none)")
    parser.add_argument("--ki-style", choices=["maturity", "daily", "none"], default="maturity",
                        help="maturity = European KI; daily = daily-close KI; none = strike-only FCN")
    parser.add_argument("--ladder", type=float, nargs="+", default=None,
                        help="KI levels (or strike levels for --ki-style none) in percent")
    parser.add_argument("--rate", type=float, default=3.9, help="USD rate in percent")
    parser.add_argument("--paths", type=int, default=None)
    args = parser.parse_args()
    n = len(args.vols)
    corr = [[1.0 if i == j else args.corr for j in range(n)] for i in range(n)]
    default_ladder = [80, 85, 90, 95] if args.ki_style == "none" else [50, 55, 59, 65, 70]
    ladder = [x / 100 for x in (args.ladder or default_ladder)]
    terms = FCNTerms(tenor_months=args.tenor, ko=args.ko / 100, rate=args.rate / 100, ki_levels=ladder,
                     ko_start_month=args.ko_start, strike=args.strike / 100, ki_style=args.ki_style)
    paths = args.paths or (6000 if args.ki_style == "daily" else 20000)
    result = ballpark_range(args.vols, corr, terms, paths)
    label = "Strike" if args.ki_style == "none" else "KI"
    print("Indicative only. Not a firm quote.")
    print(f"KI style: {args.ki_style}; strike {args.strike:.0f}% ; KO {args.ko:.1f}% monthly from month {args.ko_start}")
    print(f"{label:>6} {'coupon p.a. ballpark':>22} {'P(KO)':>7} {'P(loss)':>8} {'exp life':>9}")
    for level, row in result.items():
        print(
            f"{level*100:>6.0f} {row['low']*100:>9.1f}% - {row['high']*100:>5.1f}%"
            f" {row['p_ko']*100:>6.0f}% {row['p_ki']*100:>7.1f}% {row['exp_life_m']:>7.1f}m"
        )


if __name__ == "__main__":
    _main()
