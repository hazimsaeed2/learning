# EPAT Practical Trading Systems

Working title: **EPAT Practical Trading Systems: From Market Microstructure to Research, Risk, Machine Learning, Options, and Live Execution**

This is a book skeleton only. It defines the textbook structure, chapter sections, learning objectives, sources, and practice references. It does not contain full chapters.

## Target Reader

The target reader is a quant-minded trader, finance student, systematic trading researcher, or developer who wants to build practical trading systems from evidence rather than from tips or isolated formulas.

The reader should be comfortable with basic algebra, basic statistics, and beginner Python. The book will teach the trading workflow, but it will not assume professional quant experience.

## Promise of the Book

By the end of the book, the reader should be able to move from a trading observation to a tested, risk-controlled, operationally aware trading strategy. The book will emphasize practical judgment: clean data, correct return math, honest backtesting, cost realism, portfolio context, model-risk controls, and live-trading discipline.

## Required Background

- Basic Python syntax and notebooks.
- Basic pandas-style tabular data handling.
- Basic probability/statistics vocabulary: mean, variance, standard deviation, correlation.
- Basic finance vocabulary: price, return, order, position, portfolio, volatility.
- No prior options, machine learning, broker API, or market microstructure expertise is assumed.

## How To Use This Book

Read Parts 1-6 in order if you are new to systematic trading. Parts 7-9 can be read selectively once the foundation is clear. Work through the `Practice Now` notebook references as you read; the practice is part of the book, not an optional supplement.

Every chapter must follow the `book_project/CHAPTER_WRITING_STANDARD.md` structure: why it matters, plain-English explanation, hand-checkable example, formula or logic after intuition, trading interpretation, failure modes, practice box, expected notebook output, summary, and check-yourself questions.

Future chapter drafts should be written under `book_project/chapters/`. Shared book assets should go under `book_project/assets/`, and finished export-ready outputs should go under `book_project/final/`.

## Part 1: Trading Foundations

### Chapter 1. What Markets Are Actually Doing

Learning objectives:
- Explain why liquidity, spread, depth, and impact determine whether a strategy can be traded.
- Distinguish market participants, execution styles, and trading algorithm categories.
- Interpret VWAP, TWAP, POV, and order-book examples as trading constraints.

Chapter sections:
1. Markets as a matching and liquidity system
2. Order book depth, spread, and queue priority
3. Execution benchmarks: VWAP, TWAP, POV
4. Participants, incentives, and adverse selection
5. Why market microstructure changes strategy design
6. Practice Now: classify execution styles and inspect intraday profiles

Chapter source references:
- `Week 3-1 MMT-01 Execution Strategy - I.html`
- `Week 4-1 MMT-02 Execution Strategy - II.html`
- `Week 5-2 MMT-03 Overview of Electronic and Algorithmic.html`
- `Market Microstructure for Trading (MMT)/MMT01 Execution Strategy I`
- `Market Microstructure for Trading (MMT)/MMT02 Execution Strategy II`
- `Market Microstructure for Trading (MMT)/MMT03 Overview Of Electronic And Algorithmic Trading`

Chapter practice references:
- `Week 5-2 MMT-03 code/Week 5-2 MMT-03 Overview of Electronic and Algorithmic_validated_practice.ipynb`
- `Week 4-1 MMT-02 code/Week 4-1 MMT-02 Execution Strategy II_validated_practice.ipynb`

### Chapter 2. From Observation to Tradable Edge

Learning objectives:
- Convert a market observation into a testable hypothesis and strategy rule set.
- Separate expected value from win rate and from realized sample luck.
- Identify risk, adverse selection, and compliance constraints before testing.

Chapter sections:
1. Observation, hypothesis, strategy, and trading business
2. Expected value as the definition of edge
3. Win rate, payoff asymmetry, and sizing
4. Trade review and sampling error
5. Compliance and automation discipline
6. Practice Now: map an observation into a tradable workflow

Chapter source references:
- `Week 13-2 OTS-01 General Trading Theory.html`
- `Week 4-2 EFS-01 Strategy Building in Equities.html`
- `Options Trading & Strategies (OTS)/OTS01 General Trading Theory`
- `Equity, FX, & Futures Strategies (EFS)/EFS01 Strategy Building In Equities`

Chapter practice references:
- `Week 13-2 OTS-01 General Trading Theory code/Week 13-2 OTS-01 General Trading Theory_validated_practice.ipynb`
- `Week 4-2 EFS-01 code/Week 4-2 EFS-01 Strategy Building in Equities_validated_practice.ipynb`

### Chapter 3. Transaction Costs, TCA, and Implementation Shortfall

Learning objectives:
- Decompose implementation shortfall into delay, execution, opportunity, and fixed costs.
- Interpret arrival cost, VWAP slippage, RPM percentile, and value add.
- Explain why gross alpha can vanish after transaction costs.

Chapter sections:
1. Why gross returns are not tradable returns
2. The implementation shortfall identity
3. Post-trade metrics and execution quality
4. Pre-trade impact and participation decisions
5. Transaction-cost sensitivity in strategy testing
6. Practice Now: reconcile an implementation shortfall table

