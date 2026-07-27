#!/usr/bin/env python3
"""
FCN Indicative Pricer — Public Data Only
Computes an indicative coupon range for a worst-of FCN using public market data.
This is NOT an issuer pricer. It is a screening tool that mimics issuer logic
with conservative assumptions.

Model: Black-Scholes + autocall probability adjustment + issuer-style spread markup.
"""
import math
import random
from datetime import datetime


def black_scholes_put(S, K, T, r, sigma):
    """Black-Scholes put price."""
    if T <= 0 or sigma <= 0:
        return max(K - S, 0)
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    nd1_neg = 0.5 * (1 + math.erf(-d1 / math.sqrt(2)))
    nd2_neg = 0.5 * (1 + math.erf(-d2 / math.sqrt(2)))
    return K * math.exp(-r * T) * nd2_neg - S * nd1_neg


def autocall_prob(S, K, T, r, sigma, ko_level, obs_per_year=12):
    """
    Rough autocall probability for a monthly-observed KO.
    Uses a simple barrier approximation. Very conservative.
    """
    if ko_level <= 0:
        return 0.0
    # Simplified: probability of hitting KO level at least once
    # Using reflection principle approximation
    mu = r - 0.5 * sigma ** 2
    lambda_ = (mu + math.sqrt(mu ** 2 + 2 * r * sigma ** 2)) / sigma ** 2
    # This is a rough desk approximation, not a full Monte Carlo
    prob_hit = math.exp(-2 * math.log(S / ko_level) * lambda_)
    # Monthly observation reduces probability slightly
    prob_hit *= 0.85  # observation frequency discount
    return min(prob_hit, 1.0)


def worst_of_mc(S_list, sigma_list, corr_matrix, T, r, n_sims=10000, steps=63):
    """
    Monte Carlo worst-of path simulation.
    Returns: (prob_ki, prob_ko, expected_coupon_periods)
    """
    n_assets = len(S_list)
    dt = T / steps

    # Cholesky decomposition for correlated normals
    def cholesky(A):
        n = len(A)
        L = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                s = sum(L[i][k] * L[j][k] for k in range(j))
                if i == j:
                    L[i][j] = math.sqrt(A[i][i] - s)
                else:
                    L[i][j] = (A[i][j] - s) / L[j][j]
        return L

    L = cholesky(corr_matrix)

    ki_count = 0
    ko_count = 0
    total_coupon_periods = 0

    for _ in range(n_sims):
        paths = [S_list[i] for i in range(n_assets)]
        coupon_periods = 0
        ki_triggered = False
        ko_triggered = False

        for step in range(1, steps + 1):
            # Generate correlated normals
            z_raw = [random.gauss(0, 1) for _ in range(n_assets)]
            z = [sum(L[i][j] * z_raw[j] for j in range(n_assets)) for i in range(n_assets)]

            for i in range(n_assets):
                drift = (r - 0.5 * sigma_list[i] ** 2) * dt
                diffusion = sigma_list[i] * math.sqrt(dt) * z[i]
                paths[i] *= math.exp(drift + diffusion)

            worst = min(paths)
            # Check KO (monthly approx: every steps//obs_per_year steps)
            if not ko_triggered and step % (steps // 12 if steps >= 12 else 1) == 0:
                if worst >= 100:  # KO at 100% of initial
                    ko_triggered = True
                    break
            # Check KI (continuous for conservatism)
            if worst < 70:  # Example KI level
                ki_triggered = True

            coupon_periods += 1

        if ki_triggered:
            ki_count += 1
        if ko_triggered:
            ko_count += 1
        total_coupon_periods += coupon_periods

    return {
        "prob_ki": ki_count / n_sims,
        "prob_ko": ko_count / n_sims,
        "avg_coupon_periods": total_coupon_periods / n_sims,
    }


def indicative_coupon(
    spot_list,
    vol_list,
    corr_matrix,
    tenor_months,
    ki_level,
    ko_level,
    risk_free_rate,
    issuer_spread=0.015,  # 150bp issuer markup over fair value
    issuer_margin=0.005,  # 50bp issuer profit margin
):
    """
    Compute indicative annualized coupon range for a worst-of FCN.

    Args:
        spot_list: list of spot prices (normalized to 100)
        vol_list: list of annualized volatilities (decimal)
        corr_matrix: correlation matrix (list of lists)
        tenor_months: note tenor in months
        ki_level: knock-in level (e.g., 70 for 70%)
        ko_level: knock-out level (e.g., 100 for 100%)
        risk_free_rate: annual risk-free rate (decimal)
        issuer_spread: issuer funding/credit spread (decimal)
        issuer_margin: issuer profit margin (decimal)

    Returns:
        dict with indicative coupon range and model details
    """
    T = tenor_months / 12.0
    n_assets = len(spot_list)

    # Normalize spots to 100
    S_norm = [100.0] * n_assets

    # Run Monte Carlo
    mc_result = worst_of_mc(S_norm, vol_list, corr_matrix, T, risk_free_rate)

    # Fair value approximation: digital coupon + put spread
    # Simplified: coupon ≈ (risk_free + issuer_spread) / (1 - prob_ko) + vol_premium - ki_risk
    base_rate = risk_free_rate + issuer_spread
    vol_premium = sum(vol_list) / n_assets * 0.25  # rough vol premium
    ki_risk = mc_result["prob_ki"] * 0.10  # 10% haircut if KI likely
    ko_discount = mc_result["prob_ko"] * 0.05  # 5% reduction if KO likely

    fair_coupon = base_rate + vol_premium - ki_risk - ko_discount
    issuer_coupon_low = fair_coupon - issuer_margin
    issuer_coupon_high = fair_coupon + issuer_margin * 0.5  # issuer rarely gives full fair value

    return {
        "indicative_coupon_low": round(issuer_coupon_low * 100, 2),
        "indicative_coupon_mid": round(fair_coupon * 100, 2),
        "indicative_coupon_high": round(issuer_coupon_high * 100, 2),
        "unit": "% p.a.",
        "model": "Monte Carlo worst-of + BS put spread approximation",
        "mc_results": mc_result,
        "assumptions": {
            "tenor_years": T,
            "ki_level": ki_level,
            "ko_level": ko_level,
            "risk_free_rate": risk_free_rate,
            "issuer_spread": issuer_spread,
            "issuer_margin": issuer_margin,
            "n_simulations": 10000,
            "correlation": corr_matrix,
        },
        "caveat": "Indicative only. Not an issuer quote. Calibrate with real RFQ. Model uses conservative public-data assumptions.",
        "timestamp": datetime.now().isoformat(),
    }


def main():
    # Example: 2-asset worst-of FCN
    result = indicative_coupon(
        spot_list=[100, 100],
        vol_list=[0.45, 0.50],
        corr_matrix=[[1.0, 0.6], [0.6, 1.0]],
        tenor_months=6,
        ki_level=70,
        ko_level=100,
        risk_free_rate=0.0540,
    )
    print(result)


if __name__ == "__main__":
    main()
