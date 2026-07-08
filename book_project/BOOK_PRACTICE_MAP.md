# Book Practice Map

This map binds each chapter to one primary practice artifact. The notebook section/cell headings are taken from the inspected notebooks. The practice references are skeleton anchors for future chapter writing; they are not chapter prose.

## Practice References By Chapter

### Chapter 1. What Markets Are Actually Doing

- Concept explained: Market participants, algorithm categories, execution schedules, and cost distributions.
- Exact code folder: `Week 5-2 MMT-03 code`
- Exact notebook path: `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_validated_practice.ipynb`
- Exact notebook section/cell heading: `## Part 3 — Slicing schedules: VWAP, TWAP, POV`
- Data file used: `Week 5-2 MMT-03 code/mmt03_intraday_profiles.csv`
- Expected output: Schedule/profile tables and charts comparing execution styles.
- What the reader should observe: Different execution algorithms trade off urgency, market impact, and benchmark tracking.
- How the practice connects to the explanation: It turns the chapter's market-structure discussion into concrete execution schedule choices.

### Chapter 2. From Observation to Tradable Edge

- Concept explained: Expected value, edge, risk, and the difference between win rate and profitable trading.
- Exact code folder: `Week 13-2 OTS-01 General Trading Theory code`
- Exact notebook path: `Week 13-2 OTS-01 General Trading Theory code/Week 13-2 OTS-01 General Trading Theory_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 1. Edge = expected value (the loaded-coin canonical example)`
- Data file used: `Week 13-2 OTS-01 General Trading Theory code/ots01_edge_risk_map.csv`
- Expected output: Edge/risk reference table and expected-value calculations.
- What the reader should observe: A high win rate is not the same thing as positive expected value.
- How the practice connects to the explanation: It gives the chapter's edge definition a small, auditable calculation before moving to trading systems.

### Chapter 3. Transaction Costs, TCA, and Implementation Shortfall

- Concept explained: Implementation shortfall, post-trade metrics, and pre-trade market-impact checks.
- Exact code folder: `Week 7-3 MMT-04 The Algorithmic Trading Process code`
- Exact notebook path: `Week 7-3 MMT-04 The Algorithmic Trading Process code/Week 7-3 MMT-04 The Algorithmic Trading Process_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 2. TCA identity and post-trade checks`
- Data file used: `Week 7-3 MMT-04 The Algorithmic Trading Process code/mmt04_implementation_shortfall_breakdown.csv`
- Expected output: Implementation shortfall component table and post-trade metric summary.
- What the reader should observe: Paper return minus actual return must reconcile to execution, delay, opportunity, and fixed costs.
- How the practice connects to the explanation: It makes cost realism measurable instead of rhetorical.

### Chapter 4. Python for Trading Research

- Concept explained: Python data structures, NumPy vectorization, and simple market-data signal construction.
- Exact code folder: `Week 5-1 PBQ-01 code`
- Exact notebook path: `Week 5-1 PBQ-01 code/Week 5-1 PBQ-01 Basics of Python Programming_validated_practice.ipynb`
- Exact notebook section/cell heading: `## Part 5 â€” NumPy: arrays & vectorisation`
- Data file used: `Week 5-1 PBQ-01 code/TCS.NS.csv`
- Expected output: Vectorized calculations and TCS signal-count output.
- What the reader should observe: Vectorized operations express the same research logic more reliably than manual loops.
- How the practice connects to the explanation: It establishes the core Python mechanics used throughout the rest of the book.

### Chapter 5. Cleaning and Structuring Market Data

- Concept explained: Reading exchange data, cleaning columns, date handling, and DataFrame inspection.
- Exact code folder: `Week 7-1 Tutorial Python after PBQ-02 code`
- Exact notebook path: `Week 7-1 Tutorial Python after PBQ-02 code/Week 7-1 Tutorial Doubt-Solving Python after PBQ-02_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 3. Read a market-data CSV`
- Data file used: `Week 7-1 Tutorial Python after PBQ-02 code/HDFCBANK_exchange_tutorial_raw.csv`
- Expected output: Cleaned market-data frame and source range audit.
- What the reader should observe: Small data issues such as trailing spaces and date parsing can break a research workflow.
- How the practice connects to the explanation: It demonstrates that data cleaning is a trading research control, not clerical work.

