"""
Python implementation of VX_ES_rollreturn_testset.

Out-of-sample (testset) run of the VX vs ES roll-return strategy on
data from 2012-05-08 through 2015-08-28. Reports CAGR, Sharpe, max DD
and Calmar ratio. Note: roll-return sign convention is flipped vs the
training-set script (contango = short VX), reflecting the corrected
implementation in Ernie Chan's later edition.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import loadmat

from fwdshift import backshift, fwdshift
from smartsum import smartsum
from _utils import calculateMaxDD, intersect_with_index


def main():
    entryThreshold = 0.1
    onewaytcost = 0 / 10000

    vx_md = loadmat("inputDataDaily_VX_20150828.mat")
    tday = vx_md["tday"].flatten().astype(int)
    contracts = [c[0] for c in vx_md["contracts"].flatten()]
    VX = vx_md["cl"].astype(float) / 1000.0 # prices multiplied by 1000 in input file

    # Spot VIX is stored as contract '0000$'
    vix_idx = contracts.index("0000$")
    VIX = VX[:, vix_idx].copy()
    VX = np.delete(VX, vix_idx, axis=1)
    del contracts[vix_idx]

    es_md = loadmat("inputDataDaily_ES_20150828.mat")
    ES = es_md["cl"].astype(float).flatten()
    tday_ES = es_md["tday"].flatten().astype(int)

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
        # NOTE: sign convention (+) here matches the corrected testset
        dailyRoll = (VX[idx, c] - VIX[idx]) / dte

        positions[idx[dailyRoll > entryThreshold], c] = -1 * 0.35
        positions[idx[dailyRoll > entryThreshold], -1] = -1
        positions[idx[dailyRoll < -entryThreshold], c] = 1 * 0.35
        positions[idx[dailyRoll < -entryThreshold], -1] = 1

        endIdx_prev = endIdx

    y = np.column_stack([VX * 1000, ES * 50])

    pos_shifted = backshift(1, positions)
    y_shifted = backshift(1, y)
    denom = smartsum(np.abs(backshift(1, positions * y)), dim=2)
    ret = smartsum(pos_shifted * (y - y_shifted), dim=2) / denom \
        - onewaytcost * smartsum(np.abs(positions * y - backshift(1, positions * y)), dim=2) / denom
    ret = np.where(np.isnan(ret), 0, ret)

    # Restrict to testset window (post training cut-off)
    mask = tday > 20120507
    ret = ret[mask]
    tday = tday[mask]

    cumret = np.cumprod(1 + ret) - 1
    dates = pd.to_datetime(tday.astype(str), format="%Y%m%d")
    plt.plot(dates, cumret)
    plt.title("VX vs ES (testset only)")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns")

    cagr = np.prod(1 + ret) ** (252 / len(ret)) - 1
    sharpe = np.sqrt(252) * np.mean(ret) / np.std(ret, ddof=1)
    print(f"CAGR={cagr:f} Sharpe={sharpe:f}")
    maxDD, maxDDD = calculateMaxDD(cumret)
    print(f"maxDD={maxDD:f} maxDDD={maxDDD} Calmar ratio={-cagr/maxDD:f}")
    plt.show()


if __name__ == "__main__":
    main()
