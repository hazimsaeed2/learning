# EPAT Book Topic Workflow

Inspection date: 2026-07-07

This workflow reorganizes the EPAT material into a practical trading book sequence. It does not follow week order except where the week order already supports the best learning path.

## Design Principle

The book should move from market reality to research workflow, then to statistical evidence, strategy design, backtesting, risk, machine learning, options, live execution, and a final professional playbook. Python basics and optional tutorials should support the learning path, but they should not dominate the main narrative unless the intended reader is a beginner programmer.

## Part 1: Trading Foundations

### Chapter 1. What Markets Are Actually Doing

- Why this chapter belongs here: A reader should understand the market venue, order book, participants, and cost mechanics before evaluating any strategy.
- Source files supporting it: MMT01, MMT02, and MMT03 source packets; `Week 3-1 MMT-01 Execution Strategy - I.html`; `Week 4-1 MMT-02 Execution Strategy - II.html`; `Week 5-2 MMT-03 Overview of Electronic and Algorithmic.html`.
- Code/notebook files supporting it: `Week 3-1 MMT-01 code/*practice.ipynb`; `Week 4-1 MMT-02 code/*practice.ipynb`; `Week 5-2 MMT-03 code/*practice.ipynb`.
- Key concepts to teach: order book depth, VWAP, order-flow imbalance, market impact, algorithm types, participant incentives, volume schedules, execution style selection.
- Practice exercises available: order-book depth calculations, VWAP trade calculations, dynamic discretion scenarios, algorithm taxonomy tables, intraday profile interpretation.
- Reader should understand: A trading strategy does not execute in a vacuum; alpha, liquidity, spread, impact, and venue behavior are linked.

### Chapter 2. From Observation to Tradable Edge

- Why this chapter belongs here: The book needs a disciplined definition of a strategy before any code or model is introduced.
- Source files supporting it: `Week 13-2 OTS-01 General Trading Theory.html`; OTS01 source PDFs; `Week 4-2 EFS-01 Strategy Building in Equities.html`.
- Code/notebook files supporting it: `Week 13-2 OTS-01 General Trading Theory code/*validated_practice.ipynb`; `Week 4-2 EFS-01 code/*validated_practice.ipynb`.
- Key concepts to teach: observation vs hypothesis vs strategy vs business, edge/risk map, adverse selection, trade review, automation discipline, compliance workflow, strategy specification.
- Practice exercises available: observation-to-business pipeline, edge/risk mapping, trade-review noise demo, EFS01 strategy metric checklist.
- Reader should understand: A trade idea is not a strategy until it has rules, risk limits, testability, execution logic, and a review process.

### Chapter 3. Transaction Costs, TCA, and Implementation Shortfall

- Why this chapter belongs here: Cost realism should be introduced before performance metrics so readers do not confuse gross returns with tradable returns.
- Source files supporting it: MMT04 original packet; `Week 7-3 MMT-04 The Algorithmic Trading Process.html`; TBP05 cost material.
- Code/notebook files supporting it: `Week 7-3 MMT-04 The Algorithmic Trading Process code/*validated_practice.ipynb`; `Week 16-1 TBP-05 code/02_backtest_costs_and_traps.py`; TBP05 validated notebook.
- Key concepts to teach: implementation shortfall, arrival cost, VWAP slippage, RPM percentile, value add, market-impact parameters, participation rate, cost sensitivity.
- Practice exercises available: TCA identity checks, post-trade metric calculations, market-impact diagnostics, TBP05 cost-impact sweeps.
- Reader should understand: A strategy has to survive execution costs, participation constraints, and measurable post-trade accountability.

## Part 2: Market Data and Python Research Workflow

### Chapter 4. Python for Trading Research

- Why this chapter belongs here: The reader needs enough Python and notebook fluency to follow the rest of the book.
- Source files supporting it: PBQ01 and PBQ02 source packets; `Week 5-1 PBQ-01 Basics of Python Programming.html`; `Week 6-3 PBQ-02 Python Basics for Quants.html`; `Week 8-1 Python_Cheat_Sheet.html`.
- Code/notebook files supporting it: PBQ01/PBQ02 validated notebooks; Python cheat sheet validated notebook.
- Key concepts to teach: imports, data structures, vectorization, pandas access patterns, missing data, shift discipline, reproducibility.
- Practice exercises available: TCS signal counting, vectorization benchmark, missing-data workflow, cheat-sheet return-math checks.
- Reader should understand: How to load, inspect, transform, and validate market data without introducing avoidable research mistakes.

