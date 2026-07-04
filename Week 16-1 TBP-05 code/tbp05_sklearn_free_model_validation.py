"""
Sklearn-free validation companion for TBP-05.

This additive script does not replace the original lecture scripts. It computes
the same core Buy-Low-Sell-High regression and backtest metrics using NumPy
least squares, so it runs in environments where scikit-learn is unavailable.
"""

from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "SPY.csv"

def add_yield(hist):
    hist = hist.copy()
    hist["close_yesterday"] = hist["close"].shift(1)
    hist["yield_yesterday"] = (hist["close"] - hist["close_yesterday"]) / hist["close_yesterday"]
    hist["yield_tomorrow"] = hist["yield_yesterday"].shift(-1)
    return hist.dropna()

def fit_ols(x, y):
    X = np.column_stack([np.asarray(x, dtype=float).reshape(-1), np.ones(len(y))])
    beta, *_ = np.linalg.lstsq(X, np.asarray(y, dtype=float), rcond=None)
    return beta[0], beta[1]

def backtest(h, rate=0.0):
    b = h.copy()
    b["decision"] = np.where(b["yield_yesterday"] < rate, 1, -1)
    b["result"] = b["decision"] * b["yield_tomorrow"]
    b["strategy"] = np.cumprod(b["result"] + 1)
    b["buy_and_hold"] = np.cumprod(b["yield_tomorrow"] + 1)
    return b

def main():
    hist = pd.read_csv(DATA, header=0, index_col=0)
    hist.columns = [c.lower() for c in hist.columns]
    h = add_yield(hist)
    slope, intercept = fit_ols(h["yield_yesterday"], h["yield_tomorrow"])
    sweep = {round(i * 0.001, 3): backtest(h, i * 0.001)["strategy"].iloc[-2] for i in range(-20, 21)}
    best = max(sweep, key=sweep.get)
    out = pd.DataFrame(
        [
            {"metric": "rows", "value": len(hist)},
            {"metric": "ols_slope", "value": round(float(slope), 6)},
            {"metric": "ols_intercept", "value": round(float(intercept), 8)},
            {"metric": "best_threshold", "value": best},
            {"metric": "best_threshold_final", "value": round(float(sweep[best]), 4)},
        ]
    )
    print(out.to_string(index=False))
    out.to_csv(HERE / "tbp05_sklearn_free_model_validation_output.csv", index=False)

if __name__ == "__main__":
    main()
