import psutil
import self as self


class Util_Disk:

    def get_disk_partition(self):
        disk_partition = psutil.disk_partitions()
        format_string = "{:<8}{:<7}{:7}"
        print(format_string.format("Drive","Type","Options"))

        for i in (0,1):
            partition = disk_partition[i]
            print(format_string.format(partition.device,partition.fstype,partition.opts))

class Menu:

    def search_by_name(self):
        return "test.ss"

    def search_by_size(self):
        return "test.ss"

    def search_file_by_option(self,search_type):

        if search_type == 1:
            print (self.search_by_size())
        elif search_type == 2:
            print (self.search_by_name())
            name_file = str(input("Enter file's name:"))
            path_file = str(input("Enter the path"))
            validate_data = Validator(name_file,path_file)
            
        else:
            print ("Error - Does not exist this option")

    def menu_main(self):
        print(" -------------- Search directories and files ----------------------")
        print ("1 - Directory")
        print ("2 - Files")
        option_search = int(input('Enter option to search the file or directory:'))
        self.sub_menu(option_search)

    def sub_menu(self,option_search):
        if option_search == 1:
            print("1. All disk")
            disk_partition = psutil.disk_partitions()
            format_string = "{:<8}{:<7}{:7}"
            print(format_string.format("Drive", "Type", "Options"))

            for i in (0, 0):
                partition = disk_partition[i]
                print(format_string.format(partition.device, partition.fstype, partition.opts))


            self.option_search_directory = int(input('Enter option:'))

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


