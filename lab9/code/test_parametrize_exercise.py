from typing import List

import pytest


def norm(vec: List[float], norm_deg: int):
    return sum(pow(v, norm_deg) for v in vec)**(1/norm_deg)


@pytest.mark.parametrize("vec_len", list(range(1, 10)))
@pytest.mark.parametrize("norm_num", list(range(1, 10)))
def test_norm(vec_len, norm_num):
    assert norm([1] * vec_len, norm_num) == vec_len ** (1/norm_num)

@pytest.mark.parametrize("vector, norm_deg, exp_value", [([2.0, 3.0], 2, (4+9)**0.5)])
def test_norm_val(vector, norm_deg, exp_value):
    assert norm(vector, norm_deg) == exp_value



