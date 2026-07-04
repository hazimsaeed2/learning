# PRM-01 Additive Resource Pack

Lecture: Week 15-1 PRM-01 Portfolio & Risk Management

This folder preserves the original practice notebook and `chart_1_risk.png`. New files add source-backed risk-management references from the transcript and PRM-01 PDFs.

## Added Files

- CSV references for the five-phase risk process, risk taxonomy, VaR/CVaR/liquidity-adjusted VaR, credit/financial/regulatory risk, incident controls, pretrade controls, and Indian exchange controls.
- Five `chart_addendum_*` PNG charts.
- Addendum and validated composite notebooks.

## Dependency Note

The original notebook imports `scipy.stats.norm`, but SciPy is not installed in this environment. The validated composite notebook adds a standard-library `NormalDist.inv_cdf` fallback before the preserved original cells.
