# EPAT Book Source Inventory

Inspection date: 2026-07-07

This inventory is a planning document for a practical trading book. It records the source material and the usable book assets found in the EPAT repository. It does not draft chapters.

## Repository Layers Found

- Original course source folders: `Market Microstructure for Trading (MMT)`, `Statistics for Financial Markets (SFM)`, `Python Basics Its Quant Ecosystem (PBQ)`, `Data Analysis & Modeling in Python (DMP)`, `Advanced Statistics for Quant Strategies (ASQ)`, `Equity, FX, & Futures Strategies (EFS)`, `Portfolio Optimization & Risk Management (PRM)`, `Options Trading & Strategies (OTS)`, `Machine Learning for Trading (MLT)`, `Trading & Back-testing Platforms (TBP)`, `Trading Tech, Infra & Operations (TIO)`, and `intro`.
- Generated lecture pages: root-level `Week *.html` pages, study guides, and transcript text/HTML files where available.
- Validated practice assets: 45 week-specific code folders with notebooks, CSV/Excel data files, charts, README files, validation reports, and execution summaries.
- Repository-level validation: `VALIDATION_QUEUE.md`, `VALIDATION_COVERAGE_AUDIT.md`, `VALIDATION_COVERAGE_AUDIT.csv`, and `VALIDATION_COVERAGE_AUDIT.json`. The audit reports 45 completed lecture validations and no remaining validation coverage gaps.
- Book/build folder: `book_assets` exists, but no files were present in it at the final inspection pass.

## Source-Only Or Supporting Packets

These topics are present in the original source folders but are not always represented as standalone validated week code folders. They should be merged into chapters or appendices, not blindly treated as core chapters.

| Topic | Source files found | Code/notebooks/data/charts | Teaches | Assessment |
|---|---|---|---|---|
| Intro/orientation | `intro/EPATGuideMap.pdf`, `intro/EPAT-Structure..pdf`, `intro/EPAT-Orientation-Presentation-batch-69.pdf`, `intro/Tentative-Lecture-ScheduleBatch-68.pdf` | No topic code folder | Program orientation and course map | Useful context only; not a book chapter. |
| SFM01 Introduction to Excel | Source PDFs and exercise zips under `Statistics for Financial Markets (SFM)/SFM01 Introduction to Excel` | No validated week code folder | Spreadsheet basics and introductory finance workflow | Weak for a Python-first trading book; use as optional appendix. |
| SFM02 Basic Statistics | Source PDFs and exercise zips under `Statistics for Financial Markets (SFM)/SFM02 Basic Statistics` | No standalone week code folder; SFM03 validates practical statistics | Basic descriptive statistics | Duplicated by SFM03 and later risk/stat chapters; use as background. |
| PBQ optional tutorial after PBQ-01 | `PBQ01-Tutorial-Inclass-Exercises-File.zip` | Week 6-1 validated tutorial code exists | Python remedial practice | Supporting lab, not core chapter. |
| PBQ optional tutorial after PBQ-02 | `PBQ02TutorialClassFiles.zip` | Week 7-1 validated tutorial code exists | Pandas and data cleanup practice | Supporting lab, not core chapter. |
| DMP original packet | `DMP-01Strategy-Back-Testing-using-Python.pdf`, `DMP-02-03-04-Lecture-Summary.pdf`, `DMP-05QuantiPyLN.pdf`, Python practice zips, guided mini-project zips | Validated DMP week folders cover the usable code | Backtesting, OOP, event-driven architecture, QuantiP | Strong as source support; split across book chapters. |
| TBP cloud computing optional | Cloud lecture notes, EC2 overview, AMI launch guide under `Trading & Back-testing Platforms (TBP)/Tutorial Session - Cloud Computing (Optional)` | No validated week code folder | Cloud deployment basics | Useful for live-trading appendix; needs modernization before book treatment. |
| TBP Live Trading using IB API | `Live-Trading-Using-IB-API.pdf`, lecture objectives, source zip | Related coverage in TBP01 and TBP05 code folders | Broker connection and live trading flow | Source-only and platform-specific; merge with live trading workflow. |
| TBP supplementary LLMs in trading | `Large-Language-Models-for-Trading.pdf`, `AlpacaAccountSetupGuide.pdf`, `LLMsforTradingPython.zip` | No validated week code folder | LLM-assisted trading workflow | Weak/current-sensitive; include only if refreshed. |
| TBP supplementary AI agents | `Quantitative-Trading-Using-AI-Agents-1.pdf`, OpenAI/Make setup guide | No validated week code folder | AI-agent automation | Weak/current-sensitive; requires current API/tool verification before inclusion. |

## Validated Week/Topic Inventory

### Week 3-1 MMT-01 Execution Strategy I

- Source files: `Week 3-1 MMT-01 Execution Strategy - I.html`, `Week 3-1 MMT-01 Execution Strategy - I_study.html`, `Week 3-1 MMT-01 Execution Strategy - I_transcript.txt`; original packet in `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I`.
- Code folder: `Week 3-1 MMT-01 code`
- Notebooks: `Week 3-1 MMT-01 Execution Strategy I_practice.ipynb`, `Week 3-1 MMT-01 Execution Strategy I_resource_addendum_practice.ipynb`
- Data files: `mmt01_depth_structure.csv`, `mmt01_orderbook_abc.csv`, `mmt01_pro_rata_sell_10.csv`, `mmt01_vwap_trades.csv`
- Charts: `chart_1_orderbook_depth.png`, `chart_2_vwap.png`, `chart_3_ofi_impact.png`, `chart_addendum_1_orderbook_depth.png`, `chart_addendum_2_vwap.png`, `chart_addendum_3_ofi_impact.png`
- Teaches: order books, depth, VWAP, order-flow imbalance, market impact intuition.
- Assessment: Strong concept foundation; lighter than later topics on validated notebooks but very useful early in the book.

### Week 3-2 SFM-03 Practical Session Basic Statistics using Excel

- Source files: `Week 3-2 SFM-03 Practical Session Basic Statistics using Excel.html`, study guide, transcript; original packet in `Statistics for Financial Markets (SFM)/SFM-03 Practical session Basic Statistics using Excel`.
- Code folder: `Week 3-2 SFM-03 code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `nifty.csv`, `portfolio_sbi_icici.csv`, `sfm03_practice_answer_key.csv`, `sfm03_practice_nifty_returns.csv`
- Charts: `chart_1_frontier.png`, `chart_2_montecarlo.png`, `chart_3_bollinger.png`, `chart_addendum_1_sfm03_limit_comparison.png`, `chart_addendum_2_sfm03_bessel_sample.png`, `chart_addendum_3_sfm03_practice_mc.png`
- Teaches: mean, variance, standard deviation, Monte Carlo intuition, Bollinger-style statistics, basic portfolio math.
- Assessment: Strong for statistics bridge; duplicated by PRM02 and PBQ02 in places but useful as the first quantitative chapter support.

### Week 4-1 MMT-02 Execution Strategy II

- Source files: `Week 4-1 MMT-02 Execution Strategy - II.html`, study guide, transcript; original packet in `Market Microstructure for Trading (MMT)/MMT02 Execution Strategy II`.
- Code folder: `Week 4-1 MMT-02 code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `microsoft_intraday.csv`, `mmt02_dynamic_discretion_scenarios.csv`, `mmt02_execution_rules.csv`, `mmt02_order_specifications.csv`, `mmt02_volume_schedule.csv`
- Charts: `chart_1_vwap.png`, `chart_2_ev.png`, `chart_addendum_1_mmt02_volume_schedule.png`, `chart_addendum_2_mmt02_dynamic_discretion.png`, `chart_addendum_3_mmt02_order_logic_flow.png`
- Teaches: execution algorithms, dynamic discretion, volume schedules, order specifications.
- Assessment: Strong for execution chapter; practical and distinct from strategy alpha material.

