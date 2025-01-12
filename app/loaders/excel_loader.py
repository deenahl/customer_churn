from app.logger import setup_logging
logger = setup_logging("ExcelLoader")

from pandas import read_excel, DataFrame
from app.interfaces.dataset_loader import DatasetLoader

class ExcelLoader(DatasetLoader):
    def load(self, filepath: str, **kwargs) -> DataFrame:
        """
        Load an Excel File into a Pandas DataFrame
        :param filepath: Path to the Excel File
        :param kwargs: additional arguments such as sheet_name
        :return: pd.DataFrame
        """
        try:
            return read_excel(filepath, **kwargs)
        except Exception as e:
            logger.error(e)
            raise e

