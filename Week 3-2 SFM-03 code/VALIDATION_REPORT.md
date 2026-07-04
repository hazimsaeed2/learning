# SFM-03 Validation Report

## 1. Files reviewed

Validation instructions:
- `CHEAT_SHEET_CREATION_PROMPT.md`
- Attached validation prompt from `.codex/attachments/83ea0f9d-e0db-4a79-8b85-43e641069a4f/pasted-text.txt`

EPAT intro context:
- `intro/EPAT-Orientation-Presentation-batch-69.pdf`
- `intro/EPAT-Structure..pdf`
- `intro/EPATGuideMap.pdf`
- `intro/Tentative-Lecture-ScheduleBatch-68.pdf`

Existing SFM-03 study pack:
- `Week 3-2 SFM-03 Practical Session Basic Statistics using Excel_transcript.txt`
- `Week 3-2 SFM-03 Practical Session Basic Statistics using Excel_study.html`
- `Week 3-2 SFM-03 Practical Session Basic Statistics using Excel.html`
- `Week 3-2 SFM-03 code/Week 3-2 SFM-03 Basic Statistics_practice.ipynb`
- `Week 3-2 SFM-03 code/portfolio_sbi_icici.csv`
- `Week 3-2 SFM-03 code/nifty.csv`
- `Week 3-2 SFM-03 code/chart_1_frontier.png`
- `Week 3-2 SFM-03 code/chart_2_montecarlo.png`
- `Week 3-2 SFM-03 code/chart_3_bollinger.png`

Official SFM-03 resources:
- `Statistics for Financial Markets (SFM)/SFM-03 Practical session Basic Statistics using Excel/SFM-03-Lecture-Summary.docx.pdf`
- `Statistics for Financial Markets (SFM)/SFM-03 Practical session Basic Statistics using Excel/SFM-03FAQs.pdf`
- `Statistics for Financial Markets (SFM)/SFM-03 Practical session Basic Statistics using Excel/SFM-03Instructions-and-Key-Takeaways.docx.pdf`
- `Statistics for Financial Markets (SFM)/SFM-03 Practical session Basic Statistics using Excel/SFM-03Practical-Session-Basic-Statistics-using-ExcelLN.pdf`
- `Statistics for Financial Markets (SFM)/SFM-03 Practical session Basic Statistics using Excel/SFM03-Inclass-Exercises-Files.zip`
- `Statistics for Financial Markets (SFM)/SFM-03 Practical session Basic Statistics using Excel/SFM03PracticeExercises.zip`

Files inspected inside archives:
- `SFM_03_data_Raw_Data.xlsm`
- `SFM_03_data_Raw_Data_Solution1.xlsm`
- `SFM_03_other_explanations.xlsm`
- `SFM_03_Exercise_Template.xlsx`
- `SFM_03_Student_Instruction_Document.docx`
- `SFM_03_Worked_Solution.xlsx`

## 2. Existing strengths

The original SFM-03 pack already covered the main lecture arc: log returns, sample variance and Bessel correction, covariance, efficient-frontier construction, random walk price ranges, annualization, simple-vs-log return drift, Monte Carlo VaR and expected shortfall, and Bollinger Bands. The original notebook used the real lecture datasets and executed successfully.

## 3. Missing transcript content

| Missing item | Source location | Required destination | Action taken |
| --- | --- | --- | --- |
| Transcript risk limit around 1.03% and how it changes the portfolio answer | Transcript opening portfolio problem | Study guide, cheat sheet, notebook | Added source-difference table and frontier chart comparing 1.03%, 1.303%, and 2.7% limits. |
| Excel use-case boundary: Excel for back-of-the-envelope work, Python for larger/repeatable research | Transcript Q&A | Study guide, cheat sheet | Added modern best-practice warning. |
| Independence should be tested, not assumed | Transcript Q&A | Study guide, cheat sheet | Added warning to test autocorrelation, regimes, skew, kurtosis, and volatility clustering. |
| Expected shortfall explanation via average of outcomes below the VaR threshold | Transcript Q&A | Study guide, cheat sheet, notebook | Added formula map with `AVERAGEIF` and addendum Monte Carlo output. |

## 4. Missing resource content