### Week 4-2 EFS-01 Strategy Building in Equities

- Source files: `Week 4-2 EFS-01 Strategy Building in Equities.html`, study guide, transcript; original packet in `Equity, FX, & Futures Strategies (EFS)/EFS01 Strategy Building In Equities`.
- Code folder: `Week 4-2 EFS-01 code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `nifty_daily.csv`, `efs01_assignment_metric_checklist.csv`, `efs01_derivative_signal_rules.csv`, `efs01_expiry_vwap_setup.csv`, `efs01_parameter_surface.csv`
- Charts: `chart_1_strategy.png`, `chart_2_kelly.png`, `chart_3_drawdown.png`, `chart_4_pnl_dist.png`, `chart_addendum_1_efs01_parameter_surface.png`, `chart_addendum_2_efs01_derivative_quadrants.png`, `chart_addendum_3_efs01_expiry_vwap_setup.png`
- Teaches: moving-average systems, in-sample/out-of-sample splits, parameter surfaces, hit ratio, Kelly sizing, drawdown, PnL distribution.
- Assessment: Strong core strategy-design material; some momentum and crossover ideas recur later.

### Week 5-1 PBQ-01 Basics of Python Programming

- Source files: `Week 5-1 PBQ-01 Basics of Python Programming.html`, study guide, transcript; original packet in `Python Basics Its Quant Ecosystem (PBQ)/PBQ01 Basics Of Python Programming`.
- Code folder: `Week 5-1 PBQ-01 code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `TCS.NS.csv`, `pbq01_faq_reference.csv`, `pbq01_library_map.csv`, `pbq01_tcs_signal_counts.csv`, `pbq01_vectorization_benchmark.csv`, `pbq01_workflow_reference.csv`
- Charts: `chart_1_tcs_signals.png`, `chart_addendum_1_pbq01_vectorization_benchmark.png`, `chart_addendum_2_pbq01_pandas_access_patterns.png`, `chart_addendum_3_pbq01_missing_data_signals.png`
- Teaches: Python syntax, imports, vectorization, pandas access patterns, simple signal counting.
- Assessment: Strong as onboarding; too basic for the main book unless the book assumes no programming background.

### Week 5-2 MMT-03 Overview of Electronic and Algorithmic Trading

- Source files: `Week 5-2 MMT-03 Overview of Electronic and Algorithmic.html`, study guide, transcript; original packet in `Market Microstructure for Trading (MMT)/MMT03 Overview Of Electronic And Algorithmic Trading`.
- Code folder: `Week 5-2 MMT-03 code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `mmt03_algorithm_taxonomy.csv`, `mmt03_decision_process.csv`, `mmt03_execution_styles.csv`, `mmt03_intraday_profiles.csv`, `mmt03_market_participants.csv`, `mmt03_strategy_classification.csv`
- Charts: `chart_1_impact.png`, `chart_2_dilemma.png`, `chart_3_schedules.png`, `chart_4_costdist.png`, `chart_addendum_1_mmt03_market_landscape.png`, `chart_addendum_2_mmt03_algorithm_taxonomy.png`, `chart_addendum_3_mmt03_intraday_profiles.png`
- Teaches: electronic trading participants, algorithm taxonomy, execution styles, intraday profiles, cost distributions.
- Assessment: Strong foundations; overlaps with MMT01, MMT02, and TIO architecture.

### Week 6-1 Tutorial Python after PBQ

- Source files: `Week 6-1 Tutorial Doubt-Solving on Python after PBQ.html`, study guide, transcript; original optional PBQ tutorial zip.
- Code folder: `Week 6-1 Tutorial Python code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `TCS.NS.csv`, `week6_bracket_reference.csv`, `week6_import_reference.csv`, `week6_learning_tools_reference.csv`, `week6_magic_reference.csv`, `week6_tcs_visualization_stats.csv`
- Charts: `chart_1_timeit.png`, `chart_addendum_1_week6_import_decision_flow.png`, `chart_addendum_2_week6_namespace_and_brackets.png`, `chart_addendum_3_week6_tcs_visualization_practice.png`
- Teaches: imports, namespaces, bracket/indexing rules, notebook tools, simple visualization practice.
- Assessment: Useful remedial lab; duplicated by PBQ01/PBQ02 and should be appendix material.

### Week 6-2 TIO-01 System Architecture

- Source files: `Week 6-2 TIO-01 System Architecture.html`, study guide, transcript; original packet in `Trading Tech, Infra & Operations (TIO)/TIO01 System Architecture`.
- Code folder: `Week 6-2 TIO-01 System Architecture code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `tio01_connectivity_latency_reference.csv`, `tio01_exchange_architecture_components.csv`, `tio01_market_data_methods.csv`, `tio01_news_scoring_reference.csv`, `tio01_order_manager_queues.csv`, `tio01_retail_infra_faq.csv`
- Charts: `chart_1_latency.png`, `chart_2_dispersion.png`, `chart_addendum_1_tio01_exchange_side_architecture.png`, `chart_addendum_2_tio01_market_data_methods.png`, `chart_addendum_3_tio01_connectivity_latency_queues.png`, `chart_addendum_4_tio01_news_score_stack.png`
- Teaches: exchange-side architecture, market data methods, latency, order management queues, news scoring stack.
- Assessment: Strong for production architecture; should be later in book after research/backtesting.

### Week 6-3 PBQ-02 Python Basics for Quants

- Source files: `Week 6-3 PBQ-02 Python Basics for Quants.html`, study guide, transcript; original packet in `Python Basics Its Quant Ecosystem (PBQ)/PBQ02 Python Basics For Quants`.
- Code folder: `Week 6-3 PBQ-02 Python Basics for Quants code`
- Notebooks: practice, resource addendum, resource continuation, strict resource validation, and validated practice notebooks.
- Data files: `TCS.NS.csv`, `AXISBANK_data_hygiene.csv`, `pbq02_dataframe_selection_reference.csv`, `pbq02_data_hygiene_summary.csv`, `pbq02_faq_resource_reference.csv`, `pbq02_mini_project_reference.csv`, `pbq02_missing_data_reference.csv`, `pbq02_quant_calculation_reference.csv`, `pbq02_signal_counts.csv`, `pbq02_strict_resource_validation_summary.json`, `pbq02_tcs_addendum_feature_stats.csv`, `pbq02_var_es_summary.csv`, `pbq02_var_es_summary_corrected.csv`
- Charts: `chart_1_tcs.png`, `chart_addendum_1_pbq02_pandas_workflow_map.png`, `chart_addendum_2_pbq02_tcs_returns_rolling.png`, `chart_addendum_3_pbq02_missing_apply_signal_workflow.png`, `chart_continuation_1_pbq02_data_hygiene.png`, `chart_continuation_2_pbq02_var_es.png`, `chart_continuation_2_pbq02_var_es_corrected.png`, `chart_continuation_3_pbq02_resource_bridge.png`
- Teaches: pandas workflow, data hygiene, missing data handling, quant calculations, VaR/ES basics.
- Assessment: Strong practical data chapter support; duplicates later risk metrics but is useful early.

### Week 7-1 Tutorial Python after PBQ-02

- Source files: `Week 7-1 Tutorial Doubt-Solving on Python after PBQ-02.html`, study guide, transcript; original optional PBQ02 tutorial zip.
- Code folder: `Week 7-1 Tutorial Python after PBQ-02 code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `TCS.NS.csv`, `AAPL_daily_tutorial.csv`, `HDFCBANK_exchange_tutorial_raw.csv`, `HDFCBANK_exchange_tutorial_clean.csv`, `PBQ_02_tutorial_data_aapl_daily_source.xls`, `Quote-Equity-HDFCBANK-EQ-19-02-2024-to-19-02-2025_source.xls`, `week7_hdfc_calendar_slice_summary.csv`, `week7_hdfc_feature_sample.csv`, `week7_pandas_tutorial_reference.csv`, `week7_source_file_inventory.csv`, `week7_tutorial_resource_stats.csv`
- Charts: `candles_preview.png`, `chart_1_candles.png`, `chart_addendum_1_week7_source_data_ranges.png`, `chart_addendum_2_week7_hdfc_column_cleanup.png`, `chart_addendum_3_week7_calendar_slicing.png`, `chart_addendum_4_week7_dataframe_modification.png`
- Teaches: exchange data cleanup, calendar slicing, OHLC candles, DataFrame modification.
- Assessment: Strong lab material; should be integrated into data-workflow exercises.