### Chapter 6. Building Reusable Strategy Code

- Concept explained: Using OOP to package strategy parameters, methods, and backtest results.
- Exact code folder: `Week 8-2 DMP-02 Introduction to OOP code`
- Exact notebook path: `Week 8-2 DMP-02 Introduction to OOP code/Week 8-2 DMP-02 Introduction to Object Oriented Programming_validated_practice.ipynb`
- Exact notebook section/cell heading: ``## Part 2 — Applying OOP: a `BacktestingCrossover` class``
- Data file used: `Week 8-2 DMP-02 Introduction to OOP code/nifty50_daily.csv`
- Expected output: Two strategy objects with comparable equity curves and parameter metrics.
- What the reader should observe: A strategy object makes parameter comparisons explicit and repeatable.
- How the practice connects to the explanation: It shows why reusable code is needed before scaling from one notebook to a research process.

### Chapter 7. Return Math and Basic Statistics

- Concept explained: Simple returns, log returns, variance, standard deviation, and Bessel correction.
- Exact code folder: `Week 3-2 SFM-03 code`
- Exact notebook path: `Week 3-2 SFM-03 code/Week 3-2 SFM-03 Basic Statistics_validated_practice.ipynb`
- Exact notebook section/cell heading: `## Part 1 â€” Returns from scratch, and why **log** returns`
- Data file used: `Week 3-2 SFM-03 code/nifty.csv`
- Expected output: Return series, summary statistics, and annualized volatility.
- What the reader should observe: Return definitions determine compounding and risk calculations.
- How the practice connects to the explanation: It gives every later performance metric a verified arithmetic foundation.

### Chapter 8. Risk, Drawdowns, and Performance Metrics

- Concept explained: Strategy scorecards, hit ratio, normalized hit ratio, Kelly sizing, and drawdown.
- Exact code folder: `Week 4-2 EFS-01 code`
- Exact notebook path: `Week 4-2 EFS-01 code/Week 4-2 EFS-01 Strategy Building in Equities_validated_practice.ipynb`
- Exact notebook section/cell heading: `## Part 3 â€” Hit ratio and the *normalised* hit ratio`
- Data file used: `Week 4-2 EFS-01 code/efs01_assignment_metric_checklist.csv`
- Expected output: Strategy metric checklist with hit-ratio and payoff-ratio interpretation.
- What the reader should observe: A strategy can have a modest win rate and still have positive expectancy if payoff asymmetry is favorable.
- How the practice connects to the explanation: It ties performance metrics to trading decisions rather than to isolated formulas.

### Chapter 9. Statistical Testing for Market Data

- Concept explained: Stationarity, autocorrelation, and price-vs-return diagnostics.
- Exact code folder: `Week 10-1 ASQ-01 Statistical Analysis code`
- Exact notebook path: `Week 10-1 ASQ-01 Statistical Analysis code/Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 3. Prices vs returns — volatility clustering`
- Data file used: `Week 10-1 ASQ-01 Statistical Analysis code/market_data.csv`
- Expected output: Price/return diagnostic plots and stationarity check tables.
- What the reader should observe: Prices and returns have different statistical behavior; models should not treat them interchangeably.
- How the practice connects to the explanation: It grounds statistical testing in visual and numerical market-data evidence.

### Chapter 10. Time-Series Forecasting and Volatility Models

