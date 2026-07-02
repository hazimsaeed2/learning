import numpy as np
import pandas as pd

def ma_crossover(data, short_lookback, long_lookback):
    data['ma_long'] = data['Close'].ewm(span=long_lookback).mean()
    data['ma_short'] = data['Close'].ewm(span=short_lookback).mean()  

    data['ma_signal'] = np.where(data.ma_short > data.ma_long, 1, 0)    
    data.iloc[:long_lookback,-1] = np.nan
    return data


def compute_adx(data, adx_threshold):
    data['adx'] = calculate_adx(data, period=14)['ADX']
    data['adx_signal'] = np.where(data.adx > adx_threshold, 1, 0)    
    data.iloc[:14,-1] = np.nan
    return data


def calculate_adx(df, period=14):
    # Calculate True Range (TR)
    df['H-L'] = df['High'] - df['Low']
    df['H-PC'] = np.abs(df['High'] - df['Close'].shift(1))
    df['L-PC'] = np.abs(df['Low'] - df['Close'].shift(1))
    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)

    # Calculate +DM and -DM
    df['+DM'] = np.where(df['High'] - df['High'].shift(1) > df['Low'].shift(1) - df['Low'], 
                         df['High'] - df['High'].shift(1), 0)
    df['-DM'] = np.where(df['Low'].shift(1) - df['Low'] > df['High'] - df['High'].shift(1), 
                         df['Low'].shift(1) - df['Low'], 0)

    # Smooth the TR, +DM, and -DM
    df['TR_smooth'] = df['TR'].rolling(window=period).sum()
    df['+DM_smooth'] = df['+DM'].rolling(window=period).sum()
    df['-DM_smooth'] = df['-DM'].rolling(window=period).sum()

    # Calculate +DI and -DI
    df['+DI'] = (df['+DM_smooth'] / df['TR_smooth']) * 100
    df['-DI'] = (df['-DM_smooth'] / df['TR_smooth']) * 100

    # Calculate ADX (the smoothed version of the absolute difference between +DI and -DI)
    df['ADX'] = np.nan
    df['ADX'] = df[['+DI', '-DI']].apply(lambda x: np.abs(x[0] - x[1]), axis=1)
    df['ADX'] = df['ADX'].rolling(window=period).mean()

    return df[['ADX', '+DI', '-DI']]