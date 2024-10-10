from pathlib import Path
import sqlite3
from backtest import *


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
    init_folders()
    init_db()
    
    with sqlite3.connect('GeneratedDatas/output.db') as conn:
        while True:
            runBacktest(db_con=conn)


if __name__ == "__main__":
        main()
        