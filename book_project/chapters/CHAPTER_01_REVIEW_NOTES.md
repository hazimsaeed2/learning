# Chapter 1 Review Notes

## Draft File

`book_project/chapters/CHAPTER_01_WHAT_MARKETS_ARE_ACTUALLY_DOING.md`

## Draft Status

- Generated from scratch using `book_project/CHAPTER_WRITING_STANDARD.md`.
- Chapter status in tracker should remain `drafted`.
- User approval should remain `not_approved`.
- Chapter 2 was not drafted.

## Source Files Used

Planning and control files:

- `book_project/CHAPTER_WRITING_STANDARD.md`
- `book_project/BOOK_CHAPTER_TRACKER.md`
- `book_project/PROJECT_STATUS.md`
- `book_project/EPAT_BOOK_OUTLINE.md`
- `book_project/BOOK_TOPIC_WORKFLOW.md`
- `book_project/BOOK_PRACTICE_MAP.md`
- `book_project/BOOK_SOURCE_INVENTORY.md`
- `book_project/BOOK_GAPS_AND_QUESTIONS.md`
- `book_project/chapters/chapter_01_source_brief.md`

Chapter source files:

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

## Planned Outline Sections Covered

The Chapter 1 teaching spine from `EPAT_BOOK_OUTLINE.md` was preserved:

- Markets as a matching and liquidity system
- Order book depth, spread, and queue priority
- Execution benchmarks: VWAP, TWAP, POV
- Participants, incentives, and adverse selection
- Why market microstructure changes strategy design
- Practice Now: classify execution styles and inspect intraday profiles

## Planned Outline Sections Merged Or Omitted

- No planned outline sections were omitted.
- The sections were kept as explicit chapter sections instead of being merged into generic standard headings.
- Supporting ideas from MMT01, MMT02, and MMT03 were synthesized into the planned section sequence rather than repeated as lecture summaries.

## Notebook And Code References Used

Primary Practice Now reference:

- Code folder: `Week 5-2 MMT-03 code`
- Notebook: `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_validated_practice.ipynb`
- Book-facing notebook section/cell heading: `## Part 3 - Slicing schedules: VWAP, TWAP, POV`

Encoding caveat:

- `BOOK_PRACTICE_MAP.md` and the source notebook display an encoding artifact around the dash in some contexts. The chapter uses a clean ASCII hyphen in the book-facing heading and tells the reader to search for `Part 3` and `Slicing schedules` if their local notebook displays the artifact.

Supporting notebooks considered:

- `Week 3-1 MMT-01 code/Week 3-1 MMT-01 Execution Strategy I_practice.ipynb`
- `Week 3-1 MMT-01 code/Week 3-1 MMT-01 Execution Strategy I_resource_addendum_practice.ipynb`
- `Week 4-1 MMT-02 code/Week 4-1 MMT-02 Execution Strategy II_validated_practice.ipynb`
- `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_resource_addendum_practice.ipynb`

No new notebooks or practice scripts were created.

## Data Files Referenced

- `Week 3-1 MMT-01 code/mmt01_orderbook_abc.csv`
- `Week 3-1 MMT-01 code/mmt01_depth_structure.csv`
- `Week 3-1 MMT-01 code/mmt01_vwap_trades.csv`
- `Week 4-1 MMT-02 code/mmt02_volume_schedule.csv`
- `Week 4-1 MMT-02 code/mmt02_dynamic_discretion_scenarios.csv`
- `Week 4-1 MMT-02 code/mmt02_execution_rules.csv`
- `Week 4-1 MMT-02 code/mmt02_order_specifications.csv`
- `Week 5-2 MMT-03 code/mmt03_intraday_profiles.csv`
- `Week 5-2 MMT-03 code/mmt03_execution_styles.csv`
- `Week 5-2 MMT-03 code/mmt03_market_participants.csv`
- `Week 5-2 MMT-03 code/mmt03_algorithm_taxonomy.csv`

## Visuals Embedded

Copied visuals:

- Source: `Week 3-1 MMT-01 code/chart_1_orderbook_depth.png`
  - Book copy: `book_project/assets/chapter_01/orderbook_depth.png`
  - Used as: Figure 1.1, order-book depth visual.
  - Why needed: supports the hand-checkable example and shows that liquidity is distributed across price levels.
