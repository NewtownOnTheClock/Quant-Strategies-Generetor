from backtesting import Strategy, Backtest
from strategiebuilder import StrategyGenerator
from pathlib import Path
import pandas as pd
import datetime as dt
import os

# Init the folders
def init_folders():
    output_dir = Path("GeneratedData")
    output_dir.mkdir(parents=True, exist_ok=True)
    return

def check_existing_indicators_combination(df_file_path, indicators_info: dict) -> bool:
    try:
        df = pd.read_csv(df_file_path)
        is_in = indicators_info in df["indicators_used"].values
        if is_in:
            raise Exception(f"{dt.datetime.now()}: indicators combination already used!")
        return is_in
    
    except Exception:
        print(f"{dt.datetime.now()}: tested backtest file unexistant or problematic")
        return 
        

class SignalStrategy(Strategy):
    def init(self):
        pass

    def next(self):
        current_signal = self.data.Signal[-1]
        if current_signal == 1:
            if not self.position:
                self.buy()
        elif current_signal == -1:
            if self.position:
                self.position.close()


def runBacktest(cash=100_000):
    tested_backtests_path = "GeneratedData/tested_backtests.csv"
    col_to_keep = ["Start", 
                   "End", 
                   "Duration", 
                   "Exposure Time [%]", 
                   "Equity Final [$]", 
                   "Equity Peak [$]", 
                   "Return [%]", 
                   "Buy & Hold Return [%]", 
                   "Return (Ann.) [%]", 
                   "Volatility (Ann.) [%]", 
                   "Sharpe Ratio", 
                   "Sortino Ratio", 
                   "Calmar Ratio", 
                   "Max. Drawdown [%]", 
                   "Avg. Drawdown [%]", 
                   "Max. Drawdown Duration", 
                   "Avg. Drawdown Duration", 
                   "# Trades,Win Rate [%]", 
                   "Best Trade [%]", 
                   "Worst Trade [%]", 
                   "Avg. Trade [%]", 
                   "Max. Trade Duration", 
                   "Avg. Trade Duration", 
                   "Profit Factor,Expectancy [%]", 
                   "SQN","Kelly Criterion", 
                   "indicators_used",
                   "ticker"]
    
    for i in range(25):
        # Get the OHLC data
        OHLC, indicators_info, ticker = StrategyGenerator().signal()
        try:
            existing_indicators_combination = check_existing_indicators_combination(tested_backtests_path, indicators_info=indicators_info)
            if existing_indicators_combination:
                continue
            
            bt = Backtest(OHLC, SignalStrategy, cash=cash)
            stats: pd.DataFrame = bt.run().to_frame().T
            stats["indicators_used"] = str(indicators_info)
            stats["ticker"] = ticker
            stats = stats.drop(columns={col for col in stats.columns if col not in col_to_keep})

            if not Path(tested_backtests_path).exists() or os.stat(tested_backtests_path).st_size == 0:
                stats.to_csv(tested_backtests_path, index=False)
            else:
                tested_backtests = pd.read_csv(tested_backtests_path)
                tested_backtests = pd.concat([tested_backtests, stats], axis=0, ignore_index=True).sort_values("Sharpe Ratio", ascending=False)
                tested_backtests.to_csv(tested_backtests_path, index=False)
            #print(tested_backtests)

        except Exception as e:
            with open("GeneratedData/log.txt", "a") as f:
                f.write(f"{dt.datetime.now()}: {e} \n")


if __name__ == "__main__":
    init_folders()
    runBacktest()