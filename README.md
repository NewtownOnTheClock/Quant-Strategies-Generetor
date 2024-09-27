# Quant Strategies Generator
Quant Strategies Generator is a research based project allowing the generation of backtests based on a random mix of financial indicators. The project is still early in it's developement stage, but more features will come soon.

## Features
- Fetch financial data
- Generate a investment strategy, based on the random selection of financial indicators
- Backtest the strategy
- Report the result in a csv file called tested_backtests.csv sorting by higher Sharpe Ratio

The framework [backtesting.py](https://github.com/kernc/backtesting.py) is used for the backtesting portion on the project

## Installation
The use of a [virtual environement](https://docs.python.org/3/library/venv.html) and python 3.12 is required
[TA-LIB](https://github.com/TA-Lib/ta-lib-python) also needs to be downloaded for the code to run

```
$ git clone https://github.com/NewtownOnTheClock/Quant-Strategies-Generetor.git

$ pip install -r requirements.txt
```

## Quickstart
```
$ python backtest.py
```