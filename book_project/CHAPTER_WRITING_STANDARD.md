# Chapter Writing Standard

This file is the master chapter-generation standard for the EPAT practical trading book. It applies before any chapter is drafted. It must be read with:

- `book_project/EPAT_BOOK_OUTLINE.md`
- `book_project/BOOK_TOPIC_WORKFLOW.md`
- `book_project/BOOK_PRACTICE_MAP.md`
- `book_project/BOOK_SOURCE_INVENTORY.md`
- `book_project/BOOK_GAPS_AND_QUESTIONS.md`

The standard is additive, not destructive. It adds beginner-first textbook teaching requirements, but it must not replace each chapter's own planned outline, topic sequence, practice reference, source evidence, or validation caveats.

## Core Principle

Each chapter must read like a real book chapter.

The reader should be able to:

1. Read the chapter without running code.
2. Understand the concept from plain English, examples, tables, visuals, and trading interpretation.
3. Later open the referenced notebook, code, and data and reproduce the practice.
4. Return one year later, read the Master Recap, and remember the chapter.

The chapter is the teaching artifact. The notebook is the practice artifact. Do not make the chapter a notebook walkthrough, lecture summary, cheat sheet, or checklist.

## Core Voice

Preserve these rules:

- Write as a senior trading educator and quant researcher.
- Start from the practical trading problem.
- Prefer plain English before equations or code.
- Use course files as source evidence, but rewrite explanations as original educational prose.
- Do not copy lecture wording except short labels, formulas, file names, notebook headings, and unavoidable technical terms.
- Treat weak or failed results as useful evidence.
- Avoid promotional language.
- Use precise claims: "this backtest shows," not "this strategy works."
- Reference code as practice material, not as the main teaching.
- Be honest about evidence quality: gross vs net, in-sample vs out-of-sample, mock vs live, local validation vs broker execution.
- Do not imply profitability, robustness, or production readiness unless the source validation supports it.

## Priority Rule: Preserve The Chapter Teaching Spine

Every chapter must preserve its own topic-specific flow.

The standard sections are added around the chapter's natural teaching flow. They must not flatten every chapter into the same generic structure.

For each chapter:

- Use the planned chapter sections from `book_project/EPAT_BOOK_OUTLINE.md`.
- Use the topic sequencing and learning path from `book_project/BOOK_TOPIC_WORKFLOW.md`.
- Use the exact primary practice reference from `book_project/BOOK_PRACTICE_MAP.md`.
- Use `book_project/BOOK_SOURCE_INVENTORY.md` to confirm source files, notebooks, data files, charts, and source strength.
- Use `book_project/BOOK_GAPS_AND_QUESTIONS.md` to preserve weak areas, duplicated topics, source disagreements, and current-sensitive caveats.
- If a planned outline section is important, keep it as its own section.
- If two planned outline sections are merged, explain this in the chapter review notes.
- Do not silently omit planned sections.
- Do not promote supporting tutorials or duplicated material into the main chapter unless the outline/workflow makes it central.

Example:

If Chapter 1 includes:

- Markets as a matching and liquidity system
- Order book depth, spread, and queue priority
- Execution benchmarks: VWAP, TWAP, POV
- Participants, incentives, and adverse selection
- Why microstructure changes strategy design

Then all of those ideas must appear clearly in the chapter. The required standard sections may frame, introduce, summarize, and test those ideas, but they may not replace them.

## Required Chapter Structure

Every chapter must include the following, while preserving chapter-specific planned sections:

1. Why This Matters
2. Chapter Map
3. Key Terms Before We Start
4. Plain-English Explanation
5. Chapter-specific teaching sections from `EPAT_BOOK_OUTLINE.md`
6. Detailed hand-checkable example
7. Formula or logic only after intuition
8. Visual anchor, if useful
9. Real trading interpretation
10. What can go wrong
11. Practice Now
12. How To Read The Practice Output
13. Master Recap: What To Remember One Year From Now
14. Check Yourself with answer hints
15. Bridge to the next chapter

The exact section order may be adjusted only when the chapter's teaching spine requires it. If adjusted, the review notes must explain why.

Do not use these sections as empty headings. Each section must teach something concrete.

## Beginner-First Requirement

Every chapter must be understandable by a motivated reader with zero prior knowledge of that chapter's topic.

Define important vocabulary before using it heavily.

The teaching flow should move from:

1. The practical trading problem.
2. The beginner mental model.
3. The key terms.
4. The chapter-specific teaching sequence.
5. The hand-checkable example.
6. The formula, logic, or decision rule.
7. The trading interpretation.
8. The notebook practice.

If the topic is technical, the first explanation must still be plain enough for a first-time reader to follow. This applies to GARCH, PCA, options Greeks, reinforcement learning, REST APIs, portfolio optimization, NLP, backtesting platforms, market microstructure, and live-trading operations.

