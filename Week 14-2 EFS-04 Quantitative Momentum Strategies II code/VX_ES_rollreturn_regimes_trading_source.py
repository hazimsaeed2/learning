"""
Python implementation of VX_ES_rollreturn_regimes_trading.

Same VX/ES roll-return back-test as VX_ES_rollreturn.py but using the
regime-derived hedge ratio 0.315377 (estimated in
VX_ES_rollreturn_regimes.py) instead of the default 0.35.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

from fwdshift import backshift, fwdshift
from smartsum import smartsum
from _utils import calculateMaxDD, intersect_with_index


def main():
    entryThreshold = 0.1
    onewaytcost = 1 / 10000
    hedgeRatio = 0.315377 # from VX_ES_rollreturn_regimes.py

    vx_md = loadmat("inputDataDaily_VX_20120507.mat")
    tday = vx_md["tday"].flatten().astype(int)
    contracts = [c[0] for c in vx_md["contracts"].flatten()]
    cl = vx_md["cl"].astype(float)

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

    positions = np.zeros((VX.shape[0], VX.shape[1] + 1))
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
        dailyRoll = -(VX[idx, c] - VIX[idx]) / dte

        long_mask = dailyRoll > entryThreshold
        short_mask = dailyRoll < -entryThreshold
        positions[idx[long_mask], c] = 1 * hedgeRatio
        positions[idx[long_mask], -1] = 1
        positions[idx[short_mask], c] = -1 * hedgeRatio
        positions[idx[short_mask], -1] = -1

        endIdx_prev = endIdx

    y = np.column_stack([VX * 1000, ES * 50])

    pos_shifted = backshift(1, positions)
    y_shifted = backshift(1, y)
    denom = smartsum(np.abs(backshift(1, positions * y)), dim=2)
    ret = smartsum(pos_shifted * (y - y_shifted), dim=2) / denom \
        - onewaytcost * smartsum(np.abs(positions * y - backshift(1, positions * y)), dim=2) / denom
    ret = np.where(np.isnan(ret), 0, ret)

    cumret = np.cumprod(1 + ret) - 1
    plt.plot(cumret)
    plt.title(f"VX vs ES with regime hedge ratio {hedgeRatio}")

    APR = np.prod(1 + ret) ** (252 / len(ret)) - 1
    Sharpe = np.sqrt(252) * np.mean(ret) / np.std(ret, ddof=1)
    print(f"APR={APR:f} Sharpe={Sharpe:f}")
    maxDD, maxDDD = calculateMaxDD(cumret)
    print(f"maxDD={maxDD:f} maxDDD={maxDDD}")
    plt.show()


if __name__ == "__main__":
    main()
