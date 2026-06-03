import pandas as pd
import numpy as np
import yfinance as yf

class Asset:
    def __init__(self, config_data: pd.DataFrame):
        self.ticker = config_data.loc[0, "ticker"]
        self.yfticker = yf.Ticker(self.ticker)
        self.start = config_data.loc[0, "start"]
        self.end = config_data.loc[0, "end"]

    def load_price_data(self) -> None:
        self.data = self.yfticker.history(start = self.start, end = self.end)
        self.data.columns = self.data.columns.str.lower()

    def calculate_features(self, window: int = 1) -> None:
        self.data["close_lag"] = self.data["close"].shift(window)
        self.data["ratio"] = self.data["close"]/self.data["close_lag"]
        self.data["return"] = np.log(self.data["ratio"])
        self.data["return_lag"] = self.data["return"].shift(window)
        self.data["direction"] = np.sign(self.data["return_lag"])