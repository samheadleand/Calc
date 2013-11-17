import pytest

import Calc2

@pytest.mark.parametrize(('input', 'expected'), [
    ('1+1', 2),
    ('1 + 1', 2),
    ('2-1', 1),
    ('2*2', 4),
    ('4/2', 2),
    ('2+5+3', 10), # 1 2
    ('(1+2)*3', 9), # 4 4
    ('5+7-2', 10), # 2 3
    ('6+2=', 8), # 3 1
    ('1+2*3', 7), # 5 5
])

# Ordering: Importance (1 Important, 5 Unimportant)
#           Difficulty (1 Easy, 5 Difficult)

def test_calc(input, expected):
    assert Calc2.complete_sum(input) == expected
