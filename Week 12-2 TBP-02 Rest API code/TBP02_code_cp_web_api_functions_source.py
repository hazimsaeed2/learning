# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:54:23 2021

@author: Jay Parmar - QuantInsti Quantitative Learning Pvt Ltd

@documentation: https://www.interactivebrokers.com/api/doc.html
"""

# Import necessary libraries
import requests
from pprint import pprint
import warnings
import json
import pandas as pd
import time

# Ignore warnings
warnings.filterwarnings(action='ignore')

def validate_sso():
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Session/paths/~1sso~1validate/get
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to validate sso
    end_point = 'sso/validate'
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define parameters
    payload = {}
    
    # Request data
    response = requests.get(url, headers=headers, data=payload, verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Prints the response
    pprint(parsed_res)
    
    print('*' * 50)

def logout():
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Session/paths/~1logout/post
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to end the current session
    end_point = 'logout'
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define parameters
    payload={}
    
    # Request data
    response = requests.post(url, headers=headers, data=payload, verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Prints the response
    pprint(parsed_res)
    
    print('*' * 50)

def reauthenticate():
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Session/paths/~1iserver~1reauthenticate/post
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to reauthenticate the user
    end_point = 'iserver/reauthenticate'
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define parameters
    payload={}
    
    # Request data
    response = requests.post(url, headers=headers, data=payload, verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Prints the response
    pprint(parsed_res)
    
    print('*' * 50)

def auth_status():
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Session/paths/~1iserver~1auth~1status/post
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to check authentication status
    end_point = 'iserver/auth/status'
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define parameters
    payload = {}
    
    # Request data
    response = requests.post(url, headers=headers, data=payload, verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    print(f'Response: {response.text}')
    
    print('\n')
    
    print('Parsed Response:')
    
    # Parse the response
    parsed_res = json.loads(response.text) # Converts JSON object to native Python data structure
    
    print(type(parsed_res))
    
    # Prints the response
    # print(parsed_res)
    
    pprint(parsed_res)
    
    print('*' * 50)
    
def tickle():
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Session/paths/~1tickle/post
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint for keeping server connection alive
    end_point = 'tickle'
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define payload
    payload={}
    
    # Request data
    response = requests.post(url, headers=headers, data=payload, verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Prints the response
    pprint(parsed_res)
    
    print('*' * 50)
    
def fetch_contract_details(conid):
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Contract/paths/~1iserver~1contract~1{conid}~1info/get
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to fetch contract details
    end_point = 'iserver/contract/' + conid + '/info'
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define parameters
    payload={}
    
    # Request data
    response = requests.get(url, headers=headers, data=payload, verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Prints the response
    pprint(parsed_res)
    
    print('*' * 50)

def fetch_historical_data():
    
    """
    Documentation link: https://www.interactivebrokers.com/api/doc.html#tag/Market-Data/paths/~1iserver~1marketdata~1history/get

    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint
    end_point = 'iserver/marketdata/history'
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define payload
    payload = {}
    
    parameters = {'conid': '173418084',
                  'exchange': 'NSE',
                  'period': '1d',
                  'bar': '1min'
                  }
    
    # Request data
    response = requests.get(url, 
                            headers=headers, 
                            data=payload, 
                            params=parameters,
                            verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text) # JSON String to Python dictionary
    
    # Extract historical data from the responsse
    historical_data= parsed_res['data']
    
    # Create a dataframe from the received data
    data = pd.DataFrame.from_records(historical_data)
    
    # Convert epoch timestamps to human readable date time format
    data['t'] = pd.to_datetime(data['t'], unit='ms', utc=True)

    # Convert timezone
    data['t'] = data['t'].dt.tz_convert('Asia/Kolkata')
    
    # Set date as index
    data.set_index('t', drop=True, inplace=True)
    
    # print(data)
    
    return data
    
    # print('*' * 50)

def fetch_ltp(contract_id):
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Market-Data/paths/~1iserver~1marketdata~1snapshot/get
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint for fetching snapshot data
    end_point = 'iserver/marketdata/snapshot'
    
    # Create an URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define the payload
    payload = {}
    
    # Define parameters / Query string parameters
    parameters = {
        'conids': contract_id,
        'fields': '31'
        }
    
    # Request data
    response = requests.get(url, 
                            headers=headers, 
                            data=payload, 
                            params=parameters,
                            verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    print(parsed_res)
    
    if '31' in parsed_res[0].keys():
        last_price = parsed_res[0]['31']
        print('Last Price:', last_price)
        
    if '_updated' in parsed_res[0].keys():
        last_time = parsed_res[0]['_updated']
        updated = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_time/1000))
        print('Updated on:', updated)
    
    print('*' * 50)

