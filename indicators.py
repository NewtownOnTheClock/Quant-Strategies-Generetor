from fetchdata import Data
import random as rnd
import talib as ta

# Momentum Indicators
class RSI(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
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
    
class ADX(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
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


class ADXR(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
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
    

class APO(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
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


# Overlap Studies
class SMA(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
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


class EMA(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"EMA_{self.period}": ta.EMA(self.Close, self.period)} 
    

class HT_TRENDLINE(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.indicator_type = {
            "Relation": "price_related",
        }

    def calculate(self) -> dict:
        return {f"HT_TRENDLINE": ta.HT_TRENDLINE(self.Close)} 
    

class DEMA(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"DEMA_{self.period}": ta.DEMA(self.Close, self.period)}
    

class KAMA(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"KAMA_{self.period}": ta.KAMA(self.Close, self.period)}
    

class MA(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"MA_{self.period}": ta.MA(self.Close, self.period)}
    

class MIDPOINT(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"MIDPOINT_{self.period}": ta.MIDPOINT(self.Close, self.period)}
    

class MIDPRICE(Data):
    def __init__(self, OHLC) -> None:
        super().__init__(OHLC)
        self.indicator_type = {
            "Relation": "price_related",
        }
        self.period = self.rnd_period()
    
    def rnd_period(self) -> int:
        return rnd.randint(5, 300)
    
    def calculate(self) -> dict:
        return {f"MIDPRICE_{self.period}": ta.MIDPRICE(self.High, self.Low, self.period)}