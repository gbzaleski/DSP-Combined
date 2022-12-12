from math import isclose


def test_add():
    assert 2 + 3 == 5


def test_div():
    assert isclose(5 / 2, 2.5)
