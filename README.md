# py-utils

A collection of Python utility functions for date operations.

## Installation

```bash
pip install py-utils
```

## Usage

```python
from date_utils import day_of_year, day_of_year_business
import datetime

# Calculate day of year
print(day_of_year("2024-01-15"))  # 15
print(day_of_year(datetime.date(2024, 12, 31)))  # 366 (leap year)

# Calculate business days since start of year
print(day_of_year_business("2024-01-15"))  # Business days up to Jan 15
print(day_of_year_business(datetime.date(2024, 12, 31)))  # Total business days in year
```

## Functions

### `day_of_year(date)`
Returns the day of the year (1-366) for a given date. Accepts:
- String in "YYYY-MM-DD" format
- `datetime.date` object
- `datetime.datetime` object

### `day_of_year_business(date)`
Returns the number of business days (weekdays) so far this year for a given date. Accepts the same date formats as `day_of_year`.

## License

See LICENSE file for details.