# Week 6-3 PBQ-02 Python Basics for Quants Code Resources

Additive resources generated for the PBQ-02 validation pass. The original practice notebook and existing chart were not replaced.

## Files added

- `Week 6-3 PBQ-02 Python Basics for Quants_resource_addendum_practice.ipynb` - standalone addendum for late-session pandas and quant calculations.
- `Week 6-3 PBQ-02 Python Basics for Quants_validated_practice.ipynb` - original practice notebook plus the additive section.
- `chart_addendum_1_pbq02_pandas_workflow_map.png` - CSV-to-feature workflow map.
- `chart_addendum_2_pbq02_tcs_returns_rolling.png` - TCS close, moving averages, returns, and rolling volatility.
- `chart_addendum_3_pbq02_missing_apply_signal_workflow.png` - missing-value audit and `np.where` regime counts.
- `pbq02_dataframe_selection_reference.csv` - `[]`, `.loc`, `.iloc`, filtering, rounding, and drop reference.
- `pbq02_quant_calculation_reference.csv` - `diff`, `pct_change`, `shift`, rolling, EWM, `apply`, `np.where`, and `groupby` reference.
- `pbq02_missing_data_reference.csv` - missing-data handling guidance.
- `pbq02_tcs_addendum_feature_stats.csv` - computed TCS feature statistics.
- `pbq02_signal_counts.csv` - volume-regime signal counts.

## Source anchors

- Official PBQ-02 objectives: NumPy ndarrays, pandas Series/DataFrames, CSV/Excel read-write, DataFrame methods, percentage change, rolling, shift, missing/NaN data, and groupby.
- Official PBQ-02 solution notebook: late-section cells on `df.info()`, `.loc`, `.iloc`, boolean filters, `diff`, `pct_change`, `shift`, rolling averages, missing-value methods, `apply`, `np.where`, and `to_excel`.
- PBQ-02 FAQ: `np.where` vs `df.where`, nested `np.where`, tuple immutability, and distributions for prices/returns.

## Continuation resources added after the interrupted run

- `AXISBANK_data_hygiene.csv` - supplied Data Hygiene Auditor resource data copied into the local code folder.
- `Week 6-3 PBQ-02 Python Basics for Quants_resource_continuation_practice.ipynb` - additive resource continuation notebook preserving the live/API project as reference and using local data.
- `Week 6-3 PBQ-02 Python Basics for Quants_strict_resource_validation_practice.ipynb` - strict offline validation notebook for FAQ examples, data hygiene, and VaR/ES resources.
- `pbq02_data_hygiene_summary.csv` - offline AXISBANK hygiene checks.
- `pbq02_var_es_summary.csv` - earlier generated VaR/ES table, preserved as-is.
- `pbq02_var_es_summary_corrected.csv` - corrected additive VaR/ES table with explicit SciPy/Shapiro status and parametric CVaR.
- `pbq02_faq_resource_reference.csv` - FAQ reference rows for multi-ticker yfinance, where variants, tuples, nested conditions, `%whos`, and flexible function inputs.
- `pbq02_mini_project_reference.csv` - resource map for Data Hygiene Auditor and Monte Carlo VaR/ES mini-projects.
- `chart_continuation_1_pbq02_data_hygiene.png` - offline data hygiene chart.
- `chart_continuation_2_pbq02_var_es.png` - earlier generated VaR/ES chart, preserved as-is.
- `chart_continuation_2_pbq02_var_es_corrected.png` - corrected VaR/ES chart.
- `chart_continuation_3_pbq02_resource_bridge.png` - FAQ/resource bridge chart.
- `pbq02_strict_resource_validation_summary.json` - execution summary for the strict notebook.
