import pandas as pd
import numpy as np
from strategy.generator import strategyname

def max_drawdown(df: pd.DataFrame, strategy_name: strategyname) -> dict[str: any]:
    cumulative_trade_return = df["_".join([strategy_name.value,"cumulative_trade_return"])]
    rolling_max = cumulative_trade_return.cummax()
    drawdown = (np.exp(cumulative_trade_return) - np.exp(rolling_max))/np.exp(rolling_max)
    trough_date = drawdown.idxmin()
    peak_date = cumulative_trade_return[:trough_date].idxmax()
    mdd = drawdown.min()
    cumulative_trade_return.plot()
    cumulative_trade_return[peak_date:trough_date].plot()

    return {
        "max_drawdown": mdd,
        "peak_date": peak_date,
        "trough_date": trough_date
    }

def buy_and_hold(df: pd.DataFrame, strategy_name: strategyname) -> float:
    cumulative_return = df["return"].cumsum()
    cumulative_bh_trade_return = df["_".join([strategy_name.value,"cumulative_trade_return"])]
    return cumulative_bh_trade_return.iloc[-1]

def sharpe_ratio():
    pass

