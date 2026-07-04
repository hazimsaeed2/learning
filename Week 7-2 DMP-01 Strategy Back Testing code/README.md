# Week 7-2 DMP-01 Strategy Back Testing Code Resources

Additive resources generated for the DMP-01 validation pass. The original practice notebook, local NSE CSV, and equity chart were not replaced.

## Original files retained

- `Week 7-2 DMP-01 Strategy Back Testing_practice.ipynb`
- `nse_daily.csv`
- `chart_1_equity.png`

## Files added

- `DMP_01_code_Tutorial Session_source.ipynb` - raw source notebook from the official tutorial zip.
- `DMP_01_data_tutorial_nse_source.csv` - raw source CSV from the official tutorial zip; it matches the existing `nse_daily.csv`.
- `Log Returns vs Simple Returns_source.xlsx` - raw source workbook.
- `Week 7-2 DMP-01 Strategy Back Testing_resource_addendum_practice.ipynb` - standalone addendum notebook.
- `Week 7-2 DMP-01 Strategy Back Testing_validated_practice.ipynb` - original notebook plus additive source/workbook section.
- `dmp01_source_file_inventory.csv` - tutorial zip inventory.
- `dmp01_vectorized_workflow_reference.csv` - seven-step workflow reference.
- `dmp01_log_simple_workbook_reference.csv` - parsed workbook return comparison.
- `dmp01_long_short_crossover_sample.csv` - local SMA50/SMA200 long-short dataframe.
- `dmp01_long_short_crossover_metrics.csv` - local tear-sheet proxy metrics.
- `dmp01_event_vs_vectorized_check.csv` - vectorized versus event-style loop equivalence check.
- `chart_addendum_1_dmp01_workflow_map.png`
- `chart_addendum_2_dmp01_log_simple_workbook.png`
- `chart_addendum_3_dmp01_long_short_crossover.png`
- `chart_addendum_4_dmp01_metrics_snapshot.png`
- `chart_addendum_5_dmp01_event_loop_check.png`
- `dmp01_validation_execution_summary.json`

## Source anchors

- Transcript: strategy workflow, simple/log returns, `cumsum`/`cumprod`, `.shift()`, vectorized versus event-driven testing, SMA strategy, MACD, and quantstats preview.
- Official source notebook: vectorized workflow, long-short moving-average crossover, signals, positions, returns, analysis, and event-driven loop preview.
- Official workbook: log returns versus simple returns compounding example.
