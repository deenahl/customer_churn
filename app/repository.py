from logging import getLogger
logger = getLogger("Repository")

from app.Factory.FileLoaderFactory import FileLoaderFactory

class DatasetRepository:
    def __init__(self):
        self.factory = FileLoaderFactory()

    def load_dataset(self, filepath: str, **kwargs):
        """
        Load dataset with appropriate loader
        :param filepath: path to file
        :param kwargs: additional arguments for loading datasets
        :return: pandas dataframe
        """
        try:
            loader = self.factory.get_loader(filepath)
            return loader.load(filepath=filepath, **kwargs)
        except Exception as e:
            raise e