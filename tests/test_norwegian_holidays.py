import pytest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from helpers import is_norwegian_holiday


@pytest.mark.parametrize(
    "day, month, year, expected",
    [
        (1, 1, 2023, True),
        (14, 4, 2022, True),
        (15, 4, 2022, True),
        (18, 4, 2022, True),
        (26, 5, 2022, True),
        (5, 6, 2022, True),
        (6, 6, 2022, True),
        (25, 12, 2022, True),
        (26, 12, 2022, True),
        (17, 5, 2022, True),
        (2, 2, 2023, False),
    ]
)
def test_is_norwegian_holiday(day: int, month: int, year: int, expected: bool):
    assert is_norwegian_holiday(day, month, year) == expected
