import pandas as pd
import numpy as np
from strategy.generator import BaseStrategy
import matplotlib.pyplot as plt

class Backtester:
    def __init__(self, strategy: BaseStrategy, start = None, end = None):
        self.strategy = strategy
        self.start = strategy.asset.start if start is None else start
        self.end = strategy.asset.end if end is None else end

    def test(self):
        self.strategy.asset.data["trade_return"] = self.strategy.asset.data["return"]*self.strategy.asset.data["signal"]
        self.strategy.asset.data["cumulative_trade_return"] = self.strategy.asset.data["trade_return"].cumsum()
        plt.plot(self.strategy.asset.data["cumulative_trade_return"])
        plt.savefig("equity_chart.jpg")
        _ = self.strategy.asset.data["trade_return"] >= 0
        self.win_rate = _.sum()/len(self.strategy.asset.data["trade_return"])
        print(f"win_rate:{self.win_rate}")