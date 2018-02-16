from menu import MenuParameter
from menu import Util_Disk
from src.com.jalasoft.search_files.utils.ValidatorNumber import ValidatorNumber
from src.com.jalasoft.search_files.utils.logging import logger

class MainMenu():
    validate_number = ValidatorNumber()
    menu_option = MenuParameter()
    get_disks = Util_Disk()

    def search_by_option(self, option):
        if self.validate_number.is_number(option) == True:
            if option == 1:
                self.menu_option.search_option_basic()
            elif option == 2:
                self.menu_option.search_option_advanced()
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


menu_search = MainMenu()
menu_search.menu_main()