# Week 16-1 (TBP-05) — Lecture Code Folder

**Everything for this lecture's code lives in this one folder** — the practice notebook,
the data file it needs, two runnable scripts, and the original live-trading strategies.
Packaged so you can run it on your own laptop with **no broker, no IBridgePy, no errors**.

The real lecture data ships here too: `SPY.csv` = SPY daily prices, 2001-2021 (5096 rows).

---

## Start here — the notebook

| File | What it is |
|---|---|
| `..._practice.ipynb` | **The main thing.** Open it and run it cell by cell. Every code cell has a plain-English markdown cell above it. It builds three models/strategies (linear-regression Buy-Low-Sell-High, a MACD version, and a Moving-Average Crossover) plus the two backtest traps, and then **Part 4 turns every live-trading `.py` robot in `reference_ibridgepy_strategies/` into a runnable offline backtest** (Buy-Low-Sell-High robot, the MA(5)/MA(60) crossover family, and the VIX strategy) — so you see the real robot code *and* its output curve. All on the real `SPY.csv`, with charts and tables inline. To use a different stock, change one line in the config cell. |

Open it in VS Code or Jupyter; it uses `SPY.csv` from this folder automatically. The notebook
is the single place that holds **all** of this lecture's code — the two scripts below and the
reference robots are reproduced inside it as runnable, executed sections.

---

## Also runnable as plain scripts

You need Python with: `pandas numpy matplotlib scikit-learn`

```
pip install pandas numpy matplotlib scikit-learn
```

Then, from inside this folder:

| Command | What it does |
|---|---|
| `python 01_buy_low_sell_high_model.py` | The full lecture model: builds the yield columns, fits the linear regression (coef = **−0.10**, proving SPY mean-reverts), screens 5 stocks, backtests "buy if it fell", and sweeps the threshold (best ≈ **1.1%**). Saves 3 charts. |
| `python 02_backtest_costs_and_traps.py` | Shows why that great backtest is a lie: transaction costs wipe a daily strategy out, and an honest train/test split kills the 1.1% edge. Saves 2 charts. |

Charts are written next to the scripts as `chart_1_regression.png` … `chart_5_out_of_sample.png`.

### Verified numbers (from this exact `SPY.csv`)
- Linear regression slope = **−0.1012** (negative ⇒ mean reversion)
- Threshold 0%: strategy ×5.24 vs buy & hold ×4.53
- Threshold 1.1%: strategy ×19.03 vs buy & hold ×4.53
- Best threshold from the full-history sweep = **0.011 (1.1%)** — exactly the instructor's number
- With realistic transaction cost the daily strategy turns **negative**

---

## What is REFERENCE only (`reference_ibridgepy_strategies/`)

These are the **exact live-trading strategy files from the lecture**. They are written for
**IBridgePy + Interactive Brokers**, so they call functions like `order_target_percent()`,
`schedule_function()`, `request_historical_data()` that only exist when IBridgePy is
installed and connected to a broker. They **will not run standalone** — they are here so you
can read precisely how the ideas become a real trading robot.

| File | Idea it teaches |
|---|---|
| `demo_buy_low_sell_high.py` | The buy-low-sell-high rule as a live robot: decide at 15:59 ET each day. |
| `moving_average_crossover_1_basic.py` | MA(5) vs MA(60) crossover, the classic starter strategy. |
| `moving_average_crossover_2_trading_day.py` | Adds a holiday / trading-day check. |
| `moving_average_crossover_early_close.py` | Handles half-days (1 PM early close). |
| `moving_average_crossover_email.py` | Emails your account balance after the close. |
| `moving_average_crossover_handle_error.py` | Wraps orders in try/except so one error doesn't crash the robot. |
| `moving_average_crossover_minute_bar.py` | Same idea but checks every minute instead of once a day. |
| `example_VIX_predicts_returns.py` | A second strategy from an academic paper: trade SPY using VIX percentiles. |

The five MA-crossover files are the lecture's "from a toy to a real robot" progression —
each one adds the **one** thing live trading needs that a backtest never told you about
(holidays, early closes, notifications, error handling, higher frequency).

---

## How the pieces fit the lecture

1. **Idea** → buy SPY when it dropped, sell when it rose (mean reversion).
2. **Data** → `SPY.csv`.
3. **Model** → `01_...py` linear regression proves the idea has signal.
4. **Backtest** → `01_...py` rate sweep; `02_...py` the honest version.
5. **Robot** → `reference_ibridgepy_strategies/` turns the rule into live IBridgePy code.
6. **Go live** → run the robot on a paper account first, then real money.