Chapter source references:
- `Week 7-3 MMT-04 The Algorithmic Trading Process.html`
- `Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms.html`
- `Market Microstructure for Trading (MMT)/MMT04 The Algorithmic Trading Process`
- `Trading & Back-testing Platforms (TBP)/TBP-04 & 05-Backtest And Live Trade Algo Strategies I & II`

Chapter practice references:
- `Week 7-3 MMT-04 The Algorithmic Trading Process code/Week 7-3 MMT-04 The Algorithmic Trading Process_validated_practice.ipynb`
- `Week 16-1 TBP-05 code/02_backtest_costs_and_traps.py`

## Part 2: Market Data and Python Research Workflow

### Chapter 4. Python for Trading Research

Learning objectives:
- Use Python, NumPy, and pandas to inspect and transform market data.
- Explain why vectorization matters for research speed and consistency.
- Avoid common indexing, missing-data, and shift mistakes.

Chapter sections:
1. Research notebooks as trading laboratories
2. Python objects, arrays, and vectorized calculations
3. pandas data access patterns
4. Missing data and signal construction
5. Reproducibility checks and common mistakes
6. Practice Now: build a simple TCS signal workflow

Chapter source references:
- `Week 5-1 PBQ-01 Basics of Python Programming.html`
- `Week 6-3 PBQ-02 Python Basics for Quants.html`
- `Week 8-1 Python_Cheat_Sheet.html`
- `Python Basics Its Quant Ecosystem (PBQ)/PBQ01 Basics Of Python Programming`
- `Python Basics Its Quant Ecosystem (PBQ)/PBQ02 Python Basics For Quants`

Chapter practice references:
- `Week 5-1 PBQ-01 code/Week 5-1 PBQ-01 Basics of Python Programming_validated_practice.ipynb`
- `Week 6-3 PBQ-02 Python Basics for Quants code/Week 6-3 PBQ-02 Python Basics for Quants_validated_practice.ipynb`
- `Week 8-1 Python_Cheat_Sheet code/Week 8-1 Python_Cheat_Sheet_validated_practice.ipynb`

### Chapter 5. Cleaning and Structuring Market Data

Learning objectives:
- Clean OHLCV data and exchange exports into analysis-ready tables.
- Handle dates, calendars, column names, and file round-trips correctly.
- Explain why data hygiene is part of strategy validation.

Chapter sections:
1. The OHLCV schema and market-data assumptions
2. Reading CSV and Excel market files
3. Calendar slicing and date indexes
4. Candles and feature-ready price data
5. Data audits before research
6. Practice Now: clean HDFCBANK exchange data

Chapter source references:
- `Week 7-1 Tutorial Doubt-Solving on Python after PBQ-02.html`
- `Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01.html`
- `Week 6-3 PBQ-02 Python Basics for Quants.html`

Chapter practice references:
- `Week 7-1 Tutorial Python after PBQ-02 code/Week 7-1 Tutorial Doubt-Solving Python after PBQ-02_validated_practice.ipynb`
- `Week 8-1 Tutorial Python after DMP-01 code/Week 8-1 Tutorial Session - Doubt Solving on Python after DMP-01_validated_practice.ipynb`

### Chapter 6. Building Reusable Strategy Code

Learning objectives:
- Explain why trading research needs reusable objects and modules.
- Convert repeated notebook logic into classes and functions.
- Identify the roles of data, alpha, and performance modules.

Chapter sections:
1. From one-off notebooks to reusable research code
2. Objects, methods, and class attributes
3. A backtesting class as a strategy container
4. Modular alpha, data, and performance analytics
5. Validation controls for reusable code
6. Practice Now: compare two strategy objects

Chapter source references:
- `Week 8-2 DMP-02 Introduction to Object Oriented Programming.html`
- `Week 9-1 DMP-03 Object Oriented Programming In Python.html`
- `Week 25-1 DMP-05 QuantiP.html`
- `Data Analysis & Modeling in Python (DMP)`

Chapter practice references:
- `Week 8-2 DMP-02 Introduction to OOP code/Week 8-2 DMP-02 Introduction to Object Oriented Programming_validated_practice.ipynb`
- `Week 25-1 DMP-05 QuantiP code/Week 25-1 DMP-05 QuantiP_validated_practice.ipynb`
- `Week 25-1 DMP-05 QuantiP code/alpha.py`
- `Week 25-1 DMP-05 QuantiP code/data.py`
- `Week 25-1 DMP-05 QuantiP code/performance_analytics.py`

## Part 3: Returns, Risk, Statistics, and Time Series

### Chapter 7. Return Math and Basic Statistics

Learning objectives:
- Calculate simple and log returns from first principles.
- Explain compounding, annualization, variance, standard deviation, and covariance.
- Use small examples to verify return and risk formulas.

Chapter sections:
1. Price changes and return definitions
2. Simple returns vs log returns
3. Mean, variance, standard deviation, and Bessel correction
4. Covariance and basic portfolio math
5. Annualization and Monte Carlo intuition
6. Practice Now: compute returns and volatility from Nifty data

