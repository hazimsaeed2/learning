# TBP-01 Validation Report

Lecture: Week 10-2 TBP-01 IB Python API

## Files Reviewed

- `Week 10-2 TBP-01 IB Python API.html`
- `Week 10-2 TBP-01 IB Python API_study.html`
- `Week 10-2 TBP-01 IB Python API.txt`
- `Week 10-2 TBP-01 IB Python API code/Week 10-2 TBP-01 IB Python API_practice.ipynb`
- `Week 10-2 TBP-01 IB Python API code/historical_sample.csv`
- `Trading & Back-testing Platforms (TBP)/TBP01 IB Python API` PDFs and source ZIP

## Additive Changes Made

- Added source inventory, safe notebook execution audit, mock API checks, historical-data checks, live-scope controls, and validation controls.
- Added five validation charts with `chart_addendum_*_tbp01_*.png` names.
- Added an addendum notebook and a validated notebook copy. The original notebook remains unchanged.
- Appended marked validation sections to the main HTML page and study guide.

## Source Inventory

| artifact | artifact_type | exists | size_bytes | rows | columns | note |
| --- | --- | --- | --- | --- | --- | --- |
| Week 10-2 TBP-01 IB Python API_practice.ipynb | practice_notebook | True | 96929 |  |  | 8 code cells, 13 markdown cells |
| historical_sample.csv | source_data | True | 75044 | 962 | 6 | 2017-01-02 through 2020-11-27 |
| chart_1_ibapi.png | original_chart | True | 59270 |  |  | Existing chart preserved; addendum charts use separate names. |
| TBP-01-Lecture-Objectives-Prerequisities.pdf | source_pdf | True | 147411 | 1 | 12 | 1064 text chars; keyword hits in columns field. |
| TBP-01IB-Python-API.pdf | source_pdf | True | 567617 | 28 | 125 | 6029 text chars; keyword hits in columns field. |
| TBP-01Pre-requisites-Installation-Guide.pdf | source_pdf | True | 879513 | 3 | 43 | 2922 text chars; keyword hits in columns field. |
| TBP01-Lecture-Summary.pdf | source_pdf | True | 526095 | 6 | 81 | 3803 text chars; keyword hits in columns field. |
| TBP01-Inclass-Exercises-File.zip | source_zip | True | 33104 | 18 |  | Source ZIP inventoried; original archive preserved. |

## Notebook Execution

| metric | value | unit | reading |
| --- | --- | --- | --- |
| code_cells | 8 | cells | Original executable cells. |
| markdown_cells | 13 | cells | Original explanatory cells. |
| safe_execution_errors | 0 | errors | PASS |
| sync_time_seconds | 0.1522 | seconds | Sequential mock requests. |
| async_time_seconds | 0.0701 | seconds | Threaded mock requests. |
| async_speedup | 2.1699 | multiple | Sync time divided by async time. |
| historical_callback_rows | 10 | bars | Rows received through mock historicalData callbacks. |
| cleanup_connected_state | False | bool | Mock app disconnected after safe execution. |

## Mock API Metrics

| check | value | unit | reading |
| --- | --- | --- | --- |
| mini_server_ping | PONG | response | Structured request/response concept. |
| mini_server_time | server-time: 12:00:00 | response | Known request returns known response. |
| mini_server_error | ERROR: unknown request | response | Unknown request handled explicitly. |
| request_side_class | EClient | mock_class | Sends requests in the teaching mock. |
| response_side_class | EWrapper | mock_class | Receives callbacks in the teaching mock. |
| strategy_inheritance | Strategy(EClient, EWrapper) | class | Double inheritance mirrors IB API pattern. |
| listener_thread | daemon=True | thread | Mock listener runs separately from main request flow. |

## Historical Data Checks

| metric | value | unit | reading |
| --- | --- | --- | --- |
| source_rows | 962 | rows | Rows in local historical sample. |
| source_columns | 6 | columns | Date/OHLCV columns. |
| first_date | 2017-01-02 | date | Start date in source CSV. |
| last_date | 2020-11-27 | date | End date in source CSV. |
| callback_rows_requested | 10 | bars | Notebook requests tail(10). |
| callback_first_date | 2020-11-13 | date | First callback bar in request. |
| callback_last_date | 2020-11-27 | date | Last callback bar in request. |
| callback_close_min | 12719.950195 | price | Minimum close in callback sample. |
| callback_close_max | 13055.150391 | price | Maximum close in callback sample. |

## Live Scope Controls

| scope_item | validated_here | note |
| --- | --- | --- |
| TWS / IB Gateway running | no | Notebook uses a local mock, not a real socket. |
| IB account authentication | no | No credentials or live broker session are used. |
| API port and clientId settings | concept only | The example shows host/port/clientId shape but does not probe a live endpoint. |
| Market data permissions | no | Historical bars come from historical_sample.csv. |
| Callback wiring | yes | Mock EClient queues messages and EWrapper callbacks receive them. |
| Threaded listener pattern | yes | Execution uses a listener thread; validator disconnects the mock app afterward. |
| Order placement / fills | no | TBP-01 focuses on connectivity and data callbacks, not live orders. |

## Validation Controls

| control | lecture_application | additive_note |
| --- | --- | --- |
| Safe notebook execution | Run mock IB API notebook with noninteractive plotting. | Original file preserved; validator replaces plt.show only during temp execution. |
| Request/response audit | MiniServer PING/TIME/error examples. | Structured responses are recorded in CSV. |
| Async timing audit | Synchronous vs threaded mock waits. | Speedup is measured locally and may vary slightly per run. |
| Callback flow audit | EClient requests and EWrapper callbacks. | currentTime and historicalData callbacks execute through the mock listener. |
| Historical sample audit | reqHistoricalData mock returns tail rows. | 10 bars from local CSV are verified. |
| Live trading scope | IB API architecture. | No real TWS/Gateway, account, permissions, market data farm, or orders are validated. |

## Additive Scope Note

The original content is preserved. The validation addendum confirms the teaching mock and callback architecture only. It does not validate a real TWS/Gateway session, account authentication, market-data permissions, socket connectivity, live order placement, or broker-side order state.

## Notebook Validation

| Notebook | Code cells | Errors | Execution exception |
| --- | ---: | ---: | --- |
| `Week 10-2 TBP-01 IB Python API_practice.ipynb` | 8 | 0 | None |
| `Week 10-2 TBP-01 IB Python API_resource_addendum_practice.ipynb` | 4 | 0 | None |
| `Week 10-2 TBP-01 IB Python API_validated_practice.ipynb` | 12 | 0 | None |

## HTML Validation

| File | body open/close | html open/close | Generated chart refs | Missing generated charts |
| --- | ---: | ---: | ---: | --- |
| `Week 10-2 TBP-01 IB Python API.html` | 1/1 | 1/1 | 10 | None |
| `Week 10-2 TBP-01 IB Python API_study.html` | 1/1 | 1/1 | 5 | None |

Status: PASS
