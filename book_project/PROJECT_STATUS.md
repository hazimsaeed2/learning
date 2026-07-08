# Project Status

Updated: 2026-07-07

## Files Moved Into `book_project/`

- `BOOK_SOURCE_INVENTORY.md` -> `book_project/BOOK_SOURCE_INVENTORY.md`
- `BOOK_TOPIC_WORKFLOW.md` -> `book_project/BOOK_TOPIC_WORKFLOW.md`
- `BOOK_GAPS_AND_QUESTIONS.md` -> `book_project/BOOK_GAPS_AND_QUESTIONS.md`
- `EPAT_BOOK_OUTLINE.md` -> `book_project/EPAT_BOOK_OUTLINE.md`
- `BOOK_PRACTICE_MAP.md` -> `book_project/BOOK_PRACTICE_MAP.md`
- `CHAPTER_WRITING_STANDARD.md` -> `book_project/CHAPTER_WRITING_STANDARD.md`

## Folders Created

- `book_project/`
- `book_project/chapters/`
- `book_project/assets/`
- `book_project/final/`

## Files Already Existed

- The six planning files already existed in the repository root before cleanup.
- `book_project/` did not exist before this cleanup.
- No duplicate planning files existed inside `book_project/`, so no root-vs-project conflict needed merging.

## Missing Files

- No required planning files are missing.
- No chapter draft files exist yet in `book_project/chapters/`.
- No book-specific assets exist yet in `book_project/assets/`.
- No final assembled outputs exist yet in `book_project/final/`.

## Internal Reference Updates

- `book_project/EPAT_BOOK_OUTLINE.md` now points to `book_project/CHAPTER_WRITING_STANDARD.md`.
- `book_project/CHAPTER_WRITING_STANDARD.md` now points to:
  - `book_project/BOOK_SOURCE_INVENTORY.md`
  - `book_project/BOOK_TOPIC_WORKFLOW.md`
  - `book_project/BOOK_PRACTICE_MAP.md`
- `book_project/BOOK_CHAPTER_TRACKER.md` was created to track chapter status, source briefs, drafts, review notes, approvals, and next actions.
- Future chapter prompts must read `book_project/BOOK_CHAPTER_TRACKER.md` first.
- Chapter status must be updated in `book_project/BOOK_CHAPTER_TRACKER.md` after each source brief, draft, approval, or revision.
- Future chapter drafts are directed to `book_project/chapters/`.
- Shared book-specific assets are directed to `book_project/assets/`.
- Final assembled outputs are directed to `book_project/final/`.

## Where The Next Chapter Should Be Written

Write Chapter 1 here:

`book_project/chapters/CHAPTER_01_WHAT_MARKETS_ARE_ACTUALLY_DOING.md`

## Chapter 1 Preflight

Status: completed on 2026-07-07.

Preflight brief created:

`book_project/chapters/chapter_01_source_brief.md`

Files verified:

