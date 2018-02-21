import unittest
from src.com.jalasoft.search_files.search.directory import Directory


class DirectoryTest(unittest.TestCase):

    def setUp(self):
        self.directory = Directory()
        self.path = "D:\librostxt"

    def test_get_directory_path(self):
        self.directory.set_dir_path(self.path)
        expected = "D:\\librostxt"
        self.assertEqual(self.directory.get_dir_path(), expected)

    def test_get_the_directory_name(self):
        self.directory.set_dir_path(self.path)
        expected = "librostxt"
        self.assertEqual(self.directory.get_dir_name(), expected)

    def test_get_the_directory_size(self):
        self.directory.set_dir_path(self.path)
        expected = 2621443
        self.assertEqual(self.directory.get_dir_size(), expected)

    def test_is_directory(self):
        self.directory.set_dir_path(self.path)
        self.assertTrue(self.directory.is_directory(self.directory.get_dir_path()))


if __name__ == '__main__':
    unittest.main()