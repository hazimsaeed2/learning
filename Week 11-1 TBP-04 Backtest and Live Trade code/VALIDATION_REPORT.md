# TBP-04 Validation Report

Lecture: Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie

## Files Reviewed

- `Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie.html`
- `Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie_study.html`
- `Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie.txt`
- `Week 11-1 TBP-04 Backtest and Live Trade code/Week 11-1 TBP-04 Backtest and Live Trade_practice.ipynb`
- `Week 11-1 TBP-04 Backtest and Live Trade code/spy_like_daily.csv`
- `Trading & Back-testing Platforms (TBP)/TBP-04 & 05-Backtest And Live Trade Algo Strategies I & II`

## Additive Changes Made

- Added source inventory, dependency/execution audit, regression metrics, strategy metrics, timeframe controls, and validation controls.
- Added five validation charts with `chart_addendum_*_tbp04_*.png` names.
- Added an addendum notebook and a validated notebook copy. The original notebook remains unchanged.
- Appended marked validation sections to the main HTML page and study guide.

## Source Inventory

| artifact | artifact_type | exists | size_bytes | rows | columns | note |
| --- | --- | --- | --- | --- | --- | --- |
| Week 11-1 TBP-04 Backtest and Live Trade_practice.ipynb | practice_notebook | True | 282507 |  |  | 8 code cells, 16 markdown cells |
| spy_like_daily.csv | source_data | True | 75044 | 962 | 6 | 2017-01-02 through 2020-11-27 |
| chart_1_swing.png | original_chart | True | 88518 |  |  | Existing chart preserved; addendum charts use separate names. |
| IBridgePy-and-Interactive-Brokers-v3.pdf | source_pdf | True | 1440482 | 60 | 180 | 15083 text chars; keyword hits in columns field. |
| TBP-04-05Instructions-and-Key-Takeaways.pdf | source_pdf | True | 125993 | 2 | 39 | 2558 text chars; keyword hits in columns field. |
| TBP04-and-05-Lecture-Summary.pdf | source_pdf | True | 415192 | 7 | 106 | 7115 text chars; keyword hits in columns field. |
| TBP04-05-Assignment.zip | source_zip | True | 38670 | 1 |  | Source ZIP inventoried; archive preserved. |
| TBP04-05-Inclass-Exercises-File.zip | source_zip | True | 1449255 | 30 |  | Source ZIP inventoried; archive preserved. |
| TradeContextEnricher.zip | source_zip | True | 148512 | 5 |  | Source ZIP inventoried; archive preserved. |

## Dependency And Execution

| metric | value | unit | reading |
| --- | --- | --- | --- |
| sklearn_available | no | environment | ModuleNotFoundError |
| original_execution_errors | 1 | errors | ModuleNotFoundError: No module named 'sklearn' |
| original_failure_cell | 8 | cell | Import cell when sklearn is unavailable. |
| fallback_scope | single-feature OLS | validated_copy | Validated notebook injects a minimal LinearRegression fallback only for this teaching notebook. |

## Regression Metrics

| metric | value | unit | reading |
| --- | --- | --- | --- |
| source_rows | 962 | rows | Rows in local daily sample. |
| regression_rows | 960 | rows | After lag/lead return construction. |
| first_date | 2017-01-02 | date | Start date. |
| last_date | 2020-11-27 | date | End date. |
| single_feature_coef | -0.0806509 | coefficient | Negative coefficient indicates weak daily mean reversion. |
| intercept | 0.00059608 | return | OLS intercept. |
| correlation | -0.08065009 | correlation | Very weak predictor/target relationship. |

## Strategy Metrics

| metric | value | unit | reading |
| --- | --- | --- | --- |
| swing_total_pct | -3.4144 | percent | Mean-reversion swing strategy total return. |
| buy_hold_total_pct | 58.3075 | percent | Buy-and-hold over target return window. |
| swing_sharpe | 0.045655 | ratio | Annualized daily Sharpe. |
| buy_hold_sharpe | 0.730134 | ratio | Annualized daily Sharpe. |
| swing_max_drawdown_pct | -29.5094 | percent | Swing strategy drawdown. |
| buy_hold_max_drawdown_pct | -38.4399 | percent | Buy-and-hold drawdown. |
| swing_win_rate_pct | 47.1875 | percent | Positive strategy days. |

## Timeframe Controls

| series | rows | coef | corr | interpretation |
| --- | --- | --- | --- | --- |
| NIFTY daily | 960 | -0.0806509 | -0.08065009 | weak; sign unstable across timeframe |
| NIFTY 2-day | 479 | 0.13538068 | 0.13535959 | weak; sign unstable across timeframe |
| NIFTY weekly | 202 | 0.04808157 | 0.04812845 | weak; sign unstable across timeframe |

## Validation Controls

| control | lecture_application | additive_note |
| --- | --- | --- |
| Original notebook execution | Run TBP-04 practice notebook in temp folder. | Original fails locally because sklearn is unavailable. |
| Validated fallback copy | Permit local execution without installing packages. | Minimal single-feature LinearRegression fallback is injected only in the validated copy. |
| Regression replication | Yesterday-to-today return predicts today-to-tomorrow return. | Coefficient and correlation are both weak. |
| Strategy scorecard | Swing mean-reversion rule. | Swing strategy underperforms buy-and-hold on this sample. |
| Timeframe stability | Daily, 2-day, weekly coefficient comparison. | Sign flips across timeframes, reinforcing thin-edge caution. |
| Live-trading scope | Backtest and live-trade strategy workflow. | No broker connectivity, live orders, commissions, slippage, or production risk checks are validated here. |

## Additive Correction

The original notebook requires `sklearn` and fails locally before execution. The validated copy uses a labelled single-feature OLS fallback to make the workflow executable here. This fallback is for the teaching example only and does not overwrite original values or replace the intended library.

## Notebook Validation

| Notebook | Code cells | Errors | Execution exception |
| --- | ---: | ---: | --- |
| `Week 11-1 TBP-04 Backtest and Live Trade_practice.ipynb` | 8 | 1 | ModuleNotFoundError: No module named 'sklearn' |
| `Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie_resource_addendum_practice.ipynb` | 4 | 0 | None |
| `Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie_validated_practice.ipynb` | 13 | 0 | None |

## HTML Validation

| File | body open/close | html open/close | Generated chart refs | Missing generated charts |
| --- | ---: | ---: | ---: | --- |
| `Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie.html` | 1/1 | 1/1 | 10 | None |
| `Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie_study.html` | 1/1 | 1/1 | 5 | None |

Status: PASS with original dependency gap documented.
