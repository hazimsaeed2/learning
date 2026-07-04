"""
Python implementation of CL_rev.

Crude oil (CL) futures: combination of momentum and short-term reversal
strategy. Compares the combo (AND), pure momentum, pure reversal, and
combo (OR) cumulative-return curves.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

from fwdshift import backshift


def main():
    lookback1 = 30
    lookback2 = 40

    md = loadmat("inputDataOHLCDaily_20120504.mat")
    syms = [s[0] for s in md["syms"].flatten()]
    tday_all = md["tday"]
    cl_all = md["cl"]

    idx = syms.index("CL")
    cl = cl_all[:, idx].astype(float)
    tday = tday_all[:, idx].astype(int)

    dates = pd.to_datetime(tday.astype(str), format="%Y%m%d")

    # Combo (AND): mean reversion at lookback1 AND momentum at lookback2
    longs = (cl < backshift(lookback1, cl)) & (cl > backshift(lookback2, cl))
    shorts = (cl > backshift(lookback1, cl)) & (cl < backshift(lookback2, cl))

    def positions_to_ret(longs, shorts):
        positions = np.zeros_like(cl)
        positions[longs] = 1
        positions[shorts] = -1
        ret = backshift(1, positions) * (cl - backshift(1, cl)) / backshift(1, cl)
        ret[np.isnan(ret)] = 0
        return ret

    ret = positions_to_ret(longs, shorts)
    cumret = np.cumprod(1 + ret) - 1

    plt.plot(dates, cumret, "r", label="ComboAND")
    APR = np.prod(1 + ret) ** (252 / len(ret)) - 1
    Sharpe = np.sqrt(252) * np.mean(ret) / np.std(ret, ddof=1)
    print(f"APR={APR:.6f} Sharpe={Sharpe:.6f}")
    # APR=0.117600 Sharpe=1.100368

    # Momentum only
    longs = cl > backshift(lookback2, cl)
    shorts = cl < backshift(lookback2, cl)
    ret = positions_to_ret(longs, shorts)
    cumret = np.cumprod(1 + ret) - 1
    plt.plot(dates, cumret, "g", label="Momentum")

    # Reversal only
    longs = cl < backshift(lookback1, cl)
    shorts = cl > backshift(lookback1, cl)
    ret = positions_to_ret(longs, shorts)
    cumret = np.cumprod(1 + ret) - 1
    plt.plot(dates, cumret, "k", label="Reversal")

    # Combo (OR)
    longs = (cl < backshift(lookback1, cl)) | (cl > backshift(lookback2, cl))
    shorts = (cl > backshift(lookback1, cl)) | (cl < backshift(lookback2, cl))
    positionsL = np.zeros_like(cl)
    positionsS = np.zeros_like(cl)
    positionsL[longs] = 1
    positionsS[shorts] = -1
    positions = positionsL + positionsS
    ret = backshift(1, positions) * (cl - backshift(1, cl)) / backshift(1, cl)
    ret[np.isnan(ret)] = 0
    cumret = np.cumprod(1 + ret) - 1
    plt.plot(cumret, "c", label="ComboOR")

    plt.legend()
    plt.title("CL: ComboAND / Momentum / Reversal / ComboOR")
    plt.show()


if __name__ == "__main__":
    main()
