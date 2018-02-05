import os
import datetime as dt
from src.com.jalasoft.search_files.search.directory import Directory
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.utils.validator import Validator


class Search:

    def __init__(self, search_criterial):
        self.search_criterial = search_criterial
        self.path = ""

    def set_path(self, new_path):
        self.path = new_path

    def get_path(self):
        return self.path

    def set_search_criterial(self, new_search_criterial):
        self.search_criterial = new_search_criterial

    def get_detail_search_criterial(self):
        print("__________________DETAIL__CRITERIAL________________")
        print(self.search_criterial["file_name"])
        print(self.search_criterial["path"])
        print(self.search_criterial["owner"])
        print(self.search_criterial["create_date"])
        print(self.search_criterial["modified_date"])
        print(self.search_criterial["end_date"])
        print(self.search_criterial["start_date"])
        print(self.search_criterial["ext"])
        print(self.search_criterial["kind"])

    def is_directory(self, dir_path):
        return os.path.isdir(dir_path)

    def is_file(self, file_path):
        return os.path.isfile(file_path)

    def _search_general(self, path):
        pass

    def get_all_directories(self, path):
        list_directories = []
        for root, directories, files in os.walk(path):
            for dir in directories:
                pathx = os.path.join(root, dir)
                list_directories.append(pathx)
        return list_directories

    def get_all_files(self, path):
        list_files = []
        for root, directories, files in os.walk(path):
            for file in files:
                path = os.path.join(root, file)
                list_files.append(path)
        return list_files

    def get_total_search(self, result_of_search):
        return len(result_of_search)

    def printer_directories(self, list_result):
        for dir in list_result:
            print(dir)

    def search_by_name(self, name_dir, path):
        list_result_search = []
        list_dir = self.get_all_directories(path)
        for dir in list_dir:
            namedir = os.path.basename(dir)
            if namedir == name_dir:
                list_result_search.append(dir)
        return list_result_search

    def search_by_file_name(self, name_file, path):
        list_result_search = []
        list_dir = self.get_all_files(path)
        for dir in list_dir:
            file_name = os.path.basename(dir)
            if file_name == name_file:
                list_result_search.append(dir)
        return list_result_search

    def search_by_extension(self, extension, path):
        list_result_search = []
        list_files = self.get_all_files(path)
        for dir in list_files:
            file_extension = os.path.splitext(dir)[1]
            if file_extension == extension:
                list_result_search.append(dir)
        return list_result_search

    def search_by_file_size(self, size, path):
        list_result_search = []
        list_files = self.get_all_files(path)
        for dir in list_files:
            file_size = os.path.getsize(dir)
            if file_size == size:
                list_result_search.append(dir)
        return list_result_search

    def search_by_range_date(self, path):
        # define epoch time
        t0 = dt.datetime.utcfromtimestamp(0)

        # define time ranges
        d1 = (dt.datetime(2015, 1, 1) - t0).total_seconds()
        d2 = (dt.datetime(2015, 1, 31) - t0).total_seconds()

        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                f = '/'.join([dirpath, filename])
                ctime = os.stat(f)[-1]
                if ctime >= d1 and ctime <= d2:
                    print(f)



if __name__ == '__main__':

    criterial_basic = {
            "file_name": 'IntelGFX.txt',
            "path": 'C:\Intel\Logs',
            "owner": 'dgs',
            "create_date": '15/05/2017',
            "modified_date":'15/05/2017',
            "end_date":'18/05/2017',
            "start_date": '20/05/2017',
            "ext": '.txt',
            "kind":'basic'}

    path_with_file = "C:\Intel\Logs\IntelGFX.txt"
    path_directory = "C:\Intel\Logs"

    obj_search = Search(criterial_basic)
    obj_search.get_detail_search_criterial()

    obj_search.printer_directories(obj_search.get_all_files(path_directory))
    obj_search.printer_directories(obj_search.get_all_directories("C:\\Intel"))
    print(obj_search.is_directory(path_directory))
    print(obj_search.is_file(path_with_file))
    obj_search.printer_directories(obj_search.search_by_file_name("webdav.txt", "C:\\xampp"))
    obj_search.printer_directories(obj_search.search_by_name("webdav", "C:\\xampp"))
    obj_search.printer_directories(obj_search.search_by_extension(".txt", "C:\\xampp"))
    obj_search.printer_directories(obj_search.search_by_file_size(222, "C:\\xampp"))