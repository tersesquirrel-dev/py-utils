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


if __name__ == "__main__":
    unittest.main()