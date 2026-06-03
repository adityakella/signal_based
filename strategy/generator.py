import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from data.loader import Asset

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
    def __init__(self, asset: Asset):
        self.asset = asset
        self.check_strategy_evidence()

    def generate_signal(self):
        self.asset.data["signal"] = -1*self.asset.data["direction"]

    def check_strategy_evidence(self):
        print(self.asset.data.groupby("direction")["return"].agg(["mean", "count", "sum"]))
