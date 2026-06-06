import pandas as pd
import numpy as np


def max_drawdown(df: pd.DataFrame):
    cumulative_trade_return = df["cumulative_trade_return"]
    rolling_max = df["cumulative_trade_return"].cummax()
    drawdown = (np.exp(cumulative_trade_return) - np.exp(rolling_max))/np.exp(rolling_max)
    trough_date = drawdown.idxmin()
    peak_date = cumulative_trade_return[:trough_date].idxmax()
    max_drawdown = drawdown.min()
    cumulative_trade_return.plot()
    cumulative_trade_return[peak_date:trough_date].plot()
    print(peak_date)
    print(trough_date)
    return np.log(max_drawdown + 1)

def buy_and_hold():
    pass

def sharpe_ratio():
    pass

