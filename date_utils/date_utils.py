import datetime


class DateUtils:
    _holidays = set()
    @staticmethod
    def set_holidays(holidays):
        """Set a list of holidays to exclude from business day calculations.
        
        Args:
            holidays: List of dates (date objects, datetime objects, or strings in YYYY-MM-DD format)
        """
        DateUtils._holidays = set()
        for holiday in holidays:
            DateUtils._holidays.add(DateUtils._normalize_date(holiday))

    @staticmethod
    def _normalize_date(date):
        """Convert string or datetime to date object."""
        if isinstance(date, str):
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        elif isinstance(date, datetime.datetime):
            return date.date()
        return date

    @staticmethod
    def day_of_year(date):
        """Return the day of the year (1-366) for a given date."""
        date = DateUtils._normalize_date(date)
        return date.timetuple().tm_yday

    @staticmethod
    def day_of_year_business(date):
        """Return the number of business days (weekdays) so far this year for a given date."""
        date = DateUtils._normalize_date(date)
        
        year = date.year
        start_date = datetime.date(year, 1, 1)
        
        business_days = 0
        current_date = start_date
        
        while current_date <= date:
            if current_date.weekday() < 5 and current_date not in DateUtils._holidays:  # Monday=0, Friday=4 and not a holiday
                business_days += 1
            current_date += datetime.timedelta(days=1)
        
        return business_days