### Week 7-2 DMP-01 Strategy Back Testing using Python

- Source files: `Week 7-2 DMP-01 Strategy Back Testing using Python.html`, study guide, transcript; DMP source packet and guided mini-project.
- Code folder: `Week 7-2 DMP-01 Strategy Back Testing code`
- Notebooks: source tutorial notebook plus practice, resource addendum, and validated practice notebooks.
- Data files: `DMP_01_data_tutorial_nse_source.csv`, `Log Returns vs Simple Returns_source.xlsx`, `nse_daily.csv`, `dmp01_event_vs_vectorized_check.csv`, `dmp01_log_simple_workbook_reference.csv`, `dmp01_long_short_crossover_metrics.csv`, `dmp01_long_short_crossover_sample.csv`, `dmp01_source_file_inventory.csv`, `dmp01_vectorized_workflow_reference.csv`
- Charts: `chart_1_equity.png`, `equity_preview.png`, `chart_addendum_1_dmp01_workflow_map.png`, `chart_addendum_2_dmp01_log_simple_workbook.png`, `chart_addendum_3_dmp01_long_short_crossover.png`, `chart_addendum_4_dmp01_metrics_snapshot.png`, `chart_addendum_5_dmp01_event_loop_check.png`
- Teaches: simple vs log returns, vectorized backtesting, long/short crossover, equity curve, metrics, event-loop check.
- Assessment: Strong core backtesting chapter material.

### Week 7-3 MMT-04 The Algorithmic Trading Process

- Source files: `Week 7-3 MMT-04 The Algorithmic Trading Process.html`; original packet in `Market Microstructure for Trading (MMT)/MMT04 The Algorithmic Trading Process`.
- Code folder: `Week 7-3 MMT-04 The Algorithmic Trading Process code`
- Notebooks: multiple source notebooks for TCA/market impact plus resource addendum and validated practice notebooks.
- Data files: `MMT_04_other_Questions_from_Presentation_Slides_Answers_source.xlsx`, `mmt04_implementation_shortfall_breakdown.csv`, `mmt04_mi_data_diagnostics.csv`, `mmt04_post_trade_metrics.csv`, `mmt04_pre_trade_model_parameters.csv`, `mmt04_source_pdf_inventory.csv`, `mmt04_source_zip_inventory.csv`, `mmt04_tca_example_inputs.csv`, `mmt04_validation_controls.csv`
- Charts: `chart_addendum_1_mmt04_source_inventory.png`, `chart_addendum_2_mmt04_implementation_shortfall.png`, `chart_addendum_3_mmt04_post_trade_metrics.png`, `chart_addendum_4_mmt04_mi_data_diagnostics.png`, `chart_addendum_5_mmt04_pre_trade_model.png`
- Teaches: implementation shortfall, post-trade metrics, market impact parameters, optimal POV, TCA workflow.
- Assessment: Very strong execution and TCA material; essential for practical trading realism.

### Week 8-1 Python Cheat Sheet

- Source files: `Week 8-1 Python_Cheat_Sheet.html`, `CHEAT_SHEET_CREATION_PROMPT.md`
- Code folder: `Week 8-1 Python_Cheat_Sheet code`
- Notebooks: resource addendum and validated practice notebooks.
- Data files: `pycs_common_mistakes.csv`, `pycs_dependency_scope.csv`, `pycs_html_audit.csv`, `pycs_parameter_corrections.csv`, `pycs_return_math_checks.csv`, `pycs_synthetic_backtest_metrics.csv`, `pycs_validation_controls.csv`, `pycs_workflow_controls.csv`
- Charts: `chart_addendum_1_pycs_html_dependency_audit.png`, `chart_addendum_2_pycs_calendar_row_correction.png`, `chart_addendum_3_pycs_synthetic_backtest.png`, `chart_addendum_4_pycs_shift_return_math.png`, `chart_addendum_5_pycs_mistake_controls.png`
- Teaches: common Python and trading-research mistakes, return math, shift discipline, synthetic backtest checks.
- Assessment: Strong reference appendix; overlaps with PBQ/DMP.

### Week 8-1 Tutorial after DMP-01

- Source files: `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01.html`, study guide, text file.
- Code folder: `Week 8-1 Tutorial Python after DMP-01 code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `nifty50_daily.csv`, `dmp01_tutorial_crossover_metrics.csv`, `dmp01_tutorial_csv_roundtrip_timezone.csv`, `dmp01_tutorial_data_inventory.csv`, `dmp01_tutorial_html_audit.csv`, `dmp01_tutorial_notebook_metrics.csv`, `dmp01_tutorial_validation_controls.csv`, `dmp01_tutorial_vectorization_checks.csv`
- Charts: `chart_1_crossover.png`, `chart_addendum_1_dmp01_tutorial_data_notebook_audit.png`, `chart_addendum_2_dmp01_tutorial_csv_timezone.png`, `chart_addendum_3_dmp01_tutorial_crossover_equity.png`, `chart_addendum_4_dmp01_tutorial_signal_position.png`, `chart_addendum_5_dmp01_tutorial_vectorization_controls.png`
- Teaches: crossover practice, CSV round-trips, timezone care, vectorization controls.
- Assessment: Strong lab; duplicate with DMP01, useful as exercises.

### Week 8-2 DMP-02 Introduction to Object Oriented Programming

- Source files: `Week 8-2 DMP-02 Introduction to Object Oriented Programming.html`, study guide, text file; DMP source packet.
- Code folder: `Week 8-2 DMP-02 Introduction to OOP code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `nifty50_daily.csv`, `dmp02_backtest_metrics.csv`, `dmp02_class_design_controls.csv`, `dmp02_html_audit.csv`, `dmp02_notebook_execution.csv`, `dmp02_oop_concept_checks.csv`, `dmp02_source_inventory.csv`, `dmp02_validation_controls.csv`
- Charts: `chart_1_oop.png`, `chart_addendum_1_dmp02_source_notebook_audit.png`, `chart_addendum_2_dmp02_oop_concept_map.png`, `chart_addendum_3_dmp02_backtest_equity.png`, `chart_addendum_4_dmp02_parameter_comparison.png`, `chart_addendum_5_dmp02_method_pipeline.png`
- Teaches: OOP concepts, class design, strategy pipeline encapsulation, parameter comparison.
- Assessment: Strong for code architecture chapter; not a trading alpha chapter by itself.

