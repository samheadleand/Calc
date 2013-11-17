import pytest

import Calc2

@pytest.mark.parametrize(('input', 'expected'), [
    ('1+1', 2),
    ('1 + 1', 2),
    ('2-1', 1),
    ('2*2', 4),
    ('4/2', 2),
])
def test_calc(input, expected):
    assert Calc2.complete_sum(input) == expected