| Missing item | Resource file | Required destination | Action taken |
| --- | --- | --- | --- |
| Exact official Bessel sample `[2051, 2053, 2055, 2050, 2051]`, population mean 2050, sample mean 2052 | `SFM_03_other_explanations.xlsm` | Study guide, cheat sheet, notebook | Added full arithmetic table and chart. |
| Workbook formula map for log returns, mean, stdev, covariance, portfolio variance, Monte Carlo, VaR, ES, Bollinger | `SFM_03_data_Raw_Data_Solution1.xlsm` | Study guide, cheat sheet, notebook | Added formula map and reusable Python equivalents. |
| Slide-deck problem statement with 2.7% volatility limit | `SFM-03Practical-Session-Basic-Statistics-using-ExcelLN.pdf` | Study guide, cheat sheet, notebook | Added source-difference comparison against transcript limits. |
| 20-day Monte Carlo details, percentile range, and expected shortfall | `SFM-03Practical-Session-Basic-Statistics-using-ExcelLN.pdf` | Study guide, cheat sheet, notebook | Added formula map and reproducible MC addendum. |
| Practice exercise pack using HDB, SBIN, and NIFTY from Stooq | `SFM03PracticeExercises.zip` | Study guide, cheat sheet, notebook, data files | Added exercise answer-key table, extracted CSVs, and notebook section. |
| FAQ cautions on normality, fat tails, annualization, log-vs-simple consistency | `SFM-03FAQs.pdf` | Study guide, cheat sheet | Added and reinforced warnings and best-practice notes. |

## 5. Source differences and alternatives

| Topic | Lecture method | Resource method | Difference | When to use each | Action taken |
| --- | --- | --- | --- | --- | --- |
| Portfolio risk limit | Transcript uses about 1.03% daily volatility, with a possible 1.303% wording artifact | Slide deck states 2.7% volatility | The feasible set changes. 1.03% gives a near-ICICI mix; 2.7% makes every sampled portfolio feasible. | Use the transcript limit to understand investor risk aversion; use 2.7% when following the official slide problem. | Added comparison table and chart. |
| Simple vs log Monte Carlo | Lecture prefers log returns because continuous compounding avoids drift correction | Workbook also shows simple-return MC with drift `mu - sigma^2/2` | Both can be valid if used consistently. | Use log returns for additive multi-period modeling; use simple returns only with drift correction and consistency checks. | Preserved both methods in addendum. |
| VaR and ES | Transcript explains VaR floor and expected shortfall conversationally | Workbook uses `PERCENTILE` and `AVERAGEIF` | Same idea, different implementation detail. | Use formulas in Excel; use percentiles and conditional means in Python. | Added formula map. |
| Bollinger Bands | Lecture discusses mean reversion and normal-range intuition | Workbook specifies 20-period average and 20-period sample stdev bands | Workbook is the exact spreadsheet implementation. | Use lecture intuition to interpret; use workbook formula for reproduction. | Added exact `SMA20 +/- 2*STDEV.S` formula. |

## 6. Accuracy corrections

| Existing statement/code | Problem | Corrected version | Files updated |
| --- | --- | --- | --- |
| Original notebook's miniature Bessel example used a different five-point sample than the official explanation workbook | It was mathematically fine but not the official workbook sample | Official sample is `[2051, 2053, 2055, 2050, 2051]`, with population variance 7.2, uncorrected sample variance 3.2, corrected sample variance 4.0 | Added to study guide, cheat sheet, addendum notebook, validated composite notebook. Original notebook preserved. |
| Single portfolio answer without source-limit distinction | Transcript and slide deck use different volatility limits | Both limits are documented and compared | Added source-difference chart/table to HTML and notebooks. |

## 7. Expert enhancements added

| Enhancement | Why it matters | Label used | Files updated |
| --- | --- | --- | --- |
| Independence and normality diagnostics | Random walk, annualization, VaR, and Bollinger all rely on assumptions that can fail | Modern best practice | Study guide, cheat sheet |
| Excel vs Python workflow boundary | Prevents using spreadsheets for large, fragile, repeated research workflows | Modern best practice | Study guide, cheat sheet |
| Reproducible Monte Carlo seed | Makes outputs auditable and repeatable | Modern best practice | Addendum notebook, validated notebook |
| Source-difference chart | Shows the practical effect of changing the risk limit | Expert enhancement | HTML, notebooks, chart PNG |
| Validated composite notebook | Preserves original notebook while meeting the strict markdown-before-code rule | Validation enhancement | New notebook, README |

## 8. Notebook and code validation

Executed files:
- `Week 3-2 SFM-03 code/Week 3-2 SFM-03 Basic Statistics_practice.ipynb`
- `Week 3-2 SFM-03 code/Week 3-2 SFM-03 Basic Statistics_resource_addendum_practice.ipynb`
- `Week 3-2 SFM-03 code/Week 3-2 SFM-03 Basic Statistics_validated_practice.ipynb`

