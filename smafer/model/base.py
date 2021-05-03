# utf-8
# Python 3.9
# 2021-05-03


from abc import abstractmethod, ABC
import pandas as pd


class __BaseModel(ABC):

    @abstractmethod
    def __init__(self, estimator, *args, **kwargs) -> None: pass

    @abstractmethod
    def fit(self, *args, **kwargs) -> pd.Series: pass

    @abstractmethod
    def predict(self, *args, **kwargs) -> pd.Series: pass