### Chapter 5. Cleaning and Structuring Market Data

- Why this chapter belongs here: Most trading research errors start with dates, symbols, missing rows, or bad joins.
- Source files supporting it: PBQ02, Week 7-1 tutorial, DMP01 tutorial material.
- Code/notebook files supporting it: `Week 7-1 Tutorial Python after PBQ-02 code/*validated_practice.ipynb`; `Week 8-1 Tutorial Python after DMP-01 code/*validated_practice.ipynb`; PBQ02 continuation notebooks.
- Key concepts to teach: OHLCV schema, raw exchange data cleanup, calendar slicing, candles, CSV/Excel round-trips, timezone checks, data-range audits.
- Practice exercises available: HDFCBANK cleanup, AAPL daily candles, Nifty CSV round-trip, calendar slicing, DataFrame modification.
- Reader should understand: Clean research data is an engineered artifact, not something to assume from a vendor download.

### Chapter 6. Building Reusable Strategy Code

- Why this chapter belongs here: Before building complex systems, the reader needs code structure that can carry strategies, metrics, and data access.
- Source files supporting it: DMP02/DMP03 source summaries; DMP05 QuantiP packet.
- Code/notebook files supporting it: `Week 8-2 DMP-02 Introduction to OOP code/*validated_practice.ipynb`; `Week 9-1 DMP-03 OOP in Python code/*validated_practice.ipynb`; `Week 25-1 DMP-05 QuantiP code/alpha.py`, `data.py`, `performance_analytics.py`.
- Key concepts to teach: classes, methods, encapsulation, strategy pipeline design, reusable alpha/data/performance modules, validation controls.
- Practice exercises available: OOP concept checks, backtest class pipeline, OLS strategy metrics, QuantiP framework modules.
- Reader should understand: How to organize trading research so a strategy can be tested, extended, and reviewed rather than trapped in one-off notebook cells.

## Part 3: Returns, Risk, Statistics, and Time Series

### Chapter 7. Return Math and Basic Statistics

- Why this chapter belongs here: Every later strategy, risk, and ML chapter depends on correct return and distribution calculations.
- Source files supporting it: SFM02 source packet, SFM03 practical packet, PBQ02 VaR/ES material, DMP01 return material.
- Code/notebook files supporting it: `Week 3-2 SFM-03 code/*validated_practice.ipynb`; `Week 7-2 DMP-01 Strategy Back Testing code/*validated_practice.ipynb`; PBQ02 validated notebooks.
- Key concepts to teach: simple returns, log returns, mean, variance, standard deviation, annualization, sample vs population variance, Monte Carlo, basic tail metrics.
- Practice exercises available: Nifty returns, log vs simple workbook, Bessel correction chart, Monte Carlo practice, PBQ02 VaR/ES corrected reference.
- Reader should understand: The numeric language used to describe returns and risk, and how small formula choices affect strategy conclusions.

### Chapter 8. Risk, Drawdowns, and Performance Metrics

- Why this chapter belongs here: Strategy evaluation must be risk-adjusted and path-aware before any optimization or live deployment.
- Source files supporting it: EFS01, PRM01, DMP05, TBP05 source materials.
- Code/notebook files supporting it: `Week 4-2 EFS-01 code/*validated_practice.ipynb`; `Week 15-1 PRM-01 Portfolio & Risk Management code/*validated_practice.ipynb`; `Week 25-1 DMP-05 QuantiP code/performance_analytics.py`.
- Key concepts to teach: hit ratio, normalized hit ratio, drawdown, Kelly sizing, VaR, CVaR, liquidity risk, incident controls, transaction-cost metrics.
- Practice exercises available: EFS01 metric checklist, Kelly chart, PRM01 VaR/CVaR liquidity demo, DMP05 drawdown recovery table.
- Reader should understand: A profitable strategy can still be weak if its sizing, drawdown, tail risk, or cost profile is unacceptable.

