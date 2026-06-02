import pandas as pd
import numpy as np
import yfinance as yf

class Data:
    def __init__(self, config_data: pd.DataFrame):
        self.ticker = config_data.loc[0, "ticker"]
        self.yfticker = yf.Ticker(self.ticker)
        self.start = config_data.loc[0, "start"]
        self.end = config_data.loc[0, "end"]

    def load_price_data(self):
        self.price_data = self.yfticker.history(start = self.start, end = self.end)
        self.price_data.columns = self.price_data.columns.str.lower() 