import yfinance as yf
import pandas as pd
import random as rnd

class Data:
    def __init__(self, OHLC) -> None:  
        self.OHLC = OHLC
        self.Open = OHLC["Open"]
        self.High = OHLC["High"]
        self.Low = OHLC["Low"]
        self.Close = OHLC["Close"]

        self.ticker_list = ["SPY", "QQQ", "BTC-USD", "ETH-USD"]


    def get_OHLC(self, ticker="rnd", start="2015-01-01", end=None) -> pd.DataFrame:
        if ticker == "rnd":
            rnd_pick = rnd.choice(["SPY", "QQQ", "BTC-USD", "ETH-USD"])
            df: pd.DataFrame = yf.download(tickers=rnd_pick, start=start, end=end).drop(columns={"Adj Close"})

            return rnd_pick, df
        else:
            df: pd.DataFrame = yf.download(tickers=ticker, start=start, end=end).drop(columns={"Adj Close"})

            return ticker, df
