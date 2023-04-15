import pytest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from helpers import is_except_from_next_day_holiday_rule


@pytest.mark.parametrize(
    "day, month, year, expected",
    [
        (30, 4, 2023, True),
        (24, 12, 2022, False),
        (16, 5, 2021, True),
        (29, 2, 2024, False),
        (20, 5, 2020, True),
    ]
)
def test_is_except_from_next_day_holiday_rule(day: int, month: int, year: int, expected: bool):
    assert is_except_from_next_day_holiday_rule(day, month, year) == expected
