#!/usr/bin/env python3
"""
Monte Carlo Worst-of Simulator
Simulates correlated GBM paths for worst-of FCN pricing.
"""
import math
import random
from datetime import datetime

def cholesky(A):
    n = len(A)
    L = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k]*L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(A[i][i] - s)
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    return L

def simulate_worst_of(S_list, sigma_list, corr_matrix, T, r,
                      ki_level, ko_level, n_sims=10000, steps=126):
    n = len(S_list)
    dt = T / steps
    L = cholesky(corr_matrix)
    results = []
    for _ in range(n_sims):
        paths = [s for s in S_list]
        ki_hit = False
        ko_hit = False
        coupons_earned = 0
        for step in range(1, steps+1):
            z_raw = [random.gauss(0,1) for _ in range(n)]
            z = [sum(L[i][j]*z_raw[j] for j in range(n)) for i in range(n)]
            for i in range(n):
                drift = (r - 0.5*sigma_list[i]**2)*dt
                diff = sigma_list[i]*math.sqrt(dt)*z[i]
                paths[i] *= math.exp(drift + diff)
            worst = min(paths)
            if step % (steps//12 if steps>=12 else 1) == 0 and not ko_hit:
                if worst >= ko_level:
                    ko_hit = True
                    coupons_earned += 1
                    break
            if worst < ki_level:
                ki_hit = True
            coupons_earned += 1
        results.append({"ko": ko_hit, "ki": ki_hit, "coupons": coupons_earned, "final_worst": worst})
    ko_prob = sum(1 for r in results if r["ko"]) / n_sims
    ki_prob = sum(1 for r in results if r["ki"]) / n_sims
    avg_coupons = sum(r["coupons"] for r in results) / n_sims
    return {
        "prob_ko": ko_prob,
        "prob_ki": ki_prob,
        "avg_coupons": avg_coupons,
        "timestamp": datetime.now().isoformat()
    }

def main():
    result = simulate_worst_of(
        S_list=[100, 100],
        sigma_list=[0.45, 0.50],
        corr_matrix=[[1.0, 0.6], [0.6, 1.0]],
        T=0.5, r=0.054, ki_level=70, ko_level=100
    )
    print(result)

if __name__ == "__main__":
    main()
