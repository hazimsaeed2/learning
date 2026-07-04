"""
Python implementation of GLD_GC.

Long GLD (ETF) vs short GC (gold futures) daily-return spread. Computes
average annualised return, Sharpe ratio, APR and max-drawdown stats.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

from fwdshift import backshift
from _utils import calculateMaxDD, intersect_with_index


def main():
    gc_md = loadmat("inputData_GC_1600_20100802.mat")
    gld_md = loadmat("inputData_ETF.mat")

    gc_tday = gc_md["tday"].flatten().astype(int)
    gc_cl = gc_md["cl"].flatten().astype(float)

    gld_syms = [s[0] for s in gld_md["syms"].flatten()]
    gld_cl_all = gld_md["cl"]
    gld_tday = gld_md["tday"].flatten().astype(int)

    gld_idx = gld_syms.index("GLD")
    gld_cl = gld_cl_all[:, gld_idx].astype(float)

    tday, idx1, idx2 = intersect_with_index(gc_tday, gld_tday)
    gc_cl = gc_cl[idx1]
    gld_cl = gld_cl[idx2]

    ret = (gld_cl - backshift(1, gld_cl)) / backshift(1, gld_cl) \
        - (gc_cl - backshift(1, gc_cl)) / backshift(1, gc_cl)
    ret[np.isnan(ret)] = 0

    cumret = np.cumprod(1 + ret) - 1
    plt.plot(cumret)

    riskFreeRate = 0.02 / 252
    avgAnnRet = 252 * np.nanmean(ret)
    sharpe = np.sqrt(252) * np.nanmean(ret - riskFreeRate) / np.nanstd(ret - riskFreeRate, ddof=1)
    print(f"Avg Ann Ret={avgAnnRet:7.4f} Sharpe ratio={sharpe:4.2f}")
    APR = np.prod(1 + ret) ** (252 / len(ret)) - 1
    print(f"APR={APR:10.4f}")
    maxDD, maxDDD = calculateMaxDD(cumret)
    print(f"Max DD ={maxDD:f} Max DDD in days={maxDDD}")
    plt.title("GLD - GC spread cumulative returns")
    plt.show()


if __name__ == "__main__":
    main()