### Week 9-1 DMP-03 OOP in Python

- Source files: `Week 9-1 DMP-03 Object Oriented Programming In Python.html`, study guide, text file; DMP source packet.
- Code folder: `Week 9-1 DMP-03 OOP in Python code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `eod_prices.csv`, `dmp03_emh_autocorr_checks.csv`, `dmp03_html_audit.csv`, `dmp03_notebook_execution.csv`, `dmp03_ols_backtest_metrics.csv`, `dmp03_return_risk_metrics.csv`, `dmp03_source_inventory.csv`, `dmp03_validation_controls.csv`
- Charts: `chart_1_emh.png`, `chart_addendum_1_dmp03_source_notebook_audit.png`, `chart_addendum_2_dmp03_random_walk_acf.png`, `chart_addendum_3_dmp03_return_risk_drawdown.png`, `chart_addendum_4_dmp03_ols_backtest_equity.png`, `chart_addendum_5_dmp03_validation_summary.png`
- Teaches: EMH/random walk, autocorrelation, OLS strategy demo, return-risk reporting.
- Assessment: Strong bridge from code architecture to empirical market testing.

### Week 9-2 DMP-04 Event-Driven Backtesting

- Source files: `Week 9-2 DMP-04 Event Driven Back-Testing and working with Live Data Stream.html`, study guide, text file; DMP source packet.
- Code folder: `Week 9-2 DMP-04 Event-Driven Backtesting code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `eod_prices.csv`, `dmp04_backtest_sweep_metrics.csv`, `dmp04_event_contract_checks.csv`, `dmp04_html_audit.csv`, `dmp04_notebook_execution.csv`, `dmp04_risk_stats.csv`, `dmp04_source_inventory.csv`, `dmp04_validation_controls.csv`
- Charts: `chart_1_event.png`, `chart_addendum_1_dmp04_source_notebook_audit.png`, `chart_addendum_2_dmp04_event_flow_counts.png`, `chart_addendum_3_dmp04_equity_curve.png`, `chart_addendum_4_dmp04_parameter_sweep.png`, `chart_addendum_5_dmp04_risk_summary.png`
- Teaches: event types, event contracts, backtest loops, parameter sweeps, risk summaries.
- Assessment: Strong core backtesting architecture material.

### Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data

- Source files: root HTML, study guide, text file; original packet in `Advanced Statistics for Quant Strategies (ASQ)/ASQ01 Statistical Analysis of Financial Market Data`.
- Code folder: `Week 10-1 ASQ-01 Statistical Analysis code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `market_data.csv`, `asq01_acf_stationarity_checks.csv`, `asq01_dependency_execution.csv`, `asq01_html_audit.csv`, `asq01_ma_weekly_metrics.csv`, `asq01_rolling_ar_metrics.csv`, `asq01_source_inventory.csv`, `asq01_validation_controls.csv`
- Charts: `chart_1_arima.png`, `chart_addendum_1_asq01_source_dependency_audit.png`, `chart_addendum_2_asq01_price_return_stationarity.png`, `chart_addendum_3_asq01_ma_crossover_equity.png`, `chart_addendum_4_asq01_weekly_acf.png`, `chart_addendum_5_asq01_rolling_ar_equity.png`
- Teaches: stationarity, ACF/PACF, autoregression, ARIMA intuition, rolling forecast strategy.
- Assessment: Strong statistics/time-series chapter; original dependency gap documented in validation.

### Week 10-2 TBP-01 IB Python API

- Source files: root HTML, study guide, text file; original packet in `Trading & Back-testing Platforms (TBP)/TBP01 IB Python API`.
- Code folder: `Week 10-2 TBP-01 IB Python API code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `historical_sample.csv`, `tbp01_historical_data_checks.csv`, `tbp01_html_audit.csv`, `tbp01_live_scope_controls.csv`, `tbp01_mock_api_metrics.csv`, `tbp01_notebook_execution.csv`, `tbp01_source_inventory.csv`, `tbp01_validation_controls.csv`
- Charts: `chart_1_ibapi.png`, `chart_addendum_1_tbp01_source_notebook_audit.png`, `chart_addendum_2_tbp01_sync_async_timing.png`, `chart_addendum_3_tbp01_callback_flow.png`, `chart_addendum_4_tbp01_historical_sample.png`, `chart_addendum_5_tbp01_live_scope_controls.png`
- Teaches: Interactive Brokers API model, callbacks, historical data, sync/async timing, live-scope controls.
- Assessment: Strong teaching material; live API material is mocked/offline for validation.

### Week 11-1 TBP-04 Backtest and Live Trade

- Source files: root HTML, study guide, text file; original packet in `Trading & Back-testing Platforms (TBP)/TBP-04 & 05-Backtest And Live Trade Algo Strategies I & II`.
- Code folder: `Week 11-1 TBP-04 Backtest and Live Trade code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `spy_like_daily.csv`, `tbp04_dependency_execution.csv`, `tbp04_html_audit.csv`, `tbp04_regression_metrics.csv`, `tbp04_source_inventory.csv`, `tbp04_strategy_metrics.csv`, `tbp04_timeframe_controls.csv`, `tbp04_validation_controls.csv`
- Charts: `chart_1_swing.png`, `chart_addendum_1_tbp04_source_dependency_audit.png`, `chart_addendum_2_tbp04_swing_regression.png`, `chart_addendum_3_tbp04_strategy_equity.png`, `chart_addendum_4_tbp04_timeframe_coefficients.png`, `chart_addendum_5_tbp04_scope_controls.png`
- Teaches: regression strategy, swing trading logic, timeframe controls, strategy metrics.
- Assessment: Strong, with original dependency gap documented; overlaps with TBP05 and backtesting chapters.

### Week 12-1 ASQ-02 Time Series Modeling with Python

- Source files: root HTML, study guide, text file; original packet in `Advanced Statistics for Quant Strategies (ASQ)/ASQ02 Time Series Modeling with Python`.
- Code folder: `Week 12-1 ASQ-02 Time Series Modeling code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `market_data.csv`, `asq02_cost_drag_metrics.csv`, `asq02_dependency_execution.csv`, `asq02_fixed_auto_arima_metrics.csv`, `asq02_html_audit.csv`, `asq02_source_inventory.csv`, `asq02_validation_controls.csv`, `asq02_volatility_garch_metrics.csv`
- Charts: `chart_1_arch.png`, `chart_addendum_1_asq02_source_dependency_audit.png`, `chart_addendum_2_asq02_fixed_auto_arima.png`, `chart_addendum_3_asq02_cost_drag.png`, `chart_addendum_4_asq02_volatility_regimes.png`, `chart_addendum_5_asq02_garch_risk_sizing.png`
- Teaches: ARIMA, ARCH/GARCH, volatility regimes, cost drag, risk sizing.
- Assessment: Strong time-series and volatility bridge; original dependency gap documented.

### Week 12-2 TBP-02 REST API

