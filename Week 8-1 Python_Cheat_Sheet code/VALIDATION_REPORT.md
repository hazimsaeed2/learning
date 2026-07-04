# Python Cheat Sheet Validation Report

Lecture/support page: Week 8-1 Python_Cheat_Sheet

## Files Reviewed

- `Week 8-1 Python_Cheat_Sheet.html`

## Static HTML Audit

| item | value | reading |
| --- | --- | --- |
| file_size_bytes | 50382 | Static HTML support page. |
| html_open | 1 | HTML tag count. |
| html_close | 1 | HTML tag count. |
| body_open | 1 | Body tag count. |
| body_close | 1 | Body tag count. |
| sections | 9 | Major content sections. |
| tables | 16 | Reference tables. |
| code_blocks | 20 | Code blocks. |
| term_shift(2) | 12 | Key workflow term frequency. |
| term_pct_change | 6 | Key workflow term frequency. |
| term_cumprod | 11 | Key workflow term frequency. |
| term_rolling | 8 | Key workflow term frequency. |
| term_dropna | 8 | Key workflow term frequency. |
| term_np.where | 8 | Key workflow term frequency. |
| term_yfinance | 3 | Key workflow term frequency. |
| term_look-ahead | 4 | Key workflow term frequency. |
| term_SMA | 34 | Key workflow term frequency. |
| term_LMA | 27 | Key workflow term frequency. |

## Dependency Scope

| dependency | available_locally | version | fallback_or_note |
| --- | --- | --- | --- |
| numpy | yes | 2.2.6 |  |
| pandas | yes | 3.0.3 |  |
| matplotlib | yes | 3.11.0 |  |
| yfinance | yes | 0.2.33 | Installed locally; download signature is decorated in this version, so live keyword support should be checked in the target environment. |
| bs4 | yes | 4.12.2 |  |

## Additive Corrections

| item | original_value | additive_calendar_check | note |
| --- | --- | --- | --- |
| raw_rows | 962 | 783 | Business-day count before exchange holidays for 2017-01-01 through 2020-01-01. |
| rows_after_dropna | 899 | 720 | Approximate rows after 63-day LMA plus previous-day shift warmup; live Yahoo data may vary by holidays. |
| yfinance_multi_level_index | Always add multi_level_index=False | environment note | Local yfinance is available, but the decorated signature does not expose this keyword in version-specific introspection. |

## Workflow And Synthetic Backtest

| step | workflow_step | rule | additive_check |
| --- | --- | --- | --- |
| 1 | Download data | Use daily market data; avoid relying on live download for validation. | offline synthetic data used |
| 2 | Calculate SMA/LMA | 21-day and 63-day rolling means. | verified |
| 3 | Shift prev columns | Use shift(1) for yesterday's SMA/LMA. | verified |
| 4 | dropna | Remove warmup rows after rolling windows. | verified |
| 5 | Signals | np.where or boolean masks for crossovers. | verified |
| 6 | Positions | Forward-fill non-zero signals. | verified |
| 7 | Returns | Use position.shift(2) times pct_change. | verified |
| 8 | Equity | Use (1+r).cumprod(). | verified |
| 9 | Square off | Close final open position in execution-grade backtest. | documented |

| metric | value | unit | reading |
| --- | --- | --- | --- |
| synthetic_business_days | 783 | rows | Offline business-day calendar sanity check. |
| synthetic_rows_after_dropna | 720 | rows | After 21/63 MA, previous columns, and dropna. |
| buy_signals | 7 | count | Offline synthetic crossover count. |
| sell_signals | 8 | count | Offline synthetic crossover count. |
| buy_hold_total_pct | 48.6926 | percent | Synthetic buy-and-hold result. |
| shift2_strategy_total_pct | -12.9779 | percent | Bias-controlled daily strategy result. |
| no_shift_strategy_total_pct | 0.7004 | percent | Shows why shift controls are audited. |

## Return Math And Mistake Controls

| check | value | formula |
| --- | --- | --- |
| simple_growth_from_cumprod | 1.48692569 | (1 + pct_change).cumprod() |
| log_growth_from_exp_cumsum | 1.48692569 | exp(log_return.cumsum()) |
| absolute_difference | 0.0 | must be near zero for same path |
| list_times_3 | [1, 2, 1, 2, 1, 2] | list repeats |
| array_times_3 | [3, 6] | array multiplies elementwise |

| mistake | risk | fix |
| --- | --- | --- |
| No multi_level_index check | Column names can be nested or version-dependent. | Inspect actual yfinance output. |
| dropna without assignment/inplace | NaN warmup rows stay. | Use data = data.dropna() or inplace=True. |
| No position.shift(2) | Look-ahead bias. | Shift execution-aware position before applying returns. |
| list * scalar | Repeats list. | Convert to numpy array for elementwise math. |
| cumsum for simple-return equity | Wrong compounding. | Use (1+r).cumprod(). |
| read_csv without parse_dates | Date stays a string column. | Use index_col and parse_dates where appropriate. |

## Validation Controls

| control | lecture_application | additive_note |
| --- | --- | --- |
| Static HTML audit | Support page has no notebook/source package. | Counts sections, tables, code blocks, and key terms. |
| Calendar sanity check | Original row counts are approximate. | Adds business-day row-count correction without editing original. |
| Look-ahead control | position.shift(2) is the core backtest safety rule. | Synthetic backtest compares shifted and unshifted paths. |
| Return math | Simple returns compound; log returns add. | cumprod and exp(cumsum(log)) reconciliation added. |

## Notebook Validation

| Notebook | Code cells | Errors | Execution exception |
| --- | ---: | ---: | --- |
| `Week 8-1 Python_Cheat_Sheet_resource_addendum_practice.ipynb` | 4 | 0 |  |
| `Week 8-1 Python_Cheat_Sheet_validated_practice.ipynb` | 4 | 0 |  |

## HTML Validation

| File | body open/close | html open/close | Generated chart refs | Missing generated charts |
| --- | ---: | ---: | ---: | --- |
| `Week 8-1 Python_Cheat_Sheet.html` | 1/1 | 1/1 | 10 | None |

Status: PASS
