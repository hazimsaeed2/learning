# EPAT Book Gaps and Questions

Inspection date: 2026-07-07

This document records issues to resolve before writing the book. It focuses on source strength, code/explanation balance, duplicated material, source disagreements, and author decisions needed before drafting chapters.

## Topics With Weak Source Material

### Source-only or current-sensitive topics

- `Trading & Back-testing Platforms (TBP)/Supplementary Lecture 1 Large Language Models in Trading`
  - Weakness: No validated week code folder was found, and LLM tooling changes quickly.
  - Book handling: Treat as optional appendix unless refreshed with current, working code and current API guidance.

- `Trading & Back-testing Platforms (TBP)/Supplementary Lecture 2 Quantitative Trading Using AI Agents`
  - Weakness: Source-only and current-sensitive. The Make/OpenAI setup guidance may age quickly.
  - Book handling: Do not include in the main book without a new validation pass.

- `Trading & Back-testing Platforms (TBP)/Tutorial Session - Cloud Computing (Optional)`
  - Weakness: Source PDFs exist, but no validated code/deployment artifact was found.
  - Book handling: Use as a short infrastructure appendix, not as a full chapter.

- `Trading & Back-testing Platforms (TBP)/Live Trading using IB API`
  - Weakness: Source packet exists, but no standalone validated week code folder was found.
  - Book handling: Merge into the API/live-trading chapters with TBP01 and TBP05.

- `Statistics for Financial Markets (SFM)/SFM01 Introduction to Excel`
  - Weakness: Source-only Excel material, no validated Python book artifact.
  - Book handling: Use only as optional appendix/background.

- `Statistics for Financial Markets (SFM)/SFM02 Basic Statistics`
  - Weakness: Source-only for this repo view; practical coverage is stronger in SFM03, PBQ02, DMP01, PRM02.
  - Book handling: Fold key concepts into return/statistics chapters.

### Topics that are strong as lectures but weak as standalone book chapters

- Python tutorials after PBQ-01, PBQ-02, and DMP-01
  - Weakness: Useful exercises, but not conceptually distinct enough for separate chapters.
  - Book handling: Convert into labs and appendices.

- OTS01 General Trading Theory
  - Weakness: Important but broad and philosophical; not purely options despite being in the OTS module.
  - Book handling: Use early as trading-process framing and later as trade-review/discipline support.

- TIO02 regulatory and desk operations
  - Weakness: Regulatory and cost details are time-sensitive.
  - Book handling: Include only with a statement of jurisdiction and a refreshed current-state review before publication.

## Topics Where Code Exists But Explanation Is Weak

- TBP02 REST API
  - Code strength: Multiple source Python scripts, endpoint references, mock logs, WebSocket messages, offline RSI strategy.
  - Explanation gap: Needs a platform-neutral explanation of REST vs WebSocket architecture, authentication, rate limits, retries, idempotency, and order state machines.

- TBP05 Backtest and Live Trade II
  - Code strength: Scripts, IBridgePy reference strategies, cost traps, robot controls.
  - Explanation gap: Needs a clear live-trading control narrative: scheduler, error handling, early close, alerting, reconnects, and kill switches.

- DMP05 QuantiP
  - Code strength: Reusable modules `alpha.py`, `data.py`, `performance_analytics.py`.
  - Explanation gap: Needs a coherent architecture chapter that explains how the modules fit together and how to extend them safely.

- MLT04 Machine Learning Strategy Pipeline
  - Code strength: Walk-forward scripts, feature lists, SHAP selection, batch comparisons, holdout results.
  - Explanation gap: Needs a careful, original teaching sequence for embargoes, feature families, leakage, and why the validated result can fail production readiness.

- TBP03 Blueshift
  - Code strength: MACD, RSI, and PCA stat-arb scripts.
  - Explanation gap: Needs platform-neutral translation so the chapter is not only a Blueshift manual.

## Topics Where Explanation Exists But Code Is Weak

- SFM01 Introduction to Excel
  - Explanation strength: Introductory spreadsheet source materials.
  - Code weakness: No validated Python artifact; not central to a practical Python trading book.

- SFM02 Basic Statistics
  - Explanation strength: Basic statistics source PDFs.
  - Code weakness: No standalone validated folder; use SFM03/PBQ02/PRM02 code instead.

- TBP Cloud Computing
  - Explanation strength: Cloud lecture notes and EC2 setup PDFs.
  - Code weakness: No validated deployment recipe or infrastructure-as-code artifact.

- Live Trading using IB API
  - Explanation strength: Dedicated live-trading source PDF and source zip.
  - Code weakness: No separate validated week folder; live connectivity cannot be locally verified.

- Supplementary LLMs and AI Agents
  - Explanation strength: Source PDFs and zip/setup guide.
  - Code weakness: No current validated code path; highly dependent on current vendor APIs.

## Duplicated Topics

- Python fundamentals
  - Sources: PBQ01, PBQ02, Week 6-1 tutorial, Week 7-1 tutorial, Week 8-1 Python cheat sheet, Week 8-1 DMP tutorial.
  - Resolution: One concise Python/data workflow part, then appendices/labs.

- Moving-average and indicator strategies
  - Sources: EFS01, DMP01, ASQ01, TBP03, TBP05.
  - Resolution: Use as a running example, but avoid retelling the same crossover lesson in every part.

