from strategiebuilder import StrategyGenerator
from fetchdata import Data
from stats import Stats
from pathlib import Path
import sqlite3
from backtest import *
import itertools
import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', type=int, help="Define the number or iterations")
    parser.add_argument('-sr', '--sharpe', type=float, default=0.9, help="Define the threshold of Sharpe Ratio at witch the graph are saved")
    parser.add_argument('-t', '--tickers', nargs="*", type=str, default=["SPY", "QQQ", "BTC-USD", "ETH-USD"], help="Define the tickers to do the backtests on")
    parser.add_argument('-s', '--start', type=str, default="2015-01-01", help="Define the start date to backtests")
    parser.add_argument('-e', '--end', type=str, default="2024-01-01", help="Define the end date to backtests")
    return parser.parse_args()


def init_folders():
    output_dir = Path("GeneratedDatas/graphs/")
    data_dir = Path("Datas")
    output_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    return

def init_db():
    sql_init = """CREATE TABLE IF NOT EXISTS outputs (
                'Start' text,
                'End' text,
                'Duration' text,
                'Exposure Time [%]' float,
                'Equity Final [$]' float,
                'Equity Peak [$]' float,
                'Return [%]' float,
                'Buy & Hold Return [%]' float,
                'Return (Ann.) [%]' float,
                'Volatility (Ann.) [%]' float,
                'Sharpe Ratio' float, 
                'Sortino Ratio' float, 
                'Calmar Ratio' float, 
                'Max. Drawdown [%]' float, 
                'Avg. Drawdown [%]' float, 
                'Max. Drawdown Duration' text, 
                'Avg. Drawdown Duration' text, 
                '# Trades' integer,
                'Win Rate [%]' float, 
                'Best Trade [%]' float, 
                'Worst Trade [%]' float, 
                'Avg. Trade [%]' float, 
                'Max. Trade Duration' text, 
                'Avg. Trade Duration' text, 
                'Profit Factor' float,
                'Expectancy [%]' float, 
                'SQN' float,
                'Kelly Criterion' float, 
                'indicators_used' text,
                'ticker' text,
                'datetime' text
        )"""
    try:
        with sqlite3.connect('GeneratedDatas/output.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql_init)
            conn.commit()
    except sqlite3.Error as e:
        print(e)

def main():
    args = parse_arguments()
    sharpe_threshold = args.sharpe
    max_iter = args.num
    tickers = args.tickers
    start_date = args.start
    end_date = args.end

    init_folders()
    init_db()

    with sqlite3.connect('GeneratedDatas/output.db') as conn:
        i = 0
        top_sharpe = 0
        wheel = itertools.cycle(["/ ", "- ", "\\ ", "| "])
        stats = Stats(conn, "outputs")
        
        
        while True:
            # Get the OHLC data
            data = Data()
            ticker, b_ohlc = data.get_OHLC(tickers, start_date, end_date)

            # Make the strategy
            strat = StrategyGenerator(b_ohlc)
            i_ohlc, indicators_info = strat.signal()
            
            # Run backtest
            sharpe_tested = runBacktest(db_con=conn, OHLC=i_ohlc, indicators_info=indicators_info, ticker=ticker, sharpe_saving_threshold=sharpe_threshold)
            
            # Update print values
            sharpe_tested = 0 if sharpe_tested is None else sharpe_tested
            top_sharpe = max(top_sharpe, sharpe_tested)
            i += 1
            sym = next(wheel) 
            print("\033[F\033[K\033[F\033[K\033[F\033[K", end="")
            print(f"Backtesting ... {sym}")
            print(f"Strategies tested: {i:.0f}")
            print(f"Top Sharpe Ratio tested: {top_sharpe:.2f}")

            # Break the loop if the max number of iteration is reached 
            if max_iter is not None and i >= max_iter:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
    
    return print(stats.summary.to_string())


if __name__ == "__main__":
        main()
