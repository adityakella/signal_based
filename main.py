import pandas as pd
import numpy as np 
from data.loader import Asset
from strategy.generator import MeanReversionStrategy
from performance.backtest import Backtester


config_data = pd.read_json("config.json")
stock = Asset(config_data)
stock.load_price_data()
stock.calculate_features()
strategy = MeanReversionStrategy(stock)
strategy.generate_signal()
backtest = Backtester(strategy)
backtest.test()