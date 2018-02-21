import unittest
from src.com.jalasoft.search_files.menu.menu import MenuParameter
from src.com.jalasoft.search_files.menu.searchcriteria import SearchCriteria


class SearchCriteriaTest(unittest.TestCase):

    search_criteria_t = SearchCriteria()
    menu_parameter = MenuParameter()

    def test_is_instance_of_search_criteria(self):
        self.assertIsInstance(self.search_criteria_t,SearchCriteria)

    def test_is_instance_of_menu_parameter(self):
        self.assertIsInstance(self.menu_parameter, MenuParameter)

    def test_set_size_criteria_with_valid_parameter(self):
        self.search_criteria_t.set_size_criteria('=',10,'mb')
        self.assertEqual('=',self.search_criteria_t.get_size_criteria()[0])
        self.assertEqual(10, self.search_criteria_t.get_size_criteria()[1])
        self.assertEqual('mb', self.search_criteria_t.get_size_criteria()[2])

    def test_lengh_size_criteria_equal_to_three(self):
        self.search_criteria_t.set_size_criteria('=', 10, 'mb')
        self.assertEqual(3, len(self.search_criteria_t.get_size_criteria()))

    def test_set_file_name_into_dictionary_with_valid_parameter(self):
        self.search_criteria_t.set_file_name('map.sdf')
        self.assertEqual('map.sdf',self.search_criteria_t.get_file_name())

    def test_set_file_path_with_valid_parameter(self):
        self.search_criteria_t.set_path('D:\materias\JALA\python\devFund2_py\\ui2')
        self.assertEqual( 'D:\materias\JALA\python\devFund2_py\\ui2', self.search_criteria_t.get_path())

    def test_set_file_extension_with_valid_parameter(self):
        self.search_criteria_t.set_extension('.txt')
        self.assertEqual('.txt' , self.search_criteria_t.get_extension())

    def test_set_create_date_of_file_by_range_into_dictionary(self):
        create_date_start = "2018/12/12"
        create_date_end = "2018/12/14"
        self.search_criteria_t.set_create_date(create_date_start,create_date_end)
        self.assertEqual("2018/12/12",self.search_criteria_t.get_create_date_start())
        self.assertEqual("2018/12/14", self.search_criteria_t.get_create_date_end())

    def test_set_modified_date_of_file_by_range_into_dictionary(self):
        create_date_start = '2018/12/12'
        create_date_end = '2018/12/14'
        self.search_criteria_t.set_modified_date(create_date_start, create_date_end)
        self.assertEqual('2018/12/12',self.search_criteria_t.get_modified_date_start())
        self.assertEqual('2018/12/14', self.search_criteria_t.get_modified_date_end())

    def test_set_access_date_of_file_by_range_into_dictionary(self):
        create_date_start = '2018/12/12'
        create_date_end = '2018/12/14'
        self.search_criteria_t.set_access_date(create_date_start, create_date_end)
        start_s = self.search_criteria_t.get_access_date_start()
        end_s = self.search_criteria_t.get_access_date_end()
        self.assertEqual(create_date_start, start_s)
        self.assertEqual(create_date_end, end_s)

    def test_set_file_name_with_valid_parameter_and_without_extension(self):
        self.search_criteria_t.set_file_name('test')
        name = str(self.search_criteria_t.get_file_name())
        self.assertEqual('test', name)

    def test_set_file_name_with_valid_parameter_and_with_extension(self):
        self.search_criteria_t.set_file_name('nani.txt')
        name = str(self.search_criteria_t.get_file_name())
        self.assertEqual('nani.txt',name)

    def test_set_file_owner_with_valid_parameter(self):
        self.search_criteria_t.set_file_owner('Administrators')
        owner = str(self.search_criteria_t.get_file_owner())
        self.assertEqual('Administrators', owner)

    def test_set_search_type_for_searching(self):
        self.search_criteria_t.set_search_type(1)
        self.assertEqual(1, self.search_criteria_t.get_search_type())

    def test_set_content_of_file_for_searching(self):
        self.search_criteria_t.set_word_into_file('maria')
        self.assertEqual('maria', self.search_criteria_t.get_word_into_file())

    def test_get_all_data_of_dictionary(self):
        create_date_start = '2018/12/12'
        create_date_end = '2018/12/14'
        self.search_criteria_t.set_search_type(1)
        self.search_criteria_t.set_path('D:\materias\JALA\python\devFund2_py\\ui2')
        self.search_criteria_t.set_file_owner('Administrators')
        self.search_criteria_t.set_file_name('nani.txt')
        self.search_criteria_t.set_extension('.txt')
        self.search_criteria_t.set_create_date(create_date_start, create_date_end)
        self.search_criteria_t.set_access_date(create_date_start, create_date_end)
        self.search_criteria_t.set_modified_date(create_date_start, create_date_end)
        self.search_criteria_t.set_word_into_file('comments')
        self.assertEqual({
                "search_type": 1,
                "file_name": 'nani.txt',
                "path": 'D:\materias\JALA\python\devFund2_py\\ui2',
                "owner": 'Administrators',
                "create_date": {"c_start_date": '2018/12/12', "c_end_date": '2018/12/14'},
                "modified_date": {"m_start_date": '2018/12/12', "m_end_date": '2018/12/14'},
                "access_date": {"a_start_date": '2018/12/12', "a_end_date": '2018/12/14'},
                "file_extension": '.txt',
                "word_into_file": 'comments'}, self.search_criteria_t.get_dictionary())

    def test_get_array_of_size_criteria(self):
        self.search_criteria_t.set_size_criteria('=', 10, 'mb')
        self.assertEqual(['=',10,'mb'],self.search_criteria_t.get_size_criteria())


if __name__ == "__main__":
	unittest.main()