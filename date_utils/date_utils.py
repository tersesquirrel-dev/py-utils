import datetime


class DateUtils:
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
            if current_date.weekday() < 5:  # Monday=0, Friday=4
                business_days += 1
            current_date += datetime.timedelta(days=1)
        
        return business_days