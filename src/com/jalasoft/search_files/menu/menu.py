import psutil
import sys
from SearchCriteria import SearchCriteria
from src.com.jalasoft.search_files.utils.validator import Validator
#from src.com.jalasoft.search_files.search.directory import Search
from src.com.jalasoft.search_files.search.search import Search


class Util_Disk(object):

    def get_disk(self, option):
        disk_part = psutil.disk_partitions()
        disk = disk_part[option - 1]
        return disk.device

    #Get disk partition
    def get_disk_partition(self):
        disk_partition = psutil.disk_partitions()
        for i in (0, 0):
            partition = disk_partition[i]
            print('{0:2s} {1:3s}'.format(("|"), partition.device))


class Menu:

    # Builter method of menu
    def __init__(self):
        self.name_file = ''
        self.format_type = ['KB', 'MB', 'GB', 'kb', 'mb', 'gb']
        self.size_file = 0
        # self.validate = ValidateOption()
        self.get_disks = Util_Disk()

        self.validate_data = Validator()
        self.search_criteria = SearchCriteria()
        self.search = Search()
        self.search.set_search_criterial(self.search_criteria)

    # Print the result of a list
    def print_to_result(self, list_result):
        for dir in list_result:
            print(dir)

    # Enter date range in search_criteria for searching
    def parameter_date_range(self):
        date_range_option = input("Do you want  to search by date range? Y/N: ")
        if date_range_option == 'Y' or date_range_option == 'y':
            start_date = input('Enter start date: e.g. 03/12/2018 (mm-dd-yy): ')
            end_date = input('Enter end date: e.g. 03/12/2018 (mm-dd-yy): ')
            if self.validate_data.validate_format_date(start_date) == True and self.validate_data.validate_format_date(
                    end_date) == True:
                self.search_criteria.set_end_date(start_date)
                self.search_criteria.set_end_date(end_date)

    # Enter create or modified date in search_criteria for searching
    def parameter_date(self):
        file_date_option = input("Do you want  to search by create or update date ? Y/N: ")
        if file_date_option == 'Y' or file_date_option == 'y':
            file_create_date = input('Enter the create date of file: 03/12/2018 (mm-dd-yy): ')
            file_update_date = input('Enter the update date of file: 03/12/2018 (mm-dd-yy): ')
            if self.validate_data.validate_format_date(file_create_date) == True:
                self.search_criteria.set_create_date(file_create_date)
            elif self.validate_data.validate_format_date(file_update_date) == True:
                self.search_criteria.set_modified_date(file_update_date)

    # Return sign value for searching by size criteria
    def sign_value_to_size(self):
        print("Do you want  to search file greater than?, e.g. > 10 enter 1")
        print("Do you want  to search file less than?, e.g 10 < ,enter 2")
        print("Do you want  to search file equal to?, = 10, enter 3")
        option = ''
        sign_option = input("Enter the option: ")
        if self.validate_data.is_number(int(sign_option)):
            if int(sign_option) == 1:
                option = '>'
            if int(sign_option) == 2:
                option = '<'
            if int(sign_option) == 3:
                option = '='
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
    def parameter_size_criteria(self ):
        size_option = input("Do you want  to search by file size? Y/N: ")
        if size_option == 'Y' or size_option == 'y':
            file_size = input('Enter the file size:')
            sign_value = self.sign_value_to_size()
            format_type = self.format_type_of_file()

            if self.validate_data.is_number(int(file_size)) == True:
                self.search_criteria.set_file_size(file_size+format_type)
                self.search_criteria.set_size_criteria(sign_value, file_size, format_type)
                # self.print_to_result(self.search.search_by_size(self.size_file, self.path_file))
            else:
                print("Error: Oops!  That was no valid size criteria.  Try again...")

    # Enter file extension in search_criteria for searching
    def parameter_extension(self):
        file_ext_option = input("Do you want  to search by file extension? Y/N: ")
        if file_ext_option == 'Y' or file_ext_option == 'y':
            file_ext = input('Enter the file extension: e.g .txt :')
            if self.validate_data.validate_name(file_ext) == True:
                self.search_criteria.set_extension(file_ext)

    # Enter file/directory path in search_criteria for searching
    def parameter_path(self):
        file_path_option = input("Do you want  to search into path? Y/N: ")
        if file_path_option == 'Y' or file_path_option == 'y':
            file_path = str(input('Enter the path: e.g."C:\\python" : '))
            if self.validate_data.validate_path(file_path) == True:
                self.search_criteria.set_path(file_path)
                # self.print_to_result(self.search.search_by_name(self.name_file, self.path_file))
            else:
                print("Error: Oops!  That was no valid criteria.  Try again...")
                self.parameter_path()

    # Enter file name in search_criteria for searching
    def parameter_name(self):
        file_name_option = input("Do you want  to search by name? Y/N : ")
        if file_name_option == 'Y' or file_name_option == 'y':
            file_name = input('Enter file or directory name: e.g. python or test.xt : ')
            if self.validate_data.validate_name(file_name) == True:
                self.search_criteria.set_file_name(file_name)

    # Enter file/directory owner in search_criteria for searching
    def parameter_owner(self):
        file_owner_option = input("Do you want  to search by file/directoy owner? Y/N : ")
        if file_owner_option == 'Y' or file_owner_option == 'y':
            file_owner = input('Enter the file owner or directory owner: e.g. mario: ')
            if self.validate_data.validate_name(file_owner) == True:
                self.search_criteria.set_file_owner(file_owner)

    # Basic search with some criterias to search a file or directory
    # Basic flag to search is set to 1
    def search_option_basic(self):
        print("Enter following datas for searching or skipping if something is not necessary")
        self.search_criteria.set_search_type(1)
        # Call parameter_path to enter path
        self.parameter_path()

        # Call to enter file name or directory name
        self.parameter_name()

        # Call parameter_owner for entering file owner or directory owner
        self.parameter_owner()

        # Call parameter_extension to enter size
        self.parameter_extension()

        #print(self.search_criteria.get_dictionary())
        try:
            if self.search.search_by_file_name() is not None:
                print("----------------")
                print("Result: search by file name:: ")
                self.print_to_result(self.search.search_by_file_name())
                print("----------------")
            if self.search.search_by_name() is not None:
                print("----------------")
                print("Result: search by name:: ")
                print(self.search.search_by_name())
            if self.search.search_by_extension() is not None:
                print("----------------")
                print("Result: search by extension:: ")
                self.print_to_result(self.search.search_by_extension())
                print("----------------")
            if self.search.get_all_directories(self.search_criteria.get_path()) is not None:
                print("----------------")
                print("Result: search all directories :: ")
                self.print_to_result(self.search.get_all_directories(self.search_criteria.get_path()))
                print("----------------")
            """
            if self.search.get_all_files(self.search_criteria.get_path()) is not None:
                print("----------------")
                print("Result: search all files ::  ")
                self.print_to_result(self.search.get_all_files(self.search_criteria.get_path()))
                print("----------------")
            """
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    # Advanced search with some criteria to search a file or directory
    # Advanced flag to search is set to 1
    def search_option_advanced(self):
        #self.search_option_basic()
        self.search_criteria.set_search_type(2)

        # Call parameter_path to enter path
        self.parameter_path()

        # Call to enter file name or directory name
        self.parameter_name()

        # Call parameter_extension to enter size
        self.parameter_extension()

        # Call parameter_owner for entering file owner or directory owner
        self.parameter_owner()

        # Call parameter_size_criteria to set paramaters of size criteria
        self.parameter_size_criteria()

        # Call parameter_date_range to enter date range
        self.parameter_date_range()

        # Call parameter_date to enter create or update date
        self.parameter_date()

        #      print(self.search_criteria.get_dictionary())
        try:

            if self.search.search_by_file_name() is not None:
                print(self.search.search_by_file_name())
            if self.search.search_by_name() is not None:
                print(self.search.search_by_file_name())
            if self.search.search_by_extension() is not None:
                print(self.search.search_by_extension())

            print(self.search.search_by_file_size())
            if self.search.search_by_file_size() is not None:
                print("----------------")
                print("Result: search by size ::  ")
                self.print_to_result(self.search.search_by_file_size())
            if self.search.search_by_range_date() is not None:
                print("----------------")
                print("Result: search by range ::  ")
                self.print_to_result(self.search.search_by_range_date())
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def search_by_option(self, option):
        if self.validate_data.is_number(option) == True:
            if option == 1:
                self.search_option_basic()
            elif option == 2:
                self.search_option_advanced()
        else:
            return "Error : That is not valid option. Try again..."

    def menu_main(self):
        print(" -------------- Search directories and files ----------------------")
        print("Following devices are available to search :)")
        self.get_disks.get_disk_partition()
        print("-------------------------------------")
        print("If you want you to exit, enter 0 !")
        print("-------------------------------------")
        self.sub_menu()

    def sub_menu(self, catch=None):
        try:
            option_search_file = 10
            while (option_search_file > 0):
                print(' Search file or folder by:')
                print("1 - Search Basic")
                print("2 - Search Advanced")
                option_search_file = int(input('Enter option:'))
                self.search_by_option(option_search_file)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


menu_search = Menu()

menu_search.menu_main()
