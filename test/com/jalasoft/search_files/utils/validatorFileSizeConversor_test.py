import unittest
from src.com.jalasoft.search_files.utils.validatorFileSizeConversor import ValidatorFileSizeConversor


class ValidatorTest(unittest.TestCase):


    valid = ValidatorFileSizeConversor()

    # Test validate if the name_file have the right extension
    def test_validate_convert__to_format_type_size_send_into_right(self):
        size_value = "3847653"
        format_type = "KB"
        self.assertTrue(self.valid.convert_to_base(size_value, format_type))

    def test_validate_convert__to_format_type_size_send_into_right(self):
        size_value = "843"
        format_type = "MB"
        self.assertTrue(self.valid.convert_to_base(size_value, format_type))

    def test_validate_convert__to_format_type_size_send_into_right(self):
        size_value = "3847"
        format_type = "GB"
        self.assertTrue(self.valid.convert_to_base(size_value, format_type))


    def test_validate_convert__to_format_type_size_send_into_right(self):
        size_value = "35147"
        format_type = "TB"
        self.assertTrue(self.valid.convert_to_base(size_value, format_type))

    def test_validate_convert__to_format_type_size_send_into_right(self):
        size_value = "325.56"
        format_type = "mb"
        self.assertFalse(self.valid.convert_to_base(size_value, format_type))    


if __name__ == "__main__":
	unittest.main()