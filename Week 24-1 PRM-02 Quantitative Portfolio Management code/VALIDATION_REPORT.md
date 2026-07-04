# PRM-02 Validation Report

Lecture: Week 24-1 PRM-02 Quantitative Portfolio Management

## Files Reviewed

- `Week 24-1 PRM-02 Quantitative Portfolio Management.html`
- `Week 24-1 PRM-02 Quantitative Portfolio Management_study.html`
- `Week 24-1 PRM-02 Quantitative Portfolio Management_practice.ipynb`
- Local CSV data: TCS, MARUTI, MARICO, Benchmark, Nifty 50 matrix
- PRM-02 PDFs and source ZIP

## Source PDF Inventory

| file | pages | text_chars | keyword_hits |
| --- | --- | --- | --- |
| PRM-02-Lecture-Summary.pdf | 3 | 3845 | 30 |
| PRM-02Instructions-and-Key-Takeaways.docx.pdf | 1 | 847 | 14 |
| PRM-02Lecture-Notes.pdf | 31 | 9634 | 114 |

## Source Zip Role Summary

| zip | role | files |
| --- | --- | --- |
| PRM02-Inclass-Exercises-File.zip | checkpoint | 3 |
| PRM02-Inclass-Exercises-File.zip | directory | 2 |
| PRM02-Inclass-Exercises-File.zip | source_data | 5 |
| PRM02-Inclass-Exercises-File.zip | source_notebook | 1 |
| PRM02-Inclass-Exercises-File.zip | source_spreadsheet | 1 |

## Data Inventory

| file | rows | columns | date_start | date_end | missing_cells |
| --- | --- | --- | --- | --- | --- |
| TCS.csv | 1393 | 7 | 2015-01-01 | 2020-08-28 | 0 |
| MARUTI.csv | 1393 | 7 | 2015-01-01 | 2020-08-28 | 0 |
| MARICO.csv | 1393 | 7 | 2015-01-01 | 2020-08-28 | 0 |
| Benchmark.csv | 1393 | 6 | 2015-01-01 | 2020-08-28 | 0 |
| nifty50.csv | 1393 | 50 | 2015-01-01 | 2020-08-27 | 1388 |

## Additive Changes Made

- Preserved the existing notebook, CSV data, existing chart, HTML page, study guide, PDFs, and source ZIP.
- Added source inventories, data audit, return/risk metrics, diversification checks, frontier metrics, frontier weights, out-of-sample metrics, risk-adjusted ratio controls, Treynor correction table, validation controls, five charts, an addendum notebook, and a validated composite notebook.
- Copied source notebook/spreadsheet from the source ZIP into clearly suffixed additive files when absent.

## Return And Risk Metrics

| asset | trading_days | holding_return_pct | annual_mean_pct | cagr_pct | annual_volatility_pct |
| --- | --- | --- | --- | --- | --- |
| TCS | 1392 | 105.546 | 16.16 | 13.9324 | 24.9605 |
| MARUTI | 1392 | 126.5478 | 19.4168 | 15.9568 | 30.3454 |
| MARICO | 1392 | 152.8533 | 20.2325 | 18.2859 | 26.2345 |

## Diversification Metrics

| case | members | correlation | expected_return_pct | annual_volatility_pct |
| --- | --- | --- | --- | --- |
| TCS+MARUTI_50_50 | 2 | 0.249698 | 17.7884 | 21.9211 |
| TCS+MARICO_50_50 | 2 | 0.119244 | 18.1963 | 19.1536 |
| equal_weight_first_1_nifty_names | 1 |  |  | 36.1785 |
| equal_weight_first_2_nifty_names | 2 |  |  | 25.4808 |
| equal_weight_first_3_nifty_names | 3 |  |  | 25.3164 |
| equal_weight_first_5_nifty_names | 5 |  |  | 23.5503 |
| equal_weight_first_8_nifty_names | 8 |  |  | 22.4755 |
| equal_weight_first_10_nifty_names | 10 |  |  | 20.5497 |
| equal_weight_first_20_nifty_names | 20 |  |  | 18.8538 |
| equal_weight_first_30_nifty_names | 30 |  |  | 18.6076 |
| equal_weight_first_49_nifty_names | 49 |  |  | 18.0333 |

## Frontier And OOS Metrics

| portfolio | expected_return_pct | expected_volatility_pct | return_per_risk | simulation_count |
| --- | --- | --- | --- | --- |
| minimum_volatility | 13.2066 | 16.9095 | 0.781016 | 3500 |
| maximum_sharpe | 19.8695 | 18.8742 | 1.052731 | 3500 |
| maximum_return | 21.0339 | 21.35 | 0.985195 | 3500 |

