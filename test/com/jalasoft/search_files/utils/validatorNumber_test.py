import unittest
from src.com.jalasoft.search_files.utils.validatorNumber import ValidatorNumber


class ValidatorNumber_test(unittest.TestCase):


    valid = ValidatorNumber()


    # Test is a number
    def test_is_number_true(self):
        self.assertTrue(self.valid.is_number(2))

    def test_is_a_string_number(self):
        self.assertFalse(self.valid.is_number("number"))

    def test_is_character_instead_number_number(self):
        self.assertFalse(self.valid.is_number("*"))

    def test_is_a_long_positive_number(self):
        self.assertTrue(self.valid.is_positive(1020212154758458458444))


    # Test is possitive number
    def test_is_positive_number(self):
        self.assertTrue(self.valid.is_positive(5))

    def test_is_negative_number_instead_positive(self):
        self.assertFalse(self.valid.is_positive(-5))


if __name__ == "__main__":
    unittest.main()
