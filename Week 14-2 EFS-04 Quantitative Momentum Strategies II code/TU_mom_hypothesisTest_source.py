"""
Python implementation of TU_mom_hypothesisTest.

Repeats the TU momentum back-test and performs two hypothesis tests
on the resulting Sharpe-style statistic:

  1. Gaussian test (mean/std * sqrt(N))
  2. Monte-Carlo over Pearson-distributed simulated market returns,
     matching the first four sample moments of the observed series.

NOTE: `pearsrnd` is reproduced via the scipy.stats `pearson3`
fallback when only the first 3 moments are achievable. For the kurtosis-
matching variant we use the Fleishman / Pearson system via
`scipy.stats.pearson3` (skew only) plus standardization. This is a
documented approximation — see comment block below.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.stats import skew, kurtosis, pearson3

from fwdshift import backshift, lag


def pearsrnd(mu, sigma, sk, ku, n):
    """Approximate pearsrnd: draws n samples from a distribution
    in the Pearson system matching (mu, sigma, skewness, kurtosis).
    We use scipy.stats.pearson3 to match skewness, then rescale to (mu,
    sigma). Excess kurtosis matching is only approximate.
    """
    if abs(sk) < 1e-8:
        return mu + sigma * np.random.randn(n)
    z = pearson3.rvs(skew=sk, size=n)
    z = (z - z.mean()) / z.std(ddof=1)
    return mu + sigma * z


def main():
    md = loadmat("inputDataOHLCDaily_20120511.mat")
    syms = [s[0] for s in md["syms"].flatten()]
    idx = syms.index("TU")
    tday = md["tday"][:, idx].astype(int)
    cl = md["cl"][:, idx].astype(float)

    lookback = 250
    holddays = 25

    longs = cl > backshift(lookback, cl)
    shorts = cl < backshift(lookback, cl)

    pos = np.zeros(len(cl))
    for h in range(holddays):
        long_lag = np.nan_to_num(backshift(h, longs.astype(float))).astype(bool)
        short_lag = np.nan_to_num(backshift(h, shorts.astype(float))).astype(bool)
        pos[long_lag] += 1
        pos[short_lag] -= 1

    marketRet = (cl - lag(cl)) / lag(cl)
    marketRet[~np.isfinite(marketRet)] = 0

    ret = backshift(1, pos) * marketRet / holddays
    ret[np.isnan(ret)] = 0

    # Gaussian hypothesis test
    gauss_stat = np.mean(ret) / np.std(ret, ddof=1) * np.sqrt(len(ret))
    print(f"Gaussian Test statistic={gauss_stat:4.2f}")

    # Monte-Carlo with pearson-distributed market returns
    moments = (np.mean(marketRet), np.std(marketRet, ddof=1),
               skew(marketRet, bias=False), kurtosis(marketRet, fisher=False, bias=False))
    numBetter = 0
    nSamples = 10000
    rng = np.random.default_rng(0)
    np.random.seed(0)

    for sample in range(nSamples):
        marketRet_sim = pearsrnd(*moments, len(marketRet))
        cl_sim = np.cumprod(1 + marketRet_sim) - 1

        longs_sim = cl_sim > backshift(lookback, cl_sim)
        shorts_sim = cl_sim < backshift(lookback, cl_sim)

        pos_sim = np.zeros(len(cl_sim))
        for h in range(holddays):
            long_sim_lag = np.nan_to_num(backshift(h, longs_sim.astype(float))).astype(bool)
            short_sim_lag = np.nan_to_num(backshift(h, shorts_sim.astype(float))).astype(bool)
            pos_sim[long_sim_lag] += 1
            pos_sim[short_sim_lag] -= 1

        ret_sim = backshift(1, pos_sim) * marketRet_sim / holddays
        ret_sim[~np.isfinite(ret_sim)] = 0

        if np.mean(ret_sim) >= np.mean(ret):
            numBetter += 1

    p_val = numBetter / nSamples
    print(f"Randomized prices: p-value={p_val:f}")


if __name__ == "__main__":
    main()