Chapter source references:
- `Week 3-2 SFM-03 Practical Session Basic Statistics using Excel.html`
- `Week 7-2 DMP-01 Strategy Back Testing using Python.html`
- `Statistics for Financial Markets (SFM)/SFM02 Basic Statistics`
- `Statistics for Financial Markets (SFM)/SFM-03 Practical session Basic Statistics using Excel`

Chapter practice references:
- `Week 3-2 SFM-03 code/Week 3-2 SFM-03 Basic Statistics_validated_practice.ipynb`
- `Week 7-2 DMP-01 Strategy Back Testing code/Week 7-2 DMP-01 Strategy Back Testing_validated_practice.ipynb`

### Chapter 8. Risk, Drawdowns, and Performance Metrics

Learning objectives:
- Calculate drawdown, Sharpe-style ratios, hit ratio, and normalized hit ratio.
- Explain position sizing and Kelly intuition without overstating its live usability.
- Connect VaR/CVaR and liquidity risk to strategy controls.

Chapter sections:
1. Return alone is not performance
2. Drawdowns and path dependence
3. Hit ratio, payoff ratio, and normalized hit ratio
4. Kelly sizing and fractional Kelly discipline
5. VaR, CVaR, liquidity, and risk controls
6. Practice Now: evaluate a strategy scorecard

Chapter source references:
- `Week 4-2 EFS-01 Strategy Building in Equities.html`
- `Week 15-1 PRM-01 Portfolio & Risk Management.html`
- `Week 25-1 DMP-05 QuantiP.html`
- `Portfolio Optimization & Risk Management (PRM)/PRM01 Portfolio Management & Risk Management for Algorithmic Trading`

Chapter practice references:
- `Week 4-2 EFS-01 code/Week 4-2 EFS-01 Strategy Building in Equities_validated_practice.ipynb`
- `Week 15-1 PRM-01 Portfolio & Risk Management code/Week 15-1 PRM-01 Portfolio & Risk Management_validated_practice.ipynb`
- `Week 25-1 DMP-05 QuantiP code/performance_analytics.py`

### Chapter 9. Statistical Testing for Market Data

Learning objectives:
- Explain stationarity and why returns are modeled differently from prices.
- Interpret ACF/PACF and autocorrelation diagnostics.
- Distinguish correlation, cointegration, and causal evidence.

Chapter sections:
1. Prices, returns, and stationarity
2. Random walks and weak predictability
3. ADF, ACF, and PACF as diagnostic tools
4. Correlation vs cointegration
5. IID assumptions and regime risk
6. Practice Now: test predictability in returns

Chapter source references:
- `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data.html`
- `Week 9-1 DMP-03 Object Oriented Programming In Python.html`
- `Week 17-1 EFS-02 Statistical Arbitrage and Pair trading Equity, FX & Futures Strategies.html`
- `Week 22-1 MLT-05 Statistical Arbitrage with PCA.html`

Chapter practice references:
- `Week 10-1 ASQ-01 Statistical Analysis code/Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data_validated_practice.ipynb`
- `Week 9-1 DMP-03 OOP in Python code/Week 9-1 DMP-03 Object Oriented Programming In Python_validated_practice.ipynb`

### Chapter 10. Time-Series Forecasting and Volatility Models

Learning objectives:
- Explain AR, MA, ARIMA, ARCH, and GARCH from intuition first.
- Build rolling forecasts and evaluate them after cost drag.
- Compare volatility estimators and volatility regime behavior.

Chapter sections:
1. Forecasting one step ahead
2. ARIMA order and information criteria
3. Rolling forecasts and instability
4. Volatility clustering and heteroscedasticity
5. ARCH/GARCH and risk sizing
6. Practice Now: compare ARIMA and GARCH outputs

Chapter source references:
- `Week 10-1 ASQ-01 Statistical Analysis of Financial Market Data.html`
- `Week 12-1 ASQ-02 Time Series Modeling with Python.html`
- `Week 19-2 OTS-04 Volatility Measurement, Forecasting, and Structuring Volatility Trades Options Trading & Strategie.html`
- `Advanced Statistics for Quant Strategies (ASQ)`

Chapter practice references:
- `Week 12-1 ASQ-02 Time Series Modeling code/Week 12-1 ASQ-02 Time Series Modeling with Python_validated_practice.ipynb`
- `Week 19-2 OTS-04 Volatility Measurement code/Week 19-2 OTS-04 Volatility Measurement_validated_practice.ipynb`

## Part 4: Indicators, Signals, and Strategy Design

### Chapter 11. Indicator Strategies and Rule-Based Systems

Learning objectives:
- Convert indicators into signals, positions, and strategy returns.
- Explain why shifting positions prevents lookahead bias.
- Evaluate parameter surfaces and out-of-sample behavior.

Chapter sections:
1. Indicators as rules, not predictions
2. Signal, position, and return alignment
3. Moving-average crossover as a teaching system
4. RSI and MACD as platform examples
5. Parameter robustness and out-of-sample testing
6. Practice Now: build and evaluate a crossover rule

