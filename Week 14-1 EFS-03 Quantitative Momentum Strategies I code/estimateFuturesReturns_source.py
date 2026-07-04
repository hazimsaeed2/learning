"""
Python implementation of estimateFuturesReturns.

For corn futures (C2):
  1. Estimates the average annualised spot return by OLS on log(spot)
     against time.
  2. Fits gamma (roll-yield slope) on each day by regressing log of the
     first 5 consecutive-month contracts against contract index, then
     scales to annualised roll return.

Notes:
  - `regress(y, X)` returns the coefficients; we use
    numpy.linalg.lstsq.
  - Contracts are assumed two months apart, hence gamma = -6 * slope.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

from fwdshift import fwdshift
from smartmean2 import smartmean


def main():
    md = loadmat("inputDataDaily_C2_20120813.mat")
    tday = md["tday"].flatten().astype(int)
    contracts = [c[0] for c in md["contracts"].flatten()]
    cl = md["cl"].astype(float).copy()

    # Find spot price column
    spot_idx = contracts.index("0000$")
    spot = cl[:, spot_idx].copy()
    cl = np.delete(cl, spot_idx, axis=1)
    del contracts[spot_idx]

    T = np.arange(1, len(spot) + 1, dtype=float)
    mask = np.isfinite(spot)
    spot_v = spot[mask]
    T_v = T[mask]
    X = np.column_stack([T_v, np.ones_like(T_v)])
    beta, *_ = np.linalg.lstsq(X, np.log(spot_v), rcond=None)
    print(f"Average annualized spot return={252*beta[0]:f}")

    # Fitting gamma to forward curve, day by day
    gamma = np.full(len(tday), np.nan)
    for t in range(len(tday)):
        FT = cl[t, :]
        idx = np.where(np.isfinite(FT))[0]
        if len(idx) < 5:
            continue
        idxDiff = np.diff(idx)
        # require first 4 differences == 1 (consecutive months)
        if not np.all(idxDiff[:4] == 1):
            continue
        FT5 = FT[idx[:5]]
        T5 = np.arange(1, 6, dtype=float)
        X5 = np.column_stack([T5, np.ones_like(T5)])
        beta5, *_ = np.linalg.lstsq(X5, np.log(FT5), rcond=None)
        # Contracts are 2 months apart -> 6 = 12 months / 2
        gamma[t] = -6 * beta5[0]

    valid = np.isfinite(gamma)
    gamma_v = gamma[valid]
    tday_v = tday[valid]

    plt.plot(gamma_v)
    plt.title("Annualised roll return (gamma) — Corn")

    print(f"Average annualized roll return={smartmean(gamma_v):f}")
    plt.show()


if __name__ == "__main__":
    main()
