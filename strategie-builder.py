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


# Momentum Indicators
class RSI(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.period = self.rnd_period()
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        return rnd.randint(1, 50)
    
    def rnd_bound(self) -> dict:
        upper_bound = rnd.randint(50, 100)
        lower_bound = rnd.randint(1, 49)
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}
    
    def calculate(self):
        return {f"RSI_{self.period}": ta.RSI(self.Close, self.period)}

   
# Overlap Studies
class SMA(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.period = self.rnd_period()

    def rnd_period(self) -> int:
        return rnd.randint(20, 300)
    
    def calculate(self):
        return {f"SMA_{self.period}": ta.SMA(self.Close, self.period)}  


class IndicatorsPicker:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC

        self.momentum_indicators = [
            RSI(self.OHLC)
        ]

        self.overlap_studies = [
            SMA(self.OHLC)
        ]

        self.selected_indicators = self.select_indicators()
    
    def select_indicators(self):
        nb_mom_indicators = rnd.randint(1, len(self.momentum_indicators))
        nb_overlap_studies = rnd.randint(1, len(self.overlap_studies))

        chosen_mom_indicators = rnd.sample(self.momentum_indicators, k=nb_mom_indicators)
        chosen_overlap_studies = rnd.sample(self.overlap_studies, k=nb_overlap_studies)

        result = {}
        for mom_indicators, overlap_studies in zip(chosen_mom_indicators, chosen_overlap_studies):
            result.update(mom_indicators.calculate())
            result.update(overlap_studies.calculate())
        return result
    

    def return_df(self) -> pd.DataFrame:
        for k, v in self.selected_indicators.items():
            self.OHLC[k] = v
        return self.OHLC


strat = IndicatorsPicker(df)
print(strat.return_df().tail())



