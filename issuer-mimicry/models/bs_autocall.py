#!/usr/bin/env python3
"""
Black-Scholes Autocall Adjustment Model
Base analytical model for FCN coupon approximation.
"""
import math

def bs_put(S, K, T, r, sigma):
    if T <= 0 or sigma <= 0:
        return max(K - S, 0)
    d1 = (math.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    nd1 = 0.5 * (1 + math.erf(-d1/math.sqrt(2)))
    nd2 = 0.5 * (1 + math.erf(-d2/math.sqrt(2)))
    return K*math.exp(-r*T)*nd2 - S*nd1

def digital_coupon_fair_value(S, K, T, r, sigma, ko_prob, ki_level):
    """
    Rough fair value of a digital monthly coupon + downside put.
    """
    digital_rate = r + 0.008
    monthly_digital = digital_rate / 12
    expected_periods = 12 * T * (1 - ko_prob * 0.5)
    digital_value = monthly_digital * expected_periods
    put_strike = ki_level
    put_value = bs_put(S, put_strike, T, r, sigma) / S
    fair_coupon_annual = (digital_value + put_value) / T
    return fair_coupon_annual

def main():
    result = digital_coupon_fair_value(
        S=100, K=100, T=0.5, r=0.054, sigma=0.45, ko_prob=0.3, ki_level=70
    )
    print(f"Fair coupon (annualized): {result*100:.2f}%")

if __name__ == "__main__":
    main()