- Concept explained: ARIMA order selection, transaction-cost drag, volatility clustering, and GARCH forecasting.
- Exact code folder: `Week 12-1 ASQ-02 Time Series Modeling code`
- Exact notebook path: `Week 12-1 ASQ-02 Time Series Modeling code/Week 12-1 ASQ-02 Time Series Modeling with Python_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 6. Forecasting volatility — ARCH & GARCH`
- Data file used: `Week 12-1 ASQ-02 Time Series Modeling code/market_data.csv`
- Expected output: Auto-ARIMA metrics, cost-drag table, volatility-regime chart, and GARCH risk-sizing chart.
- What the reader should observe: Forecasting logic only matters if it survives rolling validation and trading costs.
- How the practice connects to the explanation: It connects time-series intuition to measurable trading and risk-sizing consequences.

### Chapter 11. Indicator Strategies and Rule-Based Systems

- Concept explained: Signal/position alignment, `.shift()`, and vectorized crossover backtesting.
- Exact code folder: `Week 7-2 DMP-01 Strategy Back Testing code`
- Exact notebook path: `Week 7-2 DMP-01 Strategy Back Testing code/Week 7-2 DMP-01 Strategy Back Testing_validated_practice.ipynb`
- Exact notebook section/cell heading: ``## 4. The `.shift()` operator â€” avoiding look-ahead bias``
- Data file used: `Week 7-2 DMP-01 Strategy Back Testing code/nse_daily.csv`
- Expected output: Long/short crossover equity curve and metrics snapshot.
- What the reader should observe: Position lagging is the difference between a valid strategy return and a lookahead error.
- How the practice connects to the explanation: It converts rule-based indicator logic into a correctly aligned backtest.

### Chapter 12. Futures, Momentum, and Regime-Aware Strategies

- Concept explained: Futures roll return, backwardation/contango, and momentum regime controls.
- Exact code folder: `Week 14-1 EFS-03 Quantitative Momentum Strategies I code`
- Exact notebook path: `Week 14-1 EFS-03 Quantitative Momentum Strategies I code/Week 14-1 EFS-03 Quantitative Momentum Strategies I_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 1. Total return = spot return + roll return`
- Data file used: `Week 14-1 EFS-03 Quantitative Momentum Strategies I code/efs03_roll_formula_reference.csv`
- Expected output: Roll-return formula map and forward-curve chart.
- What the reader should observe: Futures momentum depends on contract mechanics, not only price trend.
- How the practice connects to the explanation: It turns a strategy label, momentum, into the specific return components a trader actually earns.

### Chapter 13. ETFs and Tradable Baskets

- Concept explained: ETF index divisor, NAV, creation/redemption, basket mechanics, and arbitrage bands.
- Exact code folder: `Week 13-1 EFS-05 Trading ETFs code`
- Exact notebook path: `Week 13-1 EFS-05 Trading ETFs code/Week 13-1 EFS-05 Trading ETFs_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 4. How in-kind baskets solve BOTH flaws`
- Data file used: `Week 13-1 EFS-05 Trading ETFs code/EFS-05_data_ETF_Seminar_Data_source.xlsx`
- Expected output: Workbook sheet map, corrected creation/redemption table, and basket comparison chart.
- What the reader should observe: ETF tradability comes from the interaction between the portfolio basket and exchange trading.
- How the practice connects to the explanation: It makes ETF mechanics concrete with actual workbook-style basket data.

### Chapter 14. Statistical Arbitrage and Pairs Trading

- Concept explained: Stationarity, cointegration, mean reversion, and spread trading.
- Exact code folder: `Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading code`
- Exact notebook path: `Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading code/Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 5 · Trade the spread — *Pairs Trading on EWA & EWC*`
- Data file used: `Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading code/EWA.csv`
- Expected output: Spread bands, pair strategy metrics, and cointegration-vs-correlation comparison.
- What the reader should observe: A pair trade requires a stationary spread, not just similar-looking price charts.
- How the practice connects to the explanation: It walks from statistical diagnosis to a tradable spread rule.

### Chapter 15. PCA-Based Statistical Arbitrage