### Chapter 9. Statistical Testing for Market Data

- Why this chapter belongs here: The reader needs to distinguish signal from noise before trusting a model or indicator.
- Source files supporting it: ASQ01, DMP03, EFS02, MLT05 source materials.
- Code/notebook files supporting it: `Week 10-1 ASQ-01 Statistical Analysis code/*validated_practice.ipynb`; `Week 9-1 DMP-03 OOP in Python code/*validated_practice.ipynb`; EFS02/MLT05 validation notebooks.
- Key concepts to teach: stationarity, ADF intuition, ACF/PACF, autocorrelation, IID assumptions, correlation vs causation, cointegration diagnostics.
- Practice exercises available: ASQ01 stationarity checks, DMP03 EMH/autocorrelation checks, EFS02 stationarity diagnostics, MLT05 cointegration/Granger metrics.
- Reader should understand: Why prices and returns behave differently, and why models should be built on statistically defensible inputs.

### Chapter 10. Time-Series Forecasting and Volatility Models

- Why this chapter belongs here: Time-series models bridge basic statistics, volatility, and adaptive strategy design.
- Source files supporting it: ASQ01, ASQ02, OTS04.
- Code/notebook files supporting it: `Week 10-1 ASQ-01 Statistical Analysis code/*validated_practice.ipynb`; `Week 12-1 ASQ-02 Time Series Modeling code/*validated_practice.ipynb`; `Week 19-2 OTS-04 Volatility Measurement code/*validated_practice.ipynb`.
- Key concepts to teach: AR/MA/ARIMA, rolling forecasts, ARCH/GARCH, volatility regimes, rolling vs EWMA volatility, cost drag, risk sizing.
- Practice exercises available: rolling AR equity curve, fixed auto-ARIMA metrics, GARCH risk-sizing chart, volatility estimator comparison.
- Reader should understand: Forecasting is useful only when tested dynamically and judged after costs and regime changes.

## Part 4: Indicators, Signals, and Strategy Design

### Chapter 11. Indicator Strategies and Rule-Based Systems

- Why this chapter belongs here: Simple rule-based strategies are the cleanest place to teach hypothesis, signal, position, return, and evaluation.
- Source files supporting it: EFS01, DMP01, ASQ01, TBP03 source scripts.
- Code/notebook files supporting it: EFS01 validated notebooks; DMP01 validated notebooks; TBP03 MACD/RSI scripts; ASQ01 moving-average metrics.
- Key concepts to teach: moving-average crossover, RSI, MACD, signal vs position, parameter surfaces, in-sample/out-of-sample split, robustness plateaus.
- Practice exercises available: EFS01 parameter surface, DMP01 long/short crossover, DMP01 event-vs-vectorized check, TBP03 RSI/MACD scripts.
- Reader should understand: Simple indicators are useful teaching tools, but parameter stability and out-of-sample behavior matter more than headline return.

### Chapter 12. Futures, Momentum, and Regime-Aware Strategies

- Why this chapter belongs here: Momentum introduces cross-asset mechanics, futures rolls, and regime-specific behavior beyond single-stock indicators.
- Source files supporting it: EFS03/EFS04 original packet; EFS01 strategy foundations; ASQ time-series material.
- Code/notebook files supporting it: `Week 14-1 EFS-03 Quantitative Momentum Strategies I code/*validated_practice.ipynb`; `Week 14-2 EFS-04 Quantitative Momentum Strategies II code/*validated_practice.ipynb`.
- Key concepts to teach: roll return, back-adjustment, futures data hygiene, timestamp alignment, VIX/ES hedge logic, momentum crashes, leveraged ETF/calendar controls.
- Practice exercises available: EFS03 roll formula map, back-adjustment demo, EFS04 strategy inventory, VIX/ES hedge reference, crash-control charts.
- Reader should understand: Momentum is not just a price chart rule; contract construction, regime, funding, and crash behavior can dominate results.

### Chapter 13. ETFs and Tradable Baskets