## Chapter Map Requirement

Near the beginning, include:

```markdown
## Chapter Map
```

Explain 3-5 big ideas:

- what problem this chapter solves
- what mental model the reader needs
- what example, calculation, table, or scenario they will learn
- what practice notebook reinforces it
- what mistake the chapter helps avoid

The chapter map should orient the reader. It should not become a table of contents copied from the outline.

## Key Terms Requirement

Include:

```markdown
## Key Terms Before We Start
```

Use this table:

| Term | Plain-English Meaning | Why It Matters In Practice |
|---|---|---|

Only include terms used in the chapter.

The table should define the vocabulary needed to read the chapter, not every term from the source lecture. Avoid generic glossary dumping.

## Hand-Checkable Example Requirement

Every chapter must include one detailed example the reader can check without code.

It must include:

- setup
- small table, dataset, decision table, or scenario
- step-by-step calculation or reasoning
- intermediate result
- final result
- interpretation
- common mistake
- connection to practice notebook or code

If the chapter is conceptual, use a realistic decision table or operational scenario instead of a numeric calculation. The example must still be checkable without running a notebook.

Examples by chapter type:

- Market microstructure: small order book and fill calculation.
- Expected value: small payoff table.
- Backtesting: signal, position, return alignment over a few rows.
- Statistics: short return series and formula calculation.
- ML: small train/test or confusion-matrix example.
- Options: payoff, Greek sensitivity, or hedge adjustment example.
- APIs/live trading: request, response, order-state, or failure-handling scenario.
- Operations/regulation: risk-control or incident-response table.

## Formula Requirement

When a formula appears, explain:

- each term
- units
- what increases it
- what decreases it
- how a trader uses it
- what can make it misleading

Formula placement matters. Do not lead with equations before the reader has the intuition.

If there is no formula, state the decision rule or logic in simple steps and explain how it can fail.

Do not use formulas as decoration. Each formula must support a trading, research, risk, or operational decision.

## Visual Anchor Requirement

Check source folders for useful charts, tables, or diagrams.

Use `book_project/BOOK_SOURCE_INVENTORY.md` to identify available charts and tables. Prefer existing validated source visuals when they improve understanding.

If useful:

- copy the chart into `book_project/assets/chapter_XX/`
- embed it in the chapter
- add a caption explaining what to see and why it matters
- preserve the original source chart unchanged

Do not create decorative charts.

Do not duplicate charts that say the same thing.

Do not modify original source charts, original EPAT source files, notebooks, data files, or weekly code folders.

If no visual is useful, do not force one. Explain in review notes why no visual was used.

## Practice Now Requirement

Each chapter must have exactly one main Practice Now box.

Use the exact primary practice reference from `book_project/BOOK_PRACTICE_MAP.md`.

The Practice Now box must include:

- exact code folder
- exact notebook path
- exact notebook section/cell heading
- exact data file used
- step-by-step actions
- what output appears
- what values, columns, charts, or tables to inspect
- what mistake to check for
- one-sentence conclusion the reader should be able to write

Do not create new practice code unless explicitly approved.

Supporting notebooks, scripts, or data files may be mentioned in review notes, but the chapter should not scatter multiple competing practice assignments through the prose.

The practice must reinforce the chapter's central concept. It should not introduce a disconnected side topic.

## How To Read The Practice Output Requirement

After Practice Now, include:

```markdown
## How To Read The Practice Output
```

Explain:

- what the output means
- what good output looks like
- what weak or failed output means
- how the output connects to the hand example
- how the reader knows they understood it

If the notebook output is mocked, local-only, dependency-limited, weak, failed, or not live-validated, say that clearly.

Use validation caveats from `book_project/BOOK_GAPS_AND_QUESTIONS.md` and any relevant validation reports. Weak evidence should be taught as evidence quality, not hidden.

## Master Recap Requirement

Replace short summaries with:

```markdown
## Master Recap: What To Remember One Year From Now
```

This must be strong enough for future review.

Include:

- core mental model
- key terms
- key formula or decision rule
- main worked example lesson
- practice notebook memory
- common traps
- final decision checklist

The Master Recap is not a short "chapter summary." It is the reader's durable memory aid. It should let the reader reconstruct the chapter's practical lesson after a long gap.

## Check Yourself Requirement

Include 5-8 questions with answer hints.

Must include:

- conceptual question
- calculation or interpretation question
- failure-mode question
- practice-output question
- real-world decision question

Each question must include a short answer hint or expected answer bullet.

Questions should test the chapter's actual decision logic. Avoid trivia and copied lecture phrasing.

## Review Notes Requirement

