# utf-8
# Python 3.9
# 2021-05-03


from abc import abstractmethod, ABC
import pandas as pd


class __BaseModel(ABC):

    @abstractmethod
    def fit(self, X, y, *args, **kwargs) -> pd.Series: pass

    @abstractmethod
    def predict(self, X, *args, **kwargs) -> pd.Series: pass


class IterationModel(__BaseModel):
    pass


class WideModel(__BaseModel):
    pass