Chapter source references:
- `Week 4-2 EFS-01 Strategy Building in Equities.html`
- `Week 7-2 DMP-01 Strategy Back Testing using Python.html`
- `Week 22-2 TBP-03 Backtesting using Blueshift.html`

Chapter practice references:
- `Week 7-2 DMP-01 Strategy Back Testing code/Week 7-2 DMP-01 Strategy Back Testing_validated_practice.ipynb`
- `Week 22-2 TBP-03 Backtesting using Blueshift code/TBP03_MACD_source.py`
- `Week 22-2 TBP-03 Backtesting using Blueshift code/TBP03_rsi_strategy_source.py`

### Chapter 12. Futures, Momentum, and Regime-Aware Strategies

Learning objectives:
- Explain spot return, roll return, backwardation, and contango.
- Understand why futures data construction affects strategy returns.
- Identify momentum crashes and regime-dependent behavior.

Chapter sections:
1. Futures returns: spot plus roll
2. Forward curves and roll yield
3. Data hygiene in futures research
4. Momentum, hedges, and crisis behavior
5. Regime and crash controls
6. Practice Now: estimate roll return and inspect crash controls

Chapter source references:
- `Week 14-1 EFS-03 Quantitative Momentum Strategies I.html`
- `Week 14-2 EFS-04 Quantitative Momentum Strategies II.html`
- `Equity, FX, & Futures Strategies (EFS)/EFS03 & 04 Quantitative Momentum Strategies - I & II`

Chapter practice references:
- `Week 14-1 EFS-03 Quantitative Momentum Strategies I code/Week 14-1 EFS-03 Quantitative Momentum Strategies I_validated_practice.ipynb`
- `Week 14-2 EFS-04 Quantitative Momentum Strategies II code/Week 14-2 EFS-04 Quantitative Momentum Strategies II_validated_practice.ipynb`

### Chapter 13. ETFs and Tradable Baskets

Learning objectives:
- Explain ETF creation/redemption and secondary-market trading.
- Connect NAV, iNAV, index divisor, and basket mechanics.
- Interpret ETF premiums/discounts as arbitrage and liquidity signals.

Chapter sections:
1. ETF as listed fund and portfolio basket
2. Index divisor and corporate actions
3. Creation/redemption in the primary market
4. Secondary-market premium/discount
5. ETF trading model ladder
6. Practice Now: map a creation/redemption workbook

Chapter source references:
- `Week 13-1 EFS-05 Trading ETFs.html`
- `Equity, FX, & Futures Strategies (EFS)/EFS05 Trading ETFs`

Chapter practice references:
- `Week 13-1 EFS-05 Trading ETFs code/Week 13-1 EFS-05 Trading ETFs_validated_practice.ipynb`
- `Week 13-1 EFS-05 Trading ETFs code/EFS-05_data_ETF_Seminar_Data_source.xlsx`

### Chapter 14. Statistical Arbitrage and Pairs Trading

Learning objectives:
- Explain spread trading and hedge-ratio intuition.
- Test stationarity and cointegration before trading a pair.
- Define entry/exit bands and risk controls.

Chapter sections:
1. Pair trading as market-neutral relative value
2. Correlation is not cointegration
3. Constructing a spread and testing stationarity
4. Bollinger bands and mean reversion logic
5. Pair risk management and failure modes
6. Practice Now: trade AUDCAD and EWA/EWC spreads

Chapter source references:
- `Week 17-1 EFS-02 Statistical Arbitrage and Pair trading Equity, FX & Futures Strategies.html`
- `Equity, FX, & Futures Strategies (EFS)/EFS02 Statistical Arbitrage And Pair Trading`

Chapter practice references:
- `Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading code/Week 17-1 EFS-02 Statistical Arbitrage and Pair Trading_validated_practice.ipynb`

### Chapter 15. PCA-Based Statistical Arbitrage

Learning objectives:
- Explain PCA as variance decomposition and factor extraction.
- Use PCA diagnostics to understand factor exposures.
- Connect PCA residuals to statistical-arbitrage spreads.

Chapter sections:
1. From pairs to many-asset relative value
2. PCA intuition: rotate, rank, compress
3. Explained variance and component weights
4. PCA spreads and backtests
5. Limits of PCA stat-arb
6. Practice Now: inspect SPY/QQQ and index PCA diagnostics

Chapter source references:
- `Week 22-1 MLT-05 Statistical Arbitrage with PCA.html`
- `Machine Learning for Trading (MLT)/MLT05 Statistical Arbitrage with PCA`

Chapter practice references:
- `Week 22-1 MLT-05 Statistical Arbitrage with PCA code/Week 22-1 MLT-05 Statistical Arbitrage with PCA_validated_practice.ipynb`
- `Week 22-1 MLT-05 Statistical Arbitrage with PCA code/PCA_3_source.ipynb`

## Part 5: Backtesting and Performance Evaluation

### Chapter 16. Vectorized Backtesting

