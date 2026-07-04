"""
Python implementation of TU_mom.

Two-year U.S. Treasury note futures (TU): runs the lookback/holddays
correlation grid, computes Hurst exponent and variance ratio test,
then back-tests a long-only momentum strategy with overlapping cohorts.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.stats import pearsonr

from fwdshift import backshift, fwdshift, lag
from genhurst import genhurst
from hurstExpVratioTest import variance_ratio_test
from smartmean2 import smartmean
from _utils import calculateMaxDD


def main():
    md = loadmat("inputDataOHLCDaily_20120517.mat")
    syms = [s[0] for s in md["syms"].flatten()]
    idx = syms.index("TU")
    tday = md["tday"][:, idx].astype(int)
    cl = md["cl"][:, idx].astype(float)

    # Correlation tests
    for lookback in [1, 5, 10, 25, 60, 120, 250]:
        for holddays in [1, 5, 10, 25, 60, 120, 250]:
            ret_lag = (cl - backshift(lookback, cl)) / backshift(lookback, cl)
            ret_fut = (fwdshift(holddays, cl) - cl) / cl
            mask = ~(np.isnan(ret_lag) | np.isnan(ret_fut))
            ret_lag_v = ret_lag[mask]
            ret_fut_v = ret_fut[mask]

            step = holddays if lookback >= holddays else lookback
            indep = np.arange(0, len(ret_lag_v), step)
            ret_lag_v = ret_lag_v[indep]
            ret_fut_v = ret_fut_v[indep]

            if len(ret_lag_v) > 2:
                cc, pval = pearsonr(ret_lag_v, ret_fut_v)
            else:
                cc, pval = np.nan, np.nan
            print(f"{lookback:3d}\t{holddays:3d}\t{cc:7.4f}\t{pval:6.4f}")

    # Hurst exponent
    H, _ = genhurst(np.log(cl[np.isfinite(cl)]), q=2)
    print(f"H2={H:.6f}")

    # Variance ratio test (Lo-MacKinlay heteroscedasticity-consistent)
    h, pValue, _, _ = variance_ratio_test(np.log(cl[np.isfinite(cl)]), q=2)
    print(f"h={h}")
    print(f"pValue={pValue:.6f}")

    # Momentum backtest
    lookback = 250
    holddays = 25

    longs = cl > backshift(lookback, cl)
    shorts = cl < backshift(lookback, cl)

    pos = np.zeros(len(cl))
    for h in range(holddays):
        long_lag = backshift(h, longs.astype(float))
        long_lag = np.nan_to_num(long_lag).astype(bool)
        short_lag = backshift(h, shorts.astype(float))
        short_lag = np.nan_to_num(short_lag).astype(bool)
        pos[long_lag] += 1
        pos[short_lag] -= 1

    ret = (backshift(1, pos) * (cl - lag(cl)) / lag(cl)) / holddays
    ret[np.isnan(ret)] = 0
    cumret = np.cumprod(1 + ret) - 1

    plt.plot(cumret)
    plt.title("TU momentum cumulative returns")

    print(f"Avg Ann Ret={252*smartmean(ret):7.4f} "
          f"Ann Volatility={np.sqrt(252)*np.nanstd(ret, ddof=1):7.4f} "
          f"Sharpe ratio={np.sqrt(252)*smartmean(ret)/np.nanstd(ret, ddof=1):4.2f}")
    APR = np.prod(1 + ret) ** (252 / len(ret)) - 1
    print(f"APR={APR:10.4f}")
    maxDD, maxDDD = calculateMaxDD(cumret)
    print(f"Max DD ={maxDD:f} Max DDD in days={maxDDD}")
    print(f"Kelly f={np.mean(ret)/np.std(ret, ddof=1)**2:f}")

    plt.show()


if __name__ == "__main__":
    main()