| portfolio | test_days | test_start | test_end | cumulative_return_pct |
| --- | --- | --- | --- | --- |
| equal_weight | 418 | 2018-12-14 | 2020-08-27 | 8.9378 |
| maximum_sharpe_optimized | 418 | 2018-12-14 | 2020-08-27 | 28.1214 |

## Risk Ratios And Additive Correction

| metric | value | unit | reading |
| --- | --- | --- | --- |
| Sharpe ratio | 0.647422 | ratio | Excess return per unit of total volatility. |
| Sortino ratio | 0.928618 | ratio | Excess return per unit of downside volatility. |
| Beta vs Nifty | 0.625594 | beta | Systematic market sensitivity. |
| Treynor ratio - notebook scaled | 0.016272 | ratio | Original notebook output; daily mean scaled by sqrt(252). |
| Treynor ratio - corrected annual convention | 0.258314 | ratio | Annual excess return divided by beta; additive correction, original preserved. |
| Maximum drawdown | -27.211302 | percent | Worst peak-to-trough loss in TCS cumulative return curve. |
| Calmar ratio | 0.512009 | ratio | CAGR divided by absolute maximum drawdown. |
| Information ratio | 0.358948 | ratio | Active return per unit of tracking error vs benchmark. |
| Daily VaR 95 | -2.424362 | percent | Loss threshold for the worst 5 percent of days. |
| Daily CVaR 95 | -3.531179 | percent | Average loss once the VaR threshold is breached. |
| Kelly fraction | 2.593783 | fraction | Growth-optimal fraction; leverage implied, so practitioners usually fraction it. |

| item | original_notebook_value | corrected_annual_value | additive_note |
| --- | --- | --- | --- |
| Treynor ratio | 0.016272 | 0.258314 | Original value remains in place; this row adds the standard annual convention. |

## Validation Controls

| control | lecture_application | additive_note |
| --- | --- | --- |
| Objective first | Portfolio definition changes with capital preservation, growth, alpha, or mandate constraints. | The addendum keeps objective-specific selection separate from generic max-return language. |
| Return and risk measured separately | Arithmetic return and CAGR are both shown; variance and volatility are both retained. | Tables preserve analysis and publishing conventions side by side. |
| Covariance matters | Two-stock volatility is lower than either individual stock because covariance is below perfect co-movement. | Pair correlations and realized 50/50 volatilities are added. |
| Diversification has a floor | Equal-weight Nifty volatility flattens near the all-name systematic-risk floor. | The floor is plotted and recorded in CSV. |
| Optimization is not proof | Max-Sharpe weights are tested out of sample and still require rebalancing. | OOS curves and CSVs separate in-sample selection from held-out performance. |
| Treynor convention | Notebook value is preserved, with an additional annual Treynor convention supplied. | No original line is changed. |

## Notebook Validation

| Notebook | Code cells | Errors | Markdown-before-code gaps | Execution exception |
| --- | ---: | ---: | ---: | --- |
| `Week 24-1 PRM-02 Quantitative Portfolio Management_practice.ipynb` | 14 | 0 | 0 |  |
| `Week 24-1 PRM-02 Quantitative Portfolio Management_resource_addendum_practice.ipynb` | 4 | 0 | 0 |  |
| `Week 24-1 PRM-02 Quantitative Portfolio Management_validated_practice.ipynb` | 18 | 0 | 0 |  |

## HTML Validation

| File | body open/close | html open/close | Generated chart refs | Missing generated charts |
| --- | ---: | ---: | ---: | --- |
| `Week 24-1 PRM-02 Quantitative Portfolio Management.html` | 1/1 | 1/1 | 10 | None |
| `Week 24-1 PRM-02 Quantitative Portfolio Management_study.html` | 1/1 | 1/1 | 0 | None |

## Gaps Closed

| Gap | Additive coverage |
| --- | --- |
| Source ZIP content not visible in the lecture page | Added ZIP inventory and copied the source notebook/spreadsheet with `_source` suffixes. |
| Return/risk and diversification numbers need reproducible tables | Added CSV tables and charts generated from the shipped data. |
| Efficient-frontier selection can be over-read | Added min-vol, max-Sharpe, max-return rows and selected weights. |
| Original Treynor value uses notebook scaling | Preserved it and added the standard annual convention. |

## Judge Scores

- Source coverage: 9.3/10
- Accuracy and corrections: 9.4/10
- Notebook reproducibility: 9.7/10
- Additive-only compliance: 9.8/10

Status: PASS