- Why this chapter belongs here: ETFs connect index construction, creation/redemption mechanics, and portfolio/strategy implementation.
- Source files supporting it: EFS05 source packet; PRM02 portfolio material.
- Code/notebook files supporting it: `Week 13-1 EFS-05 Trading ETFs code/*validated_practice.ipynb`; `EFS-05_data_ETF_Seminar_Data_source.xlsx`.
- Key concepts to teach: NAV, creation/redemption basket, secondary market, index divisor, ETF arbitrage, trading model ladder.
- Practice exercises available: workbook sheet map, creation/redemption correction, NAV snapshots, basket comparison.
- Reader should understand: An ETF is both a listed instrument and a portfolio mechanism, and its tradability depends on creation/redemption and liquidity.

### Chapter 14. Statistical Arbitrage and Pairs Trading

- Why this chapter belongs here: Pair trading is the natural first market-neutral strategy before PCA and ML stat-arb.
- Source files supporting it: EFS02 source packet; ASQ stationarity material.
- Code/notebook files supporting it: `Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading code/*validated_practice.ipynb`.
- Key concepts to teach: spread construction, hedge ratio, stationarity, cointegration, correlation vs cointegration, entry/exit bands, pair-risk controls.
- Practice exercises available: AUDCAD/EURCHF/EWA/EWC pair diagnostics, spread band charts, pair strategy metrics, risk management controls.
- Reader should understand: Pair trading depends on a stable spread process, not just two assets that look correlated.

### Chapter 15. PCA-Based Statistical Arbitrage

- Why this chapter belongs here: PCA stat-arb extends pair logic from two assets to dimensions, factors, and residual spreads.
- Source files supporting it: MLT05 source packet; EFS02; PRM02 covariance concepts.
- Code/notebook files supporting it: `Week 22-1 MLT-05 Statistical Arbitrage with PCA code/PCA_3_source.ipynb`; MLT05 validated notebooks.
- Key concepts to teach: PCA, explained variance, factor exposure, principal component weights, residual/spread construction, Granger/cointegration diagnostics.
- Practice exercises available: SPY/QQQ PCA diagnostics, explained variance clusters, spread backtests, index PCA controls.
- Reader should understand: PCA is a compression and factor-extraction tool, but a trading spread still needs economic interpretation and out-of-sample evidence.

## Part 5: Backtesting and Performance Evaluation

### Chapter 16. Vectorized Backtesting

- Why this chapter belongs here: Vectorized backtesting is the fastest way to teach the mechanics of strategy return construction.
- Source files supporting it: DMP01, EFS01, ASQ01, Python cheat sheet.
- Code/notebook files supporting it: DMP01 validated notebooks; EFS01 validated notebooks; Python cheat sheet validated notebook.
- Key concepts to teach: signal, position, shift, transaction-cost placeholder, equity curve, vectorized return calculation, benchmark comparison.
- Practice exercises available: DMP01 long/short crossover sample, DMP01 metrics snapshot, cheat-sheet shift/return math controls.
- Reader should understand: Fast research backtests are useful only when they respect time order and position lag.

### Chapter 17. Event-Driven Backtesting

- Why this chapter belongs here: Event-driven logic is the bridge from research notebooks to live-like execution workflows.
- Source files supporting it: DMP04, TBP03, MMT04.
- Code/notebook files supporting it: `Week 9-2 DMP-04 Event-Driven Backtesting code/*validated_practice.ipynb`; `Week 22-2 TBP-03 Backtesting using Blueshift code/*validated_practice.ipynb`; TBP03 strategy scripts.
- Key concepts to teach: event queue, market events, signal/order/fill events, event contract, point-in-time data, lookahead controls, platform backtesting.
- Practice exercises available: DMP04 event-flow counts, parameter sweep, TBP03 point-in-time adjustment, event-engine controls.
- Reader should understand: A backtest becomes credible when it mimics information flow and order handling, not only return math.

### Chapter 18. Backtest Honesty and Failure Modes

- Why this chapter belongs here: The book needs a dedicated chapter on how backtests lie before moving to live trading or ML.
- Source files supporting it: TBP05, MLT04, EFS01, TBP03.
- Code/notebook files supporting it: TBP05 notebooks/scripts; MLT04 validated notebook; TBP03 lookahead metrics; EFS01 parameter surface.
- Key concepts to teach: lookahead bias, data leakage, parameter mining, dependency failures, train/test split, holdout degradation, cost erasure, production readiness.
- Practice exercises available: TBP05 cost and parameter rules, MLT04 leakage inflation, TBP03 lookahead point-in-time chart, EFS01 in/out-of-sample comparison.
- Reader should understand: A backtest is evidence only if its assumptions, dependencies, costs, and holdout results are visible.

