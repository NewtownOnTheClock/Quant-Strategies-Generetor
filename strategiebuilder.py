import pandas as pd
from fetchdata import Data
from indicators import *
import random as rnd
import numpy as np

class IndicatorsPicker:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC

        self.indicators = [
            # Momentum indicator
            RSI(self.OHLC),

            # Overlap studies
            SMA(self.OHLC),
            EMA(self.OHLC),
            HT_TRENDLINE(self.OHLC),
            DEMA(self.OHLC),
            KAMA(self.OHLC),
            MA(self.OHLC),
            MIDPOINT(self.OHLC),
            MIDPRICE(self.OHLC),

        ]
    
    def select_indicators(self) -> pd.DataFrame:
        nb_long_indicators = rnd.randint(1, 2)
        nb_short_indicators = rnd.randint(1, 2)

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
        self.OHLC_and_indicators, self.indicators_info = IndicatorsPicker(OHLC).select_indicators()
        self.lng_price_related, self.shrt_price_related, self.lng_bnd_realted, self.shrt_bnd_related = self.categorize_indicators()

    
    def categorize_indicators(self) -> tuple[list]:
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
        
        return long_price_related, short_price_related, long_bound_related, short_bound_related


    def crossover(self, pair_crossover: bool) -> dict:
        '''
        Return signals when the crossover is invoked by the strategy generator

        Parameters:
        ----------
        pair_crossover : bool
            if the crossover is based on one indicator and the asset price, or between two indicators

        '''
        previous_close = self.OHLC_and_indicators["Close"].shift(1)
        results = {}
        
        if pair_crossover == 0:
            for long_ind in self.lng_price_related:
                results.update({f"L_Signal_{long_ind}": np.where(
                        (self.OHLC_and_indicators[long_ind] > self.OHLC_and_indicators["Close"]) & 
                        (self.OHLC_and_indicators[long_ind].shift(1) <= previous_close), 1, 0)})
                
        elif pair_crossover == 1:
            first_ind_data = self.OHLC_and_indicators[self.lng_price_related[0]]
            second_ind_data = self.OHLC_and_indicators[self.lng_price_related[1]]
            first_ind_data_lagged = self.OHLC_and_indicators[self.lng_price_related[0]].shift(1)
            second_ind_data_lagged = self.OHLC_and_indicators[self.lng_price_related[1]].shift(1)

            results.update({f"L_Signal_{self.lng_price_related[0]}_crosso_{self.lng_price_related[1]}": np.where(
                (first_ind_data > second_ind_data) & 
                (first_ind_data_lagged <= second_ind_data_lagged), 1, 0)})
            
        return results


    def crossunder(self, pair_crossunder: bool) -> dict:
        '''
        Return signals when the crossunder is invoked by the strategy generator

        Parameters:
        ----------
        pair_crossunder : bool
            if the crossunder is based on one indicator and the asset price, or between two indicators

        '''
        previous_close = self.OHLC_and_indicators["Close"].shift(1)
        results = {}

        if pair_crossunder == 0:
            for short_ind in self.shrt_price_related:
                results.update({f"S_Signal_{short_ind}" : np.where(
                        (self.OHLC_and_indicators[short_ind] < self.OHLC_and_indicators["Close"]) & 
                        (self.OHLC_and_indicators[short_ind].shift(1) >= previous_close), -1, 0)})
                
        elif pair_crossunder == 1:
            first_ind_data = self.OHLC_and_indicators[self.shrt_price_related[0]]
            second_ind_data = self.OHLC_and_indicators[self.shrt_price_related[1]]
            first_ind_data_lagged = self.OHLC_and_indicators[self.shrt_price_related[0]].shift(1)
            second_ind_data_lagged = self.OHLC_and_indicators[self.shrt_price_related[1]].shift(1)

            results.update({f"S_Signal_{self.shrt_price_related[0]}_crossu_{self.shrt_price_related[1]}": np.where(
                (first_ind_data > second_ind_data) & 
                (first_ind_data_lagged <= second_ind_data_lagged), -1, 0)})
            
        return results

    def greater_than(self):
        results = {}
        pass

    def lower_than(self):
        pass

    def signal(self) -> pd.DataFrame:
        signal_created = {"Long": [], "Short": []}

        if len(self.lng_price_related) == 1:
            signal_info = self.crossover(pair_crossover=False)
            signal_name = next(iter(signal_info))
            signal_value = next(iter(signal_info.values()))
            signal_created["Long"].append(signal_info)
            self.OHLC_and_indicators[signal_name] = signal_value

        elif len(self.lng_price_related) == 2:
            signal_info = self.crossover(pair_crossover=True)
            signal_name = next(iter(signal_info))
            signal_value = next(iter(signal_info.values()))
            signal_created["Long"].append(signal_info)
            self.OHLC_and_indicators[signal_name] = signal_value
        
        if len(self.shrt_price_related) == 1:
            signal_info = self.crossunder(pair_crossunder=False)
            signal_name = next(iter(signal_info))
            signal_value = next(iter(signal_info.values()))
            signal_created["Short"].append(signal_info)
            self.OHLC_and_indicators[signal_name] = signal_value
            
        elif len(self.shrt_price_related) == 2:
            signal_info = self.crossunder(pair_crossunder=True)
            signal_name = next(iter(signal_info))
            signal_value = next(iter(signal_info.values()))
            signal_created["Short"].append(signal_info)
            self.OHLC_and_indicators[signal_name] = signal_value
        
        long_signals = signal_created["Long"]
        short_signals = signal_created["Short"]




        return self.OHLC_and_indicators
        


df_data = Data.get_OHLC()

strat = StategyGenerator(df_data)
print(strat.indicators_info) 
print(strat.signal())

