import pandas as pd
from abc import ABC, abstractmethod

class IDatabase(ABC):

    @abstractmethod
    def upsert(data:pd.DataFrame)->bool:
        pass

    @abstractmethod
    def delete(ids:list[str])->bool:
        pass

    @abstractmethod
    def append(data:pd.DataFrame)->bool:
        pass