## Part 6: Portfolio Construction and Risk Management

### Chapter 19. Portfolio Construction

- Why this chapter belongs here: After single strategies, the reader should learn how positions combine into portfolios.
- Source files supporting it: PRM02 source packet; SFM03 statistics packet; EFS05 basket material.
- Code/notebook files supporting it: `Week 24-1 PRM-02 Quantitative Portfolio Management code/*validated_practice.ipynb`; SFM03 notebooks.
- Key concepts to teach: covariance, correlation, diversification, systematic vs idiosyncratic risk, efficient frontier, max-Sharpe portfolio, out-of-sample portfolio evaluation.
- Practice exercises available: PRM02 return/risk metrics, diversification limit, frontier weights, out-of-sample controls.
- Reader should understand: Portfolio risk is about co-movement and constraints, not simply adding individual stock risks.

### Chapter 20. Portfolio Risk Controls

- Why this chapter belongs here: Portfolio construction without operational risk controls can create false confidence.
- Source files supporting it: PRM01, TIO02, DMP05.
- Code/notebook files supporting it: PRM01 validated notebooks; TIO02 validated notebooks; DMP05 performance analytics.
- Key concepts to teach: risk taxonomy, liquidity risk, VaR/CVaR limits, incident control map, pre-trade gateways, operational risk controls, drawdown recovery.
- Practice exercises available: PRM01 control matrix, pre-trade gateway chart, TIO02 operational/regulatory controls, DMP05 drawdown and cost metrics.
- Reader should understand: Professional risk management is a process with controls, not a single metric printed after the backtest.

## Part 7: Machine Learning for Trading

### Chapter 21. Machine Learning Foundations for Time Series

- Why this chapter belongs here: ML should be introduced only after returns, features, and validation are understood.
- Source files supporting it: MLT01 and MLT02 source packets.
- Code/notebook files supporting it: MLT01 source notebooks and validated notebook; MLT02 source notebooks and validated notebook.
- Key concepts to teach: supervised vs unsupervised learning, labels, features, train/test split, scaling, logistic regression, decision trees, random forests, confusion matrix, SVM, clustering.
- Practice exercises available: TSLA classifier, Gini worked example, split leakage controls, confusion metrics, SVM kernel metrics, K-Means elbow diagnostics.
- Reader should understand: ML is a disciplined prediction workflow, not a magic layer over weak data or leaky validation.

### Chapter 22. Feature Engineering, Model Risk, and Walk-Forward Testing

- Why this chapter belongs here: This is the central ML trading chapter because it converts ML algorithms into a full strategy research process.
- Source files supporting it: MLT04 source packet; TBP05 backtest honesty; MLT01/MLT02 foundations.
- Code/notebook files supporting it: MLT04 source notebooks and helper scripts; MLT04 validated notebook; TBP05 validated notebook.
- Key concepts to teach: benchmark model, microstructure features, feature explosion, SHAP selection, hyperparameter tuning, walk-forward validation, embargo, holdout degradation, leakage inflation.
- Practice exercises available: MLT04 batch comparison, feature-family audit, holdout results, leakage-control table, dependency controls.
- Reader should understand: A production-worthy ML strategy is judged by validation design, not by training score or model sophistication.

### Chapter 23. Neural Networks and Deep Learning Cautions

- Why this chapter belongs here: Neural networks should be presented after simpler models so the reader can judge whether added complexity is justified.
- Source files supporting it: MLT03 source packet; MLT04 model-risk material.
- Code/notebook files supporting it: MLT03 source neural-network notebooks; MLT03 validated notebook.
- Key concepts to teach: activation functions, gradient descent, backpropagation, MLP validation, indicator feature controls, text-mining bridge.
- Practice exercises available: activation/gradient reference, MLP metrics backtest, feature-indicator controls, TF-IDF model-risk controls.
- Reader should understand: Deep models add flexibility and overfitting risk; they need stronger validation, not weaker scrutiny.

