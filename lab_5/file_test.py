import os
import csv
import shutil

import pytest

from lab_2_1 import get_absolute_paths, get_relative_paths, make_csv


@pytest.fixture
def test_dataset():
    """Make dataset for test(3 files per class)
    """
    dataset_path = "lab_5/test_dataset"
    os.makedirs(dataset_path)
    for i in range(1, 6):
        class_dir = os.path.join(dataset_path, str(i))
        os.makedirs(class_dir)
        for j in range(3):  
            file_path = os.path.join(class_dir, f"file_{j}.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Text number {j} for class: {i}")
    yield dataset_path  

    shutil.rmtree(dataset_path)


def test_get_absolute_paths(test_dataset: str):
    """Get absolute paths to the dataset and checks their correctness for length and content

    Args:
        test_dataset (str): path to dataset
    """
    class_num = 1
    result = get_absolute_paths(class_num, test_dataset)

    result_paths = [os.path.abspath(path) for path in result]
    expected_files = [
        os.path.abspath(os.path.join(test_dataset, str(class_num), f"file_{j}.txt"))
        for j in range(3)
    ]

    assert len(result_paths) == len(expected_files)
    assert all(path in expected_files for path in result_paths)


def test_get_relative_paths(test_dataset: str):
    """Get relative paths to the dataset and checks their correctness for length and content

    Args:
        test_dataset (str): path to dataset
    """

    class_num = 2
    result = [os.path.normpath(path) for path in get_relative_paths(class_num, test_dataset)]
    expected_files = [
        os.path.normpath(os.path.join("lab_5/test_dataset", str(class_num), f"file_{j}.txt"))
        for j in range(3)
    ]

    assert len(result) == len(expected_files)
    assert all(path in expected_files for path in result)



def test_make_csv(test_dataset: str):
    """make csv and check correctness for path and content

    Args:
        test_dataset (str): path to test dataset
    """
    csv_path = "lab_5/paths.csv"

    make_csv(test_dataset)
    assert os.path.exists(csv_path)

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert len(rows) == 15

    for row in rows:
        absolute_path, relative_path, label = row
        assert os.path.isabs(absolute_path)

        assert os.path.normpath(relative_path).startswith(os.path.normpath("lab_5/test_dataset"))
        assert label.isdigit() and 1 <= int(label) <= 5

    os.remove(csv_path)
