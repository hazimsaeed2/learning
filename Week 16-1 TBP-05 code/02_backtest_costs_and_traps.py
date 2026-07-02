"""
Week 16-1 TBP-05  -  Step 2: Why a great backtest can be a lie
==============================================================

Step 1 found a strategy that turned $1 into ~$19. This script shows the two
traps that destroy strategies like that in real life:

    TRAP 1 - Transaction costs. Every buy/sell pays the spread + commission.
             This strategy trades almost every day, so even a tiny cost
             compounds into a disaster.

    TRAP 2 - Over-fitting. We picked the 1.1% threshold by looking at the
             whole history. A fair test is: tune on the FIRST half, then
             trade the SECOND half you never looked at.

Run it:
    python 02_backtest_costs_and_traps.py
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "SPY.csv")


def load():
    h = pd.read_csv(DATA, header=0, index_col=0)
    h.columns = [c.lower() for c in h.columns]
    h["close_yesterday"] = h["close"].shift(1)
    h["yield_yesterday"] = (h["close"] - h["close_yesterday"]) / h["close_yesterday"]
    h["yield_tomorrow"] = h["yield_yesterday"].shift(-1)
    return h.dropna()


def backtest_with_cost(h, rate=0.011, cost=0.0):
    """cost = fraction charged each time the position flips (e.g. 0.001 = 0.1%)."""
    h = h.copy()
    h["decision"] = h["yield_yesterday"].apply(lambda v: 1 if v < rate else -1)
    flips = h["decision"].diff().abs() / 2.0        # 1 when long<->short flips
    flips = flips.fillna(0)
    h["result"] = h["decision"] * h["yield_tomorrow"] - flips * cost
    h["strategy"] = np.cumprod(h["result"] + 1)
    return h


def performance(equity):
    """Total return, CAGR, Sharpe and worst drawdown from an equity curve."""
    rets = equity.pct_change().dropna()
    years = len(equity) / 252.0
    total = equity.iloc[-1] / equity.iloc[0] - 1
    cagr = (equity.iloc[-1] / equity.iloc[0]) ** (1 / years) - 1
    sharpe = np.sqrt(252) * rets.mean() / rets.std()
    drawdown = (equity / equity.cummax() - 1).min()
    return dict(total=total, cagr=cagr, sharpe=sharpe, max_dd=drawdown)


def main():
    h = load()

    # --- TRAP 1: transaction costs -----------------------------------------
    print("TRAP 1 - transaction costs (threshold fixed at 1.1%)")
    costs = [0.0, 0.0005, 0.0010, 0.0050]
    finals = []
    for c in costs:
        eq = backtest_with_cost(h, 0.011, c)["strategy"]
        finals.append(eq.iloc[-1])
        print("   cost %.2f%% -> final x%.2f  (total return %+.1f%%)"
              % (c * 100, eq.iloc[-1], (eq.iloc[-1] - 1) * 100))

    plt.figure(figsize=(8, 5))
    plt.bar([f"{c*100:.2f}%" for c in costs], finals, color="#c0392b")
    plt.axhline(1, color="black", lw=0.8)
    plt.ylabel("final growth of $1"); plt.xlabel("transaction cost per flip")
    plt.title("A tiny cost wipes out a daily strategy")
    plt.tight_layout()
    plt.savefig(os.path.join(HERE, "chart_4_cost_impact.png"), dpi=110)
    plt.close()

    # --- TRAP 2: out-of-sample test ----------------------------------------
    print("\nTRAP 2 - honest split: tune on first half, trade second half")
    half = len(h) // 2
    train, test = h.iloc[:half], h.iloc[half:]

    best_rate, best_val = None, -1
    for i in range(-20, 21):
        r = i * 0.001
        val = backtest_with_cost(train, r, 0.0)["strategy"].iloc[-1]
        if val > best_val:
            best_val, best_rate = val, r
    print("   best threshold on TRAIN half: %.3f" % best_rate)

    test_eq = backtest_with_cost(test, best_rate, 0.0)["strategy"]
    bh = np.cumprod(test["yield_tomorrow"] + 1)
    print("   that threshold on the unseen TEST half: strategy x%.2f vs buy&hold x%.2f"
          % (test_eq.iloc[-1], bh.iloc[-1]))

    perf = performance(test_eq)
    print("   out-of-sample: total %+.1f%%  CAGR %+.1f%%  Sharpe %.2f  maxDD %.1f%%"
          % (perf["total"] * 100, perf["cagr"] * 100, perf["sharpe"], perf["max_dd"] * 100))

    plt.figure(figsize=(9, 5))
    plt.plot(bh.values, color="black", label="buy & hold (test half)")
    plt.plot(test_eq.values, color="red", label="strategy (tuned on train half)")
    plt.xlabel("trading day (second half only)"); plt.ylabel("growth of $1")
    plt.title("Out-of-sample: the honest test")
    plt.legend(); plt.tight_layout()
    plt.savefig(os.path.join(HERE, "chart_5_out_of_sample.png"), dpi=110)
    plt.close()

    print("\nCharts saved: chart_4_cost_impact.png, chart_5_out_of_sample.png")


if __name__ == "__main__":
    main()
