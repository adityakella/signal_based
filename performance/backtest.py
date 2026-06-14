import pandas as pd
import numpy as np
from strategy.generator import BaseStrategy, strategyname
import matplotlib.pyplot as plt

class Backtester:
    def __init__(self, df: pd.DataFrame, strategy_name: strategyname, transaction_cost: float):
        self.df = df
        self.strategy = strategy_name.value
        self.tc = transaction_cost

    @property
    def tc(self):
        return self._tc
    
    @tc.setter
    def tc(self, transaction_cost: float):
        if(transaction_cost < 0 or transaction_cost > 1):
            raise ValueError(f"transaction cost must be between 0 and 1 (both inclusive), given {transaction_cost}")
        else:
            self._tc = transaction_cost

    def test(self) -> dict[str, float]:
        trade_return = "_".join([self.strategy,"trade_return"])
        cumulative_trade_return = "_".join([self.strategy,"cumulative_trade_return"])
        signal = "_".join([self.strategy,"signal"])

        tc_magnitude = self.df[signal].diff().abs()
        tc_magnitude.fillna(0, inplace = True)
        self.df[trade_return] = self.df["return"]*self.df[signal]
        transaction_cost = tc_magnitude*np.log(1 + self.tc)
        self.df[trade_return] = self.df[trade_return] - transaction_cost
        self.df[cumulative_trade_return] = self.df[trade_return].cumsum()

        
        winning_trades = self.df[trade_return].dropna() > 0
        neutral_trades = self.df[trade_return].dropna() == 0
        losing_trades = self.df[trade_return].dropna() < 0
        self.win_rate = winning_trades.sum()/self.df[trade_return].count()
        
        return {
            "# winning trades" : winning_trades.sum(),
            "# losing trades" : losing_trades.sum(),
            "# neutral trades" : neutral_trades.sum(),
            "# na trades" : self.df[trade_return].isna().sum(),
            "# total trades" : self.df[trade_return].count(),
            "win_rate": self.win_rate
        }