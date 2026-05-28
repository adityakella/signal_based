import pandas as pd
import numpy as np

def calculate_features(data: pd.DataFrame, window: int = 1) -> pd.DataFrame:
    data["Close_lag"] = data["Close"].shift(window)
    data["return"] = np.log(data["Close"]/data["Close_lag"])
    data["return_lag"] = data["return"].shift(window)
    data["direction"] = np.sign(data["return_lag"])
    return data