Learning objectives:
- Build a fast vectorized backtest using signal, position, and return columns.
- Explain why `.shift()` is required before applying strategy returns.
- Compare equity curves and benchmark returns correctly.

Chapter sections:
1. The seven-step strategy workflow
2. Signal construction
3. Position lagging and lookahead control
4. Equity curves and metrics
5. Vectorized limitations
6. Practice Now: run a long/short crossover backtest

Chapter source references:
- `Week 7-2 DMP-01 Strategy Back Testing using Python.html`
- `Week 8-1 Python_Cheat_Sheet.html`
- `Data Analysis & Modeling in Python (DMP)`

Chapter practice references:
- `Week 7-2 DMP-01 Strategy Back Testing code/Week 7-2 DMP-01 Strategy Back Testing_validated_practice.ipynb`
- `Week 8-1 Python_Cheat_Sheet code/Week 8-1 Python_Cheat_Sheet_validated_practice.ipynb`

### Chapter 17. Event-Driven Backtesting

Learning objectives:
- Explain event queues, event types, and event loops.
- Compare vectorized and event-driven backtest assumptions.
- Identify point-in-time and live-data-stream constraints.

Chapter sections:
1. Why event-driven backtesting exists
2. Market, signal, order, and fill events
3. Event loop and state update
4. Hyperparameters and risk statistics
5. Platform mapping to Blueshift-style APIs
6. Practice Now: run a minimal event-driven engine

Chapter source references:
- `Week 9-2 DMP-04 Event Driven Back-Testing and working with Live Data Stream.html`
- `Week 22-2 TBP-03 Backtesting using Blueshift.html`
- `Data Analysis & Modeling in Python (DMP)`
- `Trading & Back-testing Platforms (TBP)/TBP03 Backtesting using Blueshift`

Chapter practice references:
- `Week 9-2 DMP-04 Event-Driven Backtesting code/Week 9-2 DMP-04 Event Driven Back-Testing and working with Live Data Stream_validated_practice.ipynb`
- `Week 22-2 TBP-03 Backtesting using Blueshift code/Week 22-2 TBP-03 Backtesting using Blueshift_validated_practice.ipynb`

### Chapter 18. Backtest Honesty and Failure Modes

Learning objectives:
- Identify lookahead bias, leakage, overfitting, and cost omission.
- Interpret holdout degradation and production-readiness flags.
- Use dependency and validation reports as part of the research record.

Chapter sections:
1. How backtests lie
2. Lookahead and point-in-time errors
3. Parameter mining and overfitting
4. Transaction costs and cost erasure
5. Holdout degradation and production readiness
6. Practice Now: read a leakage and cost-control report

Chapter source references:
- `Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms.html`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning.html`
- `Week 22-2 TBP-03 Backtesting using Blueshift.html`

Chapter practice references:
- `Week 16-1 TBP-05 code/Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms_validated_practice.ipynb`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_validated_practice.ipynb`

## Part 6: Portfolio Construction and Risk Management

### Chapter 19. Portfolio Construction

Learning objectives:
- Calculate portfolio return and variance from weights and covariance.
- Explain diversification, correlation, and systematic risk.
- Interpret efficient-frontier and out-of-sample portfolio results.

Chapter sections:
1. Portfolio objective and universe
2. Return and risk for one asset
3. Covariance and two-asset diversification
4. Multi-asset frontier and constraints
5. Out-of-sample portfolio testing
6. Practice Now: build frontier weights

Chapter source references:
- `Week 24-1 PRM-02 Quantitative Portfolio Management.html`
- `Portfolio Optimization & Risk Management (PRM)/PRM02 Quantitative Portfolio Management`
- `Week 3-2 SFM-03 Practical Session Basic Statistics using Excel.html`

Chapter practice references:
- `Week 24-1 PRM-02 Quantitative Portfolio Management code/Week 24-1 PRM-02 Quantitative Portfolio Management_validated_practice.ipynb`

### Chapter 20. Portfolio Risk Controls

Learning objectives:
- Build a risk-control taxonomy for strategy and portfolio operations.
- Explain VaR/CVaR, liquidity, pre-trade controls, and incident management.
- Connect risk controls to desk operations and regulatory obligations.

Chapter sections:
1. Risk taxonomy for algorithmic trading
2. Market, liquidity, credit, and operational risk
3. Pre-trade gateway and risk limits
4. Incident controls and governance
5. Desk operations and regulatory controls
6. Practice Now: complete a risk control matrix

Chapter source references:
- `Week 15-1 PRM-01 Portfolio & Risk Management.html`
- `Week 26-1 TIO-02 Tackling desk operations and Regulatory environment.html`
- `Portfolio Optimization & Risk Management (PRM)/PRM01 Portfolio Management & Risk Management for Algorithmic Trading`
- `Trading Tech, Infra & Operations (TIO)/TIO02 Tackling Desk Operations and Regulatory Environment`

Chapter practice references:
- `Week 15-1 PRM-01 Portfolio & Risk Management code/Week 15-1 PRM-01 Portfolio & Risk Management_validated_practice.ipynb`
- `Week 26-1 TIO-02 Tackling desk operations and Regulatory environment code/Week 26-1 TIO-02 Tackling desk operations and Regulatory environment_validated_practice.ipynb`

