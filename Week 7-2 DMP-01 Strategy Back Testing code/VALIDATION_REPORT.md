# DMP-01 Validation Report

Lecture: Week 7-2 DMP-01 Strategy Back Testing using Python

## Files Reviewed

- `Week 7-2 DMP-01 Strategy Back Testing using Python_transcript.txt`
- `Week 7-2 DMP-01 Strategy Back Testing using Python.html`
- `Week 7-2 DMP-01 Strategy Back Testing using Python_study.html`
- `Week 7-2 DMP-01 Strategy Back Testing_practice.ipynb`
- `DMP01-Tutorial-Inclass-Exercises-File.zip`
- Official zip contents: `DMP_01_code_Tutorial Session.ipynb`, `DMP_01_data_tutorial_nse.csv`, `Log Returns vs Simple Returns.xlsx`
- PDF files present: `DMP-01Strategy-Back-Testing-using-Python.pdf`, `DMP01-Lecture-Summary.pdf`, `DMP01-FAQs.pdf`

## Additive Changes Made

- Kept the existing DMP-01 pages, practice notebook, local NSE CSV, and equity chart intact.
- Added raw source copies from the official tutorial zip.
- Added an addendum notebook and a validated composite notebook.
- Added workbook-derived simple/log return reference data.
- Added long/short SMA50/SMA200 crossover outputs, metrics, and charts.
- Added an event-style loop equivalence check.
- Added continuation sections to the cheat sheet and study guide.

## Gaps Closed

| Source gap | Additive coverage |
| --- | --- |
| Official source notebook not represented locally | Added source copy, workflow reference, resource addendum notebook, and validated composite. |
| Excel workbook on log versus simple returns | Added parsed workbook reference CSV and chart. |
| Formal seven-step vectorized workflow | Added workflow map and CSV reference. |
| Long/short moving-average crossover from source notebook | Added local SMA50/SMA200 implementation on NSE data with shifted positions. |
| Quantstats-style performance review | Added local metrics: total return, CAGR, annualized volatility, Sharpe, drawdown, exposure, and trade count. |
| Event-driven preview | Added for-loop event-style check that matches the vectorized result. |

## Accuracy Notes

- The official source NSE CSV matches the existing local `nse_daily.csv` after parsing.
- The local long/short SMA50/SMA200 crossover is a warning example, not a recommendation: buy-and-hold returns +27.82%, while the shifted long/short strategy returns -52.73%.
- The event-loop check matches the vectorized shifted-position method exactly for the long-flat SMA12 example: final equity 1.544583 in both, absolute difference 0.0.
- PDF text extraction tools/libraries were not available in this workspace; the validation relied on the transcript, source zip notebook/workbook, and existing generated pages for textual cross-checks.

## Notebook Validation

| Notebook | Code cells | Errors | Markdown-before-code gaps |
| --- | ---: | ---: | ---: |
| `Week 7-2 DMP-01 Strategy Back Testing_practice.ipynb` | 10 | 0 | 0 |
| `Week 7-2 DMP-01 Strategy Back Testing_resource_addendum_practice.ipynb` | 6 | 0 | 0 |
| `Week 7-2 DMP-01 Strategy Back Testing_validated_practice.ipynb` | 16 | 0 | 0 |

Execution warnings observed were environment-level debugger/frozen-module and Windows ZMQ selector warnings only; they did not create notebook cell errors.

## Judge Scores

- Source coverage: 9.3/10
- Accuracy and corrections: 9.5/10
- Notebook reproducibility: 9.7/10
- Additive-only compliance: 9.8/10

Status: PASS
