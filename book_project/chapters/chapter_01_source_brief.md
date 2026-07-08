# Chapter 1 Source Brief

## Chapter Title

What Markets Are Actually Doing

## Chapter Purpose

This chapter should give the reader a practical market-structure foundation before any strategy, backtest, or model is introduced. The reader should understand that every strategy ultimately becomes orders interacting with liquidity, spreads, queues, market impact, execution schedules, and venue rules.

## Source Files Verified

Primary generated files:

- `Week 3-1 MMT-01 Execution Strategy - I.html`
- `Week 3-1 MMT-01 Execution Strategy - I_study.html`
- `Week 3-1 MMT-01 Execution Strategy - I_transcript.txt`
- `Week 4-1 MMT-02 Execution Strategy - II.html`
- `Week 4-1 MMT-02 Execution Strategy - II_study.html`
- `Week 4-1 MMT-02 Execution Strategy- II_transcript.txt`
- `Week 5-2 MMT-03 Overview of Electronic and Algorithmic.html`
- `Week 5-2 MMT-03 Overview of Electronic and Algorithmic_study.html`
- `Week 5-2 MMT-03 Overview of Electronic and Algorithmic_transcript.txt`

Original MMT source packets:

- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I/FAQs-MMT-01.pdf`
- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I/LNMMT-01-02ExecutionStrategies.pdf`
- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I/MMT-01-02-Extra-Reading-Execution-Strategy.pdf`
- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I/MMT-01Algorithmic-Trading-Basics.pdf`
- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I/MMT01-Inclass-Exercises-File (1).zip`
- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I/MMT-01Instructions-and-Key-Takeaways.docx.pdf`
- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I/MMT-01-Lecture-Summary.pdf`
- `Market Microstructure for Trading (MMT)/MMT02 Execution Strategy II/LNMMT-01-02ExecutionStrategies.pdf`
- `Market Microstructure for Trading (MMT)/MMT02 Execution Strategy II/MMT-02FAQs.pdf`
- `Market Microstructure for Trading (MMT)/MMT02 Execution Strategy II/MMT02-Inclass-Excercise-File.zip`
- `Market Microstructure for Trading (MMT)/MMT02 Execution Strategy II/MMT-02-Instructions-and-Key-Takeaways (1).pdf`
- `Market Microstructure for Trading (MMT)/MMT02 Execution Strategy II/MMT-02-Lecture-Summary.pdf`
- `Market Microstructure for Trading (MMT)/MMT03 Overview Of Electronic And Algorithmic Trading/MMT03-Lecture-Objectives-Prerequisities.pdf`
- `Market Microstructure for Trading (MMT)/MMT03 Overview Of Electronic And Algorithmic Trading/MMT-03-Lecture-Summary.pdf`
- `Market Microstructure for Trading (MMT)/MMT03 Overview Of Electronic And Algorithmic Trading/MMT-03Overview-of-Electronic-and-Algorithmic-Trading.pdf`

## Notebook/Data Files Verified

MMT01:

- `Week 3-1 MMT-01 code/Week 3-1 MMT-01 Execution Strategy I_practice.ipynb`
- `Week 3-1 MMT-01 code/Week 3-1 MMT-01 Execution Strategy I_resource_addendum_practice.ipynb`
- `Week 3-1 MMT-01 code/mmt01_depth_structure.csv`
- `Week 3-1 MMT-01 code/mmt01_orderbook_abc.csv`
- `Week 3-1 MMT-01 code/mmt01_pro_rata_sell_10.csv`
- `Week 3-1 MMT-01 code/mmt01_vwap_trades.csv`

MMT02:

- `Week 4-1 MMT-02 code/Week 4-1 MMT-02 Execution Strategy II_practice.ipynb`
- `Week 4-1 MMT-02 code/Week 4-1 MMT-02 Execution Strategy II_resource_addendum_practice.ipynb`
- `Week 4-1 MMT-02 code/Week 4-1 MMT-02 Execution Strategy II_validated_practice.ipynb`
- `Week 4-1 MMT-02 code/microsoft_intraday.csv`
- `Week 4-1 MMT-02 code/mmt02_dynamic_discretion_scenarios.csv`
- `Week 4-1 MMT-02 code/mmt02_execution_rules.csv`
- `Week 4-1 MMT-02 code/mmt02_order_specifications.csv`
- `Week 4-1 MMT-02 code/mmt02_volume_schedule.csv`

MMT03:

- `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_practice.ipynb`
- `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_resource_addendum_practice.ipynb`
- `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_validated_practice.ipynb`
- `Week 5-2 MMT-03 code/mmt03_algorithm_taxonomy.csv`
- `Week 5-2 MMT-03 code/mmt03_decision_process.csv`
- `Week 5-2 MMT-03 code/mmt03_execution_styles.csv`
- `Week 5-2 MMT-03 code/mmt03_intraday_profiles.csv`
- `Week 5-2 MMT-03 code/mmt03_market_participants.csv`
- `Week 5-2 MMT-03 code/mmt03_strategy_classification.csv`

## Exact Primary Practice Now Notebook Path

`Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_validated_practice.ipynb`

## Exact Primary Practice Now Section Heading

`## Part 3 — Slicing schedules: VWAP, TWAP, POV`

This heading was verified directly from the notebook using UTF-8 reading. `book_project/BOOK_PRACTICE_MAP.md` was corrected to remove mojibake in this Chapter 1 heading.

## Key Ideas From MMT01