- Source files: root HTML, study guide, transcript text/HTML; original packet in `Trading & Back-testing Platforms (TBP)/TBP02 REST API`.
- Code folder: `Week 12-2 TBP-02 Rest API code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Scripts: Alpaca/REST/WebSocket source scripts including `Real_Time_Data_Using_Websockets_source.py`, RSI strategy files, and API helper files.
- Data files: `historical_sample.csv`, endpoint/status/websocket references, mock request/order/websocket logs, RSI strategy samples and metrics.
- Charts: `chart_1_rest.png`, `chart_addendum_1_tbp02_source_architecture.png`, `chart_addendum_2_tbp02_endpoint_coverage.png`, `chart_addendum_3_tbp02_rest_vs_websocket.png`, `chart_addendum_4_tbp02_offline_rsi_strategy.png`, `chart_addendum_5_tbp02_correction_heartbeat.png`
- Teaches: REST endpoints, status codes, WebSockets, heartbeats, offline RSI strategy, order audit logs.
- Assessment: Strong API workflow; live credentials and broker behavior remain outside local validation.

### Week 13-1 EFS-05 Trading ETFs

- Source files: root HTML, study guide, transcript; original packet in `Equity, FX, & Futures Strategies (EFS)/EFS05 Trading ETFs`.
- Code folder: `Week 13-1 EFS-05 Trading ETFs code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `EFS-05_data_ETF_Seminar_Data_source.xlsx`, `efs05_existing_vs_workbook_basket_comparison.csv`, `efs05_index_divisor_reference.csv`, `efs05_secondary_market_snapshots.csv`, `efs05_source_creation_basket.csv`, `efs05_trading_model_reference.csv`, `efs05_workbook_creation_redemption_corrected.csv`, `efs05_workbook_sheet_inventory.csv`
- Charts: `chart_1_etf.png`, `chart_addendum_1_efs05_workbook_sheet_map.png`, `chart_addendum_2_efs05_corrected_creation_redemption.png`, `chart_addendum_3_efs05_source_nav_snapshots.png`, `chart_addendum_4_efs05_existing_vs_workbook_basket.png`, `chart_addendum_5_efs05_trading_model_ladder.png`
- Teaches: ETF creation/redemption, NAV, baskets, index divisors, ETF trading models.
- Assessment: Strong but specialized; fits a instruments/strategy chapter.

### Week 13-2 OTS-01 General Trading Theory

- Source files: root HTML, study guide, transcript; original packet in `Options Trading & Strategies (OTS)/OTS01 General Trading Theory`.
- Code folder: `Week 13-2 OTS-01 General Trading Theory code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `ots01_compliance_workflow.csv`, `ots01_edge_risk_map.csv`, `ots01_observation_to_business_pipeline.csv`, `ots01_psychology_automation_controls.csv`, `ots01_source_pdf_inventory.csv`, `ots01_trade_review_noise_demo.csv`
- Charts: `chart_1_edge.png`, `chart_addendum_1_ots01_source_coverage.png`, `chart_addendum_2_ots01_observation_to_business.png`, `chart_addendum_3_ots01_edge_risk_map.png`, `chart_addendum_4_ots01_trade_review_noise.png`, `chart_addendum_5_ots01_psychology_automation_controls.png`
- Teaches: trading edge, adverse selection, compliance workflow, observation-to-business conversion, trade review, psychology controls.
- Assessment: Conceptually strong; broad and philosophical, so it should frame trading process rather than become a pure options chapter.

### Week 14-1 EFS-03 Quantitative Momentum Strategies I

- Source files: root HTML, study guide, transcript; original packet in `Equity, FX, & Futures Strategies (EFS)/EFS03 & 04 Quantitative Momentum Strategies - I & II`.
- Code folder: `Week 14-1 EFS-03 Quantitative Momentum Strategies I code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Scripts: `estimateFuturesReturns_source.py`, `GLD_GC_source.py`, `XLE_CL_rollReturn2_source.py`
- Data files: `efs03_back_adjustment_demo.csv`, `efs03_causal_momentum_framework.csv`, `efs03_futures_data_hygiene.csv`, `efs03_gold_hedge_reference.csv`, `efs03_roll_formula_reference.csv`, `efs03_sharpe_funding_cases.csv`, `efs03_source_zip_selection.csv`, `efs03_timestamp_alignment_demo.csv`
- Charts: `chart_1_roll.png`, `chart_addendum_1_efs03_source_inventory.png`, `chart_addendum_2_efs03_causal_momentum_map.png`, `chart_addendum_3_efs03_roll_formula_map.png`, `chart_addendum_4_efs03_back_adjustment_demo.png`, `chart_addendum_5_efs03_timestamp_sharpe_controls.png`
- Teaches: futures momentum, roll return, back-adjustment, hedge relationships, timestamp alignment, funding controls.
- Assessment: Strong, technical, and practical; needs careful prerequisite placement after data and return math.

### Week 14-2 EFS-04 Quantitative Momentum Strategies II

- Source files: root HTML, study guide, transcript; original EFS03/04 source packet.
- Code folder: `Week 14-2 EFS-04 Quantitative Momentum Strategies II code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Scripts: CL, Treasury, VIX/ES, roll-return, and momentum source scripts.
- Data files: `VIX_source.csv`, `efs04_autocorrelation_iid_demo.csv`, `efs04_calendar_levered_etf_reference.csv`, `efs04_momentum_crash_controls.csv`, `efs04_source_zip_selection.csv`, `efs04_strategy_inventory.csv`, `efs04_timestamp_controls.csv`, `efs04_vix_es_hedge_reference.csv`
- Charts: `chart_1_momentum2.png`, `chart_addendum_1_efs04_source_inventory.png`, `chart_addendum_2_efs04_strategy_map.png`, `chart_addendum_3_efs04_vix_es_hedge.png`, `chart_addendum_4_efs04_autocorrelation_iid.png`, `chart_addendum_5_efs04_crash_calendar_levered_controls.png`
- Teaches: momentum regimes, VIX/ES hedge logic, autocorrelation/IID issues, crash controls, leveraged ETF calendar effects.
- Assessment: Strong; overlaps with volatility and risk chapters.

### Week 15-1 PRM-01 Portfolio and Risk Management

- Source files: root HTML, study guide, transcript; original packet in `Portfolio Optimization & Risk Management (PRM)/PRM01 Portfolio Management & Risk Management for Algorithmic Trading`.
- Code folder: `Week 15-1 PRM-01 Portfolio & Risk Management code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `prm01_algo_pretrade_controls.csv`, `prm01_credit_financial_regulatory_reference.csv`, `prm01_incident_control_map.csv`, `prm01_indian_exchange_controls.csv`, `prm01_risk_process_control_matrix.csv`, `prm01_risk_taxonomy.csv`, `prm01_source_pdf_inventory.csv`, `prm01_var_cvar_liquidity_demo.csv`, `prm01_var_cvar_liquidity_reference.csv`
- Charts: `chart_1_risk.png`, `chart_addendum_1_prm01_source_inventory.png`, `chart_addendum_2_prm01_risk_process.png`, `chart_addendum_3_prm01_var_cvar_liquidity.png`, `chart_addendum_4_prm01_incident_controls.png`, `chart_addendum_5_prm01_pretrade_gateway.png`
- Teaches: risk taxonomy, VaR/CVaR, liquidity, incident controls, pre-trade controls.
- Assessment: Strong risk governance material; complements quantitative portfolio math.

### Week 15-2 OTS-02 Volatility Trading and Variance Premium

