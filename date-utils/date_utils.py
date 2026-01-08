import datetime


def day_of_year(date):
    """Return the day of the year (1-366) for a given date."""
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    elif isinstance(date, datetime.datetime):
        date = date.date()
    
    return date.timetuple().tm_yday


def day_of_year_business(date):
    """Return the number of business days (weekdays) so far this year for a given date."""
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    elif isinstance(date, datetime.datetime):
        date = date.date()
    
    year = date.year
    start_date = datetime.date(year, 1, 1)
    
    business_days = 0
    current_date = start_date
    
    while current_date <= date:
        if current_date.weekday() < 5:  # Monday=0, Friday=4
            business_days += 1
        current_date += datetime.timedelta(days=1)
    
    return business_days