def fetch_accounts():
    """
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint for fetching accounts
    end_point = 'iserver/accounts'
    
    # Create an URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define the payload
    payload = {}
    
    # Send request
    response = requests.get(url,
                            headers=headers,
                            data=payload,
                            verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    pprint(parsed_res)
    
    print('*' * 50)
    
def get_account_pnl():
    """
    https://www.interactivebrokers.com/api/doc.html#tag/PnL/paths/~1iserver~1account~1pnl~1partitioned/get
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to fetch account pnl
    end_point = 'iserver/account/pnl/partitioned'
    
    # Create an URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define parameters
    payload={}
    
    # Request data
    response = requests.get(url, 
                             headers=headers, 
                             data=payload, verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Prints the response
    pprint(parsed_res)
    
    print('*' * 50)

def get_portfolio_positions(account_id):
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Portfolio/paths/~1portfolio~1{accountId}~1positions~1{pageId}/get
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to fetch positions
    end_point = 'portfolio/' + account_id + '/positions/0'
    
    # Create an URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define parameters
    payload = {}
    
    # Request data
    response = requests.get(url,
                            headers=headers,
                            data=payload, verify=False)

    # Print status code
    print('Status Code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    positions = pd.DataFrame.from_records(parsed_res)
    
    cols = ['ticker', 'conid', 'listingExchange', 'position', 'realizedPnl', 'unrealizedPnl']
    print(positions[cols])
    
    # Prints the response
    # pprint(parsed_res)
    
    print('*' * 50)

def get_portfolio_accounts():
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Account/paths/~1portfolio~1accounts/get
    """
    
    base_url = 'https://localhost:5000/v1/api/'
    end_point = 'portfolio/accounts/'
    
    url = base_url + end_point
    
    headers = {}
    
    payload={}
    
    response = requests.get(url, headers=headers, data=payload, verify=False)
    
    print('Status code:', response.status_code, '\n')
    parsed_res = json.loads(response.text)
    
    pprint(parsed_res)
    
    print('*' * 50)
    
def get_positions_conid(conid):
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Portfolio/paths/~1portfolio~1positions~1{conid}/get
    """
    
    # get_portfolio_accounts()
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to fetch positions by contract id
    end_point = 'portfolio/positions/' + conid
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define parameters
    payload={}
    
    # Request data
    response = requests.get(url, headers=headers, data=payload, verify=False)
    
    # Print status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Prints the response
    pprint(parsed_res)
    
    print('*' * 50)
    
def get_orders():
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Order/paths/~1iserver~1account~1orders/get
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to fetch all orders
    end_point = 'iserver/account/orders'
    
    # Create a URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define payload
    payload = {}
    
    # Request data
    response = requests.get(url, headers=headers, data=payload, verify=False)
    
    # Print the status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Print the response
    pprint(parsed_res)
    
    print('*' * 50)
    
def get_order_status(order_id):
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to fetch all orders
    end_point = 'iserver/account/order/status/' + order_id
    
    # Create an URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {}
    
    # Define payload
    payload = {}
    
    # Make a request
    response = requests.get(url, headers=headers, data=payload, verify=False)
    
    # Print the status code
    print('Status code:', response.status_code, '\n')
    
    # Parse the response
    parsed_res = json.loads(response.text)
    
    # Print the response
    pprint(parsed_res)
    
    print('*' * 50)
    
def place_orders(account_id):
    """
    https://www.interactivebrokers.com/api/doc.html#tag/Order/paths/~1iserver~1account~1{accountId}~1orders/post
    """
    
    # Define the base url
    base_url = 'https://localhost:5000/v1/api/'
    
    # Define an endpoint to place orders
    end_point = 'iserver/account/' + account_id + '/orders'
    
    # Create an URL
    url = base_url + end_point
    
    # Print the URL
    print('URL:', url, '\n')
    
    # Define headers
    headers = {'Content-Type': 'application/json'}
    
    # Define order parameters
    order_parameters = {'acctId': account_id,
                        'conid': 56985419,
                        'secType': '56985419:STK',
                        'orderType': 'MKT',
                        'side': 'BUY',
                        'tif': 'DAY',
                        'price': 1529.55,
                        'quantity': 30,
                        'ticker': 'COLPAL',
                        'cOID': 'my-buy-order-12',
                        'useAdaptive': True,
                        'isCcyConv': False,
                        'outsideRTH': False
                        
        }
    
    # Define payload
    payload = {'orders':[order_parameters]}
    
    # Place order
    response = requests.post(url, 
                             headers=headers,
                             data=json.dumps(payload), # Converts Python dictionary to JSON String
                             verify=False)
    
    # Print the status code
    print('Status Code:', response.status_code, '\n')
    
    print(json.loads(response.text)) # It converts JSON data to Python data
    
    return response    










