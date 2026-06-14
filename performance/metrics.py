import pandas as pd
import numpy as np
from strategy.generator import strategyname
import matplotlib.pyplot as plt

def max_drawdown(df: pd.DataFrame, strategy_name: strategyname) -> dict[str: any]:
    cumulative_trade_return = df["_".join([strategy_name.value,"cumulative_trade_return"])]
    rolling_max = cumulative_trade_return.cummax()
    drawdown = (np.exp(cumulative_trade_return) - np.exp(rolling_max))/np.exp(rolling_max)
    trough_date = drawdown.idxmin()
    peak_date = cumulative_trade_return[:trough_date].idxmax()
    mdd = drawdown.min()
    cumulative_trade_return.plot(label = strategy_name.value)
    cumulative_trade_return[peak_date:trough_date].plot(label = "max drawdown")
    plt.legend()

    return {
        "max_drawdown": mdd,
        "peak_date": peak_date,
        "trough_date": trough_date
    }

def buy_and_hold(df: pd.DataFrame, strategy_name: strategyname) -> float:
    bh_return = df["return"].copy()
    cumulative_bh_return = bh_return.cumsum()
    cumulative_trade_return = df["_".join([strategy_name.value,"cumulative_trade_return"])]
    cumulative_bh_return.plot(label="Buy & Hold (without tc)")
    cumulative_trade_return.plot(label=strategy_name.value)
    plt.legend()
    return cumulative_bh_return.iloc[-1]

def sharpe_ratio():
    pass