- Concept explained: PCA decomposition, explained variance, component weights, and PCA spread backtests.
- Exact code folder: `Week 22-1 MLT-05 Statistical Arbitrage with PCA code`
- Exact notebook path: `Week 22-1 MLT-05 Statistical Arbitrage with PCA code/Week 22-1 MLT-05 Statistical Arbitrage with PCA_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 1 · PCA from scratch — SPY & QQQ`
- Data file used: `Week 22-1 MLT-05 Statistical Arbitrage with PCA code/spy_qqq.csv`
- Expected output: PCA diagnostics, explained-variance table, and spread backtest metrics.
- What the reader should observe: PCA finds dominant shared movement, but trading still depends on residual behavior and validation.
- How the practice connects to the explanation: It generalizes pair-trading intuition to a factor/decomposition workflow.

### Chapter 16. Vectorized Backtesting

- Concept explained: Fast backtesting with aligned signals, positions, returns, and equity curves.
- Exact code folder: `Week 7-2 DMP-01 Strategy Back Testing code`
- Exact notebook path: `Week 7-2 DMP-01 Strategy Back Testing code/Week 7-2 DMP-01 Strategy Back Testing_validated_practice.ipynb`
- Exact notebook section/cell heading: `## The 7-step approach to building a strategy`
- Data file used: `Week 7-2 DMP-01 Strategy Back Testing code/DMP_01_data_tutorial_nse_source.csv`
- Expected output: Vectorized workflow reference, equity curve, and metrics snapshot.
- What the reader should observe: A vectorized backtest is a sequence of auditable columns, not a black box.
- How the practice connects to the explanation: It provides the template for rule-based backtests throughout the book.

### Chapter 17. Event-Driven Backtesting

- Concept explained: Event queues, event-loop structure, and live-like backtest components.
- Exact code folder: `Week 9-2 DMP-04 Event-Driven Backtesting code`
- Exact notebook path: `Week 9-2 DMP-04 Event-Driven Backtesting code/Week 9-2 DMP-04 Event Driven Back-Testing and working with Live Data Stream_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 4. The engine — a single event queue and an event loop`
- Data file used: `Week 9-2 DMP-04 Event-Driven Backtesting code/eod_prices.csv`
- Expected output: Event-flow counts, equity curve, parameter sweep, and risk summary.
- What the reader should observe: Events impose sequence and state, which vectorized calculations can hide.
- How the practice connects to the explanation: It demonstrates how research logic starts resembling a live trading loop.

### Chapter 18. Backtest Honesty and Failure Modes

- Concept explained: Transaction-cost traps, overfitting, honest test splits, and live-readiness controls.
- Exact code folder: `Week 16-1 TBP-05 code`
- Exact notebook path: `Week 16-1 TBP-05 code/Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 10. Trap 2 - over-fitting (the honest test)`
- Data file used: `Week 16-1 TBP-05 code/SPY.csv`
- Expected output: Out-of-sample chart, cost-impact chart, and parameter-rule controls.
- What the reader should observe: A strategy that looks good in-sample can fail after costs and honest holdout testing.
- How the practice connects to the explanation: It gives the chapter concrete failure modes instead of abstract warnings.

### Chapter 19. Portfolio Construction

- Concept explained: Return/risk metrics, covariance, diversification, frontier weights, and out-of-sample controls.
- Exact code folder: `Week 24-1 PRM-02 Quantitative Portfolio Management code`
- Exact notebook path: `Week 24-1 PRM-02 Quantitative Portfolio Management code/Week 24-1 PRM-02 Quantitative Portfolio Management_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 3 · Two stocks are better than one — the Markowitz insight`
- Data file used: `Week 24-1 PRM-02 Quantitative Portfolio Management code/TCS.csv`
- Expected output: Diversification metrics, efficient-frontier weights, and out-of-sample portfolio comparison.
- What the reader should observe: Portfolio risk is shaped by covariance, not just each asset's standalone volatility.
- How the practice connects to the explanation: It turns diversification from a slogan into a calculation.

### Chapter 20. Portfolio Risk Controls

