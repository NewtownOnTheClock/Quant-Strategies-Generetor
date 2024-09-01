import pandas as pd
from fetchdata import Data
from indicators import *
import random as rnd
import yfinance as yf

class IndicatorsPicker:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC

        self.indicators = [
            RSI(self.OHLC),
            SMA(self.OHLC)
        ]
    
    def select_indicators(self):
        nb_long_indicators = rnd.randint(1, len(self.indicators))
        nb_short_indicators = rnd.randint(1, len(self.indicators))

        chosen_long_indicators = rnd.sample(self.indicators, k=nb_long_indicators)
        chosen_short_indicator = rnd.sample(self.indicators, k=nb_short_indicators)

        result = {"Long":{}, "Short":{}}
        for long_indicator in chosen_long_indicators:
            result["Long"].update(long_indicator.calculate())
        for short_indicator in chosen_short_indicator:
            result["Short"].update(short_indicator.calculate())
    
        for k_l, v_l in result["Long"].items():
            self.OHLC[k_l] = v_l
        for k_s, v_s in result["Short"].items():
            self.OHLC[k_s] = v_s
        
        return self.OHLC, result
    

class StategyGenerator(IndicatorsPicker):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.OHLC = OHLC
        self.indicator_OHLC, self.indicators_info = IndicatorsPicker(self.OHLC).select_indicators()
        self.possible_indicator_actions = [
            self.crossover(),
            self.crossunder(),
            self.greater_than(),
            self.lower_than(),
        ]
    

    def crossover(self):
        print(self.indicators_info["Long"].keys())
        print(self.indicators_info["Short"].keys())

    def crossunder(self):
        pass

    def greater_than(self):
        pass

    def lower_than(self):
        pass

    def long_signal(self):
        pass




df_data = Data.get_OHLC()

strat = StategyGenerator(df_data)
print(strat.indicator_OHLC)



