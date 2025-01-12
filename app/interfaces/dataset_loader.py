from pandas import DataFrame
from abc import ABC, abstractmethod

class DatasetLoader(ABC):
    @abstractmethod
    def load(self, filepath: str, **kwargs) -> DataFrame:
        """Load dataset from a given file."""
        pass
