import pandas as pd
import numpy as np

def calculate_features(data: pd.DataFrame, window: int = 1) -> pd.DataFrame:
    data["close_lag"] = data["close"].shift(window)
    data["ratio"] = data["close"]/data["close_lag"]
    data["return"] = np.log(data["ratio"])
    data["return_lag"] = data["return"].shift(window)
    data["direction"] = np.sign(data["return_lag"])
    return data