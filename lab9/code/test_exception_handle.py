import pytest
from py.error import EEXIST


def test_recreate_directory_exception(tmpdir):
    (tmpdir / "test").mkdir()
    with pytest.raises(EEXIST):
        (tmpdir / "test").mkdir()


def test_missed_key():
    dkt = {"key": 1}
    with pytest.raises(KeyError) as execinfo:
        dkt["key2"]
    assert "'key2'" == str(execinfo.value)


def test_list_exception():
    li = [1, 2, 3, 4, 5]
    assert li.index(2) == 1
    with pytest.raises(ValueError):
        li.index(6)
    with pytest.raises(IndexError):
        li[9]