## Part 7: Machine Learning for Trading

### Chapter 21. Machine Learning Foundations for Time Series

Learning objectives:
- Explain supervised, unsupervised, and classification workflows.
- Build labels and features without leaking future data.
- Interpret classifier metrics and baseline comparisons.

Chapter sections:
1. What ML is and is not in trading
2. Labels, features, and time-series splits
3. Logistic regression, decision trees, and random forests
4. Confusion matrix, precision, recall, and base rate
5. SVM and clustering as additional tools
6. Practice Now: train and evaluate a TSLA classifier

Chapter source references:
- `Week 18-1 MLT-01 Machine Learning-I Machine Learning for Trading.html`
- `Week 19-1 MLT-02 Machine Learning-II Machine Learning for Trading.html`
- `Machine Learning for Trading (MLT)/MLT01 Machine Learning-I`
- `Machine Learning for Trading (MLT)/MLT02 Machine Learning-II`

Chapter practice references:
- `Week 18-1 MLT-01 Machine Learning-I code/Week 18-1 MLT-01 Machine Learning-I_validated_practice.ipynb`
- `Week 19-1 MLT-02 Machine Learning-II code/Week 19-1 MLT-02 Machine Learning-II_validated_practice.ipynb`

### Chapter 22. Feature Engineering, Model Risk, and Walk-Forward Testing

Learning objectives:
- Design feature families and compare them to a benchmark.
- Explain SHAP-style feature selection and hyperparameter tuning as validation risks.
- Interpret walk-forward, embargo, holdout, and leakage-control results.

Chapter sections:
1. The ML strategy research pipeline
2. Benchmark and feature tiers
3. Feature explosion and selection
4. Walk-forward validation and embargo
5. Holdout degradation and production verdict
6. Practice Now: inspect XLF feature and holdout results