- The order book is the immediate trading reality: bid, ask, spread, depth, and queue shape determine how an order fills.
- A market order can walk through multiple levels of the book, so the visible best price is not the same thing as the actual execution price for a larger order.
- VWAP is a practical execution benchmark because it weights prices by traded volume.
- Time horizon matters: theoretical time to trade and practical time horizon constrain whether a desired order can be completed responsibly.
- Order-flow imbalance is a useful first intuition for how pressure on one side of the book can translate into price impact.
- Small execution differences, including one basis point, can matter at institutional scale.

## Key Ideas From MMT02

- Execution is a placement problem, not only a signal problem: where and how an order is placed changes expected value.
- VWAP can be used both as a benchmark and as a schedule for slicing execution through the day.
- Discretion and pegging rules should be conditional, not emotional; the algorithm should become more aggressive only when the economics justify it.
- Time-horizon gates help decide whether an order can finish under realistic volume and urgency assumptions.
- Significant-size checks and guardrails help prevent poor execution behavior.
- Execution tactics can reduce cost, but abusive behavior such as spoofing is not a legitimate trading process.

## Key Ideas From MMT03

- Market impact has temporary and permanent components, and a trader must manage both.
- The trader's dilemma is the urgency tradeoff: execute quickly and pay impact, or execute slowly and accept timing risk.
- VWAP, TWAP, and POV are schedule families with different assumptions about time, volume, and participation.
- Agency and principal execution differ in how risk, cost, and incentives are allocated.
- Electronic venues differ by order book structure, NBBO logic, midpoint/dark-pool behavior, smart routing, and maker-taker economics.
- Algorithmic trading is a decision process: choose order type, route, urgency, schedule, and risk guardrails based on objective and market state.

## Recommended Hand-Checkable Example

Use a five-level ask book from `Week 3-1 MMT-01 code/mmt01_orderbook_abc.csv` and ask the reader to buy 40 shares with a market order.

Example structure:

| Ask level | Ask price | Ask quantity | Shares filled | Cash spent |
|---:|---:|---:|---:|---:|
| 1 | 100.50 | 15 | 15 | 1,507.50 |
| 2 | 101.00 | 35 | 25 | 2,525.00 |
| Total |  |  | 40 | 4,032.50 |

Hand-checkable result:

- Average execution price = 4,032.50 / 40 = 100.8125
- Best ask was 100.50, but the actual average execution price was higher because the order walked the book.

This example should appear before any formula-heavy discussion. It makes spread, depth, and market impact concrete.

## Charts/Tables/Data Worth Referencing

MMT01:

- `Week 3-1 MMT-01 code/mmt01_orderbook_abc.csv`
- `Week 3-1 MMT-01 code/mmt01_depth_structure.csv`
- `Week 3-1 MMT-01 code/mmt01_vwap_trades.csv`
- `Week 3-1 MMT-01 code/chart_1_orderbook_depth.png`
- `Week 3-1 MMT-01 code/chart_2_vwap.png`
- `Week 3-1 MMT-01 code/chart_3_ofi_impact.png`

MMT02:

- `Week 4-1 MMT-02 code/mmt02_volume_schedule.csv`
- `Week 4-1 MMT-02 code/mmt02_dynamic_discretion_scenarios.csv`
- `Week 4-1 MMT-02 code/mmt02_order_specifications.csv`
- `Week 4-1 MMT-02 code/chart_addendum_1_mmt02_volume_schedule.png`
- `Week 4-1 MMT-02 code/chart_addendum_2_mmt02_dynamic_discretion.png`
- `Week 4-1 MMT-02 code/chart_addendum_3_mmt02_order_logic_flow.png`

MMT03:

- `Week 5-2 MMT-03 code/mmt03_intraday_profiles.csv`
- `Week 5-2 MMT-03 code/mmt03_algorithm_taxonomy.csv`
- `Week 5-2 MMT-03 code/mmt03_execution_styles.csv`
- `Week 5-2 MMT-03 code/mmt03_market_participants.csv`
- `Week 5-2 MMT-03 code/chart_3_schedules.png`
- `Week 5-2 MMT-03 code/chart_4_costdist.png`
- `Week 5-2 MMT-03 code/chart_addendum_2_mmt03_algorithm_taxonomy.png`
- `Week 5-2 MMT-03 code/chart_addendum_3_mmt03_intraday_profiles.png`

## Common Mistakes/Failure Modes To Teach

- Treating the quoted best bid/ask as the guaranteed execution price for the full order size.
- Ignoring depth and assuming liquidity at the top of book is enough.
- Judging a strategy by alpha signal only, without modeling spread, impact, and timing risk.
- Using VWAP as a magic execution guarantee instead of a benchmark or schedule with assumptions.
- Choosing VWAP, TWAP, or POV without matching the schedule to volume profile, urgency, and participation constraints.
- Confusing temporary market impact with permanent information impact.
- Ignoring queue priority, partial fills, and order-type behavior.
- Treating dark pools, midpoint fills, maker-taker rebates, and smart routing as free improvements without adverse-selection risk.
- Discussing algorithms without guardrails, such as maximum participation, price limits, and practical time horizon.

## Missing Files Or Weak Areas

- No missing Chapter 1 root HTML, study, transcript, source-packet, code-folder, notebook, or data files were found during preflight.
- MMT01 has practice and resource-addendum notebooks but no `validated_practice.ipynb` counterpart in the same naming pattern as MMT02/MMT03. This is not a blocker because MMT01 still has a validation report, execution summary, charts, and source-backed notebooks.
- The `Week 3-1 MMT-01 Execution Strategy I_resource_addendum_practice.ipynb` headings contain question-mark replacement characters in a few headings. Prefer the clean `Week 3-1 MMT-01 Execution Strategy I_practice.ipynb` headings for Chapter 1 prose references.
- The primary Chapter 1 Practice Now heading in `BOOK_PRACTICE_MAP.md` had mojibake and was corrected to the verified UTF-8 heading.

