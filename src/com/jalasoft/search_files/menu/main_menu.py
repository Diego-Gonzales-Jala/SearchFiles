from src.com.jalasoft.search_files.menu.menu import MenuParameter
from src.com.jalasoft.search_files.menu.util_disk import UtilDisk
from src.com.jalasoft.search_files.utils.validatorNumber import ValidatorNumber
from src.com.jalasoft.search_files.utils.logging_search import logger

class MainMenu():

    validate_number = ValidatorNumber()
    menu_option = MenuParameter()
    get_disks = UtilDisk()

    # Enter basic or advanced option to search a file with some parameters
    def search_by_option(self, option):
        if self.validate_number.is_number(option):
            logger.info("search_by_option: Enter basic or advanced search")
            if option == 1:
                self.menu_option.search_option_basic()
            elif option == 2:
                self.menu_option.search_option_advanced()
            elif option == 3:
                logger.info("search_by_option: Reading LEEME.txt")
                f = open('LEEME.txt', 'r')
                print("Reading...")
                print("----------------------------------------------------------------------")
                print(f.read())
                print("----------------------------------------------------------------------")
                f.close()
        else:
            return "Error : That is not valid option. Try again..."

    # Main method , call submenu  with search options
    def menu_main(self):
        print(" -------------- Search directories and files ----------------------")
        print("Following devices are available to search :)")
        self.get_disks.get_disk_partition()
        print("-------------------------------------")
        print("If you want you to exit, enter 0 !")
        print("-------------------------------------")
        self.sub_menu()

    #Display the options for searching
    def sub_menu(self, catch=None):
        try:
            option_search_file = 10
            while (option_search_file > 0):
                print('Search file or folder by: ')
                print("1 - Search Basic")
                print("2 - Search Advanced")
                print("3 - About Search File")
                option_search_file = int(input('Enter option:'))
                self.search_by_option(option_search_file)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


menu_search = MainMenu()
menu_search.menu_main()