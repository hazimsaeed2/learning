# TBP-05 Validation Addendum

Lecture: Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms

This file is additive. It does not replace the existing `README.md`, existing scripts, existing notebook, or existing charts.

## Local Dependency Corrections

- `sklearn` is not installed locally, so the original notebook and `01_buy_low_sell_high_model.py` fail in this environment.
- The validated notebook adds a NumPy-backed `LinearRegression` fallback and a plain-Python `display()` fallback.
- `tbp05_sklearn_free_model_validation.py` gives a standalone sklearn-free validation path.
- The IBridgePy robots remain reference-only unless run inside IBridgePy with Interactive Brokers connectivity.
