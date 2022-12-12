import pytest


def in_circle(x, y, radius=1):
    return x ** 2 + y ** 2 < radius ** 2


def test_in_circle():
    assert in_circle(0, 0)
    assert in_circle(0.5, 0.5)
    assert in_circle(9, 0, 10)
    assert not in_circle(1, 1)
    assert not in_circle(100, 1, 10)


@pytest.mark.xfail(reason="Wrong border handle")
def test_in_circle_border():
    assert in_circle(1, 0)
    assert in_circle(0, 10, 10)
