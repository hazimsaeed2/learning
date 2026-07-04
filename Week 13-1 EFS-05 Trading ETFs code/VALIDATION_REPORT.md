# EFS-05 Validation Report

Lecture: Week 13-1 EFS-05 Trading ETFs

## Files Reviewed

- `Week 13-1 EFS-05 Trading ETFs Equity, FX & Futures Strategies_transcript.txt`
- `Week 13-1 EFS-05 Trading ETFs.html`
- `Week 13-1 EFS-05 Trading ETFs_study.html`
- `Week 13-1 EFS-05 Trading ETFs_practice.ipynb`
- `EFS05-Inclass-Exercises-File.zip`
- Official workbook: `EFS-05_data_ETF_Seminar_Data.xlsx`
- PDF files present: `EFS-05ETF-Seminar.pdf`, `EFS-05-Lecture-Summary.pdf`, `EFS-05FAQs.pdf`, and `EFS-05Instructions-and-Key-Takeaways.pdf`

## Additive Changes Made

- Kept the existing EFS-05 pages, practice notebook, and original chart intact.
- Added the official workbook as a raw source copy.
- Added parsed workbook CSVs and corrected workbook-backed creation/redemption economics.
- Added a comparison showing the existing 3.50m basket is illustrative while the workbook basket is 2.434m.
- Added secondary-market basket snapshots, divisor reference, and ETF trading-model reference.
- Added an addendum notebook and a validated composite notebook.

## Gaps Closed

| Source gap | Additive coverage |
| --- | --- |
| Official workbook not represented locally | Added raw copy, sheet inventory, parsed basket CSV, and workbook-backed notebook. |
| Existing basket differs from workbook source | Preserved existing illustration and added corrected workbook calculation. |
| Secondary-market price snapshots from workbook not used | Added Slide-39/Slide-44 NAV, creation, and redemption snapshot table/chart. |
| Later transcript trading-model section not explicit in local pages | Added ETF strategy ladder reference covering low, mid, high frequency, active ETFs, and leveraged ETFs. |

## Accuracy Notes

- Official workbook Slide-22 stock basket value: 2,434,333.90.
- Cash component: 45,325.00.
- Corrected creation cost per ETF: 24.8453.
- Corrected redemption proceeds per ETF: 24.7479.
- Corrected round-trip cost per ETF: 0.0974.
- The existing 3,500,046.10 basket and 35.52/35.38 values are preserved as an illustration, not edited.

## Notebook Validation

| Notebook | Code cells | Errors | Markdown-before-code gaps | Execution exception |
| --- | ---: | ---: | ---: | --- |
| `Week 13-1 EFS-05 Trading ETFs_practice.ipynb` | 11 | 0 | 4 | None |
| `Week 13-1 EFS-05 Trading ETFs_resource_addendum_practice.ipynb` | 4 | 0 | 0 | None |
| `Week 13-1 EFS-05 Trading ETFs_validated_practice.ipynb` | 15 | 0 | 4 | None |

## Judge Scores

- Source coverage: 9.3/10
- Accuracy and corrections: 9.6/10
- Notebook reproducibility: 9.7/10
- Additive-only compliance: 9.8/10

Status: PASS
