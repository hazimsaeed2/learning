"""
Python implementation of VX_ES.

Simple scatter of VIX-futures (VX) vs S&P E-mini (ES) and an OLS hedge-
ratio regression on the post-2008-08-01 window. Useful for spotting the
linear sensitivity between volatility and equity returns.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

from _utils import intersect_with_index


def main():
    md = loadmat("inputDataOHLCDaily_20120517.mat")
    syms = [s[0] for s in md["syms"].flatten()]
    cl = md["cl"]
    tday = md["tday"]

    idxV = syms.index("VX")
    idxE = syms.index("ES")

    VX = cl[:, idxV].astype(float)
    tdayV = tday[:, idxV].astype(int)

    ES = cl[:, idxE].astype(float)
    tdayE = tday[:, idxE].astype(int)

    tday_c, iV, iE = intersect_with_index(tdayV, tdayE)
    VX = VX[iV]
    ES = ES[iE]

    plt.scatter(VX, ES)
    plt.xlabel("VX")
    plt.ylabel("ES")

    post = tday_c >= 20080801
    # regress(y, [x ones]) — least-squares, returns [slope, intercept]
    X = np.column_stack([1000 * VX[post], np.ones(post.sum())])
    y = 50 * ES[post]
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    print(f"hedgeRatio={beta[0]:f} intercept={beta[1]:f}")
    plt.show()


if __name__ == "__main__":
    main()
