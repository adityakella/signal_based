import pandas as pd
import numpy as np 
from data.loader import Asset
from strategy.generator import strategyname, MeanReversionStrategy, TrendFollowingStrategy
from performance.backtest import Backtester
from performance.metrics import max_drawdown, buy_and_hold
config_data = pd.read_json("config.json")
stock = Asset(config_data)
stock.load_price_data()
stock.calculate_features()
MeanReversionStrategy(stock)()
TrendFollowingStrategy(stock)()
Backtester(stock.data, strategyname.MEAN_REVERSION).test()
Backtester(stock.data, strategyname.TREND_FOLLOWING).test()
max_drawdown(stock.data, strategyname.MEAN_REVERSION)
max_drawdown(stock.data, strategyname.TREND_FOLLOWING)
buy_and_hold(stock.data, strategyname.MEAN_REVERSION)
buy_and_hold(stock.data, strategyname.TREND_FOLLOWING)