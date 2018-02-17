import unittest
from src.com.jalasoft.search_files.utils.validatorPath import ValidatorPath


class ValidatorTest(unittest.TestCase):

    valid = ValidatorPath()

    def name_path(self):
        self.name_path = path("C:\\Program Files (x86)")

    # Test there is a right path.
    def test_validate_A_right_path(self):
        self.assertEqual(self.valid.name_path("C:\\Program Files (x86)"))

    def test_validate_non_valid_character_in_path(self):
        self.assertFalse(self.valid.name_path("C:\\Program Files* (x86)*"))

    def test_validate_non_valid_path(self):
        self.assertFalse(self.valid.name_path("C:\\Program Files* (x86)\hola"))