import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from enum import Enum

class strategyname(Enum):
    MEAN_REVERSION = "mean_reversion"
    TREND_FOLLOWING = "trend_following"

class BaseStrategy(ABC):
    @abstractmethod
    def generate_signal(self):
        pass

    @abstractmethod
    def check_strategy_evidence(self):
        self.df["trend_following_signal"] = self.df["direction"]

class MeanReversionStrategy(BaseStrategy):
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def run(self):
        self.check_strategy_evidence()
        self.generate_signal()

    def generate_signal(self):
        print(self.df.groupby("direction")["return"].agg(["mean", "count"]))

    def check_strategy_evidence(self):
        super().check_strategy_evidence() 

class TrendFollowingStrategy(BaseStrategy):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def run(self):
        self.check_strategy_evidence()
        self.generate_signal()

    def generate_signal(self):
        self.df["trend_following_signal"] = self.df["direction"]

    def check_strategy_evidence(self):
        super().check_strategy_evidence() 