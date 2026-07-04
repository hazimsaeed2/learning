# ASQ-02 Validation Report

Lecture: Week 12-1 ASQ-02 Time Series Modeling with Python

## Files Reviewed

- `Week 12-1 ASQ-02 Time Series Modeling with Python.html`
- `Week 12-1 ASQ-02 Time Series Modeling with Python_study.html`
- `Week 12-1 ASQ-02 Time Series Modeling with Python.txt`
- `Week 12-1 ASQ-02 Time Series Modeling code/Week 12-1 ASQ-02 Time Series Modeling_practice.ipynb`
- `Week 12-1 ASQ-02 Time Series Modeling code/market_data.csv`

## Additive Changes Made

- Added source inventory, dependency/execution audit, fixed/auto ARIMA-style metrics, cost-drag metrics, volatility/GARCH-like metrics, and validation controls.
- Added five validation charts with `chart_addendum_*_asq02_*.png` names.
- Added an addendum notebook and a validated notebook copy. The original notebook remains unchanged.
- Appended marked validation sections to the main HTML page and study guide.

## Source Inventory

| artifact | artifact_type | exists | size_bytes | rows | columns | note |
| --- | --- | --- | --- | --- | --- | --- |
| Week 12-1 ASQ-02 Time Series Modeling_practice.ipynb | practice_notebook | True | 290183 |  |  | 12 code cells, 14 markdown cells |
| market_data.csv | source_data | True | 75044 | 962 | 6 | 2017-01-02 through 2020-11-27 |
| chart_1_arch.png | original_chart | True | 198354 |  |  | Existing chart preserved; addendum charts use separate names. |

## Dependency And Execution

| metric | value | unit | reading |
| --- | --- | --- | --- |
| statsmodels_available | no | environment | ModuleNotFoundError |
| arch_available | no | environment | ModuleNotFoundError |
| original_execution_errors | 1 | errors | ModuleNotFoundError: No module named 'statsmodels' |
| fallback_scope | AR-like + EWMA-GARCH-like | validated_copy | Validated copy injects minimal fallbacks for local execution only. |

## Fixed And Auto ARIMA-Style Metrics

| asset | bars | signals | fixed_strategy_pct | fixed_buy_hold_pct | fixed_excess_pct | fixed_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| NIFTY weekly | 204 | 40 | -7.7064 | 15.7761 | -23.4825 | loss-making |
| NIFTY 2-weekly | 103 | 40 | -9.8875 | 9.2522 | -19.1397 | loss-making |
| NIFTY monthly | 47 | 10 | -2.9548 | 15.7761 | -18.7309 | loss-making |
| NIFTY wk 1st-half | 102 | 40 | 22.753 | 5.9862 | 16.7668 | profitable |
| NIFTY wk 2nd-half | 102 | 40 | -7.7064 | 15.7761 | -23.4825 | loss-making |

| asset | auto_order | auto_aic | auto_strategy_pct | auto_buy_hold_pct | auto_excess_pct | fixed_excess_pct | vs_fixed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NIFTY weekly | (2, 1, 0) | 1121.1146 | -7.7064 | 15.7761 | -23.4825 | -23.4825 | worse/same |
| NIFTY 2-weekly | (2, 1, 0) | 1138.9496 | -9.8875 | 9.2522 | -19.1397 | -19.1397 | worse/same |
| NIFTY monthly | (2, 1, 0) | 571.8626 | -2.9548 | 15.7761 | -18.7309 | -18.7309 | worse/same |
| NIFTY wk 1st-half | (2, 1, 0) | 995.6203 | 22.753 | 5.9862 | 16.7668 | 16.7668 | worse/same |
| NIFTY wk 2nd-half | (2, 1, 0) | 1121.1146 | -7.7064 | 15.7761 | -23.4825 | -23.4825 | worse/same |

## Cost Drag Metrics

