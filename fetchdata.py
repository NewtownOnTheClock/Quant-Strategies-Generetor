import yfinance as yf
import pandas as pd
import random as rnd
import os


class Data:
    def __init__(self) -> None:
        self.ticker_list = [...] # TODO add tickers 

    def get_OHLC(self, tickers: list[str], start: str, end: str, to_csv: bool=True, path: str="Datas") -> pd.DataFrame:
        ticker = rnd.choice(tickers)
        start_date_abbr = "".join(start.split("-"))
        end_date_abbr = "".join(end.split("-"))

        yf_csv_list = os.listdir(path)
        is_in = str(f"{ticker}-{start_date_abbr}-{end_date_abbr}.csv") in yf_csv_list
        if is_in:
            df = pd.read_csv(f"{path}/{ticker}-{start_date_abbr}-{end_date_abbr}.csv").set_index("Date")
            df.index = pd.to_datetime(df.index)
            return ticker, df
            
        df: pd.DataFrame = yf.download(tickers=ticker, start=start, end=end).drop(columns={"Adj Close"})
        if to_csv:
            df.to_csv(f"{path}/{ticker}-{start_date_abbr}-{end_date_abbr}.csv")

            return ticker, df

