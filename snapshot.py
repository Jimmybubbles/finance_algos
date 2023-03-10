# Provides ways to work with large multidimensional arrays
import numpy as np 
# Allows for further data manipulation and analysis
import pandas as pd
from pandas_datareader import data as web # Reads stock data 
import matplotlib.pyplot as plt # Plotting
import matplotlib.dates as mdates # Styling dates


import datetime as dt # For defining dates
import mplfinance as mpf # Matplotlib finance
import os
import time

import yfinance as yf



#============================================================================================#
#all the yfinance methods
def get_info_on_stock(ticker):
    stock = yf.Ticker(ticker)

#     # Get overview of company
#     print(stock.info)

#     # Get historical closing price data
#     hist = stock.history(period="max")["Close"]
#     print(hist.head())

#     # Get financial data
#     print(stock.financials)

#     # Get major share holders
    print(stock.major_holders)

#     # Get institutional holders
#     print(stock.institutional_holders)

#     # Get balance sheet
#     print(stock.balance_sheet)

#     # Show cashflow
#     print(stock.cashflow)

#     # Show earnings
#     print(stock.earnings)

#     # Show analysts recommendations
#     print(stock.recommendations)
    
# get_info_on_stock("360_AX")


#============================================================================================#
# list of stocks to catch when reading api
stocks_not_downloaded = []
missing_stocks = []

#============================================================================================#

#Function that Returns a Stock Dataframe from a CSV
# Reads a dataframe from the CSV file, changes index to date and returns it
def get_stock_df_from_csv(folder, ticker):
    
    # Try to get the file and if it doesn't exist issue a warning
    try:
        df = pd.read_csv(folder + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df
    
    
def get_column_from_csv(file, col_name):
    # Try to get the file and if it doesn't exist issue a warning
    try:
        df = pd.read_csv(file)
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df[col_name]
    
#============================================================================================#
# download the tickers
# PATHS
tickers = get_column_from_csv("C:/Users/James/finance_algos/dataset/ASX.CSV", "Ticker")
folder = "C:/Users/James/finance_algos/datasets/"

# Function that gets a dataframe by providing a ticker and starting date
def save_to_csv_from_yahoo(folder, ticker):
    
    stock = yf.Ticker(ticker)
    
    try:
        print("Get Data for : ", ticker)
        # Get historical closing price data
        df = stock.history(period="max")
        
        # Wait 2 seconds
        time.sleep(2)
        
        if df.empty:
            stocks_not_downloaded.append(ticker)
        
        # Remove the period for saving the file name
        # Save data to a CSV file
        # File to save to 
        the_file = folder + ticker.replace(".", "_") + '.csv'
        print(the_file, " Saved")
        df.to_csv(the_file)
    except Exception as ex:
        stocks_not_downloaded.append(ticker)
        print("Couldn't Get Data for :", ticker)
        
3898 

## this loop will save data to csv
for x in range(50):
  save_to_csv_from_yahoo(folder, tickers[x])
print("Finished")