| metric | value | unit | reading |
| --- | --- | --- | --- |
| cost_rate_per_turn | 0.0003 | fraction | 0.03% per position change unit. |
| gross_total_pct | -7.9319 | percent | Before transaction costs. |
| net_total_pct | -10.1328 | percent | After transaction costs. |
| buy_hold_total_pct | 13.4691 | percent | Buy-and-hold over same window. |
| gross_excess_pct | -21.401 | percent | Gross excess over B&H. |
| net_excess_pct | -23.6019 | percent | Net excess over B&H. |
| number_of_trades | 41 | trades | Position changes counted from signal flips. |
| total_cost_drag_pct | 2.43 | percent | Sum of cost series. |

## Volatility And GARCH-Like Metrics

| metric | avg_annual_vol_pct | min_annual_vol_pct | max_annual_vol_pct | reading |
| --- | --- | --- | --- | --- |
| 2017 calm | 9.003 | 6.1871 | 10.9365 | Rolling 30-day realized annualized volatility. |
| 2018 wobble | 11.9975 | 6.7703 | 20.9505 | Rolling 30-day realized annualized volatility. |
| 2019 pre-COVID | 13.6095 | 8.064 | 23.7156 | Rolling 30-day realized annualized volatility. |
| 2020 COVID | 26.0211 | 9.1627 | 75.2086 | Rolling 30-day realized annualized volatility. |
| whole_sample_min_vol |  | 6.1871 |  | Minimum rolling realized vol. |
| whole_sample_max_vol |  |  | 75.2086 | Maximum rolling realized vol. |
| fallback_garch_alpha_beta | 0.98 |  |  | EWMA-GARCH-like persistence parameter; formal GARCH needs arch. |
| fallback_next_vol_pct | 16.3724 |  |  | Next-day annualized vol estimate from fallback. |
| latest_rolling_30d_vol_pct | 14.3852 |  |  | Latest realized vol. |

## Validation Controls

| control | lecture_application | additive_note |
| --- | --- | --- |
| Original notebook execution | Run ASQ-02 practice notebook. | Original fails locally because statsmodels/arch dependencies are unavailable. |
| Validated fallback copy | Permit local execution without installing packages. | Fallback AR-like and EWMA-GARCH-like classes are labelled and limited to this notebook. |
| Fixed versus auto order | ARIMA order selection and AIC. | Fallback AIC search is recorded separately from formal statsmodels ARIMA. |
| Transaction costs | Gross versus net strategy return. | Cost drag is explicitly subtracted from signal returns. |
| Volatility regimes | Heteroscedasticity and COVID volatility spike. | Rolling 30-day realized vol confirms non-constant risk. |
| Formal inference scope | GARCH and ARIMA modelling. | Use statsmodels/arch for production-grade model estimation. |

## Additive Correction

The original notebook requires `statsmodels` and `arch` and fails locally before execution. The validated copy uses labelled ARIMA-style and EWMA-GARCH-like fallbacks to make the workflow executable here. These fallback metrics do not overwrite the original study values and are not formal model estimates.

## Notebook Validation

| Notebook | Code cells | Errors | Execution exception |
| --- | ---: | ---: | --- |
| `Week 12-1 ASQ-02 Time Series Modeling_practice.ipynb` | 12 | 1 | ModuleNotFoundError: No module named 'statsmodels' |
| `Week 12-1 ASQ-02 Time Series Modeling with Python_resource_addendum_practice.ipynb` | 4 | 0 | None |
| `Week 12-1 ASQ-02 Time Series Modeling with Python_validated_practice.ipynb` | 17 | 0 | None |

## HTML Validation

| File | body open/close | html open/close | Generated chart refs | Missing generated charts |
| --- | ---: | ---: | ---: | --- |
| `Week 12-1 ASQ-02 Time Series Modeling with Python.html` | 1/1 | 1/1 | 10 | None |
| `Week 12-1 ASQ-02 Time Series Modeling with Python_study.html` | 1/1 | 1/1 | 5 | None |

Status: PASS with original dependency gap documented.