- Concept explained: Risk taxonomy, VaR/CVaR, liquidity controls, incident controls, and pre-trade controls.
- Exact code folder: `Week 15-1 PRM-01 Portfolio & Risk Management code`
- Exact notebook path: `Week 15-1 PRM-01 Portfolio & Risk Management code/Week 15-1 PRM-01 Portfolio & Risk Management_validated_practice.ipynb`
- Exact notebook section/cell heading: `## Phase 2-3 · Market risk — the building blocks`
- Data file used: `Week 15-1 PRM-01 Portfolio & Risk Management code/prm01_risk_process_control_matrix.csv`
- Expected output: Risk taxonomy table, VaR/CVaR liquidity demo, and pre-trade gateway chart.
- What the reader should observe: Risk management is a chain of controls around the strategy, not one end-of-report statistic.
- How the practice connects to the explanation: It translates portfolio risk into process and governance artifacts.

### Chapter 21. Machine Learning Foundations for Time Series

- Concept explained: ML task types, feature engineering, time-series split discipline, classifiers, and model metrics.
- Exact code folder: `Week 18-1 MLT-01 Machine Learning-I code`
- Exact notebook path: `Week 18-1 MLT-01 Machine Learning-I code/Week 18-1 MLT-01 Machine Learning-I_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 3 · Decision Tree & Random Forest — the full pipeline (shipped notebook, real TSLA data)`
- Data file used: `Week 18-1 MLT-01 Machine Learning-I code/TSLA.csv`
- Expected output: Classifier metrics, feature importance proxy, and leakage-control chart.
- What the reader should observe: Small accuracy improvements need baseline and leakage context.
- How the practice connects to the explanation: It grounds ML terminology in a time-ordered trading classification workflow.

### Chapter 22. Feature Engineering, Model Risk, and Walk-Forward Testing

- Concept explained: Feature families, SHAP survivors, tiered models, walk-forward validation, leakage, and holdout degradation.
- Exact code folder: `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code`
- Exact notebook path: `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 6 · Module 4 — tune, test **once**, and read the honest verdict`
- Data file used: `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/mlt04_holdout_results.csv`
- Expected output: Holdout results, leakage inflation table, and model-tier comparison charts.
- What the reader should observe: Feature sophistication is not enough; the holdout result decides whether the model is usable.
- How the practice connects to the explanation: It makes model risk and validation design the center of the ML strategy chapter.

### Chapter 23. Neural Networks and Deep Learning Cautions

- Concept explained: Neural network structure, activations, gradient descent, MLP validation, and model-risk controls.
- Exact code folder: `Week 20-1 MLT-03 Machine Learning-III code`
- Exact notebook path: `Week 20-1 MLT-03 Machine Learning-III code/Week 20-1 MLT-03 Machine Learning-III_validated_practice.ipynb`
- Exact notebook section/cell heading: ``## 3. A real neural network on EUR/USD (shipped `MLPClassifier`)``
- Data file used: `Week 20-1 MLT-03 Machine Learning-III code/EURUSD_data.csv`
- Expected output: MLP validation metrics, backtest performance, activation/gradient reference chart.
- What the reader should observe: A neural network can fit patterns without producing robust trading performance.
- How the practice connects to the explanation: It keeps deep learning tied to out-of-sample market evidence.

### Chapter 24. NLP and Sentiment as Trading Inputs

- Concept explained: Text preprocessing, vectorization, sentiment records, entity mapping, and trading-signal validation.
- Exact code folder: `Week 23-1 MLT-06 Natural Language Processing and Sentiment Analysis in Trading code`
- Exact notebook path: `Week 23-1 MLT-06 Natural Language Processing and Sentiment Analysis in Trading code/Week 23-1 MLT-06 Natural Language Processing and Sentiment Analysis in Trading_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 1 · Text preprocessing with spaCy  *(Text-Preprocessing-Demo)*`
- Data file used: `Week 23-1 MLT-06 Natural Language Processing and Sentiment Analysis in Trading code/baidu-scores-history.csv`
- Expected output: Text vectorizer metrics, sentiment overlay, and Granger/trading metrics.
- What the reader should observe: Text features need timestamp, entity, and validation controls before they can be trading inputs.
- How the practice connects to the explanation: It turns NLP from abstract text mining into a market-aligned feature workflow.