- Source: `Week 5-2 MMT-03 code/chart_3_schedules.png`
  - Book copy: `book_project/assets/chapter_01/execution_schedules.png`
  - Used as: Figure 1.2, execution schedule comparison.
  - Why needed: connects the one-shot order-book example to VWAP, TWAP, and POV slicing.
- Source: `Week 5-2 MMT-03 code/chart_addendum_3_mmt03_intraday_profiles.png`
  - Book copy: `book_project/assets/chapter_01/intraday_profiles.png`
  - Used as: Figure 1.3, intraday profile visual.
  - Why needed: supports the Practice Now section by showing that volume, volatility, and spread conditions vary through the day.

Original source charts were copied, not modified.

## Assumptions Made

- The opening chapter should be beginner-first and concept-heavy, not a code walkthrough.
- The reader is comfortable with basic arithmetic but may not know order-book vocabulary.
- The main worked example should stay small enough to check by hand.
- The chapter should focus on execution realism, while deeper implementation shortfall and TCA math should remain for Chapter 3.
- The book should normalize obvious display encoding artifacts in prose while preserving the source issue in review notes.

## Validation Caveats, Weak Areas, And Source Disagreements Preserved

- No required Chapter 1 source files, code folders, notebooks, data files, or charts were missing.
- MMT01 does not have a `validated_practice.ipynb` file using the same naming pattern as MMT02/MMT03, but it has usable practice notebooks, charts, validation report, execution summary, and data.
- The Chapter 1 source brief records replacement-character issues in one MMT01 resource-addendum notebook; the chapter uses the clean order-book data and source brief for the hand example.
- The MMT03 primary practice heading has an encoding artifact in some contexts; the chapter uses a clean book-facing heading and tells the reader how to find the section.
- MMT03 overlaps with MMT01/MMT02/TIO architecture; the chapter uses it only for participant, schedule, and intraday profile foundations, not as a production architecture chapter.

## Beginner-First Check

Satisfied.

The chapter starts from the practical problem that a trading idea must become orders and fills. It defines the market as a matching and liquidity system before using more specific execution vocabulary.

## Terminology Check

Satisfied.

The `Key Terms Before We Start` table defines the main vocabulary used in the chapter: order, fill, bid, ask, spread, order book, depth, queue priority, market order, limit order, slippage, market impact, VWAP, TWAP, POV, and adverse selection.

## Hand-Example Check

Satisfied.

The hand-checkable example uses a five-level ask book from the MMT01 data and a 40-share market buy. It shows setup, input table, step-by-step fills, intermediate remaining quantity, total cash spent, average fill price, slippage, interpretation, common mistake, and connection to schedule practice.

## Formula/Logic Explanation Check

Satisfied.

The chapter explains:

- `average fill price = total cash spent / total shares filled`
- `slippage per share = average fill price - reference price`
- `net expected result = signal edge - spread cost - market impact - timing cost - fees`

For each, the chapter explains terms, units, what increases/decreases the result, trader use, and misleading mistakes.

## Practice Now Step-By-Step Check

Satisfied.

The Practice Now box includes exact code folder, notebook path, section heading, data file, step-by-step actions, expected output, values/columns/charts to inspect, mistake to check for, and a one-sentence conclusion.

## How To Read The Practice Output Check

Satisfied.

The section explains what the VWAP/TWAP/POV output means, what good output looks like, what weak output means, how it connects to the hand example, and how the reader knows they understood it.

## Master Recap Quality Check

Satisfied.

The Master Recap includes the core mental model, key terms, formulas, worked-example lesson, practice notebook memory, common traps, and final decision checklist.

## Source Claims Precision Check

Satisfied.

The chapter does not claim that any execution algorithm is best or that any strategy works. It frames the material as execution realism, source-supported practice, and evidence interpretation.

## Weak Areas

- The chapter is intentionally conceptual and does not include a full implementation shortfall decomposition; that belongs in Chapter 3.
- The practice heading has an encoding caveat that should be fixed in `BOOK_PRACTICE_MAP.md` or source notebooks in a later cleanup pass if desired.
- The chapter uses existing source charts, not custom book-designed diagrams. This is appropriate for a source-grounded draft but could be redesigned later for final publication.

## What The User Should Approve Or Correct

- Confirm whether the beginner-first depth is appropriate for Chapter 1.
- Confirm whether the practice heading should remain normalized in book-facing text despite the source encoding artifact.
- Confirm whether the three copied visuals are the right amount for the opening chapter.
- Approve Chapter 1 or request revisions before any Chapter 2 work.
