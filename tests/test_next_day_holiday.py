import pytest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from helpers import is_next_day_holiday


@pytest.mark.parametrize(
    "day, month, year, expected",
    [
        (1, 1, 2023, False),
        (23, 12, 2022, True),
        (31, 12, 2021, True),
        (29, 2, 2024, False),
    ]
)
def test_is_next_day_holiday(day: int, month: int, year: int, expected: bool):
    assert is_next_day_holiday(day, month, year) == expected
