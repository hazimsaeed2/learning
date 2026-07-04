# PBQ-02 Validation Report

Lecture: Week 6-3 PBQ-02 Python Basics for Quants

## Files Reviewed

- `PBQ-02Python-Basics-for-QuantsLN.pdf`
- `PBQ02-Lecture-Objectives-Prerequisities.pdf`
- `Lecture-Summary-PBQ-01-and-PBQ-02.pdf`
- `PQB-02-FAQ.pdf`
- `PBQ02Inclass-Exercises-File.zip`
- `DataHygieneAuditor.zip`
- `Monte-Carlo-Simulations-to-compute-VaR-and-Expected-Shortfall.zip`
- Existing lecture pages: `Week 6-3 PBQ-02 Python Basics for Quants.html`, `Week 6-3 PBQ-02 Python Basics for Quants_study.html`
- Existing and added notebooks in this code folder.

## Additive Changes Made

- Kept the original lecture pages and prior addendum content intact.
- Added a continuation section to the cheat sheet for PBQ-02 FAQ details, Data Hygiene Auditor, and Monte Carlo VaR/ES.
- Added a matching prose continuation section to the study guide.
- Added corrected VaR/ES resources beside the earlier generated table rather than replacing it.
- Added a strict offline validation notebook for the FAQ/resource material.

## Gaps Closed

| Source gap | Additive coverage |
| --- | --- |
| FAQ details on multi-ticker `yfinance`, `df.where` vs `np.where`, boolean slicing, nested `np.where`, tuples, `%whos`, `*args`, and `**kwargs` | Added to cheat sheet, study guide, `pbq02_faq_resource_reference.csv`, and strict notebook examples. |
| Price/return distribution clarification | Added note that prices are often modeled lognormal while returns are the tested object; daily returns can be fat-tailed. |
| Data Hygiene Auditor resource | Added local AXISBANK data copy, offline hygiene summary, chart, and study explanation. |
| Monte Carlo VaR/ES mini-project | Added historical, parametric, and Monte Carlo VaR/ES summary using local TCS data. |
| Earlier generated VaR/ES blanks | Preserved `pbq02_var_es_summary.csv` and added `pbq02_var_es_summary_corrected.csv` with explicit Shapiro status and parametric CVaR. |

## Accuracy Notes

- No live `yfinance`, Gemini, or Mistral calls were made. The official resources can use those services, but this validation pass uses local files only.
- The AXISBANK missing-day check is a business-day proxy. It correctly flags dates for investigation, but an exchange holiday calendar is required before treating every missing business day as a data error.
- SciPy is not installed in this workspace, so the official Shapiro-Wilk test is marked `not_run_scipy_unavailable`. A Jarque-Bera proxy was added from skew and excess kurtosis.
- The corrected local TCS risk values are:
  - daily historical 95% VaR: -2.43%
  - daily historical 95% CVaR: -3.61%
  - daily parametric 95% VaR: -2.59%
  - daily parametric 95% CVaR: -3.27%
  - 100-day Monte Carlo 95% terminal VaR: -18.27%
  - 100-day Monte Carlo 95% terminal CVaR: -23.60%

## Notebook Validation

| Notebook | Code cells | Errors | Markdown-before-code gaps |
| --- | ---: | ---: | ---: |
| `Week 6-3 PBQ-02 Python Basics for Quants_practice.ipynb` | 20 | 0 | 0 |
| `Week 6-3 PBQ-02 Python Basics for Quants_resource_addendum_practice.ipynb` | 12 | 0 | 1 |
| `Week 6-3 PBQ-02 Python Basics for Quants_validated_practice.ipynb` | 32 | 0 | 1 |
| `Week 6-3 PBQ-02 Python Basics for Quants_strict_resource_validation_practice.ipynb` | 7 | 0 | 0 |

Execution warnings observed for the strict notebook were environment-level debugger/frozen-module and Windows ZMQ selector warnings only; they did not create cell errors.

## Judge Scores

- Source coverage: 9.6/10
- Accuracy and corrections: 9.5/10
- Notebook reproducibility: 9.4/10
- Additive-only compliance: 9.8/10

Status: PASS
