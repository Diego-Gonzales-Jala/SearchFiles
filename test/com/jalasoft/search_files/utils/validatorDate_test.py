import unittest
from src.com.jalasoft.search_files.utils.validatorDate import ValidatorDate

class ValidatorTest(unittest.TestCase):
    valid = ValidatorDate()

    # Test is format date
    def test_validate_format_date(self):
        self.assertTrue(self.valid.validate_format_date('01/02/2018'))

    def test1_validate_format_date(self):
        self.assertFalse(self.valid.validate_format_date("2018/02/04"))

    def test2_validate_format_date(self):
        self.assertTrue(self.valid.validate_format_date("12/12/3000"))

    def test3_validate_format_date(self):
        self.assertFalse(self.valid.validate_format_date("002/12/2018"))

    def test4_validate_format_date(self):
        self.assertFalse(self.valid.validate_format_date("-2/12/2018"))

    def test5_validate_format_date(self):
        self.assertFalse(self.valid.validate_format_date("2018/06/twelve"))

    def test6_validate_format_date(self):
        self.assertFalse(self.valid.validate_format_date("12/2018/12"))