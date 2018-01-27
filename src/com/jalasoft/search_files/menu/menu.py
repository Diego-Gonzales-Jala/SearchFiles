from ValidateOption import ValidateOption
import psutil


class Util_Disk(object):
      def get_disk(self, option):
          disk_part = psutil.disk_partitions()
          disk = disk_part[option - 2]
          return disk.device

      def get_disk_partition(self):
          disk_partition = psutil.disk_partitions()
          for i in (0, 1):
             partition = disk_partition[i]
             print('{0:2s} {1:3s}'.format(("|"), partition.device))


class Menu:


    def __init__(self):
        self.name_file = ''
        self.path_file = ''
        self.size_file = 0
        self.validate = ValidateOption()
        self.get_disks = Util_Disk()
        #self.validate_data = Validator(name_file,path_file)
        #self.search = Search()


    def search_option_one(self):
        self.size_file = input('Enter file size:')
        self.path_file = input('Enter the path:')
        if self.validate.is_positive(self.size_file) == True:
            print ("--",self.size_file)
            if self.validate_data.validate_path(self.path_file) == True:
                print(self.search.search_by_size(self.size_file,self.path_file))
            else:
                print ("Error: Oops!  That was no valid path.  Try again...")
                self.search_option_one()
        else:
            print ("Error: Oops!  That was no valid size.  Try again...")
            self.search_option_one()


    def search_option_two(self):
        self.name_file = str(input('Enter file name:'))
        self.path_file = str(input('Enter the path:'))
        if  self.validate_data.validate_name(self.name_file) == True and self.validate_data.validate_path(self.path_file) == True:
            print (self.search_by_name(self.name_file, self.path_file))
        else:
            print ("Error: Oops!  That was no valid name or path.  Try again...")
            self.search_option_two()
            

    def search_by_option(self, option):
        if self.validate.is_positive(option) == True:
            if option == 1:
                self.search_option_one()
            elif option == 2:
                self.search_option_two()
            elif option == 0:
                exit()
        else:
            return "Error :"

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
