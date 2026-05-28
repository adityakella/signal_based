import pandas as pd
import numpy as np

def mean_reversion(data: pd.DataFrame) -> pd.DataFrame:
    check = data.groupby("direction")["return"].agg(["sum", "mean", "count"])
    # to check if data exibits mean reversion 
    return data