import psutil

class Util_Disk:

    def get_disk(self,option):
        disk_part = psutil.disk_partitions()
        disk = disk_part[option-2]
        return disk.device

    def get_disk_partition(self):
        disk_partition = psutil.disk_partitions()
        for i in (0, 1):
            partition = disk_partition[i]
            print('{0:2d} {1:3s}'.format((i+2),partition.device))


class Menu:
    def __init__(self):
        self.name_file = ''
        self.path_file = ''
        self.size_file = 0

    def search_by_name(self, name, path):
        return path + name

    def search_by_size(self):
        return "sl"

    def search_option_one(self):
        self.size_file = str(raw_input('Enter file size:'))
        self.path_file = str(raw_input('Enter the path:'))

    def search_option_two(self):
        self.name_file = str(raw_input('Enter file name:'))
        self.path_file = str(raw_input('Enter the path:'))
        # validate_data = Validator(name_file,path_file)
        print (self.search_by_name(self.name_file, self.path_file))

    def search_by_option(self, option):
        if is_number(option) == True:
            if option == 1:
                self.search_option_one()
            elif option == 2:
                self.search_option_two()
        else:
            return "Error :"

    def menu_main(self):
        print (" -------------- Search directories and files ----------------------")
        print ("Following devices are available to search :)")
        get_disks = Util_Disk()
        get_disks.get_disk_partition()
        self.sub_menu()

    def sub_menu(self, catch=None):
        try:
            print(' Search file or folder by:')
            print ("1 - Size")
            print ("2 - Name")
            #print ("3 - List all files")
            #print ("4 - List all folders")
            option_search_file = int(input('Enter option:'))
            self.search_by_option(option_search_file)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


menu_search = Menu()
menu_search.menu_main()



