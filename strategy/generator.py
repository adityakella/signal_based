import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from enum import Enum
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_acf


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
        self.ljung_box()

    @abstractmethod
    def ljung_box(self):
        returns = self.df["return"].dropna()
        results = acorr_ljungbox(returns, lags=1)
        print(results)
        plot_acf(returns, lags=20)


class MeanReversionStrategy(BaseStrategy):
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def run(self):
        self.check_strategy_evidence()
        self.generate_signal()

    def generate_signal(self):
        self.df["_".join([strategyname.MEAN_REVERSION.value,"signal"])] = -1*self.df["direction"]

    def check_strategy_evidence(self):
        super().check_strategy_evidence() 

    def ljung_box(self):
        super().ljung_box()

class TrendFollowingStrategy(BaseStrategy):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def run(self):
        self.check_strategy_evidence()
        self.generate_signal()

    def generate_signal(self):
        self.df["_".join([strategyname.TREND_FOLLOWING.value,"signal"])] = self.df["direction"]

    def check_strategy_evidence(self):
        super().check_strategy_evidence() 

    def ljung_box(self):
        super().ljung_box()