- Source files: root HTML, study guide, transcript; original packet in `Options Trading & Strategies (OTS)/OTS02 Volatility Trading and Variance Premium`.
- Code folder: `Week 15-2 OTS-02 Volatility Trading and Variance Premium code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `ots02_adverse_selection_cost_demo.csv`, `ots02_edge_framework.csv`, `ots02_iv_hv_surface_reference.csv`, `ots02_iv_surface_demo.csv`, `ots02_live_trading_controls.csv`, `ots02_option_payoff_reference.csv`, `ots02_source_pdf_inventory.csv`, `ots02_variance_premium_demo.csv`, `ots02_variance_premium_reference.csv`, `ots02_volatility_laws.csv`
- Charts: `chart_1_vol.png`, `chart_addendum_1_ots02_source_inventory.png`, `chart_addendum_2_ots02_edge_framework.png`, `chart_addendum_3_ots02_volatility_laws.png`, `chart_addendum_4_ots02_iv_surface.png`, `chart_addendum_5_ots02_variance_premium_controls.png`
- Teaches: realized vs implied volatility, variance premium, volatility laws, adverse selection, IV surfaces, live controls.
- Assessment: Strong conceptual options/volatility bridge; demo data should not be overstated as live edge.

### Week 16-1 TBP-05 Backtest and Live Trade Algo Strategies II

- Source files: root HTML, study guide, transcript; original TBP04/05 packet.
- Code folder: `Week 16-1 TBP-05 code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Scripts: `01_buy_low_sell_high_model.py`, `02_backtest_costs_and_traps.py`, `tbp05_sklearn_free_model_validation.py`, and reference IBridgePy strategy scripts.
- Data files: `SPY.csv`, `tbp05_backtest_trap_controls.csv`, `tbp05_dependency_fallbacks.csv`, `tbp05_existing_code_inventory.csv`, `tbp05_ibridgepy_reference_map.csv`, `tbp05_live_robot_control_matrix.csv`, `tbp05_model_validation_metrics.csv`, `tbp05_source_pdf_inventory.csv`, `tbp05_source_zip_inventory.csv`
- Charts: `chart_1_regression.png`, `chart_2_equity_curve.png`, `chart_3_rate_sweep.png`, `chart_4_cost_impact.png`, `chart_5_out_of_sample.png`, plus five addendum charts on source inventory, dependency validation, backtest honesty, robot controls, and cost/parameter rules.
- Teaches: backtest traps, cost sensitivity, out-of-sample testing, IBridgePy robot controls, model validation.
- Assessment: Strong and very book-relevant; original scripts depend on unavailable packages/platforms, but validated fallbacks exist.

### Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading

