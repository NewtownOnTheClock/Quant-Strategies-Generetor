import yfinance as yf
import pandas as pd
import random as rnd
import os

class Data:
    def __init__(self, OHLC) -> None:  
        self.OHLC = OHLC
        self.Open = OHLC["Open"]
        self.High = OHLC["High"]
        self.Low = OHLC["Low"]
        self.Close = OHLC["Close"]

        self.ticker_list = ["SPY", "QQQ", "BTC-USD", "ETH-USD"]


    def get_OHLC(self, ticker="rnd", start="2015-01-01", end="2024-09-01", to_csv=True, path="Datas") -> pd.DataFrame:
        
        if ticker == "rnd":
            ticker = rnd.choice(["SPY", "QQQ", "BTC-USD", "ETH-USD"])
        
        yf_csv_list = os.listdir(path)
        is_in = str(f"{ticker}.csv") in yf_csv_list
        if is_in:
            df = pd.read_csv(f"{path}/{ticker}.csv").set_index("Date")
            df.index = pd.to_datetime(df.index)
            return ticker, df
            
        df: pd.DataFrame = yf.download(tickers=ticker, start=start, end=end).drop(columns={"Adj Close"})
        if to_csv:
            df.to_csv(f"{path}/{ticker}.csv")

            return ticker, df
