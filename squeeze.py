import os, pandas
import numpy as np
import pandas as pd
# import plotly

symbols = ['3DA_AX']

for filename in os.listdir('datasets'):
    symbol = filename.split(".")[0]
    # print(symbol)
    df = pandas.read_csv('datasets/{}'.format(filename))
    # print(df)
    
# error handling for empty dataframes
    if df.empty:
        continue
    
#21SMA

df['EMA_21'] = df['Close'].ewm(span=20, adjust=False).mean()
df['EMA_5'] = df['Close'].ewm(span=50, adjust=False).mean()
# Date,Open,High,Low,Close,Volume,Dividends,Stock Splits

# ATR calculation
high_low = df['High'] - df['Low']
high_close = np.abs(df['High'] - df['Close'].shift())
low_close = np.abs(df['Low'] - df['Close'].shift())
ranges = pd.concat([high_low, high_close, low_close], axis=1)
true_range = np.max(ranges, axis=1)
df['ATR'] = true_range.rolling(50).sum()/50

print(df)