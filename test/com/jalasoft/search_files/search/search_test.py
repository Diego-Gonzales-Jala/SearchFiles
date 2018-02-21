import unittest
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.menu.searchcriteria import SearchCriteria


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.search = Search()
        self.search_criterial = SearchCriteria()
        self.path = "C:\Python"

    def test_get_all_the_directories_given_a_path(self):
        self.search_criterial.set_path(self.path)
        list_expected = ['C:\\Python\\dos', 'C:\\Python\\uno']
        self.assertEqual(self.search.get_all_directories(self.search_criterial.get_path()), list_expected)

    def test_is_not_possible_to_get_all_the_directories_when_a_path_is_empty(self):
        self.search_criterial.set_path("")
        expected = "The path does not exist"
        self.assertEqual(self.search.get_all_directories(self.search_criterial.get_path()), expected)

    def test_is_not_possible_to_get_all_the_directories_when_the_path_is_invalid(self):
        self.search_criterial.set_path("C:\Pyth#on")
        expected = "The path is invalid"
        self.assertEqual(self.search.get_all_directories(self.search_criterial.get_path()), expected)

    def test_is_not_possible_to_get_all_the_directories_when_a_path_not_exist(self):
        self.search_criterial.set_path("C:\Python\Python")
        expected = "The path does not exist"
        self.assertEqual(self.search.get_all_directories(self.search_criterial.get_path()), expected)

    def test_get_all_the_files_given_a_path(self):
        self.search_criterial.set_path(self.path)
        list_expected = ['C:\\Python\\2017-11-28 at 11-34-31.mp4',
                         'C:\\Python\\file_hiden.txt',
                         'C:\\Python\\hiden.txt',
                         'C:\\Python\\hoy_test.txt',
                         'C:\\Python\\loca.txt',
                         'C:\\Python\\my file hiden.txt',
                         'C:\\Python\\rayada.txt',
                         'C:\\Python\\tutito.txt']
        self.assertEqual(self.search.get_all_files(self.search_criterial.get_path()), list_expected)

    def test_is_not_possible_to_get_all_the_files_when_a_path_is_empty(self):
        self.search_criterial.set_path("")
        expected = "The files does not was retrieved and the path is empty or not exist"
        self.assertEqual(self.search.get_all_files(self.search_criterial.get_path()), expected)

    def test_get_total_of_the_result_of_a_search(self):
        self.search_criterial.set_path(self.path)
        self.assertEqual(self.search.get_total_search(self.search.get_all_files(self.search_criterial.get_path())), 8)

    def test_get_zero_result_of_a_search_when_returned_empty(self):
        self.search_criterial.set_path("C:\Python\dos")
        self.assertEqual(self.search.get_total_search(self.search.get_all_files(self.search_criterial.get_path())), 0)

    def test_a_path_is_directory(self):
        self.search_criterial.set_path(self.path)
        self.assertTrue(self.search.is_directory(self.search_criterial.get_path()))

    def test_a_path_empty_is_directory(self):
        self.search_criterial.set_path("")
        self.assertFalse(self.search.is_directory(self.search_criterial.get_path()))

    def test_a_path_invalid_is_directory(self):
        self.search_criterial.set_path("C:\Python\china")
        self.assertFalse(self.search.is_directory(self.search_criterial.get_path()))

    def test_set_a_path(self):
        self.search.set_path(self.path)
        self.assertEqual(self.search.get_path(), "C:\\Python")

    def test_get_a_path(self):
        self.search.set_path(self.path)
        self.assertEqual(self.search.get_path(), "C:\\Python")

    def test_a_path_is_file(self):
        self.search_criterial.set_path("C:\Python\hoy_test.txt")
        self.assertTrue(self.search.is_file(self.search_criterial.get_path()))

    def test_a_path_empty_is_file(self):
        self.search_criterial.set_path("")
        self.assertFalse(self.search.is_file(self.search_criterial.get_path()))

    def test_search_by_directory_name(self):
        self.search_criterial.set_path("C:\Python")
        self.search_criterial.set_file_name("o")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['C:\\Python\\dos', 'C:\\Python\\uno']
        self.assertEqual(self.search.search_by_name(), expected)

    def test_search_by_directory_name_when_the_path_is_empty(self):
        self.search_criterial.set_path("")
        self.search_criterial.set_file_name("dos")
        self.search.set_search_criterial(self.search_criterial)
        expected = 'The directory name in the path does not exist'
        self.assertEqual(self.search.search_by_name(), expected)

    def test_search_by_directory_name_when_the_path_is_invalid(self):
        self.search_criterial.set_path("C:\Pyth#on\@luna")
        self.search_criterial.set_file_name("dos")
        self.search.set_search_criterial(self.search_criterial)
        expected = 'The directory name is invalid'
        self.assertEqual(self.search.search_by_name(), expected)

    def test_search_by_directory_name_when_the_path_not_exist(self):
        self.search_criterial.set_path("C:\Python\luna")
        self.search_criterial.set_file_name("dos")
        self.search.set_search_criterial(self.search_criterial)
        expected = 'The directory name in the path does not exist'
        self.assertEqual(self.search.search_by_name(), expected)

    def test_search_by_file_name(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_file_name("libro")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\librostxt.rar','D:\\librostxt\\libro_muertos.txt', 'D:\\librostxt\\libro_pirata_demo.txt']
        self.assertEqual(self.search.search_by_file_name(), expected)

    def test_search_by_file_name_when_the_filename_does_not_exist(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_file_name("luna")
        self.search.set_search_criterial(self.search_criterial)
        expected = []
        self.assertEqual(self.search.search_by_file_name(), expected)

    def test_search_by_file_name_when_the_filename_is_invalid(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_file_name("l#br@")
        self.search.set_search_criterial(self.search_criterial)
        expected = 'The file name is invalid'
        self.assertEqual(self.search.search_by_file_name(), expected)

    def test_search_by_extension(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_extension(".txt")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\ciencia_meditacion.txt',
                    'D:\\librostxt\\cristo_social.txt',
                    'D:\\librostxt\\despertar_hombre.txt',
                    'D:\\librostxt\\libro_muertos.txt',
                    'D:\\librostxt\\libro_pirata_demo.txt']
        self.assertEqual(self.search.search_by_extension(), expected)

    def test_search_by_files_with_extensionof_pdf(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_extension(".pdf")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\t-062_Asha_paper.pdf']
        self.assertEqual(self.search.search_by_extension(), expected)

    def test_search_by_files_extension_when_the_path_is_empty(self):
        self.search_criterial.set_path("")
        self.search_criterial.set_extension(".txt")
        self.search.set_search_criterial(self.search_criterial)
        expected = []
        self.assertEqual(self.search.search_by_extension(), expected)

    def test_search_by_file_size_equal_to_1kb(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_size_criteria("=", 1, "kb")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\libro_pirata_demo.txt']
        self.assertEqual(self.search.search_by_file_size(), expected)

    def test_search_by_file_size_greater_than_to_200kb(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_size_criteria(">=", 200, "kb")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\cristo_social.txt',
                    'D:\\librostxt\\librostxt.rar',
                    'D:\\librostxt\\t-062_Asha_paper.pdf',
                    'D:\\librostxt\\Testing-Bluemix.docx']
        self.assertEqual(self.search.search_by_file_size(), expected)

    def test_search_by_file_size_less_than_to_40kb(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_size_criteria("<=", 40, "kb")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\ciencia_meditacion.txt',
                    'D:\\librostxt\\despertar_hombre.txt',
                    'D:\\librostxt\\libro_pirata_demo.txt']
        self.assertEqual(self.search.search_by_file_size(), expected)

    def test_search_by_file_size_greater_to_900kb(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_size_criteria(">", 900, "kb")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\t-062_Asha_paper.pdf']
        self.assertEqual(self.search.search_by_file_size(), expected)

    def test_search_by_file_size_less_to_10kb(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_size_criteria("<", 20, "kb")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\ciencia_meditacion.txt', 'D:\\librostxt\\libro_pirata_demo.txt']
        self.assertEqual(self.search.search_by_file_size(), expected)

    def test_search_by_string_inside_file(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_file_name("afortunados")
        self.search.set_search_criterial(self.search_criterial)
        expected = {'D:\\librostxt\\cristo_social.txt',
                    'D:\\librostxt\\ciencia_meditacion.txt',
                    'D:\\librostxt\\despertar_hombre.txt',
                    'D:\\librostxt\\libro_pirata_demo.txt',
                    'D:\\librostxt\\libro_muertos.txt'}
        self.assertEqual(self.search.search_by_string_inside_file(), expected)

    def test_search_files_by_creation_in_a_range_date_between_two_dates_20180217_to_20180220(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_create_date("2018/02/17", "2018/02/20")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\librostxt.rar',
                    'D:\\librostxt\\libro_muertos.txt',
                    'D:\\librostxt\\libro_pirata_demo.txt',
                    'D:\\librostxt\\t-062_Asha_paper.pdf',
                    'D:\\librostxt\\Testing-Bluemix.docx']
        self.assertEqual(self.search.search_by_date_range_ctime(), expected)

    def test_search_files_by_creation_in_a_range_date_between_two_dates_20180220_to_20180220(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_create_date("2018/02/20", "2018/02/20")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\librostxt.rar']
        self.assertEqual(self.search.search_by_date_range_ctime(), expected)

    def test_search_files_by_modify_in_a_range_date_between_two_dates_20180208_to_20180209(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_modified_date("2018/02/08", "2018/02/09")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\ciencia_meditacion.txt',
                     'D:\\librostxt\\cristo_social.txt',
                     'D:\\librostxt\\despertar_hombre.txt',
                     'D:\\librostxt\\librostxt.rar',
                     'D:\\librostxt\\libro_muertos.txt']
        self.assertEqual(self.search.search_by_date_range_mtime(), expected)

    def test_search_files_by_modify_in_a_range_date_between_two_dates_20180220_to_20180220(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_modified_date("2018/02/20", "2018/02/20")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\libro_pirata_demo.txt']
        self.assertEqual(self.search.search_by_date_range_mtime(), expected)

    def test_search_files_by_access_in_a_range_date_between_two_dates_20180219_to_20180220(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_access_date("2018/02/19", "2018/02/20")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\librostxt.rar',
                    'D:\\librostxt\\libro_muertos.txt',
                    'D:\\librostxt\\libro_pirata_demo.txt',
                    'D:\\librostxt\\t-062_Asha_paper.pdf',
                    'D:\\librostxt\\Testing-Bluemix.docx']
        self.assertEqual(self.search.search_by_date_range_atime(), expected)

    def test_search_files_by_access_in_a_range_date_between_two_dates_20180209_to_20180209(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_access_date("2018/02/09", "2018/02/09")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\ciencia_meditacion.txt',
                    'D:\\librostxt\\cristo_social.txt',
                    'D:\\librostxt\\despertar_hombre.txt']
        self.assertEqual(self.search.search_by_date_range_atime(), expected)

    def test_search_files_by_owner(self):
        self.search_criterial.set_path("D:\librostxt")
        self.search_criterial.set_file_owner("Diego Gonzales")
        self.search.set_search_criterial(self.search_criterial)
        expected = ['D:\\librostxt\\ciencia_meditacion.txt',
                    'D:\\librostxt\\cristo_social.txt',
                    'D:\\librostxt\\despertar_hombre.txt',
                    'D:\\librostxt\\librostxt.rar',
                    'D:\\librostxt\\libro_muertos.txt',
                    'D:\\librostxt\\libro_pirata_demo.txt',
                    'D:\\librostxt\\t-062_Asha_paper.pdf',
                    'D:\\librostxt\\Testing-Bluemix.docx']
        self.assertEqual(self.search.search_by_owner(), expected)


if __name__ == '__main__':
    unittest.main()