Environment and dependencies:
- Python 3.11
- `numpy`, `pandas`, `matplotlib`, `openpyxl`, `nbformat`, `nbclient`, `IPython`
- Working directory: `Week 3-2 SFM-03 code`

Data files used:
- `portfolio_sbi_icici.csv`
- `nifty.csv`
- `sfm03_practice_nifty_returns.csv`
- `sfm03_practice_answer_key.csv`

Execution results:
- Original notebook: 12/12 code cells executed, 0 errors.
- Resource addendum notebook: 9/9 code cells executed, 0 errors.
- Validated composite notebook: 21/21 code cells executed, 0 errors.
- All validated composite code cells have a markdown explanation directly above them.
- All code-cell outputs are embedded.
- No error outputs remain.
- Relative paths work from the lecture code folder.

Warnings:
- Jupyter emitted Windows debugger/frozen-module and `pyzmq` event-loop warnings during execution. These are environment warnings, not notebook failures.

Fixes applied:
- No original SFM-03 notebook cells were changed.
- Added separate addendum and validated composite notebooks to satisfy additive-only preservation and strict validation requirements.

## 9. Final Judge results

| Dimension | Score | Notes |
| --- | ---: | --- |
| Beginner comprehension | 5 | Existing explanation plus addendum now covers transcript, resources, and assumptions. |
| Transcript coverage | 5 | Added risk-limit difference, Q&A workflow cautions, and expected shortfall details. |
| Resource coverage | 5 | Added workbook formula map, exact Bessel sample, practice zip, and FAQ cautions. |
| Alternative-method coverage | 5 | Explicitly compares transcript versus slides and log versus simple returns. |
| Worked examples | 5 | Adds exact workbook arithmetic and practice answer-key values. |
| Terminology | 5 | Key terms remain decoded; addendum clarifies Excel functions and Python equivalents. |
| Code clarity | 5 | Validated composite notebook has markdown before every code cell and visible outputs. |
| Notebook execution | 5 | 21/21 validated notebook code cells executed with no errors. |
| Visuals | 5 | Added three focused addendum charts. |
| Accuracy | 5 | Source differences are disclosed rather than hidden. |
| Practical usefulness | 5 | Adds diagnostics, workflow guidance, and reproducible Monte Carlo. |
| Formatting | 5 | HTML additions are append-only and parse successfully. |

## 10. Final status

PASS — LECTURE COMPLETE

---

## Continuation appendix after interrupted run

This appendix was added without replacing the existing validation report. The user's instruction was to keep existing material and add corrected or missing material beside it.

Additional transcript-only items added:

| Added item | Source location | Destination | Action taken |
| --- | --- | --- | --- |
| Repeated full-sample average is an end-of-window spreadsheet convenience, not a day-one live signal | Transcript around the standard-deviation walkthrough and rebalancing discussion | Study guide, cheat sheet | Added look-ahead/backtest-control note and rolling/expanding-window warning. |
| Rebalancing timing changes the sample mean and volatility | Transcript Q&A on when the portfolio decision is made | Study guide, cheat sheet | Added monthly/weekly/daily rebalance interpretation. |
| 0% to 100% portfolio grid is long-only; negative weights imply shorting and a different trading problem | Transcript efficient-frontier discussion and shorting/pair-trading Q&A | Study guide, cheat sheet | Added long-only versus short-enabled comparison. |
| Excel notation details: locked references and `E-05` scientific notation | Transcript Excel walkthrough | Study guide, cheat sheet | Added spreadsheet decoder table. |
| Expected shortfall should use a dynamic VaR-cell threshold, not a hard-coded cutoff | Transcript expected-shortfall Q&A | Study guide, cheat sheet | Added `AVERAGEIF(range,"<"&VaR_cell)` interpretation. |
| Sudden market shocks can sit outside the old 95% range until volatility catches up | Transcript Q&A on stress periods and independence | Study guide, cheat sheet | Added model-stress checklist and normal-model caveat. |
| Excel is useful for quick checks; Python is preferred for larger/repeated/high-frequency workflows | Transcript Q&A on Excel versus Python | Study guide, cheat sheet | Added tool-boundary note. |

Validation note:
- Original SFM-03 notebook remains unchanged.
- Existing resource addendum notebook remains unchanged.
- Existing validated composite notebook remains unchanged.
- Programmatic notebook inspection after this continuation found no error outputs in any SFM-03 notebook.
- The strict-compliance validated composite notebook was also executed in memory from the lecture code folder: 21/21 code cells, 0 error outputs. The notebook file was not overwritten.
- The original notebook still has 2 code cells without immediately preceding markdown; the validated composite notebook has 0 such gaps and remains the strict-compliance notebook.
