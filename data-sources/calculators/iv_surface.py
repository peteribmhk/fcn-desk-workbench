#!/usr/bin/env python3
"""
Implied Volatility Surface Calculator
Computes rough implied volatility from ATM option straddle mid prices.
Uses Black-Scholes inversion. Public data only — indicative.
"""
import math
from scipy.optimize import brentq


def black_scholes_call(S, K, T, r, sigma):
    """Black-Scholes call price."""
    if T <= 0 or sigma <= 0:
        return max(S - K, 0)
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    nd1 = 0.5 * (1 + math.erf(d1 / math.sqrt(2)))
    nd2 = 0.5 * (1 + math.erf(d2 / math.sqrt(2)))
    return S * nd1 - K * math.exp(-r * T) * nd2


def straddle_price(S, K, T, r, sigma):
    """ATM straddle price = call + put. At ATM, put = call by put-call parity approx."""
    call = black_scholes_call(S, K, T, r, sigma)
    put = call - S + K * math.exp(-r * T)  # put-call parity
    return call + put


def iv_from_straddle(S, K, T, r, straddle_mid, sigma_bounds=(0.001, 5.0)):
    """
    Invert Black-Scholes straddle price to find implied volatility.
    Returns annualized IV as decimal (e.g., 0.35 for 35%).
    """
    try:
        def objective(sigma):
            return straddle_price(S, K, T, r, sigma) - straddle_mid
        iv = brentq(objective, sigma_bounds[0], sigma_bounds[1], xtol=1e-6)
        return iv
    except Exception:
        return None


def compute_iv_proxy(spot, atm_strike, straddle_mid, tenor_months, risk_free_rate=0.05):
    """
    Compute a rough IV proxy from public option data.

    Args:
        spot: current spot price
        atm_strike: ATM strike
        straddle_mid: mid price of ATM straddle
        tenor_months: option tenor in months
        risk_free_rate: annual risk-free rate (decimal)

    Returns:
        dict with iv, annualized_vol, and caveats
    """
    T = tenor_months / 12.0
    iv = iv_from_straddle(spot, atm_strike, T, risk_free_rate, straddle_mid)
    if iv is None:
        return {
            "iv": None,
            "annualized_vol": None,
            "status": "FAILED",
            "caveat": "Could not invert BS straddle. Data may be stale or illiquid.",
        }

    # Annualized vol is approximately IV for ATM options
    annualized = iv

    return {
        "iv": round(iv, 4),
        "annualized_vol": round(annualized, 4),
        "status": "OK",
        "caveat": "Rough BS inversion from public ATM straddle. Not a full vol surface. Issuer skew/correlation not included.",
        "inputs": {
            "spot": spot,
            "atm_strike": atm_strike,
            "straddle_mid": straddle_mid,
            "tenor_years": T,
            "risk_free_rate": risk_free_rate,
        }
    }


def main():
    # Example: AAPL-like inputs
    result = compute_iv_proxy(
        spot=225.0,
        atm_strike=225.0,
        straddle_mid=12.5,
        tenor_months=3,
        risk_free_rate=0.0525,
    )
    print(result)


if __name__ == "__main__":
    main()
