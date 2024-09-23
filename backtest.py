from backtesting import Strategy, Backtest
from strategiebuilder import StrategyGenerator
from pathlib import Path
import pandas as pd
import datetime as dt

# Init the folders
def init_folders():
    output_dir = Path("GeneratedData")
    output_dir.mkdir(parents=True, exist_ok=True)


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
    col_to_keep = ["Start","End","Duration","Exposure Time [%]","Equity Final [$]","Equity Peak [$]","Return [%]","Buy & Hold Return [%]","Return (Ann.) [%]","Volatility (Ann.) [%]","Sharpe Ratio","Sortino Ratio","Calmar Ratio","Max. Drawdown [%]","Avg. Drawdown [%]","Max. Drawdown Duration","Avg. Drawdown Duration","# Trades,Win Rate [%]","Best Trade [%]","Worst Trade [%]","Avg. Trade [%]","Max. Trade Duration","Avg. Trade Duration","Profit Factor,Expectancy [%]","SQN","Kelly Criterion","indicators_used"]
    
    for i in range(5):
        # Get the OHLC data
        OHLC, indicators_info = StrategyGenerator().signal()
        try:

            bt = Backtest(OHLC, SignalStrategy, cash=cash)
            stats: pd.DataFrame = bt.run().to_frame().T
            stats["indicators_used"] = str(indicators_info)
            stats = stats.drop(columns={col for col in stats.columns if col not in col_to_keep})

            if not Path(tested_backtests_path).exists() or pd.read_csv(tested_backtests_path).empty:
                stats.to_csv(tested_backtests_path, index=False)
            else:
                tested_backtests = pd.read_csv(tested_backtests_path)
                tested_backtests = pd.concat([tested_backtests, stats], axis=0, ignore_index=True)
                tested_backtests.to_csv(tested_backtests_path, index=False)
            print(tested_backtests)

        except Exception as e:
            with open("GeneratedData/log.txt", "a") as f:
                f.write(f"{dt.datetime.now()}: {e} \n")
            bt.plot()


if __name__ == "__main__":
    init_folders()
    runBacktest()