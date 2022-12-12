import csv
import os

import pytest

DATA_FILE = os.path.join(
    os.path.dirname(__file__), "file_that_cannot_be_put_in_repository.csv"
)


def parse_file(file_path: str = DATA_FILE):
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        return [row for row in reader]


@pytest.mark.skipif(not os.path.exists(DATA_FILE), reason="Missing data file")
def test_parse_function():
    data = parse_file()
    assert len(data) == 17
    assert len(data[0]) == 11
    assert isinstance(data[0], dict)


def test_parse_function2():
    if not os.path.exists(DATA_FILE):
        pytest.skip("Missing data file")
    data = parse_file()
    assert len(data) == 17
    assert len(data[0]) == 11
    assert isinstance(data[0], dict)
