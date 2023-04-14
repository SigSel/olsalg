import pytest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from helpers import calculate_easter_sunday_date


@pytest.mark.parametrize(
    "year, "
    "expected_date",
    [
        (2021, (4, 4)),
        (2022, (17, 4)),
        (2023, (9, 4)),
        (2024, (31, 3)),
        (2025, (20, 4)),
        (2026, (5, 4))
    ]
)
def test_some_easter_dates(year: int, expected_date: tuple[int, int]) -> None:
    assert calculate_easter_sunday_date(year) == expected_date


def test_easter_date_type() -> None:
    assert isinstance(calculate_easter_sunday_date(2023)[0], int)
    assert isinstance(calculate_easter_sunday_date(2023)[1], int)

