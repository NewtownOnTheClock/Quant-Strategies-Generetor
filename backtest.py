from backtesting import Strategy, Backtest
import pandas as pd
import numpy as np
import datetime as dt


def db_exist(db_con):
    sql = "SELECT * from outputs"
    cur = db_con.cursor()
    cur.execute(sql)
    val = cur.fetchone()
    if val is not None and val[0] is not None:
        return True
    else:
        return False


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


def runBacktest(db_con, OHLC, indicators_info, ticker, sharpe_saving_threshold, cash=1_000_000):
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
                   "# Trades",
                   "Win Rate [%]", 
                   "Best Trade [%]", 
                   "Worst Trade [%]", 
                   "Avg. Trade [%]", 
                   "Max. Trade Duration", 
                   "Avg. Trade Duration", 
                   "Profit Factor",
                   "Expectancy [%]", 
                   "SQN",
                   "Kelly Criterion", 
                   "indicators_used",
                   "ticker",
                   "datetime"]
    
    try:
        bt = Backtest(OHLC, SignalStrategy, cash=cash)
        stats: pd.DataFrame = bt.run().to_frame().T
        
        stats["indicators_used"] = str(indicators_info)
        stats["ticker"] = ticker
        stats["datetime"] = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        stats = stats.drop(columns={col for col in stats.columns if col not in col_to_keep})
        
        stats = stats.astype({
            "Start": str,
            "End": str,
            "Duration": str,
            "Exposure Time [%]": float,
            "Equity Final [$]": float,
            "Equity Peak [$]": float,
            "Return [%]": float,
            "Buy & Hold Return [%]": float,
            "Return (Ann.) [%]": float,
            "Volatility (Ann.) [%]": float,
            "Sharpe Ratio": float, 
            "Sortino Ratio": float, 
            "Calmar Ratio": float, 
            "Max. Drawdown [%]": float, 
            "Avg. Drawdown [%]": float, 
            "Max. Drawdown Duration": str, 
            "Avg. Drawdown Duration": str, 
            "# Trades": int,
            "Win Rate [%]": float, 
            "Best Trade [%]": float, 
            "Worst Trade [%]": float, 
            "Avg. Trade [%]": float, 
            "Max. Trade Duration": str, 
            "Avg. Trade Duration": str, 
            "Profit Factor": float,
            "Expectancy [%]": float, 
            "SQN": float,
            "Kelly Criterion": float, 
            "indicators_used": str,
            "ticker": str,
            "datetime": str
        })
        
        if np.isnan(stats["Sharpe Ratio"][0]):
            return

        if not db_exist(db_con=db_con):
            stats.to_sql(name='outputs', con=db_con, if_exists="append", index=False)
        else:
            if stats["Sharpe Ratio"].values >= sharpe_saving_threshold:
                bt.plot(filename=f"GeneratedDatas/graphs/{stats["Sharpe Ratio"][0]}-{ticker}-{dt.datetime.now()}", open_browser=False)
            
            stats.to_sql(name='outputs', con=db_con, if_exists="append", index=False)
        return round(stats["Sharpe Ratio"][0], 3)

    except Exception as e:
        print(e)
        with open("GeneratedDatas/logs.txt", "a") as f:
            f.write(f"{dt.datetime.now()}: {e} \n")


if __name__ == "__main__":
    runBacktest()