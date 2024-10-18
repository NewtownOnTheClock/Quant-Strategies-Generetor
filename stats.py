import pandas as pd


class Stats:
    def __init__(self, db_con, table_name) -> None:
        self._db_con = db_con
        self._table_name = table_name
    
    @property
    def count_rows(self) -> int:
        sql = f"SELECT COUNT(*) FROM {self._table_name}"
        with self._db_con as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            row_count = cursor.fetchone()[0]

        return row_count
    
    def top_returns(self, top_limit: int, ticker: str = None) -> pd.DataFrame | str:
        if ticker:
            sql = f'SELECT "ticker", "Return [%]", "Buy & Hold Return [%]", "Sharpe Ratio" FROM {self._table_name} WHERE "ticker" = ? ORDER BY "Return [%]" DESC LIMIT {top_limit}'
            params = (ticker, )
        else:
            sql = f'SELECT "ticker", "Return [%]", "Buy & Hold Return [%]", "Sharpe Ratio" FROM {self._table_name} ORDER BY "Return [%]" DESC LIMIT {top_limit}'
            params = None
        with self._db_con as conn:
            if params:
                df = pd.read_sql_query(sql, conn, params=(ticker, ))
            else:
                df = pd.read_sql_query(sql, conn)
        if df.empty:
            return f'The parameters {top_limit=} and {ticker=} results in an empty query'
        else:
            return df

    def top_sharpe(self, top_limit: int, ticker: str = None) -> pd.DataFrame | str:
        if ticker:
            sql = f'SELECT "ticker", "Return [%]", "Buy & Hold Return [%]", "Sharpe Ratio" FROM {self._table_name} WHERE "ticker" = ? ORDER BY "Sharpe Ratio" DESC LIMIT {top_limit}'
            params = (ticker, )
        else:
            sql = f'SELECT "ticker", "Return [%]", "Buy & Hold Return [%]", "Sharpe Ratio" FROM {self._table_name} ORDER BY "Sharpe Ratio" DESC LIMIT {top_limit}'
            params = None
        with self._db_con as conn:
            if params:
                df = pd.read_sql_query(sql, conn, params=(ticker, ))
            else:
                df = pd.read_sql_query(sql, conn)
        if df.empty:
            return f'The parameters {top_limit=} and {ticker=} results in an empty query'
        else:
            return df
    
    @property
    def summary(self):
        s = pd.Series(dtype=object)
        s.loc["Number of strategies tested"] = self.count_rows
        s.loc["Top Sharpe Ratio Tested"] = self.top_sharpe(top_limit=1)["Sharpe Ratio"][0]
        s.loc["Top Return tested [%]"] = self.top_returns(top_limit=1)["Return [%]"][0]

        return s
