import random as rnd
from fetchdata import Data
import talib as ta
import numpy as np
import pandas as pd

# Momentum Indicators
class RSI:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]

        self.indicator_type = {
            "Relation": "bound_related",
        }
        self.period = self.rnd_period()
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        return rnd.randint(2, 50)
    
    def rnd_bound(self) -> dict:
        upper_bound = rnd.randint(50, 99)
        lower_bound = rnd.randint(1, 49)
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}
    
    def calculate(self) -> dict:
        return {f"RSI_{self.period}": ta.RSI(self.Close, self.period)}
    
class ADX:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]

        self.indicator_type = {
            "Relation": "bound_related",
        }
        self.period = self.rnd_period()
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        return rnd.randint(2, 50)

    def rnd_bound(self) -> dict:
        upper_bound = rnd.randint(50, 99)
        lower_bound = rnd.randint(1, 49)
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}

    def calculate(self) -> dict:
        return {f"ADX_{self.period}": ta.ADX(self.High, self.Low, self.Close, self.period)}


class ADXR:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "bound_related",
        }
        self.period = self.rnd_period()
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        return rnd.randint(2, 50)

    def rnd_bound(self) -> dict:
        upper_bound = rnd.randint(50, 99)
        lower_bound = rnd.randint(1, 49)
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}

    def calculate(self) -> dict:
        return {f"ADXR_{self.period}": ta.ADXR(self.High, self.Low, self.Close, self.period)}
    

class APO:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "bound_related",
        }
        self.fast_period, self.slow_period = self.rnd_period()
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        fast_period = rnd.randint(2, 25)
        slow_period = rnd.randint(fast_period, 50)
        return fast_period, slow_period

    def rnd_bound(self) -> dict:
        upper_bound = 0
        lower_bound = 0
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}

    def calculate(self) -> dict:
        return {f"APO_{self.fast_period}_{self.slow_period}": ta.APO(self.Close, self.fast_period, self.slow_period, matype=0)}


class BOP:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "bound_related",
        }
        self.period = 'No period'
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_bound(self) -> dict:
        upper_bound = 0
        lower_bound = 0
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}

    def calculate(self) -> dict:
        return {f"BOP": ta.BOP(self.Open, self.High, self.Low, self.Close)}


class CCI:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "bound_related",
        }
        self.period = self.rnd_period()
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        return rnd.randint(2, 50)

    def rnd_bound(self) -> dict:
        upper_bound = rnd.randint(25, 300)
        lower_bound = rnd.randint(-300, 25)
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}

    def calculate(self) -> dict:
        return {f"CCI_{self.period}": ta.CCI(self.High, self.Low, self.Close, self.period)}


class CMO:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "bound_related",
        }
        self.period = self.rnd_period()
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        return rnd.randint(2, 50)

    def rnd_bound(self) -> dict:
        upper_bound = rnd.randint(25, 75)
        lower_bound = rnd.randint(-75, 25)
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}

    def calculate(self) -> dict:
        return {f"CMO_{self.period}": ta.CMO(self.Close, self.period)}
    

class MACD:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "bound_related",
        }
        self.fast_period, self.slow_period, self.signal_period = self.rnd_period()
        self.signal = self.rnd_bound()
        self.upper_bound = self.signal["upper_bound"]
        self.lower_bound = self.signal["lower_bound"]

    def rnd_period(self) -> int:
        fast_period = rnd.randint(2, 25)
        slow_period = rnd.randint(fast_period, 50)
        signal_period = rnd.randint(2, 25)
        return fast_period, slow_period, signal_period

    def rnd_bound(self) -> dict:
        upper_bound = 0
        lower_bound = 0
        return {"upper_bound": upper_bound, "lower_bound": lower_bound}

    def calculate(self) -> dict:
        macd, macdsignal, macdhist = ta.MACD(self.Close, self.fast_period, self.slow_period, self.signal_period)
        macd_df = pd.DataFrame({"macd": macd.values, "macd_signal": macdsignal.values}).set_index(macd.index)
        macd_df['crossover'] = np.where(macd_df["macd"].values > macd_df["macd_signal"].values, 1, -1)
        macd_series = pd.Series(macd_df["crossover"])
        return {f"MACD_{self.fast_period}_{self.slow_period}_{self.signal_period}": macd_series}


# Overlap Studies
class SMA:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()

    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"SMA_{self.period}": ta.SMA(self.Close, self.period)} 
    
    def signal(self) -> dict:
        signal = []
        return {f"Signal_SMA_{self.period}": signal} 


class EMA:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"EMA_{self.period}": ta.EMA(self.Close, self.period)} 
    

class HT_TRENDLINE:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
        
        self.indicator_type = {
            "Relation": "price_related",
        }

    def calculate(self) -> dict:
        return {f"HT_TRENDLINE": ta.HT_TRENDLINE(self.Close)} 
    

class DEMA:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]

        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"DEMA_{self.period}": ta.DEMA(self.Close, self.period)}
    

class KAMA:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]

        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"KAMA_{self.period}": ta.KAMA(self.Close, self.period)}
    

class MA:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]

        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"MA_{self.period}": ta.MA(self.Close, self.period)}
    

class MIDPOINT:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]

        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"MIDPOINT_{self.period}": ta.MIDPOINT(self.Close, self.period)}
    

class MIDPRICE:
    def __init__(self, OHLC) -> None:
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]

        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"MIDPRICE_{self.period}": ta.MIDPRICE(self.High, self.Low, self.period)}
    

# Other Stock Market Data
class InterMarketIndicator(Data):
    def __init__(self, OHLC) -> None:
        super().__init__()
        self.OHLC = OHLC
        self.Open = self.OHLC["Open"]
        self.High = self.OHLC["High"]
        self.Low = self.OHLC["Low"]
        self.Close = self.OHLC["Close"]
    
    # TODO: Add other securities for pair trading