import psutil
import sys
from src.com.jalasoft.search_files.menu.SearchCriteria import SearchCriteria
#from FilterMenu import FilterMenu
#from src.com.jalasoft.search_files.utils.validator import Validator
from src.com.jalasoft.search_files.utils.validatorDate import ValidatorDate
from src.com.jalasoft.search_files.utils.validatorFileSizeConversor import ValidatorFileSizeConversor
from src.com.jalasoft.search_files.utils.ValidatorNumber import ValidatorNumber
from src.com.jalasoft.search_files.utils.validatorPath import ValidatorPath
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.utils.logging import logger

class Util_Disk(object):

    def get_disk(self, option):
        logger.info("get disk: Enter")
        disk_part = psutil.disk_partitions()
        disk = disk_part[option - 1]
        logger.info("get_disk: Load disk")
        return disk.device

    #Get disk partition
    def get_disk_partition(self):
        logger.info("get disk partition: Enter")
        disk_partition = psutil.disk_partitions()
        for i in (0, 0):
            partition = disk_partition[i]
            print('{0:2s} {1:3s}'.format(("|"), partition.device))
        logger.info("get_disk: Load disk")

class MenuParameter:

    # Builter method of menu parameter
    def __init__(self):
        self.name_file = ''
        self.format_type = ['KB', 'MB', 'GB', 'kb', 'mb', 'gb']
        self.size_file = 0
        # self.validate = ValidateOption()
        self.get_disks = Util_Disk()

        self.validate_date = ValidatorDate()
        self.validate_number = ValidatorNumber()
        self.validate_path = ValidatorPath()
        self.conversor_size = ValidatorFileSizeConversor()
        self.search_criteria = SearchCriteria()
        #self.filter = FilterMenu()
        self.search = Search()
        self.search.set_search_criterial(self.search_criteria)

    # Print the result of a list
    def print_to_result(self, list_result):
        for dir in list_result:
            print(dir)

    def option_parameter_by_date(self):
        print("Do you want  to search file by create date?,  enter 1")
        print("Do you want  to search file by modified date?, enter 2")
        print("Do you want  to search file by access date?, enter 3")
        option_type_d = int(input('Enter option:'))
        if self.validate_number.is_number(option_type_d) == True:
            if option_type_d == 1:
                start_date_c = input('Enter start date: e.g. 2018/02/15 (yyyy-mm-dd): ')
                end_date_c = input('Enter end date: e.g. 2018/02/15 (yyyy-mm-dd): ')
                if start_date_c != '' and end_date_c != '':
                    self._parameter_create_date_by_date_range_(start_date_c,end_date_c)
            elif option_type_d == 2:
                start_date_m = input('Enter start date: e.g. 2018/02/15 (yyyy-mm-dd): ')
                end_date_m = input('Enter end date: e.g. 2018/02/15 (yyyy-mm-dd): ')
                if start_date_m != '' and end_date_m != '':
                    self._parameter_modified_date_by_date_range_(start_date_m,end_date_m)
            elif option_type_d == 3:
                start_date_a = input('Enter start date: e.g. 2018/02/15 (yyyy-mm-dd): ')
                end_date_a = input('Enter end date: e.g. 2018/02/15 (yyyy-mm-dd): ')
                if start_date_a != '' and end_date_a != '':
                    self._parameter_access_date_by_date_range_(start_date_a,end_date_a)
            else:
                print("Error: Oops!  That was no valid option.  Try again...")

    def parameter_file_content(self,string):
        if string != '':
            self.search_criteria.set_word_into_file(string)

    # Enter create date by date range in search_criteria for searching
    def _parameter_create_date_by_date_range_(self,start_date,end_date):
        logger.info("parameter_create_date_by_date_range: Enter")
        if self.validate_date.validate_format_date(start_date) == True and self.validate_date.validate_format_date(end_date) == True:
            self.search_criteria.set_create_date(start_date,end_date)
            logger.info("parameter_create_date_by_date_range: Load date range in dictionary")
        else:
            print("Error: Oops!  That was no valid date.  Try again...")

    # Enter create date by date range in search_criteria for searching
    def _parameter_modified_date_by_date_range_(self, start_date, end_date):
        logger.info("parameter_modified_date_by_date_range: Enter")
        if self.validate_date.validate_format_date(start_date) == True and self.validate_date.validate_format_date(end_date) == True:
            self.search_criteria.set_modified_date(start_date, end_date)
            logger.info("parameter_modified_date_by_date_range: Load date range in dictionary")
        else:
                print("Error: Oops!  That was no valid date.  Try again...")

    # Enter create date by date range in search_criteria for searching
    def _parameter_access_date_by_date_range_(self, start_date, end_date):
        logger.info("parameter_access_date_by_date_range: Enter")
        if self.validate_date.validate_format_date(start_date) == True and self.validate_date.validate_format_date(end_date) == True:
                self.search_criteria.set_access_date(start_date, end_date)
                logger.info("parameter_access_date_by_date_range: Load date range in dictionary")
        else:
                print("Error: Oops!  That was no valid date.  Try again...")

    # Return sign value for searching by size criteria
    def sign_value_to_size(self):
        print("Do you want  to search file greater than?, e.g. > 10 enter 1")
        print("Do you want  to search file less than?, e.g 10 < ,enter 2")
        print("Do you want  to search file equal to?, = 10, enter 3")
        print("Do you want  to search file less than and equal to?, <= 10, enter 4")
        print("Do you want  to search file greter than and equal to?, >= 10, enter 5")
        option = ''
        logger.info("sign_value_to_size: Enter")
        sign_option = input("Enter the option: ")
        if self.validate_number.is_number(sign_option):
            if int(sign_option) == 1:
                option = '>'
            if int(sign_option) == 2:
                option = '<'
            if int(sign_option) == 3:
                option = '='
            if int(sign_option) == 4:
                option = '<='
            if int(sign_option) == 5:
                option = '>='
            logger.info("sign_value_to_size: return sign value")
        return option

    # Return  format type of file for searching by size criteria
    def format_type_of_file(self):
        file_format_type = input('Enter the format type of file: e.g. KB, MB,GB: ')
        result = ""
        for type in self.format_type:
            if file_format_type == type:
                result = type
        return result

    # Enter size criteria in set_size_criteria for searching
    def parameter_size_criteria(self):
        size_option = input("Do you want  to search by file size? Y/N: ")
        if size_option == 'Y' or size_option == 'y':
            file_size = input('Enter the file size:')
            sign_value = self.sign_value_to_size()
            format_type = self.format_type_of_file()
            logger.info("parameter_size_criteria: Enter")
            if self.validate_number.is_number(file_size):
                self.search_criteria.set_size_criteria(sign_value, file_size, format_type)
                # self.print_to_result(self.search.search_by_size(self.size_file, self.path_file))
                logger.info("parameter_date_range: Load size criteria  in dictionary")
            else:
                print("Error: Oops!  That was no valid size criteria.  Try again...")
                self.parameter_size_criteria()

    # Enter file extension in search_criteria for searching
    def parameter_extension(self,file_ext):
        if file_ext != '':
            logger.info("parameter_extension: Enter")
            if self.validate_path.validate_name(file_ext) == True:
                self.search_criteria.set_extension(file_ext)
                logger.info("parameter_date_range: Load file extension  in dictionary")
            else:
                print("Error: Oops!  That was no valid size criteria.  Try again...")

    # Enter file/directory path in search_criteria for searching
    def parameter_path(self,file_path):
        if file_path != '':
            logger.info("parameter_path: Enter")
            if self.validate_path.validate_path(file_path):
                self.search_criteria.set_path(file_path)
                logger.info("parameter_path: Load file path in dictionary")
                # self.print_to_result(self.search.search_by_name(self.name_file, self.path_file))
            else:
                print("Error: Oops!  That was no valid criteria.  Try again...")
        else:
            self.search_criteria.set_path("C:\\test")


    # Enter file name in search_criteria for searching
    def parameter_name(self, file_name):
        if file_name != '':
            logger.info("parameter_name: Enter")
            if self.validate_path.validate_name(file_name):
                self.search_criteria.set_file_name(file_name)
                logger.info("parameter_name: Load file name in dictionary")
            else:
                print("Error: Oops!  That was no valid name.  Try again...")

    # Enter file/directory owner in search_criteria for searching
    def parameter_owner(self,file_owner):
        if file_owner != '':
            if self.validate_path.validate_name(file_owner):
                self.search_criteria.set_file_owner(file_owner)
            else:
                print("Error: Oops!  That was no valid name.  Try again...")

    def filter_basic_search(self):
        if self.search_criteria.get_path() != '' and self.search_criteria.get_file_name() == '' and self.search_criteria.get_file_owner() == '' and self.search_criteria.get_extension() == '':
            print("----------------")
            print("Result: search all files ::  ")
            self.print_to_result(self.search.get_all_files(self.search_criteria.get_path()))
            print("----------------")

        if self.search_criteria.get_file_name() != '':
                    print("----------------")
                    print("Result: search by  name:: ")
                    self.print_to_result(self.search.search_by_file_name())
                    self.print_to_result(self.search.search_by_name())
                    print("----------------")
        if self.search_criteria.get_file_owner() != '':
                    print("----------------")
                    print("Result: search by file owner:: ")
                    print(self.search.search_by_owner())
                    print("----------------")
        if self.search_criteria.get_extension() != '':
                    print("----------------")
                    print("Result: search by file extension:: ")
                    self.print_to_result(self.search.search_by_extension())
                    print("----------------")

    # Basic search with some criterias to search a file or directory
    # Basic flag to search is set to 1
    def search_option_basic(self):
        print("Enter following datas for searching or skipping if something is not necessary")
        self.search_criteria.set_search_type(1)
        # Call parameter_path to enter path
        file_path = str(input('Enter the path: e.g."C:\\python" : '))
        self.parameter_path(file_path)

        # Call to enter file name or directory name
        file_name = input('Enter file or directory name: e.g. python or test.xt : ')
        self.parameter_name(file_name)

        # Call parameter_owner for entering file owner or directory owner
        file_owner = input('Enter the file owner or directory owner: e.g. mario: ')
        self.parameter_owner(file_owner)

        # Call parameter_extension to enter size
        file_ext = input('Enter the file extension: e.g .txt :')
        self.parameter_extension(file_ext)

        #print(self.search_criteria.get_dictionary())
        try:
            print("Starting to search... ")
            self.filter_basic_search()

        except:
            print("Unexpected error:", sys.exc_info()[0])
            #raise

    # Advanced search with some criteria to search a file or directory
    # Advanced flag to search is set to 1
    def search_option_advanced(self):
        #self.search_option_basic()
        self.search_criteria.set_search_type(2)

        # Call parameter_path to enter path
        file_path = str(input('Enter the path: e.g."C:\\python" : '))
        self.parameter_path(file_path)

        # Call parameter_size_criteria to set paramaters of size criteria
        self.parameter_size_criteria()

        # Call option_parameter_by_date to enter date range by create/modified/access date of file
        self.option_parameter_by_date()

        # Call parameter_date to enter create or update date
        file_content_to_search = str(input('Enter the word to search into file: e.g."memet" : '))
        self.parameter_file_content(file_content_to_search)

        #      print(self.search_criteria.get_dictionary())
        try:

            print("Starting to search... ")
            # Search files by create date
            if self.search_criteria.get_create_date_start() != '':
                print("----------------")
                print("Result: search file by create date ::  ")
                self.print_to_result(self.search.search_by_date_range_ctime())

            # Search files by access date
            if self.search_criteria.get_modified_date_start() != '':
                print("----------------")
                print("Result: search file by modified date ::  ")
                self.print_to_result(self.search.search_by_date_range_mtime())

            # Search files by create date
            if self.search_criteria.get_access_date_start() != '':
                print("----------------")
                print("Result: search file by access date ::  ")
                self.print_to_result(self.search.search_by_date_range_atime())

            # Search files by create date
            if self.search_criteria.get_size_criteria()[0] != '':
                print("----------------")
                print("Result: search file by size ::  ")
                self.print_to_result(self.search.search_by_file_size())

            if self.search_criteria.get_word_into_file() != '':
                print("----------------")
                print("Result: search by content into file ::  ")
                #self.print_to_result(self.search.search_by_string_inside_file())
                self.search.search_by_string_inside_file()

        except:
            print("Unexpected error:", sys.exc_info()[0])
            #raise

    def search_by_option(self, option):
        if self.validate_number.is_number(option):
            if option == 1:
                self.search_option_basic()
            elif option == 2:
                self.search_option_advanced()
        else:
            return "Error : That is not valid option. Try again..."
