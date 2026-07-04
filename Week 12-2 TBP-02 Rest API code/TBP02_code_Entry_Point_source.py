# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:50:30 2021

@author: Jay Parmar

@documentation: https://interactivebrokers.github.io/cpwebapi/index.html
"""

from cp_web_api_functions import (fetch_historical_data, 
                                  fetch_ltp,
                                  fetch_accounts, 
                                  get_account_pnl,
                                  auth_status, 
                                  reauthenticate, 
                                  get_portfolio_positions,
                                  fetch_contract_details, 
                                  get_positions_conid, 
                                  get_orders,
                                  place_orders, 
                                  validate_sso, 
                                  logout, 
                                  get_order_status)

# To check authentication status
auth_status()

# To fetch account details
fetch_accounts()

# To fetch a particular contract details
fetch_contract_details('173418084')

# To fetch ltp of a given contract
fetch_ltp('56985419')

# To fetch historical data of a given contract
df = fetch_historical_data()

print(df)

# To place order
res = place_orders('DU5017537')

# To get all order details
get_orders()

# Fetch order status of a given order
get_order_status('245264899')

# Fetch all portfolio positions
get_portfolio_positions('DU5017537')

# Fetch all positions of a particular contract
get_positions_conid('56985419')

# Fetch account PnL
get_account_pnl()

# Validate SSO
validate_sso()

# Reauthenticate user
reauthenticate()

# Logout user
logout()


















