
import pytest
from operator import itemgetter
from nbp_change import calc_statistics

@pytest.mark.parametrize("given_arg,expected_range", [("USD", (3, 8)), ("EUR", (3, 9))])
def test_value(given_arg, expected_range):
    result = calc_statistics([given_arg], 10)
    assert result[given_arg]['course'] > expected_range[0]
    assert result[given_arg]['course'] < expected_range[1]

@pytest.mark.parametrize("given_arg,result_arg", [("USD", "dolar amerykański"), ("EUR", "euro")])
def test_name(given_arg, result_arg):
    result = calc_statistics([given_arg], 10)
    assert result[given_arg]['full_name'] == result_arg

def test_wrong_nmae():
    with pytest.raises(ValueError):
        calc_statistics(["YEN"], 10)

def test_list():
    assert len(calc_statistics(["USD"], 10)) == 1
    assert len(calc_statistics(["EUR", "JPY", "USD"], 10)) == 3


print(calc_statistics(["USD"], 10))