- Source files: root HTML, study guide, transcript; original packet in `Equity, FX, & Futures Strategies (EFS)/EFS02 Statistical Arbitrage And Pair Trading`.
- Code folder: `Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `AUDCAD.csv`, `EURCHF.csv`, `EWA.csv`, `EWC.csv`, `efs02_cointegration_vs_correlation.csv`, `efs02_data_inventory.csv`, `efs02_pair_selection_controls.csv`, `efs02_pair_strategy_metrics.csv`, `efs02_risk_management_controls.csv`, `efs02_source_pdf_inventory.csv`, `efs02_source_zip_inventory.csv`, `efs02_stationarity_diagnostics.csv`
- Charts: `chart_1_pairs.png`, `chart_addendum_1_efs02_source_data_inventory.png`, `chart_addendum_2_efs02_stationarity_diagnostics.png`, `chart_addendum_3_efs02_spread_bands.png`, `chart_addendum_4_efs02_pair_controls.png`, `chart_addendum_5_efs02_correlation_vs_cointegration.png`
- Teaches: pairs selection, stationarity, cointegration vs correlation, spread bands, risk controls.
- Assessment: Strong; duplicated later by PCA stat-arb, so the book should sequence pairs first, PCA second.

### Week 17-2 OTS-03 Options Pricing Models and Greeks

- Source files: root HTML, study guide, transcript; original packet in `Options Trading & Strategies (OTS)/OTS03 Options Pricing Models and Greeks`.
- Code folder: `Week 17-2 OTS-03 Options Pricing Models and Greeks code`
- Notebooks: source Black-Scholes notebook plus practice, resource addendum, and validated practice notebooks.
- Data files: `ots03_black_scholes_input_sensitivity.csv`, `ots03_greeks_reference.csv`, `ots03_model_assumption_controls.csv`, `ots03_option_pricing_reference.csv`, `ots03_parity_arbitrage_check.csv`, `ots03_portfolio_greeks.csv`, `ots03_source_pdf_inventory.csv`, `ots03_source_zip_inventory.csv`
- Charts: `chart_1_greeks.png`, `chart_addendum_1_ots03_source_and_dependency_inventory.png`, `chart_addendum_2_ots03_black_scholes_sensitivity.png`, `chart_addendum_3_ots03_greek_surface_reference.png`, `chart_addendum_4_ots03_put_call_parity_arbitrage.png`, `chart_addendum_5_ots03_model_limit_controls.png`
- Teaches: Black-Scholes, Greeks, put-call parity, model assumptions, portfolio Greeks.
- Assessment: Strong options foundation.

### Week 18-1 MLT-01 Machine Learning I

- Source files: root HTML, study guide, transcript; original packet in `Machine Learning for Trading (MLT)/MLT01 Machine Learning-I`.
- Code folder: `Week 18-1 MLT-01 Machine Learning-I code`
- Notebooks: source ML, decision tree/random forest, logistic regression notebooks plus practice, resource addendum, and validated practice notebooks.
- Data files: `ML_Dataset.csv`, `TSLA.csv`, `mlt01_data_inventory.csv`, `mlt01_feature_engineering_audit.csv`, `mlt01_feature_importance_proxy.csv`, `mlt01_gini_impurity_worked_example.csv`, `mlt01_model_validation_metrics.csv`, `mlt01_sklearn_fallback_scope.csv`, `mlt01_source_pdf_inventory.csv`, `mlt01_source_zip_inventory.csv`, `mlt01_split_leakage_controls.csv`
- Charts: `chart_1_ml.png`, `chart_addendum_1_mlt01_source_data_dependency_inventory.png`, `chart_addendum_2_mlt01_gini_impurity_split.png`, `chart_addendum_3_mlt01_time_series_split_controls.png`, `chart_addendum_4_mlt01_model_metrics_vs_base_rate.png`, `chart_addendum_5_mlt01_feature_importance_controls.png`
- Teaches: supervised vs unsupervised learning, logistic regression, trees, random forests, feature engineering, time-series split discipline.
- Assessment: Strong ML foundation; original scikit-learn dependency handled via validated fallback.

### Week 19-1 MLT-02 Machine Learning II

- Source files: root HTML, study guide, transcript; original packet in `Machine Learning for Trading (MLT)/MLT02 Machine Learning-II`.
- Code folder: `Week 19-1 MLT-02 Machine Learning-II code`
- Notebooks: source SVM, clustering, confusion matrix/bias-variance notebooks plus practice, resource addendum, and validated practice notebooks.
- Data files: `TSLA.csv`, `companydata.csv`, `ind_nifty50list.csv`, and MLT02 metrics/inventory/control CSV files.
- Charts: `chart_1_ml2.png`, `chart_addendum_1_mlt02_source_data_dependency_inventory.png`, `chart_addendum_2_mlt02_confusion_metrics.png`, `chart_addendum_3_mlt02_svm_kernel_bias_variance.png`, `chart_addendum_4_mlt02_kmeans_elbow_clusters.png`, `chart_addendum_5_mlt02_model_risk_controls.png`
- Teaches: confusion matrix, bias-variance, SVM kernels, K-Means clustering, leakage audit.
- Assessment: Strong ML evaluation and algorithm chapter support.

### Week 19-2 OTS-04 Volatility Measurement

- Source files: root HTML, study guide, transcript; original packet in `Options Trading & Strategies (OTS)/OTS04 Volatility Measurement, Forecasting, and Structuring Volatility Trades`.
- Code folder: `Week 19-2 OTS-04 Volatility Measurement code`
- Notebooks: source volatility estimation notebook plus practice, resource addendum, and validated practice notebooks.
- Data files: `AAPL.csv`, `NFLX.csv`, `SPY.csv`, plus OTS04 estimator, GARCH fallback, shock diagnostics, variance-premium, strategy-control, and inventory CSV files.
- Charts: `chart_1_ots4.png`, `chart_addendum_1_ots04_source_data_dependency_inventory.png`, `chart_addendum_2_ots04_volatility_estimators.png`, `chart_addendum_3_ots04_rolling_vs_ewma_shock.png`, `chart_addendum_4_ots04_garch_context_forecast.png`, `chart_addendum_5_ots04_variance_premium_controls.png`
- Teaches: realized volatility estimators, rolling vs EWMA, GARCH context, variance premium, vega controls.
- Assessment: Strong; overlaps with ASQ02 and OTS02.

### Week 20-1 MLT-03 Machine Learning III

- Source files: root HTML, study guide, transcript; original packet in `Machine Learning for Trading (MLT)/MLT03 Machine Learning-III`.
- Code folder: `Week 20-1 MLT-03 Machine Learning-III code`
- Notebooks: neural network source notebooks plus practice, resource addendum, and validated practice notebooks.
- Data files: `EURUSD_data.csv`, `EURUSD_backtest.csv`, plus activation/gradient, backtest, feature-indicator, MLP metrics, TF-IDF, model-risk, inventory, and fallback CSV files.
- Charts: `chart_1_mlt3.png`, `chart_addendum_1_mlt03_source_data_dependency_inventory.png`, `chart_addendum_2_mlt03_activation_gradient_reference.png`, `chart_addendum_3_mlt03_mlp_metrics_backtest.png`, `chart_addendum_4_mlt03_feature_indicator_controls.png`, `chart_addendum_5_mlt03_tfidf_model_risk_controls.png`
- Teaches: neural networks, gradient/backprop intuition, EURUSD indicator model, text-mining bridge.
- Assessment: Strong for advanced ML concepts; needs careful caveats on modest signal quality.

### Week 20-2 OTS-05 Trade Evaluation

- Source files: root HTML, study guide, transcript; original packet in `Options Trading & Strategies (OTS)/OTS05 Trade Evaluation`.
- Code folder: `Week 20-2 OTS-05 Trade Evaluation code`
- Notebooks: source Greeks notebook plus practice, resource addendum, and validated practice notebooks.
- Data files: early exercise, Greek reference, hedge frequency, hedge volatility choice, SPY case attribution, strategy comparison, Whalley-Wilmott bands, source inventory CSV files.
- Charts: `chart_1_eval.png`, `chart_addendum_1_ots05_source_dependency_inventory.png`, `chart_addendum_2_ots05_delta_gamma_bands.png`, `chart_addendum_3_ots05_hedge_frequency_dispersion.png`, `chart_addendum_4_ots05_hedge_vol_choice.png`, `chart_addendum_5_ots05_metrics_case_attribution.png`
- Teaches: options trade attribution, hedging frequency, volatility choice, early exercise/dividends, delta/gamma bands.
- Assessment: Strong practical options risk material.

### Week 21-1 OTS-06 Creating an Options Backtesting Model

- Source files: root HTML, study guide, transcript text; original packet in `Options Trading & Strategies (OTS)/OTS06 Creating an Options Backtesting Model`.
- Code folder: `Week 21-1 OTS-06 Creating an Options Backtesting Model code`
- Notebooks: source data-download, long-call, long-strangle notebooks plus practice, resource addendum, and validated practice notebooks.
- Data files: `spx_monthly_2023.csv`, `ots06_backtest_controls.csv`, `ots06_data_inventory.csv`, `ots06_guided_project_inventory.csv`, `ots06_option_chain_quality.csv`, `ots06_sltp_exit_breakdown.csv`, `ots06_source_pdf_inventory.csv`, `ots06_source_zip_inventory.csv`, `ots06_strategy_performance.csv`, `ots06_trading_day_calendar.csv`
- Charts: `chart_1_backtest.png`, `chart_addendum_1_ots06_source_data_inventory.png`, `chart_addendum_2_ots06_spx_calendar_entries.png`, `chart_addendum_3_ots06_strategy_pnl_comparison.png`, `chart_addendum_4_ots06_equity_drawdown.png`, `chart_addendum_5_ots06_backtest_controls.png`
- Teaches: options chain quality, calendar entries, long call/strangle backtesting, SL/TP exits, strategy PnL.
- Assessment: Strong options backtesting material; needs data-quality warnings.

### Week 21-2 MLT-04 Develop a Trading Strategy using Machine Learning

- Source files: root HTML, study guide, transcript; original packet in `Machine Learning for Trading (MLT)/MLT04 How to Develop a Trading Strategy using Machine Learning`.
- Code folder: `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code`
- Notebooks: eight source pipeline notebooks plus practice, resource addendum, and validated practice notebooks.
- Scripts: `mlt04_metrics.py`, `mlt04_models.py`, `mlt04_walkforward.py`
- Data files: feature lists, batch comparison, holdout results, leakage controls, parquet inventory, saved model results, source zip summaries, validation controls.
- Charts: `chart_1_mlt4.png`, `chart_addendum_1_mlt04_source_data_inventory.png`, `chart_addendum_2_mlt04_model_tier_results.png`, `chart_addendum_3_mlt04_holdout_degradation.png`, `chart_addendum_4_mlt04_leakage_inflation.png`, `chart_addendum_5_mlt04_dependency_controls.png`
- Teaches: end-to-end ML strategy research, feature explosion, SHAP selection, hyperparameter tuning, walk-forward testing, holdout degradation, leakage.
- Assessment: Very strong capstone ML material; also contains source disagreement between batch versions and production-readiness verdicts.

### Week 22-1 MLT-05 Statistical Arbitrage with PCA

- Source files: root HTML, study guide, transcript; original MLT05 source packet.
- Code folder: `Week 22-1 MLT-05 Statistical Arbitrage with PCA code`
- Notebooks: source PCA notebook plus practice, resource addendum, and validated practice notebooks.
- Data files: `oil_pair.csv`, `spy_qqq.csv`, `tech_bank.csv`, `top40.csv`, and PCA/cointegration/spread-backtest/inventory/control CSV files.
- Charts: `chart_1_mlt5.png`, `chart_addendum_1_mlt05_source_data_inventory.png`, `chart_addendum_2_mlt05_spy_qqq_pca_diagnostics.png`, `chart_addendum_3_mlt05_explained_variance_clusters.png`, `chart_addendum_4_mlt05_spread_backtests.png`, `chart_addendum_5_mlt05_index_pca_controls.png`
- Teaches: PCA, explained variance, index PCA, PCA-based spreads, Granger/cointegration metrics.
- Assessment: Strong advanced stat-arb chapter; should follow basic pair trading.

### Week 22-2 TBP-03 Backtesting using Blueshift

- Source files: root HTML, study guide, transcript; original packet in `Trading & Back-testing Platforms (TBP)/TBP03 Backtesting using Blueshift`.
- Code folder: `Week 22-2 TBP-03 Backtesting using Blueshift code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Scripts: `TBP03_MACD_source.py`, `TBP03_rsi_strategy_source.py`, `TBP03_Statarb_using_PCA_source.py`
- Data files: `nse_prices.csv`, strategy audit, point-in-time, lookahead-bias, event-engine controls, pair diagnostics, performance, data/dependency/source inventories.
- Charts: `chart_1_blueshift.png`, `chart_addendum_1_tbp03_source_data_dependency_inventory.png`, `chart_addendum_2_tbp03_lookahead_point_in_time.png`, `chart_addendum_3_tbp03_strategy_performance.png`, `chart_addendum_4_tbp03_statarb_pair_diagnostics.png`, `chart_addendum_5_tbp03_event_engine_controls.png`
- Teaches: Blueshift platform, MACD/RSI/PCA stat-arb scripts, point-in-time data, lookahead bias, event-engine controls.
- Assessment: Strong platform-specific backtesting material; should be framed as platform example.

