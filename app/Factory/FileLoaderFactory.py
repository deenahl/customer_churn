from app.interfaces.dataset_loader import DatasetLoader
from app.loaders.csv_loader import CSVLoader
from app.loaders.excel_loader import ExcelLoader

class FileLoaderFactory:
    _loaders = {
        "csv": CSVLoader,
        "xlsx": ExcelLoader,
    }

    @staticmethod
    def get_loader(filepath: str) -> DatasetLoader:
        ext = filepath.split(".")[-1].lower()
        loader_type = FileLoaderFactory._loaders.get(ext)
        if not loader_type:
            raise ValueError(f"Unsupported file type: {filepath}")
        return loader_type()