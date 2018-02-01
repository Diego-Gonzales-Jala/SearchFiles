import os
from src.com.jalasoft.search_files.search.search import Search


class Directory(Search):
    
    def __init__(self, path=""):
        self.list_dir_result = []
        self.count_dir = 1
        self.files = []
        self.folders = []
        self.obj_search = Search(path)

    def get_path(self):
        return self.obj_search.get_path()

    def set_path(self, new_path):
        self.obj_search.set_path(new_path)

    def is_directory(self, directory_path):
        return self.obj_search.is_directory(self.get_path())

    def get_list_paths(self):
        return self.obj_search.get_list_paths()

    def get_all_directories(self, path):
        for root, directories, files in os.walk(path):
            for dir in directories:
                path = os.path.join(root, dir)
                self.list_dir_result.append(path)
                self.count_dir += 1
                self.set_total_directories(self.count_dir)
        return self.list_dir_result

    def get_all_files(self, path):
        for root, directories, files in os.walk(path):
            for file in files:
                path = os.path.join(root, file)
                self.list_dir_result.append(path)
                self.count_dir += 1
                self.set_total_directories(self.count_dir)
        return self.list_dir_result

    def set_total_directories(self, count):
        self.count_dir = count

    def get_total_directories(self):
        return self.count_dir

    def printer_directories(self, list_result):
        for dir in list_result:
            print(dir)

    def search_by_name(self, name_dir, path):
        result_search = "No fue encontrado el nombre del directorio"
        list_dir = self.get_all_directories(path)
        for dir in list_dir:
            #dir = Directory()
            #dir.set_path()

            namedir = os.path.basename(dir)
            if namedir == name_dir:
                result_search = dir

        return result_search

    def search_by_file_name(self, name_file, path):
        result_search = "File does not exist, try again..."
        list_dir = self.get_all_files(path)
        for dir in list_dir:

            namedir = os.path.basename(dir)
            if namedir == name_file:
                result_search = dir

        return result_search

    def search_by_extencion(self, file_extencion, path):
        result_search = "File extencion does not exist, try again..."
        list_ext = []
        list_dir = self.get_all_files(path)
        for file in list_dir:

            fileextencion = os.path.splitext(file)[1]
            if fileextencion == file_extencion:
                list_ext.append(file)
                #result_search = file

        return list_ext #result_search

    def search_by_size(self, file_size, path):
        result_search = "File size does not exist, try again..."
        list_size = []
        list_dir = self.get_all_files(path)
        for file in list_dir:

            filesize = os.path.getsize(file)
            #print(filesize)
            if filesize == file_size:
                list_size.append(file)
                #result_search = file

        return list_size #result_search

    def search_type(self, criterial):
        

    def search_basic(self, ):



if __name__ == '__main__':
    obj_dir = Directory("C:\\Intel")
    print(obj_dir.get_path())
    print(obj_dir.is_directory(obj_dir.get_path()))
    #print(obj_dir.get_list_paths())
    x = "C:\Python"
    list = obj_dir.get_all_directories(x)
    obj_dir.printer_directories(list)
    print("Total dir es:", obj_dir.get_total_directories())

    res = obj_dir.search_by_name(x, "demo")
    print(res)

    list_extencion = obj_dir.search_by_extencion(".py", x)
    obj_dir.printer_directories(list_extencion)

    print("-----------------size--------------------")
    list_size = obj_dir.search_by_size(72249, x)
    obj_dir.printer_directories(list_size)