### Chapter 25. Reinforcement Learning for Trading

- Concept explained: RL states, actions, rewards, Q-learning, DQN controls, fat tails, and overfit risk.
- Exact code folder: `Week 23-2 MLT-07 Reinforcement Learning in Trading code`
- Exact notebook path: `Week 23-2 MLT-07 Reinforcement Learning in Trading code/Week 23-2 MLT-07 Reinforcement Learning in Trading_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 4 · Predict **returns**, not prices`
- Data file used: `Week 23-2 MLT-07 Reinforcement Learning in Trading code/market_daily.csv`
- Expected output: Predictability checks, Q-learning results, overfit/fat-tail metrics, and reward controls.
- What the reader should observe: RL requires disciplined state/reward design and market predictability checks before any trading claim.
- How the practice connects to the explanation: It frames RL as a fragile sequential decision workflow rather than a shortcut to alpha.

### Chapter 26. Options Payoffs, Pricing, and Greeks

- Concept explained: Black-Scholes pricing, input sensitivity, Greeks, put-call parity, and model assumptions.
- Exact code folder: `Week 17-2 OTS-03 Options Pricing Models and Greeks code`
- Exact notebook path: `Week 17-2 OTS-03 Options Pricing Models and Greeks code/Week 17-2 OTS-03 Options Pricing Models and Greeks_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 2 · Black-Scholes from scratch — the closed form the exchanges use`
- Data file used: `Week 17-2 OTS-03 Options Pricing Models and Greeks code/ots03_option_pricing_reference.csv`
- Expected output: Option pricing table, Greek surface reference, and put-call parity check.
- What the reader should observe: Option price changes are driven by multiple inputs, not only the underlying price.
- How the practice connects to the explanation: It moves from payoff intuition to model outputs and arbitrage sanity checks.

### Chapter 27. Volatility Trading and Variance Premium

- Concept explained: Volatility estimators, GARCH context, variance premium, implied-vs-realized volatility, and vega controls.
- Exact code folder: `Week 19-2 OTS-04 Volatility Measurement code`
- Exact notebook path: `Week 19-2 OTS-04 Volatility Measurement code/Week 19-2 OTS-04 Volatility Measurement_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 5. Trading volatility — the variance premium & the master equation`
- Data file used: `Week 19-2 OTS-04 Volatility Measurement code/SPY.csv`
- Expected output: Volatility estimator table, rolling/EWMA shock chart, and variance-premium controls.
- What the reader should observe: Volatility measurement choice changes the interpretation of risk and expected option edge.
- How the practice connects to the explanation: It ties volatility theory to actual forecast and trade-control artifacts.

### Chapter 28. Evaluating and Backtesting Options Trades

- Concept explained: Dynamic hedging, hedge frequency, volatility choice, option-chain quality, and event-based options backtesting.
- Exact code folder: `Week 21-1 OTS-06 Creating an Options Backtesting Model code`
- Exact notebook path: `Week 21-1 OTS-06 Creating an Options Backtesting Model code/Week 21-1 OTS-06 Creating an Options Backtesting Model_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 6 · The event-based backtest engine`
- Data file used: `Week 21-1 OTS-06 Creating an Options Backtesting Model code/spx_monthly_2023.csv`
- Expected output: Strategy performance table, option-chain quality checks, SL/TP exit breakdown, and equity drawdown.
- What the reader should observe: Options backtests depend heavily on chain quality, trigger dates, and execution rules.
- How the practice connects to the explanation: It converts options strategy evaluation into a controlled event-based workflow.

### Chapter 29. Broker APIs, REST, WebSockets, and Market Data Plumbing

