import os

import pytest
from app.repository import DatasetRepository
from definitions import DATA_DIR
from pandas import DataFrame

@pytest.fixture
def dataset_repository():
    return DatasetRepository()

@pytest.mark.parametrize(
    "path_name, kwargs, expected",
    [("E Commerce Dataset.xlsx", {"sheet_name": "E Comm"}, (5630, 20)),
     ("toy_ratings.csv", {}, (21, 3))],
    ids=["Test ExcelLoader", "Test CSVLoader"]
)
def test_pass_dataset_repository_load_file(path_name, kwargs, expected, dataset_repository):
    data_path = os.path.join(DATA_DIR, path_name)
    result = dataset_repository.load_dataset(data_path, **kwargs)
    assert isinstance(result, DataFrame)
    assert result.shape == expected

