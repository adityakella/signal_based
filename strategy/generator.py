import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from data.loader import Asset
from enum import Enum

class strategyname(Enum):
    MEAN_REVERSION = "mean_reversion"
    TREND_FOLLOWING = "trend_following"

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
    
    def __call__(self):
        self.check_strategy_evidence()
        self.generate_signal()

    def generate_signal(self):
        self.asset.data["mean_reversion_signal"] = -1*self.asset.data["direction"]

    def check_strategy_evidence(self):
        print(self.asset.data.groupby("direction")["return"].agg(["mean", "count", "sum"]))

class TrendFollowingStrategy(BaseStrategy):
    def __init__(self, asset: Asset):
        self.asset = asset

    def __call__(self):
        self.check_strategy_evidence()
        self.generate_signal()

    def generate_signal(self):
        self.asset.data["trend_following_signal"] = self.asset.data["direction"]

    def check_strategy_evidence(self):
        print(self.asset.data.groupby("direction")["return"].agg(["mean", "count", "sum"]))
