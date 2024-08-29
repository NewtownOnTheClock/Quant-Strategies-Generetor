import pandas as pd
from indicators import *
import random as rnd
import yfinance as yf

df = yf.download("SPY").drop(columns={"Adj Close"})

class IndicatorsPicker:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC

        self.indicators = [
            RSI(self.OHLC),
            SMA(self.OHLC)
        ]

        self.selected_indicators = self.select_indicators()
    
    def select_indicators(self):
        nb_long_indicators = rnd.randint(1, len(self.indicators))
        nb_short_indicators = rnd.randint(1, len(self.indicators))

        chosen_long_indicators = rnd.sample(self.indicators, k=nb_long_indicators)
        chosen_short_indicator = rnd.sample(self.indicators, k=nb_short_indicators)

        result = {}
        for long_indicator, short_indicator in zip(chosen_long_indicators, chosen_short_indicator):
            result["Long"] = long_indicator.calculate()
            result["Short"] = short_indicator.calculate()
        return result
    

    def return_df(self) -> pd.DataFrame:
        for (k_l, v_l), (k_s, v_s) in zip(self.selected_indicators["Long"].items(), self.selected_indicators["Short"].items()):
            self.OHLC[k_l] = v_l
            self.OHLC[k_s] = v_s
        return self.OHLC
    

class StategyGenerator(IndicatorsPicker):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.OHLC = OHLC
        self.indicator_OHLC = IndicatorsPicker(self.OHLC)
        self.possible_indicator_actions = [
            self.crossover(),
            self.crossunder(),
            self.greater_than(),
            self.lower_than(),
        ]

    def crossover(self):
        pass

    def crossunder(self):
        pass

    def greater_than(self):
        pass

    def lower_than(self):
        pass

    def long_signal(self):
        pass
    
'''
Make sure to specify in the indicatiors if they are each one of them are based on the price of the asset or 
are they based on a specific bound
'''

# test = StategyGenerator(df)
# print(test.long_signal())

strat = IndicatorsPicker(df)
print(strat.return_df().tail())



