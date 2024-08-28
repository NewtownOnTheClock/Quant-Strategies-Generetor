import pandas as pd
from indicators import *
import random as rnd
import yfinance as yf

df = yf.download("SPY").drop(columns={"Adj Close"})

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
    

class StategyGenerator(IndicatorsPicker):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.OHLC = OHLC
        self.indicator_OHLC = IndicatorsPicker(OHLC)

    def long_signal(self):
        pass
    


strat = IndicatorsPicker(df)
print(strat.return_df().tail())



