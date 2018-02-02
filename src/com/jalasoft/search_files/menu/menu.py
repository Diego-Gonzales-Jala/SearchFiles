import psutil
from SearchCriteria import SearchCriteria
from src.com.jalasoft.search_files.utils.validator import Validator
from src.com.jalasoft.search_files.utils.ValidateOption import ValidateOption
from src.com.jalasoft.search_files.search.directory import Directory


class Util_Disk(object):
      def get_disk(self, option):
          disk_part = psutil.disk_partitions()
          disk = disk_part[option - 1]
          return disk.device

      def get_disk_partition(self):
          disk_partition = psutil.disk_partitions()
          for i in (0, 0):
             partition = disk_partition[i]
             print('{0:2s} {1:3s}'.format(("|"), partition.device))


class Menu:


    def __init__(self):
        self.name_file = ''
        self.path_file = ''
        self.size_file = 0
        self.validate = ValidateOption()
        self.get_disks = Util_Disk()

        self.validate_data = Validator()
        self.search = Directory()
        self.search_criteria = SearchCriteria()

    def print_to_result(self, list_result):
        for dir in list_result:
            print(dir)

    def search_by_date_range(self, date_option):
        if date_option == 'Y' or date_option == 'y':
            start_date = input('Enter start date:')
            end_path = input('Enter end date:')

    def search_by_date(self,file_date_option):
        if file_date_option == 'Y' or file_date_option == 'y':
            file_create_date = input('Enter the create date of file:')
            file_update_date = input('Enter the update date of file:')

    def search_by_size_criteria(self,size_option):
        if size_option == 'Y' or size_option == 'y':
            file_size = input('Enter the file size:')
            file_sign = input('Enter the sign value to search: e.g. >, <, = ')
            file_type_format = input('Enter the format type of file: e.g. KB, MB,GB')
            if self.validate.is_positive(self.file_size) == True:
                self.print_to_result(self.search.search_by_size(self.size_file, self.path_file))
            else:
                print ("Error: Oops!  That was no valid size criteria.  Try again...")

    def search_by_extension(self,file_ext_option):
        if file_ext_option == 'Y' or file_ext_option == 'y':
            file_ext = input('Enter the file extension:')
        #self.search_option_one

    #Basic search with some criterias to search a file or directory
    #Basic flag to search is set to 1
    def search_option_one(self):
        print("Enter following datas for searching or skipping if something is not necessary")
        file_name = input('Enter file name:')
        file_path = input('Enter the path: e.g."C:\\python"')
        file_owner = input('Enter the file owner:')

        option_ext = input("Do you want  to search by date range? Y/N")
        self.search_by_extension(option_ext)

        option_range = input("Do you want  to search by date range? Y/N")
        self.search_by_date_range(option_range)

        option_to_date = input("Do you want  to search by create or update date ? Y/N")
        self.search_by_date(option_to_date)

        if  self.validate_data.validate_name(self.name_file) == True and self.validate_data.validate_path(self.path_file) == True:
            self.print_to_result(self.search.search_by_name(self.name_file, self.path_file))
        else:
            print ("Error: Oops!  That was no valid criteria.  Try again...")

    #Advanced search with some criterias to search a file or directory
    #Advanced flag to search is set to 1
    def search_option_two(self):
         self.search_option_one()

    def search_by_option(self, option):
        if self.validate.is_positive(option) == True:
            if option == 1:
                self.search_option_one()
            elif option == 2:
                self.search_option_two()
        else:
            return "Error : That is not valid option. Try again..."

    def menu_main(self):
        print (" -------------- Search directories and files ----------------------")
        print ("Following devices are available to search :)")
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
                print ("1 - Search Basic")
                print ("2 - Search Advanced")
                option_search_file = (input('Enter option:'))
                self.search_by_option(option_search_file)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


menu_search = Menu()

menu_search.menu_main()
