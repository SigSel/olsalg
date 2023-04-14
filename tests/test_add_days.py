import pytest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from helpers import add_days_to_date


@pytest.mark.parametrize(
    "day, month, year, days_to_add, expected",
    [
        (13, 4, 2023, 0, (13, 4, 2023)),
        (13, 4, 2023, 10, (23, 4, 2023)),
        (31, 12, 2021, 365, (31, 12, 2022)),
        (1, 1, 2023, 365, (1, 1, 2024)),
        (13, 4, 2023, -10, (3, 4, 2023)),
        (1, 1, 2023, -365, (1, 1, 2022)),
        (31, 12, 2022, -365, (31, 12, 2021))
    ]
)
def test_add_days_to_date_valid(
        day: int,
        month: int,
        year: int,
        days_to_add: int,
        expected: tuple[int, int, int]
) -> None:
    assert add_days_to_date(day, month, year, days_to_add) == expected


@pytest.mark.parametrize(
    "day, month, year, days_to_add",
    [
        (31, 2, 2023, 0),
        (29, 2, 2023, 365)
    ]
)
def test_add_days_to_date_invalid(day: int, month: int, year: int, days_to_add: int) -> None:
    with pytest.raises(ValueError):
        add_days_to_date(day, month, year, days_to_add)