Chapter source references:
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning.html`
- `Machine Learning for Trading (MLT)/MLT04 How to Develop a Trading Strategy using Machine Learning`

Chapter practice references:
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_validated_practice.ipynb`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/mlt04_walkforward.py`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/mlt04_models.py`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/mlt04_metrics.py`

### Chapter 23. Neural Networks and Deep Learning Cautions

Learning objectives:
- Explain activation functions, gradient descent, and backpropagation intuitively.
- Evaluate neural-network results on out-of-sample market data.
- Identify why complexity increases model-risk pressure.

Chapter sections:
1. Artificial neuron intuition
2. Activation functions and nonlinear flexibility
3. Gradient descent and backpropagation
4. Neural network on EUR/USD
5. Text mining bridge and model-risk controls
6. Practice Now: inspect MLP metrics and backtest output

Chapter source references:
- `Week 20-1 MLT-03 Machine Learning-III Machine Learning for Tradin.html`
- `Machine Learning for Trading (MLT)/MLT03 Machine Learning-III`

Chapter practice references:
- `Week 20-1 MLT-03 Machine Learning-III code/Week 20-1 MLT-03 Machine Learning-III_validated_practice.ipynb`

### Chapter 24. NLP and Sentiment as Trading Inputs

Learning objectives:
- Clean and vectorize text for financial modeling.
- Align sentiment records with price data.
- Test whether sentiment adds tradable information.

Chapter sections:
1. Text as alternative data
2. Preprocessing and entity extraction
3. Vectorization, LSA, and topic modeling
4. Sentiment records and price alignment
5. Signal tests and validation controls
6. Practice Now: overlay sentiment with Baidu prices

Chapter source references:
- `Week 23-1 MLT-06 Natural Language Processing and Sentiment Analysis in Trading.html`
- `Machine Learning for Trading (MLT)/MLT06 Natural Language Processing and Sentiment Analysis in Trading`

Chapter practice references:
- `Week 23-1 MLT-06 Natural Language Processing and Sentiment Analysis in Trading code/Week 23-1 MLT-06 Natural Language Processing and Sentiment Analysis in Trading_validated_practice.ipynb`

### Chapter 25. Reinforcement Learning for Trading

Learning objectives:
- Define state, action, reward, policy, and Q-value.
- Explain Bellman updates and experience replay at a practical level.
- Identify market-specific RL failure modes: overfit, fat tails, reward hacking, and nonstationarity.

Chapter sections:
1. Why RL is different from supervised prediction
2. State, action, reward, and Bellman logic
3. Q-learning and DQN controls
4. Overfitting, fat tails, and predictability
5. Reward design and trading realism
6. Practice Now: review Q-learning and reward controls

Chapter source references:
- `Week 23-2 MLT-07 Reinforcement Learning in Trading.html`
- `Machine Learning for Trading (MLT)/MLT07 Reinforcement Learning in Trading`

Chapter practice references:
- `Week 23-2 MLT-07 Reinforcement Learning in Trading code/Week 23-2 MLT-07 Reinforcement Learning in Trading_validated_practice.ipynb`

## Part 8: Options and Volatility

### Chapter 26. Options Payoffs, Pricing, and Greeks

Learning objectives:
- Explain options payoffs and pricing inputs.
- Calculate and interpret Black-Scholes prices and Greeks.
- Use put-call parity and model assumptions as sanity checks.

Chapter sections:
1. Payoff vs P&L
2. Calls, puts, straddles, and volatility exposure
3. Black-Scholes from intuition to formula
4. Greeks as risk sensitivities
5. Parity, arbitrage, and model limits
6. Practice Now: price options and inspect Greeks

Chapter source references:
- `Week 15-2 OTS-02 Volatility Trading and Variance Premium.html`
- `Week 17-2 OTS-03 Options Pricing Models and Greeks Options Trading & Strategies.html`
- `Options Trading & Strategies (OTS)/OTS02 Volatility Trading and Variance Premium`
- `Options Trading & Strategies (OTS)/OTS03 Options Pricing Models and Greeks`

Chapter practice references:
- `Week 17-2 OTS-03 Options Pricing Models and Greeks code/Week 17-2 OTS-03 Options Pricing Models and Greeks_validated_practice.ipynb`
- `Week 15-2 OTS-02 Volatility Trading and Variance Premium code/Week 15-2 OTS-02 Volatility Trading and Variance Premium_validated_practice.ipynb`

### Chapter 27. Volatility Trading and Variance Premium

Learning objectives:
- Compare realized, implied, rolling, EWMA, and model-based volatility.
- Explain the variance premium and why it is not free money.
- Connect volatility forecasts to vega exposure and regime controls.

Chapter sections:
1. Volatility as an asset and risk factor
2. Realized vs implied volatility
3. Volatility estimators and forecast context
4. Variance premium and adverse selection
5. Structuring vol trades with controls
6. Practice Now: compare estimators and variance-premium demos

Chapter source references:
- `Week 15-2 OTS-02 Volatility Trading and Variance Premium.html`
- `Week 19-2 OTS-04 Volatility Measurement, Forecasting, and Structuring Volatility Trades Options Trading & Strategie.html`
- `Week 12-1 ASQ-02 Time Series Modeling with Python.html`

Chapter practice references:
- `Week 19-2 OTS-04 Volatility Measurement code/Week 19-2 OTS-04 Volatility Measurement_validated_practice.ipynb`
- `Week 15-2 OTS-02 Volatility Trading and Variance Premium code/Week 15-2 OTS-02 Volatility Trading and Variance Premium_validated_practice.ipynb`

### Chapter 28. Evaluating and Backtesting Options Trades

Learning objectives:
- Explain dynamic hedging, hedge frequency, and volatility choice.
- Evaluate option strategy PnL with attribution and drawdown.
- Build options backtests with chain-quality and calendar controls.

Chapter sections:
1. Options trade evaluation and hedging
2. Delta/gamma bands and hedge frequency
3. Implied vs realized volatility in hedging
4. Options chain quality and tradable contracts
5. Event-based options backtesting
6. Practice Now: backtest an ATM long-call setup

Chapter source references:
- `Week 20-2 OTS-05 Trade Evaluation Options Trading & Strategies.html`
- `Week 21-1 OTS-06 Creating an Options Backtesting Model Options Trading & Strategies.html`
- `Options Trading & Strategies (OTS)/OTS05 Trade Evaluation`
- `Options Trading & Strategies (OTS)/OTS06 Creating an Options Backtesting Model`

Chapter practice references:
- `Week 20-2 OTS-05 Trade Evaluation code/Week 20-2 OTS-05 Trade Evaluation_validated_practice.ipynb`
- `Week 21-1 OTS-06 Creating an Options Backtesting Model code/Week 21-1 OTS-06 Creating an Options Backtesting Model_validated_practice.ipynb`

## Part 9: Execution, APIs, and Live Trading Workflow

### Chapter 29. Broker APIs, REST, WebSockets, and Market Data Plumbing

Learning objectives:
- Explain broker API, REST, and WebSocket workflows.
- Interpret request components, status codes, JSON payloads, and order audit logs.
- Distinguish local mock validation from live broker readiness.

Chapter sections:
1. API mental model
2. Interactive Brokers callback architecture
3. REST request anatomy and status codes
4. WebSockets, heartbeats, and streaming data
5. Order logs and failure controls
6. Practice Now: inspect mock REST orders and WebSocket messages

Chapter source references:
- `Week 10-2 TBP-01 IB Python API.html`
- `Week 12-2 TBP-02 Rest API Trading & Back-testing Platforms.html`
- `Trading & Back-testing Platforms (TBP)/TBP01 IB Python API`
- `Trading & Back-testing Platforms (TBP)/TBP02 REST API`
- `Trading & Back-testing Platforms (TBP)/Live Trading using IB API`

Chapter practice references:
- `Week 10-2 TBP-01 IB Python API code/Week 10-2 TBP-01 IB Python API_validated_practice.ipynb`
- `Week 12-2 TBP-02 Rest API code/Week 12-2 TBP-02 Rest API_validated_practice.ipynb`

### Chapter 30. Backtesting Platforms and Live Robot Controls

Learning objectives:
- Map research logic into platform-specific strategy scripts.
- Explain scheduler, error handling, early-close, alerting, and live robot controls.
- Identify deployment dependencies and platform limitations.

Chapter sections:
1. Why platforms exist
2. Blueshift-style event engine
3. IBridgePy strategy anatomy
4. Live robot controls and reference maps
5. Dependency and operational caveats
6. Practice Now: inspect platform strategy scripts and robot scoreboard

Chapter source references:
- `Week 22-2 TBP-03 Backtesting using Blueshift.html`
- `Week 11-1 TBP-04 Backtest and Live Trade Algo Strategie.html`
- `Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms.html`
- `Trading & Back-testing Platforms (TBP)/TBP03 Backtesting using Blueshift`
- `Trading & Back-testing Platforms (TBP)/TBP-04 & 05-Backtest And Live Trade Algo Strategies I & II`

Chapter practice references:
- `Week 22-2 TBP-03 Backtesting using Blueshift code/Week 22-2 TBP-03 Backtesting using Blueshift_validated_practice.ipynb`
- `Week 16-1 TBP-05 code/Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms_validated_practice.ipynb`
- `Week 16-1 TBP-05 code/reference_ibridgepy_strategies`

### Chapter 31. Production Architecture, Desk Operations, and Regulation

Learning objectives:
- Explain trading-system architecture from market data to RMS to order gateway.
- Interpret latency, colocation, membership, and platform cost tradeoffs.
- Identify operational and regulatory controls before live trading.

Chapter sections:
1. Trading-system components
2. Market-data adapter, normalizer, and order manager
3. FIX, RMS, and fat-finger controls
4. Latency, colocation, and desk setup
5. Regulatory and operational control matrix
6. Practice Now: map a production architecture and control stack

Chapter source references:
- `Week 6-2 TIO-01 System Architecture.html`
- `Week 26-1 TIO-02 Tackling desk operations and Regulatory environment.html`
- `Trading Tech, Infra & Operations (TIO)/TIO01 System Architecture`
- `Trading Tech, Infra & Operations (TIO)/TIO02 Tackling Desk Operations and Regulatory Environment`

Chapter practice references:
- `Week 6-2 TIO-01 System Architecture code/Week 6-2 TIO-01 System Architecture_validated_practice.ipynb`
- `Week 26-1 TIO-02 Tackling desk operations and Regulatory environment code/Week 26-1 TIO-02 Tackling desk operations and Regulatory environment_validated_practice.ipynb`

## Part 10: Final Trading Playbook

### Chapter 32. The Research-to-Live Checklist

Learning objectives:
- Assemble a staged checklist from hypothesis through monitoring.
- Combine data audit, validation, cost model, risk limits, and live controls.
- Write a go/no-go research memo based on evidence.

Chapter sections:
1. The full research-to-live gate sequence
2. Hypothesis and data audit
3. Backtest, cost, and risk gates
4. Portfolio and deployment gates
5. Monitoring, review, and kill switches
6. Practice Now: complete a launch checklist

Chapter source references:
- `Week 25-1 DMP-05 QuantiP.html`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning.html`
- `Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms.html`
- `Week 15-1 PRM-01 Portfolio & Risk Management.html`
- `Week 26-1 TIO-02 Tackling desk operations and Regulatory environment.html`

