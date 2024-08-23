import talib as ta
import pandas as pd
from backtesting import Backtest, Strategy
import random as rnd
import yfinance as yf

df = yf.download("SPY").drop(columns={"Adj Close"})

class Data:
    def __init__(self, OHLC) -> None:  
        self.OHLC = OHLC
        self.Open = OHLC["Open"]
        self.Close = OHLC["Close"]
        self.High = OHLC["High"]
        self.Low = OHLC["Low"]
        

class RSI(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.period = self.rnd_period()
        self.signal = self.rnd_signal()
        self.upper_bound_signal = self.signal["upper_bound"]
        self.lower_bound_signal = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        return rnd.randint(1, 50)
    
    def rnd_signal(self) -> int:
        upper_bound = rnd.randint(50, 100)
        lower_bound = rnd.randint(1, 49)
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}
    
    def calculate(self):
        return ta.RSI(self.Close, self.period)

class Indicators:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Close = OHLC["Close"]
        self.High = OHLC["High"]
        self.Low = OHLC["Low"]
        
        self.indicators = [
            self.calculate_rsi(), 
            self.calculate_macd(), 
            self.calculate_adx(),
            ]

    def calculate_rsi(self):
        period = 14
        return {f"RSI_{period}": ta.RSI(self.Close, period)}
    
    def calculate_macd(self):
        fast_period = 12
        slow_period = 26 # Slow period must be greater than the fast period
        signal_period = 9
        return {f"MACD_{fast_period}_{slow_period}_{signal_period}": ta.MACD(self.Close, fast_period, slow_period, signal_period)[0]}
    
    def calculate_adx(self):
        period = 14
        return {f"ADX_{period}": ta.ADX(self.High, self.Low, self.Close, period)}


class StrategyPicker(Indicators):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)     

        self.selected_indicators = self.select_indicators()
    
    def select_indicators(self):
        number_of_indicator = rnd.randint(1, len(self.indicators))
        chosen_indicator = rnd.sample(self.indicators, k=number_of_indicator)
        return chosen_indicator
    

    def return_df(self):
        for indicator in self.selected_indicators:
            for k, v in indicator.items():
                self.OHLC[k] = v
        return self.OHLC


strat = StrategyPicker(df)
print(strat.return_df())
print(strat.calculate_macd().keys())


