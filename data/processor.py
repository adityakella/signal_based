import pandas as pd
import numpy as np

def calculate_features(df: pd.DataFrame, window: int = 1) -> pd.DataFrame:
    close = df["close"]
    close_lag = close.shift(window)
    ratio = close/close_lag
    df["return"] = np.log(ratio)
    return_lag = df["return"].shift(window)
    df["direction"] = np.sign(return_lag)
    return df