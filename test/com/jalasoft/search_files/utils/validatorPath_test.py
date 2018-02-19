import unittest
from src.com.jalasoft.search_files.utils.validatorPath import ValidatorPath


class ValidatorPath_test(unittest.TestCase):

    valid = ValidatorPath()

    #Test if path exist in os.
    def test_validate_A_right_path(self):
        name_path = "C:\Program Files (x86)"
        self.assertTrue(self.valid.validate_path(name_path))

    def test_validate_non_valid_path(self):
        name_path = "C:\\Program Files (x86)\holas"
        self.assertFalse(self.valid.validate_path(name_path))

    # Test validate non valid character in path
    def test_validate_non_valid_character_in_path(self):
        name_path = "C:\\Program Files (x86)*"
        self.assertFalse(self.valid.validate_path(name_path))

    def test_validate_non_valid_character_in_path_with_asterisc(self):
        name_path = "C:\Python\Scripts*"
        self.assertFalse(self.valid.validate_path(name_path))

    def test_validate_a_valid_character_in_path(self):
        name_path = "C:\Python\test-test"
        self.assertTrue(self.valid.validate_path(name_path))

    # Test if absolute path exist in os.
    def test_validate_a_right_absulte_path(self):
        absolute_path = "C:\Python\LICENSE.txt"
        self.assertTrue(self.valid.validator_exist_path(absolute_path))

    def test_validate_A_wrong_absulte_path(self):
        absolute_path = "C:\Python\LICENSER.txt"
        self.assertFalse(self.valid.validator_exist_path(absolute_path))

    # Test validate is path is empty
    def test_validate_if_empty_path_is_send(self):
        path = " "
        self.assertFalse(self.valid.validate_path_is_empty(path))

    def test_validate_if_non_empty_path_is_send(self):
        path = "C:\Python\LICENSE.txt"
        self.assertFalse(self.valid.validate_path_is_empty(path))

    def test_validate_if_an_empty_absolute_path_is_send(self):
        path = "..\Python\LICENSE.txt"
        self.assertTrue(self.valid.validate_path_is_empty(path))

    # Test validate if the name_file have the right extension
    def test_validate_if_file_name_have_right_extension_in_path_is_send(self):
        path = "..\Python\LICENSE.txt"
        extesion = ".txt"
        self.assertTrue(self.valid.validate_extension(path, extesion))

    def test_validate_if_file_name_have_invalid_extension_in_path_is_send(self):
        path = "..\Python\LICENSE.txt"
        extesion = ".tx"
        self.assertFalse(self.valid.validate_extension(path, extesion))

if __name__ == "__main__":
	unittest.main()

