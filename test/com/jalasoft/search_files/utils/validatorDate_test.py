import unittest
from src.com.jalasoft.search_files.utils.validatorDate import ValidatorDate


class ValidatorDate_test(unittest.TestCase):

    valid = ValidatorDate()

    # Test is format date YYYY/MM/DD
    def test_validate_The_Right_format_date(self):
        self.assertTrue(self.valid.validate_format_date("2018/02/19"))

    def test_validate_The_Right_format_date(self):
        self.assertTrue(self.valid.validate_format_date("2018/02/02"))

    def test_validate_wrong_formatdate(self):
        self.assertFalse(self.valid.validate_format_date("02/12/2018"))

    def test_validate_charIn_Year_format_date(self):
        self.assertFalse(self.valid.validate_format_date("*/12/12"))

    def test_validate_day_With_Extra_Number_Value_In_format_date(self):
        self.assertFalse(self.valid.validate_format_date("2018/12/002"))

    def test_validate_negativeDay_in_format_date(self):
        self.assertFalse(self.valid.validate_format_date("2018/12/-2"))

    def test_validate_DateWord_InsteadOf_DayDate_in_format_date(self):
        self.assertFalse(self.valid.validate_format_date("2018/06/twelve"))

    def test_validate_swithing_Month_and_Year_in_format_date(self):
        self.assertFalse(self.valid.validate_format_date("12/2018/12"))

    def test_validate_empty_format_date(self):
        self.assertFalse(self.valid.validate_format_date(" "))

if __name__ == "__main__":
	unittest.main()