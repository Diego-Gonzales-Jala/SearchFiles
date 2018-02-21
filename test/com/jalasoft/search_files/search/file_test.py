import unittest
from src.com.jalasoft.search_files.search.file import File


class FileTest(unittest.TestCase):

    def setUp(self):
        self.file = File()
        self.path = "D:\librostxt"

    def test_get_file_path(self):
        self.file.set_file_path(self.path + "\cristo_social.txt")
        expected = 'D:\librostxt\\cristo_social.txt'
        self.assertEqual(self.file.get_file_path(), expected, "This file path is incorrect")

    def test_get_the_file_name(self):
        self.file.set_file_path(self.path + "\cristo_social.txt")
        expected = 'cristo_social.txt'
        self.assertEqual(self.file.get_file_name(), expected, "This file name is incorrect")

    def test_get_the_file_extension(self):
        self.file.set_file_path(self.path + "\cristo_social.txt")
        expected = '.txt'
        self.assertEqual(self.file.get_file_extension(), expected, "This file extension is incorrect")

    def test_get_the_file_size(self):
        self.file.set_file_path("D:\librostxt\cristo_social.txt")
        expected = 468861
        self.assertEqual(self.file.get_file_size(), expected, "This file size is incorrect")

    def test_is_file(self):
        self.file.set_file_path(self.path + "\cristo_social.txt")
        self.assertTrue(self.file.is_file())

    def test_set_a_new_path(self):
        self.file.set_file_path("C:\Python")
        expected = "C:\\Python"
        self.assertEqual(self.file.get_file_path(), expected)


if __name__ == '__main__':
    unittest.main()