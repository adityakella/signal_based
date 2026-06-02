import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from data.loader import Data

class BaseStrategy(ABC):
    @abstractmethod
    def __init__():
        pass
    
    @abstractmethod
    def generate_signal():
        pass

    @abstractmethod
    def check_strategy_evidence():
        pass

class MeanReversionStrategy(BaseStrategy):
    def __init__(self, features_data: pd.DataFrame):
        self.features_data = features_data
        self.check_strategy_evidence()

    def generate_signal(self):
        self.features_data["signal"] = -1*self.return_data["direction_lag_return"]

    def check_strategy_evidence(self):
        print(self.features_data.groupby("direction")["return"].agg(["mean", "count", "sum"]))
