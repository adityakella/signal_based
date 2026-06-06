import pandas as pd
import numpy as np
from strategy.generator import BaseStrategy, strategyname
import matplotlib.pyplot as plt

class Backtester:
    def __init__(self, df: pd.DataFrame, strategy_name: strategyname, start = None, end = None):
        self.df = df
        self.strategy = strategy_name.value
        self.start = start
        self.end = end

    def test(self):
        trade_return = "_".join([self.strategy,"trade_return"])
        cumulative_trade_return = "_".join([self.strategy,"cumulative_trade_return"])
        signal = "_".join([self.strategy,"signal"])

        self.df[trade_return] = self.df["return"]*self.df[signal]
        self.df[cumulative_trade_return] = self.df[trade_return].cumsum()

        plt.plot(self.df[cumulative_trade_return])
        
        _ = self.df[trade_return] >= 0
        self.win_rate = _.sum()/len(self.df[trade_return])
        print(f"win_rate:{self.win_rate}")