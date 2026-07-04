# EFS-04 Additive Resource Pack

Lecture: Week 14-2 EFS-04 Quantitative Momentum Strategies II

This folder preserves the original practice notebook and `chart_1_momentum2.png`. New files add source-backed implementation details from the transcript, PDF packet, and selected MomentumWS source files.

## Added Files

- Selected source scripts, `VIX.csv`, and raw `.mat` data copied from `EFS03-04-Inclass-Exercises-File.zip`.
- CSV references for strategy inventory, timestamp controls, VIX/ES hedge mechanics, momentum-crash controls, IID autocorrelation testing, and calendar/leveraged-ETF controls.
- Five `chart_addendum_*` PNG charts.
- Addendum and validated composite notebooks.

## Dependency Note

The copied source scripts use `scipy.io.loadmat`; SciPy is not installed in this environment. The original notebook also imports `scipy.stats.pearsonr` for one autocorrelation test. The validated composite notebook adds a local `pearsonr` fallback before the preserved original cells so it can execute here without changing the original notebook.