Every chapter must create review notes in `book_project/chapters/`.

Review notes must include:

- source files used
- planned outline sections covered
- planned outline sections merged or omitted
- notebook/code references used
- data files referenced
- visuals embedded or why none were used
- assumptions made
- validation caveats, weak areas, or source disagreements preserved from `BOOK_GAPS_AND_QUESTIONS.md`
- beginner-first check
- terminology check
- hand-example check
- formula/logic explanation check
- Practice Now step-by-step check
- How To Read The Practice Output check
- Master Recap quality check
- whether source claims are precise and not overstated
- weak areas
- what user should approve or correct

Review notes are the audit trail. They should make it clear how the chapter used the source material and where the chapter made judgment calls.

## Preview Requirement

After drafting any chapter:

- regenerate `book_project/final/EPAT_Practical_Trading_Book_preview.html`
- regenerate `book_project/final/EPAT_Practical_Trading_Book_preview.md`
- keep unfinished chapters as placeholders
- update `book_project/final/BOOK_PREVIEW_STATUS.md`
- update `book_project/BOOK_CHAPTER_TRACKER.md`

Do not generate final publication-ready HTML or PDF unless explicitly requested.

The living preview must show drafted chapters in full and unfinished chapters as placeholders only. Do not write future chapter prose inside placeholders.

## Source And Validation Guardrails

Source-grounded accuracy is mandatory.

Before drafting a chapter:

- Read the chapter's row and planned sections in `EPAT_BOOK_OUTLINE.md`.
- Read the chapter's workflow entry in `BOOK_TOPIC_WORKFLOW.md`.
- Read the chapter's exact practice reference in `BOOK_PRACTICE_MAP.md`.
- Check source strength, notebooks, data, charts, and assessment in `BOOK_SOURCE_INVENTORY.md`.
- Check weak material, duplicated topics, source disagreements, and open questions in `BOOK_GAPS_AND_QUESTIONS.md`.

Preserve known caveats:

- Current-sensitive regulatory, cloud, LLM, AI-agent, API, and live-trading content requires refreshed verification before publication.
- Mock or offline API validation proves logic and controls, not live broker execution.
- ML, RL, NLP, and options examples must not be presented as automatic alpha.
- Backtests must distinguish gross, net, in-sample, out-of-sample, holdout, dependency-limited, and production-readiness evidence.
- Source disagreements, corrected files, and validation fallbacks must be surfaced when relevant.

Do not write from a single source when a chapter combines several topics. Synthesize the sources into one coherent lesson.

## Project Output Rules

- Draft chapter files must be created in `book_project/chapters/`.
- Chapter review notes must be created in `book_project/chapters/`.
- Copied visuals and book-specific assets must live under `book_project/assets/chapter_XX/`.
- Living preview outputs must be placed in `book_project/final/`.
- Final assembled manuscripts, exports, or print-ready outputs must be placed in `book_project/final/` only when explicitly requested.

Never modify original EPAT source files, original notebooks, weekly code folders, original data files, original charts, or root lecture HTML files unless the user explicitly asks for source-file maintenance.

## Non-Negotiable Chapter Quality Checklist

Before a chapter draft or revision is considered complete, verify:

- The chapter preserves the planned outline sections from `EPAT_BOOK_OUTLINE.md`.
- The chapter preserves the workflow logic from `BOOK_TOPIC_WORKFLOW.md`.
- The chapter uses the exact primary practice reference from `BOOK_PRACTICE_MAP.md`.
- The chapter is source-grounded in `BOOK_SOURCE_INVENTORY.md`.
- Weak areas and source disagreements from `BOOK_GAPS_AND_QUESTIONS.md` are handled honestly.
- A beginner can understand the chapter without external resources.
- Terms are defined before heavy use.
- The chapter includes `## Chapter Map`.
- The chapter includes `## Key Terms Before We Start`.
- The main idea is taught with a detailed hand-checkable example.
- Formula terms, units, directional effects, trader usage, and misleading mistakes are explained.
- A useful visual/table is embedded, or review notes explain why not.
- Practice Now tells the reader exactly what to run and what to inspect.
- The chapter explains how to interpret notebook output in `## How To Read The Practice Output`.
- `## Master Recap: What To Remember One Year From Now` can refresh the chapter after one year.
- `## Check Yourself` includes answer hints or expected answer bullets.
- Code is referenced as practice, not used as the main teaching.
- Trading claims are precise and not overstated.
- No new notebooks or practice scripts are created unless explicitly approved.
- Original weekly source folders are not modified.
- The living preview HTML and Markdown are regenerated after chapter drafting.
- `BOOK_PREVIEW_STATUS.md` and `BOOK_CHAPTER_TRACKER.md` are updated after chapter drafting.
