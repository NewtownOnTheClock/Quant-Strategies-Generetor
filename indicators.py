from fetchdata import Data
import random as rnd
import talib as ta

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
    
    def signal(self):
        signal = []
        return {f"Signal_SMA_{self.period}": signal} 




