# Week 12-2 TBP-02 REST API Code Resources

Additive resources generated for the TBP-02 validation pass. The original practice notebook, historical sample, and chart were not replaced.

## Original files retained

- `Week 12-2 TBP-02 Rest API_practice.ipynb`
- `historical_sample.csv`
- `chart_1_rest.png`

## Files added

- `TBP02_code_cp_web_api_functions_source.py` - source REST helper library from the class zip.
- `TBP02_code_Entry_Point_source.py` - source entry-point script.
- `Real_Time_Data_Using_Websockets_source.py` - source IB WebSocket example.
- `TBP02_code_Crypto_Data_From_Alpaca_source.py` - source Alpaca WebSocket example.
- `TBP02_other_READ_ME_source.txt` - source README.
- `TBP02_other_alpaca_keys_placeholder_source.txt` - placeholder key file from source; it contains no live credentials.
- `Strategy_TBP02_code_base_functions_source.py` - source strategy helper library.
- `Strategy_TBP02_code_RSI_Intraday_Strategy_source.py` - source RSI intraday strategy, preserved unchanged.
- `Week 12-2 TBP-02 Rest API_resource_addendum_practice.ipynb` - standalone offline addendum notebook.
- `Week 12-2 TBP-02 Rest API_validated_practice.ipynb` - original notebook plus the additive source validation section.
- `tbp02_source_file_inventory.csv`
- `tbp02_endpoint_reference.csv`
- `tbp02_status_code_reference.csv`
- `tbp02_rest_websocket_reference.csv`
- `tbp02_rsi_strategy_decision_table.csv`
- `tbp02_mock_request_log.csv`
- `tbp02_mock_websocket_messages.csv`
- `tbp02_mock_order_audit.csv`
- `tbp02_offline_rsi_strategy_sample.csv`
- `tbp02_offline_rsi_strategy_full.csv`
- `tbp02_offline_rsi_strategy_metrics.csv`
- `tbp02_heartbeat_schedule.csv`
- `chart_addendum_1_tbp02_source_architecture.png`
- `chart_addendum_2_tbp02_endpoint_coverage.png`
- `chart_addendum_3_tbp02_rest_vs_websocket.png`
- `chart_addendum_4_tbp02_offline_rsi_strategy.png`
- `chart_addendum_5_tbp02_correction_heartbeat.png`
- `tbp02_validation_execution_summary.json`

## Source anchors

- Transcript: REST as broker-agnostic HTTP request/response, five request pieces, two response parts, status-code families, JSON, manual login, and heartbeat/tickle.
- Official source zip: REST helper functions, entry point, IB WebSocket stream, Alpaca crypto stream, strategy base functions, and RSI intraday strategy.
- Local historical data: `historical_sample.csv` powers the offline corrected RSI example.

## Accuracy note

The source RSI strategy is preserved unchanged. The addendum flags and corrects the close-position branch where the source uses `order_action == 'SELL'` and `order_action == 'BUY'` instead of assignment for exit orders.
