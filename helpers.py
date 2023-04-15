from datetime import datetime, timedelta, date


def get_closing_time(input_date: date) -> int:
    closing_hour = 20
    weekday = input_date.strftime("%A")
    check_next_day = is_next_day_holiday(day=input_date.day, month=input_date.month, year=input_date.year)
    check_for_next_day_exception = is_except_from_next_day_holiday_rule(
        day=input_date.day, month=input_date.month, year=input_date.year
    )
    if is_norwegian_holiday(day=input_date.day, month=input_date.month, year=input_date.year):
        closing_hour = 0
    elif weekday == "Sunday":
        closing_hour = 0
    elif weekday == "Saturday":
        closing_hour = 18
    elif check_next_day and not check_for_next_day_exception:
        closing_hour = 18

    return closing_hour


def is_next_day_holiday(day: int, month: int, year: int) -> bool:
    next_date_day, next_date_month, next_date_year = add_days_to_date(day, month, year, 1)
    return is_norwegian_holiday(next_date_day, next_date_month, next_date_year)


def is_except_from_next_day_holiday_rule(day: int, month: int, year: int) -> bool:
    easter_sunday_day, easter_sunday_month = calculate_easter_sunday_date(year)
    day_before_ascension = add_days_to_date(easter_sunday_day, easter_sunday_month, year, 38)[:-1]
    exception_days = {
        (30, 4),
        (16, 5),
        day_before_ascension
    }

    return (day, month) in exception_days


def is_norwegian_holiday(day: int, month: int, year: int) -> bool:
    easter_sunday_day, easter_sunday_month = calculate_easter_sunday_date(year)
    norwegian_holidays = {
        (1, 1),  # New Year's Day
        (easter_sunday_day, easter_sunday_month),
        add_days_to_date(easter_sunday_day, easter_sunday_month, year, -3)[:-1],  # Maundy Thursday
        add_days_to_date(easter_sunday_day, easter_sunday_month, year, -2)[:-1],  # Good Friday
        add_days_to_date(easter_sunday_day, easter_sunday_month, year, 1)[:-1],   # Easter Monday
        add_days_to_date(easter_sunday_day, easter_sunday_month, year, 39)[:-1],  # Ascension Day
        add_days_to_date(easter_sunday_day, easter_sunday_month, year, 49)[:-1],  # Pentecost Sunday
        add_days_to_date(easter_sunday_day, easter_sunday_month, year, 50)[:-1],  # Pentecost Monday
        (25, 12), (26, 12),     # Christmas holidays
        (1, 5), (17, 5)         # Norwegian Constitution Day
    }

    return (day, month) in norwegian_holidays


def calculate_easter_sunday_date(year: int) -> tuple[int, int]:
    # Calculate Easter Sunday date using the Meeus/Jones/Butcher algorithm
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    month, day = n, p
    return day, month


def add_days_to_date(day: int, month: int, year: int, num_days: int) -> tuple[int, int, int]:
    date_string = f"{day}/{month}/{year}"
    date_ = datetime.strptime(date_string, "%d/%m/%Y")
    new_date = date_ + timedelta(days=num_days)
    return new_date.day, new_date.month, new_date.year
