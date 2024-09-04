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

        result = {}
        indicators_info = {"Long": {}, "Short": {}}

        for long_indicator in chosen_long_indicators:
            dict_indicator = long_indicator.calculate()
            indicator_name = list(dict_indicator.keys())[0]
            indicator_relation = list(long_indicator.indicator_type.values())[0]
            result.update(long_indicator.calculate())
            indicators_info["Long"].update({indicator_name: {"Relation": indicator_relation}})

        for short_indicator in chosen_short_indicator:
            dict_indicator = short_indicator.calculate()
            indicator_name = list(dict_indicator.keys())[0]
            indicator_relation = list(short_indicator.indicator_type.values())[0]
            result.update(short_indicator.calculate())
            indicators_info["Short"].update({indicator_name: {"Relation": indicator_relation}})
    
        for k_l, v_l in result.items():
            self.OHLC[k_l] = v_l
        for k_s, v_s in result.items():
            self.OHLC[k_s] = v_s
        
        return self.OHLC, indicators_info
    

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
    
    def categorize_indicators(self):
        long_price_related = []
        short_price_related = []
        long_bound_related = []
        short_bound_related = []

        for l_ind in self.indicators_info["Long"]:
            if self.indicators_info["Long"][l_ind]['Relation'] == "price_related":
                long_price_related.append(l_ind)
            elif self.indicators_info["Long"][l_ind]['Relation'] == "bound_related":
                long_bound_related.append(l_ind)

        for s_ind in self.indicators_info["Short"]:
            if self.indicators_info["Short"][s_ind]['Relation'] == "price_related":
                short_price_related.append(s_ind)
            elif self.indicators_info["Short"][s_ind]['Relation'] == "bound_related":
                short_bound_related.append(s_ind)


        print(long_price_related, short_price_related)

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


df_data = Data.get_OHLC()

strat = StategyGenerator(df_data)
strat.categorize_indicators()