### Chapter 24. NLP and Sentiment as Trading Inputs

- Why this chapter belongs here: Text data is a distinct alternative data workflow and should not be mixed into basic ML.
- Source files supporting it: MLT06 source packet.
- Code/notebook files supporting it: MLT06 source notebooks for preprocessing, tagging, LSA, MRN, PermID, topic modeling, state-space sentiment; MLT06 validated notebook.
- Key concepts to teach: text cleaning, vectorizers, topic modeling, entity metadata, sentiment records, aligning news scores to prices, testing predictive content.
- Practice exercises available: Baidu sentiment overlay, vectorizer/topic metrics, MRN metadata audit, Granger trading metrics.
- Reader should understand: Text is useful only after careful timestamping, entity mapping, and validation against price data.

### Chapter 25. Reinforcement Learning for Trading

- Why this chapter belongs here: RL is advanced and should be framed as a research method with serious risks, not a beginner trading shortcut.
- Source files supporting it: MLT07 source packet.
- Code/notebook files supporting it: MLT07 source notebooks for state/action/reward/Bellman/replay/DQN/RL main; MLT07 validated notebook.
- Key concepts to teach: state, action, reward, Bellman update, Q-learning, DQN, experience replay, fat tails, market predictability checks, reward design.
- Practice exercises available: Bellman table, Q-learning results, overfit/fat-tail metrics, reward function reference, DQN config controls.
- Reader should understand: RL can model sequential decision problems, but market nonstationarity and reward design make naive RL trading especially fragile.

## Part 8: Options and Volatility

### Chapter 26. Options Payoffs, Pricing, and Greeks

- Why this chapter belongs here: Options need a self-contained foundation before volatility trading or options backtesting.
- Source files supporting it: OTS01, OTS02, OTS03 source packets.
- Code/notebook files supporting it: OTS01 validated notebooks; OTS02 validated notebooks; OTS03 source Black-Scholes notebook and validated notebooks.
- Key concepts to teach: payoffs, implied vs realized volatility, Black-Scholes, Greeks, put-call parity, model assumptions, portfolio Greeks.
- Practice exercises available: option payoff reference, IV/HV surface, Black-Scholes sensitivity, Greek surface, parity arbitrage check.
- Reader should understand: Options are instruments whose PnL depends on price, volatility, time, and hedge behavior, not only direction.

### Chapter 27. Volatility Trading and Variance Premium

- Why this chapter belongs here: Volatility is a trading object in its own right and bridges time-series models, options, and risk.
- Source files supporting it: OTS02 and OTS04 source packets; ASQ02 GARCH material.
- Code/notebook files supporting it: OTS02 validated notebook; OTS04 source/validated notebooks; ASQ02 validated notebook.
- Key concepts to teach: realized volatility estimators, implied volatility, volatility surfaces, variance premium, GARCH context, vega exposure, adverse selection, regime controls.
- Practice exercises available: OTS02 variance premium demo, IV surface demo, OTS04 estimator comparison, rolling/EWMA shock diagnostics, GARCH context forecast.
- Reader should understand: Volatility strategies require measurement discipline, risk controls, and awareness of the gap between demo surfaces and real option chains.

### Chapter 28. Evaluating and Backtesting Options Trades

- Why this chapter belongs here: Options backtesting is structurally different from equity backtesting because chain quality, calendar, and hedging rules matter.
- Source files supporting it: OTS05 and OTS06 source packets.
- Code/notebook files supporting it: OTS05 source/validated notebooks; OTS06 source data-download, long-call, and strangle notebooks plus validated notebook.
- Key concepts to teach: hedge frequency, volatility choice for hedging, early exercise/dividends, strategy attribution, option-chain quality, SL/TP exits, options calendar entries.
- Practice exercises available: OTS05 hedge-frequency dispersion, hedge vol choice, SPY attribution, OTS06 option-chain quality, strategy performance, equity drawdown.
- Reader should understand: Options backtests are only as reliable as their chain data, execution assumptions, and hedge accounting.

## Part 9: Execution, APIs, and Live Trading Workflow

### Chapter 29. Broker APIs, REST, WebSockets, and Market Data Plumbing

