import functools
from typing import List

import pytest


@functools.lru_cache
def fibonacci(n: int):
    """Calculate n-th fibbonaci number"""
    if n < 0:
        raise ValueError("Unsupported value")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@pytest.mark.parametrize("num,res", [(0, 0), (1, 1), (2, 1), (10, 55), (18, 2584)])
def test_fibonacci(num: int, res: int):
    assert fibonacci(num) == res


@pytest.mark.parametrize("num", [-1, -7, -50])
def test_fibonacci_negative(num):
    with pytest.raises(ValueError, match="Unsupported value"):
        fibonacci(num)


def zeros_matrix(n: int, m: int) -> List[List[float]]:
    """Create n by m zeros matrix"""
    return [[0 for _ in range(m)] for _ in range(n)]


@pytest.mark.parametrize("n_size", list(range(1, 10)))
@pytest.mark.parametrize("m_size", list(range(1, 20, 2)))
def test_zero_matrix(n_size, m_size):
    matrix = zeros_matrix(n_size, m_size)
    assert len(matrix) == n_size
    assert all(map(lambda x: len(x) == m_size, matrix))
    assert all(x == 0 for y in matrix for x in y)
    matrix[0][0] = 1
    assert all(x == 0 for y in matrix[1:] for x in y)
    assert all(x == 0 for x in matrix[0][1:])
