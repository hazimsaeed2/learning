"""
Python implementation of XLE_CL_rollReturn2.

Variant of XLE_CL_rollReturn.py that determines the front contract
dynamically on each day (first column where today is finite and the
previous column is not). Otherwise identical: contango/backwardation
regime trade on USO and XLE.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

from fwdshift import fwdshift, backshift
from smartsum import smartsum
from smartmean2 import smartmean
from _utils import calculateMaxDD, intersect_with_index


def main():
    etf_md = loadmat("inputData_ETF.mat")
    syms = [s[0] for s in etf_md["syms"].flatten()]
    tday_ETF = etf_md["tday"].flatten().astype(int)
    cl_ETF = etf_md["cl"].astype(float)

    uso = cl_ETF[:, syms.index("USO")]
    xle = cl_ETF[:, syms.index("XLE")]

    cl_md = loadmat("inputDataDaily_CL_20120502.mat")
    tday = cl_md["tday"].flatten().astype(int)
    contracts = [c[0] for c in cl_md["contracts"].flatten()]
    cl = cl_md["cl"].astype(float)

    ratioMatrix = (fwdshift(1, cl.T) / cl.T).T
    ratio = np.full(ratioMatrix.shape[0], np.nan)

    for t in range(cl.shape[0]):
        # ~isfinite(cl(t, 1:end-1)) & isfinite(cl(t, 2:end)) ; +1
        not_finite_prev = ~np.isfinite(cl[t, :-1])
        finite_next = np.isfinite(cl[t, 1:])
        fronts = np.where(not_finite_prev & finite_next)[0] + 1 # +1 -> column of "back"
        if len(fronts):
            front = fronts[0]
            ratio[t] = ratioMatrix[t, front]

    tday_c, iA, iB = intersect_with_index(tday_ETF, tday)
    uso = uso[iA]
    xle = xle[iA]
    ratio = ratio[iB]

    positions = np.zeros((len(tday_c), 2))
    contango = ratio > 1
    backwardation = ratio < 1
    positions[contango, :] = [-1, 1]
    positions[backwardation, :] = [1, -1]

    prices = np.column_stack([uso, xle])
    ret = smartsum(backshift(1, positions) * (prices - backshift(1, prices)) / backshift(1, prices),
                   dim=2) / 2
    ret = np.where(np.isnan(ret), 0, ret)

    cumret = np.cumprod(1 + ret) - 1
    plt.plot(cumret)
    plt.title("USO/XLE roll-return (dynamic front)")

    print(f"Avg Ann Ret={252*smartmean(ret):7.4f} "
          f"Sharpe ratio={np.sqrt(252)*smartmean(ret)/np.nanstd(ret, ddof=1):4.2f}")
    print(f"APR={np.prod(1+ret)**(252/len(ret))-1:10.4f}")
    maxDD, maxDDD = calculateMaxDD(cumret)
    print(f"Max DD ={maxDD:f} Max DDD in days={maxDDD}")
    plt.show()


if __name__ == "__main__":
    main()