- Why this chapter belongs here: Once strategies are credible, the reader needs to understand the data/order interfaces used to run them.
- Source files supporting it: TBP01, TBP02, Live Trading using IB API source packet.
- Code/notebook files supporting it: TBP01 validated notebook; TBP02 source Python scripts and validated notebook.
- Key concepts to teach: broker API architecture, callbacks, REST endpoints, status codes, WebSockets, heartbeat, historical data checks, order audit logs.
- Practice exercises available: TBP01 callback flow, sync/async timing, TBP02 endpoint coverage, mock order audit, offline RSI strategy.
- Reader should understand: Live workflow is event-driven and failure-prone; heartbeats, logs, and scope controls are part of the trading system.

### Chapter 30. Backtesting Platforms and Live Robot Controls

- Why this chapter belongs here: Platform examples show how research logic translates into deployable strategy containers.
- Source files supporting it: TBP03 Blueshift, TBP04/05 IBridgePy and Interactive Brokers, cloud computing optional packet.
- Code/notebook files supporting it: TBP03 strategy scripts; TBP04 validated notebook; TBP05 reference IBridgePy scripts and validated notebook.
- Key concepts to teach: platform APIs, scheduling, early close behavior, error handling, email alerts, cost traps, live robot control matrix, deployment dependencies.
- Practice exercises available: TBP03 platform scripts, TBP05 reference strategy map, live robot controls, cost and parameter rules.
- Reader should understand: A live robot needs platform-specific operational controls in addition to strategy logic.

### Chapter 31. Production Architecture, Desk Operations, and Regulation

- Why this chapter belongs here: Production trading requires infrastructure, operations, compliance, and regulatory awareness.
- Source files supporting it: TIO01, TIO02, PRM01, TBP cloud packet.
- Code/notebook files supporting it: TIO01 validated notebook; TIO02 validated notebook; PRM01 control notebooks.
- Key concepts to teach: exchange-side architecture, market data connectivity, latency ladder, colocation, setup costs, operational risk controls, regulatory controls, incident response.
- Practice exercises available: TIO01 architecture charts, TIO02 membership/setup cost metrics, colocation network metrics, PRM01 incident controls.
- Reader should understand: Going live is an operating business problem, not only a research problem.

## Part 10: Final Trading Playbook

### Chapter 32. The Research-to-Live Checklist

- Why this chapter belongs here: The book should synthesize all prior chapters into a single professional workflow.
- Source files supporting it: OTS01 trading discipline, EFS01 strategy checklist, DMP05 QuantiP, MLT04 validation, TBP05 live controls, PRM01/TIO02 controls.
- Code/notebook files supporting it: DMP05 framework modules, MLT04 walk-forward scripts, TBP05 control matrices, PRM01/TIO02 control tables.
- Key concepts to teach: hypothesis, data audit, baseline, strategy construction, validation, cost model, risk limits, portfolio context, deployment controls, monitoring, kill switches.
- Practice exercises available: combine DMP05 framework, MLT04 validation table, TBP05 cost controls, PRM/TIO control matrices into a launch checklist.
- Reader should understand: A trading system moves through gates; weak evidence at any gate should stop or revise deployment.

### Chapter 33. Capstone: Build, Test, Risk-Control, and Operate a Strategy

- Why this chapter belongs here: The final chapter should force integration across data, signal, backtest, risk, portfolio, and live workflow.
- Source files supporting it: DMP01, DMP04, DMP05, EFS01/EFS02/EFS03/EFS04, PRM01/PRM02, TBP01/TBP02/TBP05, MLT04.
- Code/notebook files supporting it: DMP05 `alpha.py`, `data.py`, `performance_analytics.py`; DMP04 event framework; MLT04 walk-forward scripts; TBP02/TBP05 API/control files.
- Key concepts to teach: capstone strategy design, data and source audit, alpha module, backtest engine, risk metrics, portfolio sizing, transaction costs, live readiness, monitoring plan.
- Practice exercises available: choose a strategy family from the repo, rebuild it in the QuantiP-style framework, validate it with walk-forward/holdout controls, and produce a go/no-go memo.
- Reader should understand: The output of quant research is not a notebook PnL chart; it is a controlled trading process with evidence, limits, and operational readiness.

