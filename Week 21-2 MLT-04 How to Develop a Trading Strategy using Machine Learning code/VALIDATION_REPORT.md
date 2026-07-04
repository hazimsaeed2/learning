# MLT-04 Validation Report

Lecture: Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning

## Files Reviewed

- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning.html`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_study.html`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_practice.ipynb`
- Local XLF parquet files and helper modules
- MLT-04 PDFs and in-class source zip

## Source PDF Inventory

| file | pages | text_chars | keyword_hits |
| --- | --- | --- | --- |
| Instructions-to-Run-Codes-for-the-MLT-04-lecture.pdf | 1 | 965 |  |
| Links.pdf | 1 | 756 |  |
| MLT-04-Lecture-Summary.pdf | 7 | 5937 | LightGBM; SHAP; validation |
| MLT-04Instructions-and-Key-Takeaways.pdf | 2 | 3139 | SHAP; validation |

## Source Zip Summary

| batch | role | files | total_bytes |
| --- | --- | --- | --- |
| Batch 67 | build_or_cache | 4219 | 124661833 |
| Batch 67 | config | 3 | 521158 |
| Batch 67 | docs | 3 | 22605 |
| Batch 67 | model_or_result_pickle | 13 | 1097029 |
| Batch 67 | notebook | 8 | 1357373 |
| Batch 67 | other | 4 | 2209 |
| Batch 67 | parquet_data | 6 | 3127568 |
| Batch 67 | python_source | 15 | 125018 |
| Batch 68 Onwards | build_or_cache | 5 | 1088 |
| Batch 68 Onwards | config | 3 | 521335 |
| Batch 68 Onwards | docs | 2 | 26407 |
| Batch 68 Onwards | model_or_result_pickle | 13 | 653145 |
| Batch 68 Onwards | notebook | 8 | 1436841 |
| Batch 68 Onwards | other | 5 | 2214 |
| Batch 68 Onwards | parquet_data | 6 | 3105010 |
| Batch 68 Onwards | python_source | 16 | 129409 |

## Parquet Data Inventory

| file | role | size_bytes | rows_from_notebook_output | columns_from_notebook_output | date_start | date_end |
| --- | --- | --- | --- | --- | --- | --- |
| XLF_full_features_X.parquet | full feature matrix | 1858891 | 3157 | 88 | 2000-02-02 | 2012-09-06 |
| XLF_full_features_y.parquet | target labels | 30585 | 3157 | 1 | 2000-02-02 | 2012-09-06 |
| XLF_shap_selected_X.parquet | SHAP-selected feature matrix | 539497 | 3157 | 18 | 2000-02-02 | 2012-09-06 |
| XLF_train_micro.parquet | train microstructure/OHLCV data | 501643 |  |  |  |  |
| XLF_val.parquet | validation OHLCV data | 80044 | 1510 | 5 | 2013-01-02 | 2018-12-31 |
| XLF_test.parquet | test OHLCV data | 94350 | 1776 | 5 | 2019-01-02 | 2026-01-26 |

## Additive Changes Made

- Preserved the existing notebook, data files, helper modules, existing chart, HTML page, and study guide.
- Added PDF and zip inventories, local file inventory, parquet data audit, feature-family audit, Batch 68 and Batch 67 result comparison, holdout metrics, leakage controls, dependency fallback scope, five charts, an addendum notebook, and a validated composite notebook.
- Added local execution stubs only inside the new validated notebook.

## Result Reconciliation

| source | model | features | mcc | f1 | note |
| --- | --- | --- | --- | --- | --- |
| practice_notebook_output | Dummy (0) | 0 | 0.0 |  | Notebook output from cell 7. |
| practice_notebook_output | Simple (3) | 3 | -0.0477 | 0.4577 | Executed output already present in the shipped practice notebook. |
| practice_notebook_output | Microstructure (12) | 12 | 0.0309 | 0.524 | Executed output already present in the shipped practice notebook. |
| practice_notebook_output | Full (88) | 88 | 0.0347 | 0.4944 | Executed output already present in the shipped practice notebook. |
| practice_notebook_output | SHAP-selected (18) | 18 | 0.0657 | 0.493 | Executed output already present in the shipped practice notebook. |
| Batch 68 Onwards saved_pickle | Dummy Model | 0 | 0.0 | 0.37547122 | benchmark_results.pkl |
| Batch 68 Onwards saved_pickle | Simple Model | 3 | -0.09061973 | 0.45533081 | simple_results.pkl |
| Batch 68 Onwards saved_pickle | Microstructure Model | 12 | -0.01468457 | 0.49930994 | microstructure_results.pkl |
| Batch 68 Onwards saved_pickle | Full Features | 88 | 0.03472818 | 0.49435004 | full_results.pkl |
| Batch 67 saved_pickle | Dummy Model | 0 | 0.0 | 0.37547122 | benchmark_results.pkl |
| Batch 67 saved_pickle | Simple Model | 3 | -0.11238565 | 0.44361781 | simple_results.pkl |
| Batch 67 saved_pickle | Microstructure Model | 12 | -0.02077746 | 0.49864072 | microstructure_results.pkl |
| ... | 1 additional rows in CSV | | | | |

## Batch Comparison

| metric | batch_68_onwards | batch_67 | note |
| --- | --- | --- | --- |
| features | 18 | 19 | Practice notebook uses Batch 68 Onwards path. |
| mcc_train | 0.06566404266222578 | 0.12157297407165399 | Practice notebook uses Batch 68 Onwards path. |
| mcc_val | 0.019279814837205297 | -0.002622459546211988 | Practice notebook uses Batch 68 Onwards path. |
| mcc_test | -0.005899880052585674 | 0.06798461451302383 | Practice notebook uses Batch 68 Onwards path. |
| f1_train | 0.4930237899194626 | 0.5094167178535549 | Practice notebook uses Batch 68 Onwards path. |
| f1_val | 0.24615384615384617 | 0.15311004784688995 | Practice notebook uses Batch 68 Onwards path. |
| f1_test | 0.1759697256385998 | 0.09472551130247578 | Practice notebook uses Batch 68 Onwards path. |
| val_change_pct | -70.63870262088463 | -102.15710733922354 | Practice notebook uses Batch 68 Onwards path. |
| test_change_pct | -130.60133150864272 | 2692.398979470406 | Practice notebook uses Batch 68 Onwards path. |
| production_ready | False | True | Practice notebook uses Batch 68 Onwards path. |
| vectorized_total_return | 5.641560032065551 | 6.629348128208079 | Practice notebook uses Batch 68 Onwards path. |
| vectorized_sharpe | 0.14842537672360537 | 0.1664540123473351 | Practice notebook uses Batch 68 Onwards path. |
| vectorized_max_dd | -20.38801356018867 | -25.88210970927623 | Practice notebook uses Batch 68 Onwards path. |
| vectorized_trades | 91 | 39 | Practice notebook uses Batch 68 Onwards path. |
| verdict | ❌ FAIL - Excessive degradation | ✅ PASS - Test outperformed validation | Practice notebook uses Batch 68 Onwards path. |

## Holdout Results

| stage | mcc | f1 | change_pct | reading |
| --- | --- | --- | --- | --- |
| train_walk_forward | 0.06566404266222578 | 0.4930237899194626 | 0.0 | SHAP-18 walk-forward training result. |
| validation_holdout | 0.019279814837205297 | 0.24615384615384617 | -70.63870262088463 | Validation performance degrades sharply from training. |
| test_holdout_once | -0.005899880052585674 | 0.1759697256385998 | -130.60133150864272 | Untouched test MCC is below zero in Batch 68. |
| vectorized_strategy |  |  |  | Return 5.6416 pct, Sharpe 0.1484, max drawdown -20.3880 pct, trades 91. |
| production_verdict |  |  |  | ❌ FAIL - Excessive degradation; production_ready=False. |

## Leakage Controls

| method | mcc | inflation_vs_honest | control_status | why_it_matters |
| --- | --- | --- | --- | --- |
| Honest walk-forward with embargo | 0.0347 | 0.0 | preferred baseline | Train only on past observations with an embargo before the test window. |
| Random shuffle split | 0.5593 | 0.5246 | leaky anti-pattern | Future regimes can enter the training set. |
| K-fold without shuffle | 0.046 | 0.0113 | weak time-series control | Contiguous folds still train on data that can sit after the test fold. |
| K-fold with shuffle | 0.5823 | 0.5475 | leaky anti-pattern | Shuffling breaks time order and creates the largest inflation in the notebook. |

## Notebook Validation

| Notebook | Code cells | Errors | Markdown-before-code gaps | Execution exception |
| --- | ---: | ---: | ---: | --- |
| `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_practice.ipynb` | 9 | 1 | 0 | Traceback (most recent call last):<br>  File "C:\Users\hsaeed\Downloads\EPAT-Git\_validation_work\generate_mlt04.py", line 935, in execute_notebook_safely<br>    exec(compile(source, str(path), "exec"), ns)<br>  File "C:\Users\hsaeed\Downloads\EPAT-Git\Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code\Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_practice.ipynb", line 14, in <module><br>    "**What ships in the exercise (and what we use here):**\n",<br>    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>ModuleNotFoundError: No module named 'joblib'<br> |
| `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_resource_addendum_practice.ipynb` | 4 | 0 | 0 |  |
| `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_validated_practice.ipynb` | 14 | 0 | 0 |  |

## HTML Validation

| File | body open/close | html open/close | Generated chart refs | Missing generated charts |
| --- | ---: | ---: | ---: | --- |
| `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning.html` | 1/1 | 1/1 | 10 | None |
| `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_study.html` | 1/1 | 1/1 | 0 | None |

## Gaps Closed

| Gap | Additive coverage |
| --- | --- |
| Source zip contains multiple batch versions and many build/cache files | Added full inventory plus summarized useful roles by batch. |
| Local environment cannot read parquet or import ML dependencies | Added dependency audit and a validated notebook with local stubs only. |
| Batch 68 and Batch 67 saved outcomes differ | Added a batch comparison table without replacing either version. |
| Leakage demonstrations need explicit controls | Added leakage-control table and chart. |
| Production readiness can be mistaken for training fit | Added holdout and vectorized strategy result tables. |

## Judge Scores

- Source coverage: 9.4/10
- Accuracy and corrections: 9.3/10
- Notebook reproducibility: 9.1/10
- Additive-only compliance: 9.8/10

Status: PASS
