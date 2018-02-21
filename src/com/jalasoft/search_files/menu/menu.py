import sys
import os
import time
import win32api
import win32con
import win32security
from src.com.jalasoft.search_files.menu.searchcriteria import SearchCriteria
from src.com.jalasoft.search_files.menu.util_disk import UtilDisk
from src.com.jalasoft.search_files.utils.validatorDate import ValidatorDate
from src.com.jalasoft.search_files.utils.validatorFileSizeConversor import ValidatorFileSizeConversor
from src.com.jalasoft.search_files.utils.validatorNumber import ValidatorNumber
from src.com.jalasoft.search_files.utils.validatorPath import ValidatorPath
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.utils.logging_search import logger


class MenuParameter:

    # Builter method of menu parameter
    def __init__(self):
        self.name_file = ''
        self.format_type = ['KB', 'MB', 'GB', 'kb', 'mb', 'gb']
        self.format_sign_value = ['>', '<' , '=' , '<=' , '>=' ]
        self.get_disks = UtilDisk()

        self.validate_date = ValidatorDate()
        self.validate_number = ValidatorNumber()
        self.validate_path = ValidatorPath()
        self.conversor_size = ValidatorFileSizeConversor()
        self.search_criteria = SearchCriteria()
        self.search = Search()
        self.search.set_search_criterial(self.search_criteria)


    # Print the result of a list
    def print_to_result(self, list_result):
        print('{0:20s} {1:10s}{2:16s}          {3:20}        {4:35}'.format("File Name", "size-KB", "Created", "Last modified", "Last accessed"))
        print(
            "=================================================================================================================================")
        for dir in list_result:
            self.print_values_of_file_basic_search(dir)
        print(
            "===================================================================================================================================")

    # Check if start_date_c or/and end_date_c are empty and send to parameter_create_date_by_date_range_
    def _create_date_for_dictionary_(self,start_date_c,end_date_c):
        if start_date_c != '' and end_date_c != '':
            self.parameter_create_date_by_date_range_(start_date_c, end_date_c)
        elif start_date_c != '' and end_date_c == '':
            self.parameter_create_date_by_date_range_(start_date_c, start_date_c)
        elif start_date_c == '' and end_date_c != '':
            self.parameter_create_date_by_date_range_(end_date_c, end_date_c)

    # Check if start_date_m or/and end_date_m are empty and send to parameter_modified_date_by_date_range_
    def _modified_date_for_dictionary_(self, start_date_m, end_date_m):
        if start_date_m != '' and end_date_m != '':
            self.parameter_modified_date_by_date_range_(start_date_m, end_date_m)
        elif start_date_m != '' and end_date_m == '':
            self.parameter_modified_date_by_date_range_(start_date_m, start_date_m)
        elif start_date_m == '' and end_date_m != '':
            self.parameter_modified_date_by_date_range_(end_date_m, end_date_m)

    # Check if start_date_a or/and end_date_a are empty and send to parameter_access_date_by_date_range_
    def _access_date_for_dictionary_(self, start_date_a, end_date_a):
        if start_date_a != '' and end_date_a != '':
            self.parameter_access_date_by_date_range_(start_date_a, end_date_a)
        elif start_date_a != '' and end_date_a == '':
            self.parameter_access_date_by_date_range_(start_date_a, start_date_a)
        elif start_date_a == '' and end_date_a != '':
            self.parameter_access_date_by_date_range_(end_date_a, end_date_a)

    # Enter option for searching by date and this call date range
    def option_parameter_by_date(self):
        start_date_c = input('Enter start date: e.g. 2018/02/15 (yyyy-mm-dd): ')
        end_date_c = input('Enter end date: e.g. 2018/02/15 (yyyy-mm-dd): ')
        self._create_date_for_dictionary_(start_date_c,end_date_c)

        start_date_m = input('Enter start date: e.g. 2018/02/15 (yyyy-mm-dd): ')
        end_date_m = input('Enter end date: e.g. 2018/02/15 (yyyy-mm-dd): ')
        self._modified_date_for_dictionary_(start_date_m,end_date_m)

        start_date_a = input('Enter start date: e.g. 2018/02/15 (yyyy-mm-dd): ')
        end_date_a = input('Enter end date: e.g. 2018/02/15 (yyyy-mm-dd): ')
        self._access_date_for_dictionary_(start_date_a,end_date_a)

    # Insert string for searching into dictionary
    def parameter_file_content(self,string):
        if string != '':
            self.search_criteria.set_word_into_file(string)

    # Enter create date by date range in search_criteria for searching
    def parameter_create_date_by_date_range_(self,start_date,end_date):
        logger.info("parameter_create_date_by_date_range: Enter")
        if self.validate_date.validate_format_date(start_date) == True and self.validate_date.validate_format_date(end_date) == True:
            self.search_criteria.set_create_date(start_date,end_date)
            logger.info("parameter_create_date_by_date_range: Load date range in dictionary")
        else:
            print("Error: Oops!  That was no valid date.  Try again...")

    # Enter create date by date range in search_criteria for searching
    def parameter_modified_date_by_date_range_(self, start_date, end_date):
        logger.info("parameter_modified_date_by_date_range: Enter")
        if self.validate_date.validate_format_date(start_date) == True and self.validate_date.validate_format_date(end_date) == True:
            self.search_criteria.set_modified_date(start_date, end_date)
            logger.info("parameter_modified_date_by_date_range: Load date range in dictionary")
        else:
                print("Error: Oops!  That was no valid date.  Try again...")

    # Enter create date by date range in search_criteria for searching
    def parameter_access_date_by_date_range_(self, start_date, end_date):
        logger.info("parameter_access_date_by_date_range: Enter")
        if self.validate_date.validate_format_date(start_date) == True and self.validate_date.validate_format_date(end_date) == True:
                self.search_criteria.set_access_date(start_date, end_date)
                logger.info("parameter_access_date_by_date_range: Load date range in dictionary")
        else:
                print("Error: Oops!  That was no valid date.  Try again...")

    # Return sign value for searching by size criteria
    def sign_value_to_size(self):
        print("Do you want  to search file greater than, less than, equal to, less than and equal to, greater than and equal to?, e.g. > 10")
        sign_option = input(" >, < , = , <= , >= : enter:: ")
        option = ''
        logger.info("sign_value_to_size: Enter")
        for type in self.format_sign_value:
            if str(sign_option) in type:
                option = str(sign_option)
            else:
                option = '='
            logger.info("sign_value_to_size: return sign value")
        return option

    # Return  format type of file for searching by size criteria
    def format_type_of_file(self):
        file_format_type = input('Enter the format type of file: e.g. KB, MB,GB: ').lower()
        result = ""
        for type in self.format_type:
            if file_format_type == type:
                result = type
            else:
                result = 'kb'
        return result

    # Enter size criteria in set_size_criteria for searching
    def parameter_size_criteria(self):
            file_size = input('Enter the file size:')
            sign_value = self.sign_value_to_size()
            format_type = self.format_type_of_file()
            logger.info("parameter_size_criteria: Enter")
            if self.validate_number.is_number(file_size):
                self.search_criteria.set_size_criteria(sign_value, file_size, format_type)
                logger.info("parameter_size_criteria: Load size criteria  in dictionary")
            else:
                logger.info("parameter_size_criteria: error file size ")
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

    def print_values_of_file_basic_search(self,dir):
        file_name = os.path.basename(dir)
        #sd = win32security.GetFileSecurity(file_name, win32security.OWNER_SECURITY_INFORMATION)
        #owner_sid = sd.GetSecurityDescriptorOwner()
        #name, domain, type = win32security.LookupAccountSid(None, owner_sid)
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dir)
        file_size = self.conversor_size.convert_bytes_in_base_data(size,'KB')
        print('{0:20} {1:7}   {2:19}   {3:18}    {4:18}'.format(file_name,file_size, time.ctime(ctime), time.ctime(mtime),time.ctime(atime)))

    # Filter some parameters in base file name, file extension, file owner with path
    def filter_basic_search(self):
        list_basic = self.search.search_filter_criterial(self.search_criteria, self.search_criteria.get_search_type())
        print('{0:20s} {1:10s}{2:16s}          {3:20}        {4:35}   {5:7}'.format("File Name", "size-KB", "Created", "Last modified", "Last accessed", "Owner"))
        print("=================================================================================================================================")
        for i in list_basic:
            self.print_values_of_file_basic_search(i)
        print("===================================================================================================================================")

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

        try:
            print("Starting to search... ")
            self.filter_basic_search()

        except Exception:
            logger.error("Unexpected errors", sys.exc_info()[0])
            print("Unexpected error:", "search_option_basic")

    # Advanced search with some criteria to search a file or directory
    # Advanced flag to search is set to 1
    def search_option_advanced(self):
        print("Enter following datas for searching or skipping if something is not necessary")
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

            # Search files by content
            if self.search_criteria.get_word_into_file() != '':
                print("----------------")
                print("Result: search by content into file ::  ")
                self.print_to_result(self.search.search_by_string_inside_file())
                #self.search.search_by_string_inside_file()

        except Exception:
            #logger.error("Unexpected errors" ,sys.exc_info()[0])
            print("Unexpected error:", "search_option_advanced")

    # Call basic or advanced option to set parameters for searching
    def search_by_option(self, option):
        if self.validate_number.is_number(option):
            if option == 1:
                self.search_option_basic()
            elif option == 2:
                self.search_option_advanced()
        else:
            return "Error : That is not valid option. Try again..."
