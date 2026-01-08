# py-utils

A collection of Python utility functions for date operations.

## Installation

```bash
pip install py-utils
```

## Usage

```python
from date_utils import DateUtils
import datetime

# Calculate day of year
print(DateUtils.day_of_year("2024-01-15"))  # 15
print(DateUtils.day_of_year(datetime.date(2024, 12, 31)))  # 366 (leap year)

# Calculate business days since start of year
print(DateUtils.day_of_year_business("2024-01-15"))  # Business days up to Jan 15
print(DateUtils.day_of_year_business(datetime.date(2024, 12, 31)))  # Total business days in year

# Set holidays to exclude from business day calculations
DateUtils.set_holidays([
    "2024-01-01",  # New Year's Day
    "2024-07-04",  # Independence Day
    "2024-12-25",  # Christmas Day
])
print(DateUtils.day_of_year_business("2024-01-15"))  # Business days up to Jan 15 (excluding holidays)
```

## DateUtils Class

### `DateUtils.day_of_year(date)`
Returns the day of the year (1-366) for a given date. Accepts:
- String in "YYYY-MM-DD" format
- `datetime.date` object
- `datetime.datetime` object

### `DateUtils.day_of_year_business(date)`
Returns the number of business days (weekdays) so far this year for a given date. Accepts the same date formats as `day_of_year`.

### `DateUtils.set_holidays(holidays)`
Sets a list of holidays to exclude from business day calculations. Accepts a list of dates in any of the following formats:
- String in "YYYY-MM-DD" format
- `datetime.date` object
- `datetime.datetime` object

## Running Tests

To run the unit tests:

```bash
cd date_utils_tests
python test_date_utils.py
```

The tests use Python's built-in `unittest` framework and cover all functionality including date formats, business day calculations, and holiday exclusions.

## License

See LICENSE file for details.