- Backtesting
  - Sources: DMP01 vectorized backtesting, DMP04 event-driven backtesting, TBP03 Blueshift, TBP04/TBP05 live/backtest platforms, OTS06 options backtesting, MLT04 ML backtesting, DMP05 framework.
  - Resolution: Split into vectorized, event-driven, platform, options, ML, and capstone layers.

- Statistical arbitrage
  - Sources: EFS02 pairs trading and MLT05 PCA stat-arb.
  - Resolution: Teach pair trading first, then PCA as a generalization.

- Volatility
  - Sources: ASQ02 GARCH, OTS02 variance premium, OTS04 volatility measurement, OTS05 hedge volatility choice.
  - Resolution: Place measurement and forecasting before options volatility trades.

- Portfolio and risk metrics
  - Sources: SFM03, PBQ02 VaR/ES, EFS01 drawdown/Kelly, PRM01 risk controls, PRM02 portfolio theory, DMP05 performance analytics.
  - Resolution: Teach formulas once, then apply in strategy, portfolio, and operations chapters.

- Live/API workflow
  - Sources: TBP01 IB Python API, TBP02 REST API, TBP04/TBP05 IBridgePy, Live Trading using IB API, TBP cloud optional, TIO01/TIO02 operations.
  - Resolution: Sequence API concepts, platform examples, then operations and governance.

- Machine learning evaluation
  - Sources: MLT01/MLT02 model metrics, MLT04 leakage/holdout pipeline, TBP05 model validation, MLT07 overfit controls.
  - Resolution: Put basic ML metrics in the ML foundations chapter and advanced validation in the ML strategy pipeline chapter.

## Source Disagreements and Corrections To Preserve

- MLT04 batch results conflict
  - Validation found Batch 68 Onwards and Batch 67 saved outcomes differ. Batch 68 had excessive degradation and production readiness false, while a Batch 67 comparison showed a different verdict.
  - Book handling: Use this as a teaching example of versioned data/model evidence, not as a clean success story.

- PRM02 Treynor ratio convention
  - Validation notes preserved the notebook-scaled value and added the standard annual Treynor convention.
  - Book handling: Explain the convention explicitly and avoid silently mixing scales.

- PBQ02 VaR/ES corrected file pair
  - Both `pbq02_var_es_summary.csv` and `pbq02_var_es_summary_corrected.csv` exist.
  - Book handling: Use the corrected calculation and explain the correction if relevant.

- ASQ01/ASQ02 model performance instability
  - Rolling AR/time-series examples can underperform buy-and-hold or shift across data pulls.
  - Book handling: Present as model diagnostics and process, not as an alpha promise.

- TBP05 dependency and README issues
  - Original scripts depend on packages such as scikit-learn; validation added a sklearn-free fallback. The validation report also notes README encoding damage.
  - Book handling: Use the validated fallback for reproducibility and explain the production dependency separately.

- OTS01 dependency fallback
  - Original notebook used SciPy; validated notebook added a fallback for local execution.
  - Book handling: Teach the correct SciPy-based approach, but keep the fallback for reproducible local examples.

- API/live trading evidence
  - TBP01/TBP02/TBP05 have strong mock/offline validation, but live broker connectivity was not validated locally.
  - Book handling: Be explicit that local validation proves logic and controls, not live broker execution.

- Regulatory/current data
  - TIO02 includes `tio02_current_regulatory_update.csv`, but regulations and membership costs can change.
  - Book handling: Verify before publication and label jurisdiction clearly.

## Questions To Answer Before Writing The Book

1. Who is the target reader: beginner Python user, intermediate trader, quant researcher, or professional developer?

2. Should the book be India/NSE-first, US-market-first, or global? The repo mixes Nifty/TCS/HDFCBANK/Indian exchange material with SPY/TSLA/AAPL/IB/Alpaca examples.

3. Should Excel material be included in the main text, or should SFM01/SFM02 be appendix/background only?

4. How much Python basics should the book teach directly versus assuming the reader can already use pandas and notebooks?

5. Should the book use one running strategy example across chapters, or let each module keep its original examples?

6. Should source notebooks be cleaned into a single book code package, or should the book reference the existing week folders as-is?

7. For live trading chapters, should the book be platform-neutral or explicitly teach Interactive Brokers, IBridgePy, Alpaca, and Blueshift?

8. Should LLMs and AI agents be included now, postponed, or treated as a brief appendix requiring current-tool refresh?

9. Should options be a full major part of the book or a compact advanced section?

10. Should the final capstone be equity momentum, statistical arbitrage, ML classification, or options backtesting?

11. What publication stance should the book take on financial advice, disclaimers, jurisdiction, and live trading risk?

12. Should all examples be fully reproducible offline, even if that requires synthetic/mock data, or should some chapters require live broker/vendor access?

13. Should the final book preserve EPAT week labels in chapter notes, or hide week order and present only the new book structure?

14. Do you want the final book to emphasize professional caution and failed/weak strategies as teaching evidence, or prioritize successful examples?

15. What output format is the target: Markdown manuscript, HTML book, PDF/print layout, notebooks plus text, or all of these?

## Recommended Pre-Writing Decisions

- Choose the reader level before drafting any chapter.
- Choose the market focus before rewriting examples.
- Decide whether Python bootcamp content is main text or appendix.
- Decide whether live trading chapters should require live APIs.
- Decide whether to refresh current-sensitive LLM, cloud, and regulatory material.
- Pick one capstone path so the final playbook has a coherent endpoint.

