import unittest
import datetime
import sys
import os

# Add the parent directory to the path so we can import date_utils
sys.path.insert(0, '../date_utils')

from date_utils import DateUtils


class TestDateUtils(unittest.TestCase):
    
    def test_day_of_year_with_date_string(self):
        """Test day_of_year with date string input."""
        result = DateUtils.day_of_year("2023-01-01")
        self.assertEqual(result, 1)
        
        result = DateUtils.day_of_year("2023-12-31")
        self.assertEqual(result, 365)
        
        result = DateUtils.day_of_year("2024-12-31")  # Leap year
        self.assertEqual(result, 366)
    
    def test_day_of_year_with_datetime(self):
        """Test day_of_year with datetime input."""
        result = DateUtils.day_of_year(datetime.datetime(2023, 6, 15))
        self.assertEqual(result, 166)
    
    def test_day_of_year_with_date(self):
        """Test day_of_year with date input."""
        result = DateUtils.day_of_year(datetime.date(2023, 6, 15))
        self.assertEqual(result, 166)
    
    def test_day_of_year_business_weekday(self):
        """Test day_of_year_business for weekday dates."""
        result = DateUtils.day_of_year_business("2023-01-02")  # Monday
        self.assertEqual(result, 1)  # Jan 1 was Sunday, so only Jan 2 counts
        
        result = DateUtils.day_of_year_business("2023-01-06")  # Friday
        self.assertEqual(result, 5)  # Mon-Fri = 5 business days
    
    def test_day_of_year_business_weekend(self):
        """Test day_of_year_business for weekend dates."""
        result = DateUtils.day_of_year_business("2023-01-07")  # Saturday
        self.assertEqual(result, 5)  # Same as Friday, since weekend doesn't count
        
        result = DateUtils.day_of_year_business("2023-01-08")  # Sunday
        self.assertEqual(result, 5)  # Still 5 business days
    
    def test_day_of_year_business_with_datetime(self):
        """Test day_of_year_business with datetime input."""
        result = DateUtils.day_of_year_business(datetime.datetime(2023, 1, 6))  # Friday
        self.assertEqual(result, 5)
    
    def test_day_of_year_business_with_date(self):
        """Test day_of_year_business with date input."""
        result = DateUtils.day_of_year_business(datetime.date(2023, 1, 6))  # Friday
        self.assertEqual(result, 5)
    
    def test_day_of_year_business_leap_year(self):
        """Test day_of_year_business in leap year."""
        result = DateUtils.day_of_year_business("2024-01-05")  # Friday of leap year
        self.assertEqual(result, 5)  # Same as non-leap year for this period
    
    def test_day_of_year_business_spanning_weeks(self):
        """Test day_of_year_business across multiple weeks."""
        result = DateUtils.day_of_year_business("2023-01-15")  # Sunday
        # Week 1: 5 days (Jan 2-6), Week 2: 5 days (Jan 9-13)
        # Jan 15 is Sunday, so no additional business days
        self.assertEqual(result, 10)
    
    def test_set_holidays_with_strings(self):
        """Test set_holidays with string dates."""
        holidays = ["2023-01-02", "2023-01-16"]  # Monday dates
        DateUtils.set_holidays(holidays)
        
        # Test that Jan 2 (Monday holiday) is not counted
        result = DateUtils.day_of_year_business("2023-01-06")  # Friday
        self.assertEqual(result, 4)  # Should be 4, not 5 (Jan 2 excluded)
        
        # Test that Jan 16 (Monday holiday) is not counted
        result = DateUtils.day_of_year_business("2023-01-20")  # Friday
        # Week 1: 4 days (Jan 3-6), Week 2: 5 days (Jan 9-13), Week 3: 4 days (Jan 17-20)
        self.assertEqual(result, 13)
    
    def test_set_holidays_with_dates(self):
        """Test set_holidays with date objects."""
        holidays = [datetime.date(2023, 1, 2), datetime.datetime(2023, 1, 16)]
        DateUtils.set_holidays(holidays)
        
        result = DateUtils.day_of_year_business("2023-01-06")  # Friday
        self.assertEqual(result, 4)  # Jan 2 excluded
    
    def test_set_holidays_mixed_types(self):
        """Test set_holidays with mixed date types."""
        holidays = ["2023-01-02", datetime.date(2023, 1, 16), datetime.datetime(2023, 2, 20)]
        DateUtils.set_holidays(holidays)
        
        result = DateUtils.day_of_year_business("2023-02-24")  # Friday
        # Calculate expected: Jan 3-6 (4), Jan 9-13 (5), Jan 17-20 (4), Jan 23-27 (5)
        # Jan 30-Feb 3 (5), Feb 6-10 (5), Feb 13-17 (5), Feb 21-24 (4)
        # Total: 4+5+4+5+5+5+5+4 = 37
        self.assertEqual(result, 37)
    
    def test_set_holidays_weekend_ignored(self):
        """Test that holidays on weekends don't affect business day count."""
        holidays = ["2023-01-07", "2023-01-08"]  # Saturday, Sunday
        DateUtils.set_holidays(holidays)
        
        result = DateUtils.day_of_year_business("2023-01-08")  # Sunday
        self.assertEqual(result, 5)  # Should be same as without weekend holidays
    
    def test_set_holidays_empty_list(self):
        """Test set_holidays with empty list."""
        DateUtils.set_holidays([])
        
        result = DateUtils.day_of_year_business("2023-01-06")  # Friday
        self.assertEqual(result, 5)  # Should be normal business day count
    
    def test_set_holidays_overwrite(self):
        """Test that set_holidays overwrites previous holidays."""
        # Set initial holidays
        DateUtils.set_holidays(["2023-01-02"])
        result = DateUtils.day_of_year_business("2023-01-06")
        self.assertEqual(result, 4)
        
        # Overwrite with different holidays
        DateUtils.set_holidays(["2023-01-03"])
        result = DateUtils.day_of_year_business("2023-01-06")
        self.assertEqual(result, 4)  # Still 4, but now Jan 3 is excluded instead of Jan 2


if __name__ == "__main__":
    unittest.main()