- Concept explained: API concepts, REST request components, status codes, order payloads, WebSockets, and heartbeat logic.
- Exact code folder: `Week 12-2 TBP-02 Rest API code`
- Exact notebook path: `Week 12-2 TBP-02 Rest API code/Week 12-2 TBP-02 Rest API_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 2. The anatomy of a request â€” five pieces`
- Data file used: `Week 12-2 TBP-02 Rest API code/tbp02_mock_order_audit.csv`
- Expected output: Endpoint reference tables, mock request logs, order audit logs, WebSocket message table.
- What the reader should observe: Live trading plumbing is a stateful communication problem with explicit failure modes.
- How the practice connects to the explanation: It gives API architecture a testable offline artifact before discussing live credentials.

### Chapter 30. Backtesting Platforms and Live Robot Controls

- Concept explained: Platform strategy scripts, backtest-to-live transition, IBridgePy reference robots, and robot control matrix.
- Exact code folder: `Week 16-1 TBP-05 code`
- Exact notebook path: `Week 16-1 TBP-05 code/Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 11. Part 4 - From a backtest to a LIVE robot (the IBridgePy strategies)`
- Data file used: `Week 16-1 TBP-05 code/tbp05_live_robot_control_matrix.csv`
- Expected output: IBridgePy reference map, robot scoreboard, live-robot control matrix.
- What the reader should observe: A live robot is strategy logic plus scheduling, alerts, error handling, and operational boundaries.
- How the practice connects to the explanation: It bridges research backtests to platform-specific live controls.

### Chapter 31. Production Architecture, Desk Operations, and Regulation

- Concept explained: Trading-system architecture, market-data adapters, FIX, RMS, latency, colocation, membership, and regulation.
- Exact code folder: `Week 6-2 TIO-01 System Architecture code`
- Exact notebook path: `Week 6-2 TIO-01 System Architecture code/Week 6-2 TIO-01 System Architecture_validated_practice.ipynb`
- Exact notebook section/cell heading: `## 1. Components of a trading system`
- Data file used: `Week 6-2 TIO-01 System Architecture code/tio01_exchange_architecture_components.csv`
- Expected output: Architecture component map, latency queue chart, market-data method table.
- What the reader should observe: Production trading systems are built from interacting infrastructure and control components.
- How the practice connects to the explanation: It makes production architecture visible before discussing desk setup and regulation.

### Chapter 32. The Research-to-Live Checklist

- Concept explained: Combining strategy workflow, validation, cost checks, risk controls, and live controls into a launch checklist.
- Exact code folder: `Week 25-1 DMP-05 QuantiP code`
- Exact notebook path: `Week 25-1 DMP-05 QuantiP code/Week 25-1 DMP-05 QuantiP_validated_practice.ipynb`
- Exact notebook section/cell heading: `## Part 1 — The professional strategy workflow`
- Data file used: `Week 25-1 DMP-05 QuantiP code/dmp05_validation_controls.csv`
- Expected output: Professional strategy workflow, strategy cost checks, diversification checks, and validation controls.
- What the reader should observe: Research, costs, risk, and validation form one gate sequence.
- How the practice connects to the explanation: It gives the final checklist a concrete framework rather than a generic list.

### Chapter 33. Capstone: Build, Test, Risk-Control, and Operate a Strategy

- Concept explained: End-to-end capstone strategy workflow using reusable modules, backtest metrics, cost checks, and go/no-go evidence.
- Exact code folder: `Week 25-1 DMP-05 QuantiP code`
- Exact notebook path: `Week 25-1 DMP-05 QuantiP code/Week 25-1 DMP-05 QuantiP_validated_practice.ipynb`
- Exact notebook section/cell heading: `### 4 & 5 · Combining alphas, backtesting with cost, judging honestly`
- Data file used: `Week 25-1 DMP-05 QuantiP code/nifty_stocks_prices.csv`
- Expected output: Trade log, strategy cost metrics, diversification metrics, beta/BAB checks, and final control tables.
- What the reader should observe: A capstone strategy is judged by an evidence package, not a single chart.
- How the practice connects to the explanation: It ties the full book workflow into a final strategy dossier.
