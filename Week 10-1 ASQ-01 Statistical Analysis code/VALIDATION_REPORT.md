# ASQ-01 Validation Report

Lecture: Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data

## Files Reviewed

- `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data.html`
- `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data_study.html`
- `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data.txt`
- `Week 10-1 ASQ-01 Statistical Analysis code/Week 10-1 ASQ-01 Statistical Analysis_practice.ipynb`
- `Week 10-1 ASQ-01 Statistical Analysis code/market_data.csv`

## Additive Changes Made

- Added dependency/execution audit, source inventory, MA/weekly metrics, ACF/stationarity checks, rolling AR fallback metrics, and validation controls.
- Added five validation charts with `chart_addendum_*_asq01_*.png` names.
- Added an addendum notebook and a validated notebook copy. The original notebook remains unchanged.
- Appended marked validation sections to the main HTML page and study guide.

## Source Inventory

| artifact | artifact_type | exists | size_bytes | rows | columns | note |
| --- | --- | --- | --- | --- | --- | --- |
| Week 10-1 ASQ-01 Statistical Analysis_practice.ipynb | practice_notebook | True | 615942 |  |  | 13 code cells, 17 markdown cells |
| market_data.csv | source_data | True | 75044 | 962 | 6 | 2017-01-02 through 2020-11-27 |
| chart_1_arima.png | original_chart | True | 132549 |  |  | Existing chart preserved; addendum charts use separate names. |

## Dependency And Execution

| metric | value | unit | reading |
| --- | --- | --- | --- |
| statsmodels_available | no | environment | ModuleNotFoundError |
| original_execution_errors | 1 | errors | ModuleNotFoundError: No module named 'statsmodels' |
| original_failure_cell | 2 | cell | First import cell when statsmodels is unavailable. |
| fallback_scope | educational | validated_copy | Validated notebook injects AR(1), ADF-like, ACF/PACF plotting fallbacks only for local execution. |

## MA And Weekly Metrics

| metric | value | unit | reading |
| --- | --- | --- | --- |
| daily_rows_after_returns | 961 | rows | Daily OHLCV after pct_change dropna. |
| daily_first_date | 2017-01-03 | date | Start date after first return. |
| daily_last_date | 2020-11-27 | date | End date. |
| ma_rows | 932 | rows | After 10/30 rolling windows and shifted signal. |
| ma_10_30_total_pct | 26.0441 | percent | Moving-average crossover total return. |
| ma_window_buy_hold_pct | 47.2899 | percent | Buy-and-hold over the same MA window. |
| weekly_observations | 203 | weeks | Weekly OHLC after resample and return dropna. |

## ACF And Stationarity Checks

| check | value | unit | reading |
| --- | --- | --- | --- |
| weekly_band | 0.137565 | correlation | Approximate +/-1.96/sqrt(N) band. |
| weekly_acf_lags_1_5 | [0.0481, 0.1412, 0.0986, -0.1823, 0.0902] | correlations | Autocorrelation of weekly returns. |
| weekly_pacf_lags_1_5 | [0.0481, 0.1392, 0.0889, -0.219, 0.0896] | correlations | OLS fallback partial autocorrelation. |
| acf_lags_outside_band | 2 | lags | Weekly return lags outside the simple band. |
| adf_like_weekly_price_stat | -1.8302 | stat | Fallback ADF-style regression statistic, not statsmodels. |
| adf_like_weekly_price_p | 0.2 | rough_p | Heuristic p bucket; use statsmodels for formal inference. |
| adf_like_weekly_return_stat | -13.4909 | stat | Fallback ADF-style regression statistic, not statsmodels. |
| adf_like_weekly_return_p | 0.01 | rough_p | Heuristic p bucket; use statsmodels for formal inference. |

## Rolling AR Metrics

| metric | value | unit | reading |
| --- | --- | --- | --- |
| rolling_window | 100 | weeks | Training window for AR(1) fallback. |
| forecast_rows | 103 | weeks | Rows after rolling window and signal dropna. |
| long_weeks | 90 | weeks | Positive forecast sign. |
| short_weeks | 13 | weeks | Negative forecast sign. |
| fallback_mean_phi | 0.020915 | coefficient | Mean rolling AR(1) coefficient in fallback OLS. |
| fallback_ar1_total_pct | -15.6365 | percent | Fallback OLS AR(1) strategy total return. |
| buy_hold_total_pct | 21.2765 | percent | Buy-and-hold over same rolling forecast window. |
| fallback_ar1_sharpe | -0.277101 | ratio | Annualized weekly Sharpe. |
| buy_hold_sharpe | 0.552195 | ratio | Annualized weekly Sharpe. |
| fallback_ar1_max_drawdown_pct | -30.9372 | percent | Strategy drawdown. |
| buy_hold_max_drawdown_pct | -34.5566 | percent | Buy-and-hold drawdown. |
| fallback_ar1_win_rate_pct | 55.3398 | percent | Positive strategy weeks. |

## Validation Controls

| control | lecture_application | additive_note |
| --- | --- | --- |
| Original notebook execution | Run ASQ-01 practice notebook in a temp folder. | Original fails locally because statsmodels is unavailable. |
| Validated fallback copy | Permit local execution without installing packages. | Fallback covers only AR(1), ADF-like, ACF/PACF plotting for this notebook. |
| MA crossover replication | Daily 10/30 moving-average rule. | MA and buy-and-hold returns match the study-guide scale. |
| Stationarity scope | ADF test interpretation. | Fallback ADF-like p values are heuristic; formal inference needs statsmodels. |
| Rolling AR caution | Dynamic AR(1) weekly forecast. | Fallback OLS AR(1) differs from statsmodels ARIMA exact output; direction of underperformance remains. |
| Additive-only correction | Preserve original values. | Original study values remain; addendum records local fallback metrics separately. |

## Additive Correction

The original notebook requires `statsmodels` and fails locally before execution. The validated copy uses a labelled fallback to make the workflow executable here. Formal ARIMA and ADF inference still require `statsmodels`; the fallback metrics are recorded separately and do not overwrite original study values.

## Notebook Validation

| Notebook | Code cells | Errors | Execution exception |
| --- | ---: | ---: | --- |
| `Week 10-1 ASQ-01 Statistical Analysis_practice.ipynb` | 13 | 1 | ModuleNotFoundError: No module named 'statsmodels' |
| `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data_resource_addendum_practice.ipynb` | 4 | 0 | None |
| `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data_validated_practice.ipynb` | 18 | 0 | None |

## HTML Validation

| File | body open/close | html open/close | Generated chart refs | Missing generated charts |
| --- | ---: | ---: | ---: | --- |
| `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data.html` | 1/1 | 1/1 | 10 | None |
| `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data_study.html` | 1/1 | 1/1 | 5 | None |

Status: PASS with original dependency gap documented.
