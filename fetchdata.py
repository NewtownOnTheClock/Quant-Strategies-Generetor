import yfinance as yf
import pandas as pd

class Data:
    def __init__(self, OHLC) -> None:  
        self.OHLC = OHLC
        self.Open = OHLC["Open"]
        self.High = OHLC["High"]
        self.Low = OHLC["Low"]
        self.Close = OHLC["Close"]

    @classmethod
    def get_OHLC(self) -> pd.DataFrame:
        df: pd.DataFrame = yf.download(tickers="SPY", start="2020-01-01")
        df = df.drop(columns={"Adj Close"})
        return df

