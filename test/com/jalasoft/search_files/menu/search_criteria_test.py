import unittest
from src.com.jalasoft.search_files.menu.menu import MenuParameter
from src.com.jalasoft.search_files.menu.SearchCriteria import SearchCriteria

class SearchCriteriaTest(unittest.TestCase):

    search_criteria_t = SearchCriteria()
    menu_parameter = MenuParameter()


    def test_is_instance_of_search_criteria(self):
        self.assertIsInstance(self.search_criteria_t,SearchCriteria)

    def test_is_instance_of_menu_parameter(self):
        self.assertIsInstance(self.menu_parameter,MenuParameter)

    def test_set_file_name_into_dictionary(self):
        self.assertEqual(self.menu_parameter.parameter_name('map.sdf'),self.search_criteria_t.get_file_name())

    def test_get_size_criteria(self):
        self.search_criteria_t.set_size_criteria('=',10,'mb')
        self.assertEqual(3, len(self.search_criteria_t.get_size_criteria()))
        self.assertEqual('=',self.search_criteria_t.get_size_criteria()[0])
        self.assertEqual(10, self.search_criteria_t.get_size_criteria()[1])
        self.assertEqual('mb', self.search_criteria_t.get_size_criteria()[2])

    def test_set_file_path(self):
        self.assertEqual(self.menu_parameter.parameter_path('D:\materias\JALA\python\devFund2_py\\ui2') , self.search_criteria_t.get_path())

    def test_set_file_extension(self):
        self.assertEqual(self.menu_parameter.parameter_extension('.txt') , self.search_criteria_t.get_extension())




if __name__ == "__main__":
	unittest.main()

