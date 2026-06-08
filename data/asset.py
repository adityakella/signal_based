import pandas as pd
import numpy as np
import yfinance as yf

class Asset:
    def __init__(self, ticker: str, start: str, end: str):
        self.ticker = ticker
        self.yfticker = yf.Ticker(self.ticker)
        self.start = start
        self.end = end
        self.data = None

    def load_price_data(self) -> None:
        self.data = self.yfticker.history(start = self.start, end = self.end)
        self.data.columns = self.data.columns.str.lower()