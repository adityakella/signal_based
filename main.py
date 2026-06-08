import pandas as pd
import numpy as np 
import json
from data.asset import Asset
from data.processor import calculate_features
from strategy.generator import strategyname, MeanReversionStrategy, TrendFollowingStrategy
from performance.backtest import Backtester
from performance.metrics import max_drawdown, buy_and_hold
with open("config.json") as f:
    config = json.load(f)

stock = Asset(ticker=config["ticker"], start=config["start"], end=config["end"])

stock.load_price_data()
stock.data = calculate_features(stock.data)
mean_rev_strat = MeanReversionStrategy(stock.data)
mean_rev_strat.run()
trend_follow_strat = TrendFollowingStrategy(stock.data)
trend_follow_strat.run()
Backtester(stock.data, strategyname.MEAN_REVERSION).test()
Backtester(stock.data, strategyname.TREND_FOLLOWING).test()
max_drawdown(stock.data, strategyname.MEAN_REVERSION)
max_drawdown(stock.data, strategyname.TREND_FOLLOWING)
buy_and_hold(stock.data, strategyname.MEAN_REVERSION)
buy_and_hold(stock.data, strategyname.TREND_FOLLOWING)