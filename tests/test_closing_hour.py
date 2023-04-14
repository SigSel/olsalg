from datetime import date
import pytest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from helpers import get_closing_time


@pytest.mark.parametrize(
    "input_date, expected_closing_hour",
    [
        (date(2023, 4, 13), 20),  # Weekday
        (date(2023, 4, 15), 18),  # Saturday
        (date(2023, 4, 16), 0),   # Sunday
        (date(2023, 5, 17), 0),   # Holiday
        (date(2023, 5, 16), 18),  # Day before holiday
    ]
)
def test_get_closing_time(input_date: date, expected_closing_hour: int) -> None:
    closing_hour = get_closing_time(input_date)
    assert closing_hour == expected_closing_hour