Chapter practice references:
- `Week 25-1 DMP-05 QuantiP code/Week 25-1 DMP-05 QuantiP_validated_practice.ipynb`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning_validated_practice.ipynb`
- `Week 16-1 TBP-05 code/Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms_validated_practice.ipynb`

### Chapter 33. Capstone: Build, Test, Risk-Control, and Operate a Strategy

Learning objectives:
- Integrate data, alpha, backtest, risk, cost, and live-readiness workflows.
- Rebuild a strategy in a reusable framework.
- Produce a final strategy dossier with evidence and caveats.

Chapter sections:
1. Capstone brief and strategy choice
2. Data audit and source inventory
3. Alpha module and backtest engine
4. Risk, cost, and portfolio context
5. Live-readiness and monitoring plan
6. Practice Now: produce the final go/no-go memo

Chapter source references:
- `Week 25-1 DMP-05 QuantiP.html`
- `Week 9-2 DMP-04 Event Driven Back-Testing and working with Live Data Stream.html`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning.html`
- `Week 12-2 TBP-02 Rest API Trading & Back-testing Platforms.html`
- `Week 16-1 TBP-05 Backtest and live trade algo strategies II Trading & Back-testing Platforms.html`

Chapter practice references:
- `Week 25-1 DMP-05 QuantiP code/Week 25-1 DMP-05 QuantiP_validated_practice.ipynb`
- `Week 25-1 DMP-05 QuantiP code/alpha.py`
- `Week 25-1 DMP-05 QuantiP code/data.py`
- `Week 25-1 DMP-05 QuantiP code/performance_analytics.py`
- `Week 21-2 MLT-04 How to Develop a Trading Strategy using Machine Learning code/mlt04_walkforward.py`
