import unittest
import os
from src.com.jalasoft.search_files.utils.validator import Validator
from definition import ROOT_DIR


class ValidatorTest(unittest.TestCase):
    valid = Validator()

    # Test there is a right path.
    def test_validator_exist_path(self):
        path = os.path.join(ROOT_DIR, 'test/com/jalasoft/search_files/test_folder/test_valid_path.txt')
        self.assertTrue(self.valid.validator_exist_path(path))

    def test_is_number_true(self):
        self.assertTrue(self.valid.is_number(2))

    def test_is_number_false(self):
        self.assertFalse(self.valid.is_number("test"))

    def test_is_positive_true(self):
        self.assertTrue(self.valid.is_positive(5))

    def test_is_positive_false(self):
        self.assertFalse(self.valid.is_positive(-5))

#############################################################
        def name_path(self):
            self.name_path = path("C:\\Program Files (x86)")

        # Test there is a right path.
        def test_validate_path(self):
            self.assertEqual(self.validator.name_path(), "C:\\Program Files (x86)")

        def test_validate_path(self):
            self.assertFalse(self.validator.name_path(), "C:\\Program Files* (x86)*")

        # Test is a number.

        def test_is_number(self):
            self.assertTrue(self.file.validator.test_is_number(2))

        def test_is_number(self):
            self.assertFalse(self.file.validator.test_is_number(-2))

        def test_is_number(self):
            self.assertFalse(self.file.validator.test_is_number("number"))

        def test_is_number(self):
            self.assertFalse(self.file.validator.test_is_number(2))

        # Test is a right Date interval

        def test_validate_format_date(self):
            self.assertEqual(self.validator.Date("002/12/2018"))

        def test_validate_format_date(self):
            self.assertEqual(self.validator.Date("2/2/2018"))

        def test_validate_format_date(self):
            self.assertFalse(self.validator.Date('002/12/2018'))

        def test_validate_format_date(self):
            self.assertFalse(self.validator.Date('-2/12/2018'))

        def test_validate_format_date(self):
            self.assertFalse(self.validator.Date('2018/06/12'))

        def test_validate_format_date(self):
            self.assertFalse(self.validator.Date('12/2018/12'))

        # Test have right extension

        def test_get_the_file_extension(self):
            self.assertEqual(self.validator.get_validator_extension('.txt'))

        # Test have right extension
        def test_get_the_file_extension(self):
            self.assertFalse(self.validator.get_validator_extension(".tx"))

    if _name_ == '_main_':
        unittest.main()


