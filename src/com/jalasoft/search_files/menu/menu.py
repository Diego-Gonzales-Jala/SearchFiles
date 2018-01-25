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

    def search_by_name(self, name, path):
        return path + name

    def search_by_size(self):
        return "sl"
    def search_directory_by_option(self,search_disk):
        if search_disk == 1:
            print("hello")
        elif search_disk > 1:
            self.path_file = str(raw_input('Enter directory name:'))
            get_disk_s = Util_Disk()
            print (get_disk_s.get_disk(search_disk), self.path_file)

    def search_file_by_option(self,search_type_file):
        if search_type_file == 1:
            print (self.search_by_size())

        elif search_type_file == 2:
            self.name_file = str(raw_input('Enter file name:'))
            self.path_file = str(raw_input('Enter the path:'))
            # validate_data = Validator(name_file,path_file)
            print (self.search_by_name(self. name_file,self.path_file))

        else:
            print ("Error - Does not exist this option")

    def menu_main(self):
        print(" -------------- Search directories and files ----------------------")
        print ("1 - Directory")
        print ("2 - Files")
        option_search = int(input('Enter option to search the file or directory:'))
        self.sub_menu(option_search)

    def sub_menu(self, option_search):
        if option_search == 1:
            print(" 1 All disk")
            get_disks = Util_Disk()
            get_disks.get_disk_partition()
            option_search_directory = int(input('Enter option:'))
            self.search_directory_by_option(option_search_directory)

        elif option_search == 2:
            print(' Search file by:')
            print ("1 - Size")
            print ("2 - name")
            option_search_file = int(input('Enter option:'))

            self.search_file_by_option(option_search_file)

        else:
            print("Error - option entered ")


menu_search = Menu()
menu_search.menu_main()



