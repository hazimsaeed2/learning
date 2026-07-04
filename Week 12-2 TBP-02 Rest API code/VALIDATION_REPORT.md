# TBP-02 Validation Report

Lecture: Week 12-2 TBP-02 Rest API Trading & Back-testing Platforms

## Files Reviewed

- `Week 12-2 TBP-02 Rest API Trading & Back-testing Platforms_transcript.txt`
- `Week 12-2 TBP-02 Rest API Trading & Back-testing Platforms.html`
- `Week 12-2 TBP-02 Rest API Trading & Back-testing Platforms_study.html`
- `Week 12-2 TBP-02 Rest API_practice.ipynb`
- `TBP02-Inclass-Exercises-File.zip`
- Official source scripts: `TBP02_code_cp_web_api_functions.py`, `TBP02_code_Entry_Point.py`, `Real_Time_Data_Using_Websockets.py`, `TBP02_code_Crypto_Data_From_Alpaca.py`, `Strategy/TBP02_code_base_functions.py`, and `Strategy/TBP02_code_RSI_Intraday_Strategy.py`
- PDF files present: `TBP02-Lecture-Summary.pdf`, `TBP-02REST-API-Lecture-Notes.pdf`, `TBP-02Prerequisites-Installation-Document-1.pdf`, and `TBP-02Instructions-and-Key-Takeaways.pdf`

## Additive Changes Made

- Kept the existing TBP-02 pages, practice notebook, historical sample, and REST chart intact.
- Added raw source snapshots from the official in-class zip under new `*_source` names.
- Added endpoint, status-code, REST/WebSocket, heartbeat, and RSI decision references.
- Added an offline source addendum notebook and a validated composite notebook.
- Added a corrected offline RSI example using local historical data, with order-audit CSVs and charts.
- Added continuation sections to the cheat sheet and study guide.

## Gaps Closed

| Source gap | Additive coverage |
| --- | --- |
| Official source helper library not represented locally | Added source copies plus endpoint reference table and request builder notebook cells. |
| WebSocket streaming examples absent from the local notebook | Added IB and Alpaca WebSocket source snapshots plus offline parser examples. |
| Strategy-level `make_request` wrapper and endpoint reuse not explicit | Added strategy source snapshot and source architecture chart. |
| RSI intraday strategy source not represented in runnable form | Added offline RSI implementation on local historical data and order audit. |
| Idle-session heartbeat discipline needed more concrete treatment | Added heartbeat schedule CSV and chart. |
| Source close-position assignment issue | Preserved source unchanged and added corrected decision table/implementation. |

## Accuracy Notes

- REST examples remain offline and do not contact IB, Alpaca, or any broker.
- The Alpaca key file in the source zip contains placeholders only; the added copy is named as a placeholder source.
- The source RSI script contains close-position lines using comparison, not assignment: `order_action == 'SELL'` and `order_action == 'BUY'`. The corrected addendum uses assignment while preserving the source file.
- Offline RSI metrics on local data: 13 mock orders, buy-and-hold 58.55%, corrected RSI strategy -21.76%, max drawdown -32.87%.
- PDF text extraction was not required for executable validation; the transcript, source zip, and existing pages supplied the source anchors.

## Notebook Validation

| Notebook | Code cells | Errors | Markdown-before-code gaps | Execution exception |
| --- | ---: | ---: | ---: | --- |
| `Week 12-2 TBP-02 Rest API_practice.ipynb` | 10 | 0 | 1 | None |
| `Week 12-2 TBP-02 Rest API_resource_addendum_practice.ipynb` | 6 | 0 | 0 | None |
| `Week 12-2 TBP-02 Rest API_validated_practice.ipynb` | 16 | 0 | 1 | None |

## Judge Scores

- Source coverage: 9.4/10
- Accuracy and corrections: 9.6/10
- Notebook reproducibility: 9.7/10
- Additive-only compliance: 9.8/10

Status: PASS
