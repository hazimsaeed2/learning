"""
Python implementation of VX_ES_rollreturn_regimes.

Builds a continuous VX front-month series (forward adjustment on roll)
and a dailyRoll series, then plots ES vs VX_cont post-2008. Optional
regime splits (contango/backwardation, riskOff/riskOn) and OLS hedge
ratios — kept under `if False:` mirroring the original commented blocks.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

from fwdshift import fwdshift
from _utils import intersect_with_index


def ols_beta(y, X):
    """Return OLS coefficients (no statsmodels dependency)."""
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return beta


def main():
    vx_md = loadmat("inputDataDaily_VX_20120507.mat")
    tday = vx_md["tday"].flatten().astype(int)
    contracts = [c[0] for c in vx_md["contracts"].flatten()]
    cl = vx_md["cl"].astype(float).copy()

    vix_df = pd.read_csv("VIX.csv")
    VIX = vix_df.iloc[:, -1].values.astype(float)
    tday_VIX = pd.to_datetime(vix_df.iloc[:, 0], format="%Y-%m-%d") \
       .dt.strftime("%Y%m%d").astype(int).values

    tday_c, idx1, idx2 = intersect_with_index(tday_VIX, tday)
    VIX = VIX[idx1]
    VX = cl[idx2, :]
    tday = tday_c

    es_md = loadmat("inputDataOHLCDaily_20120507.mat")
    es_syms = [str(s.item()) if s.size==1 and s.dtype.kind=="U" else "" for s in es_md["syms"].flatten()]
    es_idx = es_syms.index("ES")
    ES = es_md["cl"][:, es_idx].astype(float)
    tday_ES = es_md["tday"][:, es_idx].astype(int)

    tday_c, idx1, idx2 = intersect_with_index(tday, tday_ES)
    VIX = VIX[idx1]
    VX = VX[idx1, :]
    ES = ES[idx2]
    tday = tday_c

    isExpireDate = np.isfinite(VX) & ~np.isfinite(fwdshift(1, VX))

    numDaysStart = 30
    numDaysEnd = 1

    VX_cont = np.full(VX.shape[0], np.nan)
    dailyRoll = np.full(VX.shape[0], np.nan)
    endIdx_prev = -1

    for c in range(len(contracts)):
        expireIdx = np.where(isExpireDate[:, c])[0]
        if len(expireIdx) == 0:
            continue
        eIdx = expireIdx[0]
        if c == 0:
            startIdx = eIdx - numDaysStart
            endIdx = eIdx - numDaysEnd
        else:
            startIdx = max(endIdx_prev + 1, eIdx - numDaysStart)
            endIdx = eIdx - numDaysEnd

        if startIdx < 0 or endIdx < 0 or startIdx > endIdx:
            endIdx_prev = endIdx
            continue

        idx = np.arange(startIdx, endIdx + 1)
        dte = np.arange(eIdx - startIdx + 1, eIdx - endIdx, -1)
        dailyRoll[idx] = -(VX[idx, c] - VIX[idx]) / dte
        VX_cont[idx] = VX[idx, c]

        # Forward-adjust subsequent contracts so the continuous series
        # is splice-free at the roll
        if c < VX.shape[1] - 1:
            adj = VX[idx[-1], c] - VX[idx[-1], c + 1]
            VX[:, c + 1:] = VX[:, c + 1:] + adj

        endIdx_prev = endIdx

    post = tday >= 20080801
    plt.scatter(ES[post], VX_cont[post])
    plt.xlabel("ES")
    plt.ylabel("VX_cont")

    # OLS hedge ratio over post-2008 valid VX_cont
    mask = post & np.isfinite(VX_cont)
    X = np.column_stack([1000 * VX_cont[mask], np.ones(mask.sum())])
    y = 50 * ES[mask]
    beta = ols_beta(y, X)
    print(f"hedge ratio ={beta[0]:f}")
    plt.show()


if __name__ == "__main__":
    main()
