import yfinance as yf

class Data:
    def __init__(self, OHLC) -> None:  
        self.OHLC = OHLC
        self.Open = OHLC["Open"]
        self.High = OHLC["High"]
        self.Low = OHLC["Low"]
        self.Close = OHLC["Close"]

