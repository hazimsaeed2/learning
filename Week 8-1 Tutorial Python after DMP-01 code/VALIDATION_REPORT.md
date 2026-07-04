# DMP-01 Tutorial Validation Report

Lecture: Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01

## Files Reviewed

- `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01.html`
- `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01_study.html`
- `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01.txt`
- `Week 8-1 Tutorial Python after DMP-01 code/Week 8-1 Tutorial Doubt-Solving Python after DMP-01_practice.ipynb`
- `Week 8-1 Tutorial Python after DMP-01 code/nifty50_daily.csv`

## Additive Changes Made

- Added CSV audits for HTML/source inventory, original notebook execution, CSV round-trip, timezone conversion, vectorization checks, crossover metrics, and validation controls.
- Added five validation charts with `chart_addendum_*_dmp01_tutorial_*.png` names.
- Added an addendum notebook and a validated copy of the notebook with the original cells preserved plus validation cells appended.
- Appended marked validation sections to the main HTML page and study guide. Existing content remains in place.

## Source Inventory

| artifact | artifact_type | exists | size_bytes | rows | columns | note |
| --- | --- | --- | --- | --- | --- | --- |
| Week 8-1 Tutorial Doubt-Solving Python after DMP-01_practice.ipynb | practice_notebook | True | 20651 |  |  | 11 code cells, 16 markdown cells |
| nifty50_daily.csv | source_data | True | 75044 | 962 | 6 | 2017-01-02 through 2020-11-27 |
| chart_1_crossover.png | original_chart | True | 104528 |  |  | Existing chart preserved; addendum charts use separate names. |

## Notebook Metrics

| metric | value | unit | reading |
| --- | --- | --- | --- |
| total_cells | 27 | cells | Original notebook cell count. |
| code_cells | 11 | cells | Code cells executed in isolated temp folder. |
| markdown_cells | 16 | cells | Narrative cells preserved in original notebook. |
| original_execution_errors | 0 | errors | PASS |
| uses_live_download | True | bool | The shipped notebook uses the local CSV, so validation is offline. |
| uses_zoneinfo | True | bool | Stdlib timezone support is used; no pytz dependency is needed for this notebook. |
| original_bh_return_pct | 40.3893 | percent | Buy-and-hold result printed by original notebook. |
| original_strategy_return_pct | 68.0406 | percent | SMA21/LMA63 crossover result printed by original notebook. |

## CSV, Timezone, And Vectorization Checks

| check | value | expected | note |
| --- | --- | --- | --- |
| plain_read_index | RangeIndex | RangeIndex | Plain pd.read_csv leaves Date as a normal column. |
| plain_read_shape | 962x6 | 962x6 | Includes Date plus OHLCV columns. |
| clean_read_index | DatetimeIndex | DatetimeIndex | index_col='Date' and parse_dates=True make it time-series-ready. |
| clean_read_shape | 962x5 | 962x5 | Date is the index, not a data column. |
| roundtrip_same_shape | True | True | CSV save/reload preserves rows and columns when read with date parsing. |
| available_timezones | 597 | near 600 | Local stdlib zoneinfo count; tutorial wording is directionally correct. |
| utc_sample_times | 09:30, 09:35, 09:40 | 09:30, 09:35, 09:40 | UTC sample intraday timestamps. |
| ist_sample_times | 15:00, 15:05, 15:10 | 15:00, 15:05, 15:10 | UTC converted to Asia/Kolkata. |

| check | value | expected | note |
| --- | --- | --- | --- |
| list_times_3_result | [1, 2, 11, 5, 8, 1, 2, 11, 5, 8, 1, 2, 11, 5, 8] | list repetition | Python list multiplication repeats elements. |
| list_times_3_length | 15 | 15 | Five source elements repeated three times. |
| array_times_3_result | [3, 6, 33, 15, 24] | [3, 6, 33, 15, 24] | Numpy array multiplication is elementwise. |
| loop_times_3_result | [3, 6, 33, 15, 24] | [3, 6, 33, 15, 24] | Iterated/event-driven style gives the same arithmetic result. |

## Crossover Metrics

| metric | value | unit | reading |
| --- | --- | --- | --- |
| source_rows | 962 | rows | Rows in shipped NIFTY-50 CSV. |
| source_columns_after_date_index | 5 | columns | OHLCV columns after Date is index. |
| first_date | 2017-01-02 | date | Start date in shipped CSV. |
| last_date | 2020-11-27 | date | End date in shipped CSV. |
| missing_values | 0 | cells | No missing values in shipped OHLCV data. |
| rows_after_21_63_ma_warmup | 900 | rows | 962 - 62 = 900 because the 63-day average first appears on row 63. |
| rows_after_return_and_position_dropna | 899 | rows | Final strategy table after position and return warmup. |
| golden_cross_signals | 4 | signals | SMA crosses above LMA. |
| death_cross_signals | 4 | signals | SMA crosses below LMA. |
| time_long | 692 | rows | Days spent long in the no-look-ahead position series. |
| time_short | 207 | rows | Days spent short in the no-look-ahead position series. |
| buy_hold_total_return_pct | 40.3893 | percent | Buy-and-hold growth over the final test window. |
| sma21_lma63_total_return_pct | 68.0406 | percent | Moving-average crossover growth over the final test window. |
| signal_value_counts | {'0.0': 891, '-2.0': 4, '2.0': 4, 'nan': 1} | dict | 0.0 is no crossover; +/-2 are crossing events. |

## Validation Controls

| control | lecture_application | additive_note |
| --- | --- | --- |
| Original notebook execution | Run the shipped practice notebook in a temporary folder. | Protects original files and confirms local CSV workflow executes. |
| CSV date parsing | Demonstrates why index_col and parse_dates matter. | Plain and clean read shapes are recorded side by side. |
| Timezone conversion | Shows UTC intraday timestamps converted to Asia/Kolkata. | Uses stdlib zoneinfo; pytz is optional for this notebook. |
| Vectorization check | Shows list repetition versus numpy elementwise multiplication. | Loop and numpy results are reconciled. |
| No look-ahead position | Uses regime.shift(1) before applying returns. | Final row count and return path are validated from the shipped CSV. |
| Offline validation | yfinance appears in the teaching material, but validation does not fetch data. | The shipped CSV makes the addendum reproducible without network access. |

## Notebook Validation

| Notebook | Code cells | Errors | Execution exception |
| --- | ---: | ---: | --- |
| `Week 8-1 Tutorial Doubt-Solving Python after DMP-01_practice.ipynb` | 11 | 0 | None |
| `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01_resource_addendum_practice.ipynb` | 5 | 0 | None |
| `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01_validated_practice.ipynb` | 16 | 0 | None |

## HTML Validation

| File | body open/close | html open/close | Generated chart refs | Missing generated charts |
| --- | ---: | ---: | ---: | --- |
| `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01.html` | 1/1 | 1/1 | 10 | None |
| `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01_study.html` | 1/1 | 1/1 | 5 | None |

Status: PASS