### Week 23-1 MLT-06 NLP and Sentiment Analysis in Trading

- Source files: root HTML, study guide, transcript; original packet in `Machine Learning for Trading (MLT)/MLT06 Natural Language Processing and Sentiment Analysis in Trading`.
- Code folder: `Week 23-1 MLT-06 Natural Language Processing and Sentiment Analysis in Trading code`
- Notebooks: source notebooks for tagging, LSA, MRN content, PermID, state-space sentiment, preprocessing, topic modeling plus practice/addendum/validated notebooks.
- Data files: `MRN-JSON-Sample.json`, `baidu-prices.csv`, `baidu-scores-history.csv`, and NLP metrics/inventory/control CSV files.
- Charts: `chart_1_nlp.png`, `chart_addendum_1_mlt06_source_data_dependency_inventory.png`, `chart_addendum_2_mlt06_text_vectorizer_metrics.png`, `chart_addendum_3_mlt06_sentiment_record_overlay.png`, `chart_addendum_4_mlt06_granger_trading_metrics.png`, `chart_addendum_5_mlt06_validation_controls.png`
- Teaches: text preprocessing, vectorization, topic modeling, sentiment records, Granger-style tests, trading signal metrics.
- Assessment: Strong specialized ML chapter; external data/vendor dependencies must be explained.

### Week 23-2 MLT-07 Reinforcement Learning in Trading

- Source files: root HTML, study guide, transcript; original packet in `Machine Learning for Trading (MLT)/MLT07 Reinforcement Learning in Trading`.
- Code folder: `Week 23-2 MLT-07 Reinforcement Learning in Trading code`
- Notebooks: many source notebooks for action, reward, state, Bellman, experience replay, DQN, synthetic time series, RL main, PnL, performance plus practice/addendum/validated notebooks.
- Data files: `market_daily.csv`, `mlt07_bellman_marshmallow_table.csv`, `mlt07_data_inventory.csv`, `mlt07_dependency_fallback_scope.csv`, `mlt07_dqn_config_controls.csv`, `mlt07_overfit_fattail_metrics.csv`, `mlt07_qlearning_results.csv`, `mlt07_reward_function_reference.csv`, `mlt07_source_pdf_inventory.csv`, `mlt07_source_zip_inventory.csv`, `mlt07_validation_controls.csv`
- Charts: `chart_1_rl.png`, `chart_addendum_1_mlt07_source_data_dependency_inventory.png`, `chart_addendum_2_mlt07_overfit_fattails.png`, `chart_addendum_3_mlt07_market_predictability_checks.png`, `chart_addendum_4_mlt07_qlearning_results.png`, `chart_addendum_5_mlt07_reward_dqn_controls.png`
- Teaches: states/actions/rewards, Bellman logic, Q-learning, DQN controls, overfitting and fat-tail risk.
- Assessment: Strong advanced chapter but should be treated cautiously; RL is not a beginner trading edge.

### Week 24-1 PRM-02 Quantitative Portfolio Management

- Source files: root HTML, study guide, transcript; original packet in `Portfolio Optimization & Risk Management (PRM)/PRM02 Quantitative Portfolio Management`.
- Code folder: `Week 24-1 PRM-02 Quantitative Portfolio Management code`
- Notebooks: source PRM02 notebook plus practice, resource addendum, and validated practice notebooks.
- Data files: `Benchmark.csv`, `MARICO.csv`, `MARUTI.csv`, `TCS.csv`, `nifty50.csv`, `PRM_02_other_Explanations_source.xlsx`, and PRM02 return/risk/frontier/diversification/OOS/control CSV files.
- Charts: `chart_1_portfolio.png`, `chart_addendum_1_prm02_source_data_inventory.png`, `chart_addendum_2_prm02_return_risk.png`, `chart_addendum_3_prm02_diversification_limit.png`, `chart_addendum_4_prm02_frontier_weights.png`, `chart_addendum_5_prm02_oos_risk_controls.png`
- Teaches: covariance, correlation, diversification, efficient frontier, Sharpe/Sortino/Treynor/Calmar/information ratios, VaR/CVaR, out-of-sample controls.
- Assessment: Very strong portfolio chapter; validation notes include Treynor convention correction.

### Week 25-1 DMP-05 QuantiP

- Source files: root HTML, study guide, transcript; DMP source packet.
- Code folder: `Week 25-1 DMP-05 QuantiP code`
- Notebooks: source BAB, beta, single-stock and multi-stock strategy framework notebooks plus practice/addendum/validated notebooks.
- Scripts: `alpha.py`, `data.py`, `performance_analytics.py`
- Data files: `nifty50_list.csv`, `nifty_stocks_prices.csv`, and QuantiP metrics for BAB, beta cross-section, diversification, drawdown recovery, liquidity strategy, costs, inventory, controls.
- Charts: `chart_1_quantip.png`, `chart_addendum_1_dmp05_source_data_dependency_inventory.png`, `chart_addendum_2_dmp05_strategy_costs.png`, `chart_addendum_3_dmp05_diversification.png`, `chart_addendum_4_dmp05_beta_cross_section.png`, `chart_addendum_5_dmp05_bab_oos_controls.png`
- Teaches: reusable quant framework, alpha/data/performance modules, beta and BAB examples, costs, drawdown recovery.
- Assessment: Very strong capstone framework material; should anchor final playbook/code architecture.

### Week 26-1 TIO-02 Desk Operations and Regulatory Environment

- Source files: root HTML, study guide, transcript; original packet in `Trading Tech, Infra & Operations (TIO)/TIO02 Tackling Desk Operations and Regulatory Environment`.
- Code folder: `Week 26-1 TIO-02 Tackling desk operations and Regulatory environment code`
- Notebooks: practice, resource addendum, and validated practice notebooks.
- Data files: `tio02_colocation_network_metrics.csv`, `tio02_current_regulatory_update.csv`, `tio02_dependency_scope.csv`, `tio02_entity_funds_table.csv`, `tio02_latency_paradigm_table.csv`, `tio02_line_latency_cost_table.csv`, `tio02_membership_cost_metrics.csv`, `tio02_operational_risk_controls.csv`, `tio02_platform_ladder.csv`, `tio02_setup_capex_plan.csv`, `tio02_source_pdf_inventory.csv`, `tio02_unit_corrections.csv`, `tio02_validation_controls.csv`
- Charts: `chart_1_deskops.png`, `chart_addendum_1_tio02_source_regulatory_inventory.png`, `chart_addendum_2_tio02_latency_ladder.png`, `chart_addendum_3_tio02_membership_setup_costs.png`, `chart_addendum_4_tio02_colocation_network.png`, `chart_addendum_5_tio02_operational_regulatory_controls.png`
- Teaches: desk setup, membership costs, latency/colocation, operational controls, regulatory environment.
- Assessment: Strong operations material, but regulatory/current-market details are time-sensitive and should be verified before book publication.

