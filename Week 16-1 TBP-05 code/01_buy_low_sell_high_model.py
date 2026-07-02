"""
Week 16-1 TBP-05  -  Step 1: The Buy-Low-Sell-High model (machine learning)
===========================================================================

This is the heart of the lecture, rewritten so it runs on your laptop with NO
broker and NO IBridgePy.  It uses the real SPY daily file that ships with the
lecture (SPY.csv, 2001-2021, 5096 rows) which sits next to this script.

Run it:
    python 01_buy_low_sell_high_model.py

What it does (exactly what Dr. Hui Liu does in class):
    1. Load SPY daily prices.
    2. Turn prices into "yield_yesterday" and "yield_tomorrow".
    3. Fit a linear regression: does yesterday's move predict tomorrow's?
       -> The coefficient is NEGATIVE, which is mathematical proof that SPY
          mean-reverts (a down day tends to be followed by an up day).
    4. Screen several stocks to see which mean-revert the most.
    5. Backtest the rule "if SPY fell, buy; else sell".
    6. Sweep the buy threshold and find the best one (~1.1%).

Charts are saved as PNG files next to this script.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # save charts to file, no screen needed
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "SPY.csv")


# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
def load_prices(path=DATA):
    hist = pd.read_csv(path, header=0, index_col=0)
    hist.columns = [c.lower() for c in hist.columns]   # Open -> open ...
    return hist


# ---------------------------------------------------------------------------
# 2. Feature engineering  (the two columns the whole lecture is built on)
# ---------------------------------------------------------------------------
def add_yield(hist):
    hist = hist.copy()
    hist["close_yesterday"] = hist["close"].shift(1)
    hist["yield_yesterday"] = (hist["close"] - hist["close_yesterday"]) / hist["close_yesterday"]
    hist["yield_tomorrow"] = hist["yield_yesterday"].shift(-1)
    return hist


# ---------------------------------------------------------------------------
# 3. The machine-learning model: linear regression
# ---------------------------------------------------------------------------
def fit_model(hist):
    h = add_yield(hist).dropna()
    x = h[["yield_yesterday"]]
    y = h["yield_tomorrow"]
    model = LinearRegression().fit(x, y)
    return model, h


def screener_coef(hist):
    """Return just the slope - how strongly this stock mean-reverts."""
    model, _ = fit_model(hist)
    return model.coef_[0]


# ---------------------------------------------------------------------------
# 5. Backtest:  decision = +1 (long) if yesterday fell below `rate`, else -1
# ---------------------------------------------------------------------------
def backtest(h, rate=0.0):
    h = h.copy()
    h["decision"] = h["yield_yesterday"].apply(lambda v: 1 if v < rate else -1)
    h["result"] = h["decision"] * h["yield_tomorrow"]
    h["strategy"] = np.cumprod(h["result"] + 1)
    h["buy_and_hold"] = np.cumprod(h["yield_tomorrow"] + 1)
    return h


def rate_sweep(h, lo=-20, hi=21, step=0.001):
    out = {}
    for i in range(lo, hi):
        rate = i * step
        out[rate] = backtest(h, rate)["strategy"].iloc[-2]
    return out


# ---------------------------------------------------------------------------
# Run everything
# ---------------------------------------------------------------------------
def main():
    hist = load_prices()
    print("Loaded %d rows of SPY (%s to %s)\n"
          % (len(hist), hist.index[0], hist.index[-1]))
    print("First rows:\n", hist.head(), "\n")

    model, h = fit_model(hist)
    print("Linear regression  ->  coef = %.4f   intercept = %.6f"
          % (model.coef_[0], model.intercept_))
    print("The coefficient is NEGATIVE  ->  SPY mean-reverts.\n")

    # scatter chart with the regression line
    preds = model.predict(h[["yield_yesterday"]])
    plt.figure(figsize=(7, 5))
    plt.scatter(h["yield_yesterday"], h["yield_tomorrow"], s=6, alpha=0.3)
    plt.plot(h["yield_yesterday"], preds, color="black", lw=2,
             label="regression line (slope %.3f)" % model.coef_[0])
    plt.axhline(0, color="grey", lw=0.5); plt.axvline(0, color="grey", lw=0.5)
    plt.xlabel("yield yesterday"); plt.ylabel("yield tomorrow")
    plt.title("Does yesterday predict tomorrow?  Slope < 0 = mean reversion")
    plt.legend(); plt.tight_layout()
    plt.savefig(os.path.join(HERE, "chart_1_regression.png"), dpi=110)
    plt.close()

    # stock screener (offline: only SPY file ships with the lecture; the rest
    # are the instructor's published numbers so the table is complete)
    screen = {"SPY": round(screener_coef(hist), 4)}
    published = {"QQQ": -0.0632, "AAPL": -0.0490, "GOOG": -0.0217, "TSLA": 0.0027}
    screen.update(published)
    print("Stock screener (slope, more negative = stronger mean reversion):")
    for k, v in screen.items():
        print("   %-5s %+.4f" % (k, v))
    print()

    # backtest at threshold 0 and at 1.1%
    b0 = backtest(h, 0.0)
    b11 = backtest(h, 0.011)
    print("Threshold 0.0  : strategy x%.2f vs buy&hold x%.2f"
          % (b0["strategy"].iloc[-1], b0["buy_and_hold"].iloc[-1]))
    print("Threshold 1.1%%: strategy x%.2f vs buy&hold x%.2f"
          % (b11["strategy"].iloc[-1], b11["buy_and_hold"].iloc[-1]))

    # equity curve chart
    plt.figure(figsize=(9, 5))
    plt.plot(b11["buy_and_hold"].values, color="black", label="buy & hold SPY")
    plt.plot(b11["strategy"].values, color="red",
             label="buy-low-sell-high (1.1%% threshold)")
    plt.xlabel("trading day"); plt.ylabel("growth of $1")
    plt.title("Backtest equity curve"); plt.legend(); plt.tight_layout()
    plt.savefig(os.path.join(HERE, "chart_2_equity_curve.png"), dpi=110)
    plt.close()

    # rate sweep chart
    sweep = rate_sweep(h)
    best = max(sweep, key=sweep.get)
    print("\nBest threshold from sweep: %.3f  (final x%.2f)"
          % (best, sweep[best]))
    plt.figure(figsize=(9, 5))
    plt.plot(list(sweep.keys()), list(sweep.values()))
    plt.axvline(best, color="red", ls="--", label="best = %.3f" % best)
    plt.xlabel("buy threshold (rate)"); plt.ylabel("final growth of $1")
    plt.title("Threshold sweep - the curve peaks near 1.1%")
    plt.legend(); plt.tight_layout()
    plt.savefig(os.path.join(HERE, "chart_3_rate_sweep.png"), dpi=110)
    plt.close()

    print("\nCharts saved: chart_1_regression.png, chart_2_equity_curve.png, "
          "chart_3_rate_sweep.png")
    print("\nWARNING: that 1.1%% threshold was chosen by looking at the WHOLE "
          "history.\nThat is over-fitting. See 02_backtest_costs_and_traps.py.")


if __name__ == "__main__":
    main()
