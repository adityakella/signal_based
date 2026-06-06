import pandas as pd
import numpy as np
from strategy.generator import strategyname

def max_drawdown(df: pd.DataFrame, strategy_name: strategyname) -> float:
    cumulative_trade_return = df["_".join([strategy_name.value,"cumulative_trade_return"])]
    rolling_max = cumulative_trade_return.cummax()
    drawdown = (np.exp(cumulative_trade_return) - np.exp(rolling_max))/np.exp(rolling_max)
    trough_date = drawdown.idxmin()
    peak_date = cumulative_trade_return[:trough_date].idxmax()
    max_drawdown = drawdown.min()
    cumulative_trade_return.plot()
    cumulative_trade_return[peak_date:trough_date].plot()
    print(peak_date)
    print(trough_date)
    return np.log(max_drawdown + 1)

def buy_and_hold(df: pd.DataFrame, strategy_name: strategyname):
    cumulative_return = df["return"].cumsum()
    cumulative_trade_return = df["_".join([strategy_name.value,"cumulative_trade_return"])]

    cumulative_return.plot()
    cumulative_trade_return.plot()

def sharpe_ratio():
    pass

