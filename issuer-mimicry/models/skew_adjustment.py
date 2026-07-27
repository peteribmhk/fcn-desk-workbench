#!/usr/bin/env python3
"""
Skew Adjustment Module
Applies issuer-style volatility skew adjustments to public ATM vol.
"""
import math

def apply_skew_adjustment(atm_vol, moneyness, skew_factor=0.03):
    ln_m = math.log(moneyness)
    adjustment = skew_factor * abs(ln_m)
    return atm_vol + adjustment

def issuer_vol_surface(atm_vol, strikes, skew_factor=0.03):
    return {k: apply_skew_adjustment(atm_vol, k/100, skew_factor)
            for k in strikes}

def main():
    surface = issuer_vol_surface(0.45, [50, 55, 59, 65, 70, 80, 90, 100])
    for k, v in surface.items():
        print(f"Strike {k}: {v*100:.2f}%")

if __name__ == "__main__":
    main()
