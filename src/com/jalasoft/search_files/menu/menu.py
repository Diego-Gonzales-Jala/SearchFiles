import psutil
from SearchCriteria import SearchCriteria, BasicSearch, AdvancedSearch
from src.com.jalasoft.search_files.utils.validator import Validator
from src.com.jalasoft.search_files.search.directory import Directory


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
        self.search = Directory()
        self.search_criteria = SearchCriteria()

    # Print the result of a list
    def print_to_result(self, list_result):
        for dir in list_result:
            print(dir)

    # Enter date range in search_criteria for searching
    def parameter_date_range(self):
        date_range_option = input("Do you want  to search by date range? Y/N: ")
        if date_range_option == 'Y' or date_range_option == 'y':
            start_date = input('Enter start date: e.g. 12-03-2018 (dd-mm-yy): ')
            end_date = input('Enter end date: e.g. 12-03-2018 (dd-mm-yy): ')
            if self.validate_data.validate_format_date(start_date) == True and self.validate_data.validate_format_date(
                    end_date) == True:
                self.search_criteria.set_end_date(start_date)
                self.search_criteria.set_end_date(end_date)

    # Enter create or modified date in search_criteria for searching
    def parameter_date(self):
        file_date_option = input("Do you want  to search by create or update date ? Y/N: ")
        if file_date_option == 'Y' or file_date_option == 'y':
            file_create_date = input('Enter the create date of file: 12-03-2018 (dd-mm-yy): ')
            file_update_date = input('Enter the update date of file: 12-03-2018 (dd-mm-yy): ')
            if self.validate_data.validate_format_date(file_create_date) == True:
                self.search_criteria.set_create_date(file_create_date)
            elif self.validate_data.validate_format_date(file_update_date) == True:
                self.search_criteria.set_modified_date(file_update_date)

    # Return sign value for searching by size criteria
    def sign_value_to_size(self):
        print("Do you want  to search file greather than?, e.g. > 10 enter 1")
        print("Do you want  to search file less than?, e.g 10 < ,enter 2")
        print("Do you want  to search file equal to?, = 10, enter 3")
        option = ''
        file_option = input("Enter the option: ")
        if self.validate_data.is_number(self.sign_option) == True:
            if file_option == 1:
                option = '>'
            elif file_option == 2:
                option = '<'
            elif file_option == 3:
                option = '='
        return option

    # Return  format type of file for searching by size criteria
    def format_type_of_file(self):
        file_format_type = input('Enter the format type of file: e.g. KB, MB,GB: ')
        if file_format_type in self.format_type:
            return file_format_type

    # Enter size criteria in set_size_criteria for searching
    def parameter_size_criteria(self, size_option):
        if size_option == 'Y' or size_option == 'y':
            file_size = input('Enter the file size:')
            sign_value = self.sign_value_to_size()
            format_type = self.format_type_of_file()
            if self.validate_data.is_number(self.file_size) == True:
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
                self.search_by_path()

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
    def search_option_one(self):
        print("Enter following datas for searching or skipping if something is not necessary")

        # Call to enter file name or directory name
        self.parameter_name()

        # Call parameter_path to enter path
        self.parameter_path()

        # Call parameter_owner for entering file owner or directory owner
        self.parameter_owner()

        # Call parameter_extension to enter size
        self.parameter_extension()

        # Call parameter_size_criteria to set paramaters of size criteria
        self.parameter_size_criteria()

        # Call parameter_date_range to enter date range
        self.parameter_date_range()

        # Call parameter_date to enter create or update date
        self.parameter_date()

        print(self.search_criteria.get_dictionary())

    # Advanced search with some criterias to search a file or directory
    # Advanced flag to search is set to 1
    def search_option_two(self):
        self.search_option_one()

    def search_by_option(self, option):
        if self.validate_data.is_number(option) == True:
            if option == 1:
                self.search_option_one()
            elif option == 2:
                self.search_option_two()
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