- `Week 3-1 MMT-01 Execution Strategy - I.html`
- `Week 3-1 MMT-01 Execution Strategy - I_study.html`
- `Week 3-1 MMT-01 Execution Strategy - I_transcript.txt`
- `Week 4-1 MMT-02 Execution Strategy - II.html`
- `Week 4-1 MMT-02 Execution Strategy - II_study.html`
- `Week 4-1 MMT-02 Execution Strategy- II_transcript.txt`
- `Week 5-2 MMT-03 Overview of Electronic and Algorithmic.html`
- `Week 5-2 MMT-03 Overview of Electronic and Algorithmic_study.html`
- `Week 5-2 MMT-03 Overview of Electronic and Algorithmic_transcript.txt`
- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I/`
- `Market Microstructure for Trading (MMT)/MMT02 Execution Strategy II/`
- `Market Microstructure for Trading (MMT)/MMT03 Overview Of Electronic And Algorithmic Trading/`
- `Week 3-1 MMT-01 code/`
- `Week 4-1 MMT-02 code/`
- `Week 5-2 MMT-03 code/`

Chapter 1 notebooks and data verified:

- `Week 3-1 MMT-01 code/Week 3-1 MMT-01 Execution Strategy I_practice.ipynb`
- `Week 3-1 MMT-01 code/Week 3-1 MMT-01 Execution Strategy I_resource_addendum_practice.ipynb`
- `Week 3-1 MMT-01 code/mmt01_orderbook_abc.csv`
- `Week 3-1 MMT-01 code/mmt01_depth_structure.csv`
- `Week 3-1 MMT-01 code/mmt01_vwap_trades.csv`
- `Week 3-1 MMT-01 code/mmt01_pro_rata_sell_10.csv`
- `Week 4-1 MMT-02 code/Week 4-1 MMT-02 Execution Strategy II_practice.ipynb`
- `Week 4-1 MMT-02 code/Week 4-1 MMT-02 Execution Strategy II_resource_addendum_practice.ipynb`
- `Week 4-1 MMT-02 code/Week 4-1 MMT-02 Execution Strategy II_validated_practice.ipynb`
- `Week 4-1 MMT-02 code/microsoft_intraday.csv`
- `Week 4-1 MMT-02 code/mmt02_volume_schedule.csv`
- `Week 4-1 MMT-02 code/mmt02_dynamic_discretion_scenarios.csv`
- `Week 4-1 MMT-02 code/mmt02_execution_rules.csv`
- `Week 4-1 MMT-02 code/mmt02_order_specifications.csv`
- `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_practice.ipynb`
- `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_resource_addendum_practice.ipynb`
- `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_validated_practice.ipynb`
- `Week 5-2 MMT-03 code/mmt03_intraday_profiles.csv`
- `Week 5-2 MMT-03 code/mmt03_algorithm_taxonomy.csv`
- `Week 5-2 MMT-03 code/mmt03_execution_styles.csv`
- `Week 5-2 MMT-03 code/mmt03_market_participants.csv`
- `Week 5-2 MMT-03 code/mmt03_strategy_classification.csv`
- `Week 5-2 MMT-03 code/mmt03_decision_process.csv`

Files missing:

- No required Chapter 1 HTML, study, transcript, source-packet, code, notebook, chart, or data files are missing.
- MMT01 does not use the `validated_practice.ipynb` naming pattern, but it has practice notebooks, source data, charts, validation report, and execution summary.

Practice-map correction made:

- `book_project/BOOK_PRACTICE_MAP.md` now uses the exact verified notebook heading `## Part 3 — Slicing schedules: VWAP, TWAP, POV` instead of the mojibake form.

Primary Practice Now reference for Chapter 1:

- Notebook: `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_validated_practice.ipynb`
- Section heading: `## Part 3 — Slicing schedules: VWAP, TWAP, POV`

## Exact Next Prompt To Use

Use this prompt next:

```text
Read book_project/BOOK_CHAPTER_TRACKER.md first. Then use book_project/PROJECT_STATUS.md, book_project/chapters/chapter_01_source_brief.md, book_project/EPAT_BOOK_OUTLINE.md, book_project/BOOK_PRACTICE_MAP.md, book_project/BOOK_SOURCE_INVENTORY.md, book_project/BOOK_TOPIC_WORKFLOW.md, and book_project/CHAPTER_WRITING_STANDARD.md.

Write Chapter 1 only: "What Markets Are Actually Doing".

Create the file:
book_project/chapters/CHAPTER_01_WHAT_MARKETS_ARE_ACTUALLY_DOING.md

After drafting, update book_project/BOOK_CHAPTER_TRACKER.md for Chapter 1.

Follow CHAPTER_WRITING_STANDARD.md exactly:
1. Why this matters
2. Plain-English explanation
3. Small hand-checkable example
4. Formula or logic only after intuition
5. Real trading interpretation
6. What can go wrong
7. Practice Now box
8. Expected notebook output
9. Chapter summary
10. Check-yourself questions

Use the verified Chapter 1 source brief and exact primary Practice Now notebook reference:
Notebook: Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_validated_practice.ipynb
Section heading: ## Part 3 — Slicing schedules: VWAP, TWAP, POV

Write original textbook prose. Do not copy lecture text. Stop after Chapter 1.
```
