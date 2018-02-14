import os
import datetime as dt

from src.com.jalasoft.search_files.menu.SearchCriteria import SearchCriteria
from src.com.jalasoft.search_files.search.directory import Directory
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.utils.validator import Validator
from src.com.jalasoft.search_files.utils.logging import logger


class Search:

    def __init__(self):
        self.search_criterial = SearchCriteria()
        self.validator = Validator()
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

    #def is_directory(self, dir_path):
    def is_directory(self):
        dir_path = self.search_criterial.get_path()
        return os.path.isdir(dir_path)

    def is_file(self, file_path):
        file_path = self.search_criterial.get_path()
        return os.path.isfile(file_path)

    def _search_general(self, path):
        pass

    def get_all_directories(self, path):
        #path = self.search_criterial.get_path()
        list_directories = []
        for root, directories, files in os.walk(path):
            for dir in directories:
                pathx = os.path.join(root, dir)
                list_directories.append(pathx)
        return list_directories

    def get_all_files(self, path):
        logger.info("get_all_files: Enter")
        #path = self.search_criterial.get_path()
        list_files = []
        logger.info("get_all_files: Load files")
        for root, directories, files in os.walk(path):
            for file in files:
                path = os.path.join(root, file)
                list_files.append(path)
        logger.info("get_all_files: Exit")
        return list_files

    def get_total_search(self, result_of_search):
        return len(result_of_search)

    def printer_directories(self, list_result):
        for dir in list_result:
            print(dir)

    def search_by_name(self):
        name_dir = self.search_criterial.get_file_name()
        path = self.search_criterial.get_path()
        list_result_search = []
        list_dir = self.get_all_directories(path)
        for dir in list_dir:
            namedir = os.path.basename(dir)
            if namedir == name_dir:
                list_result_search.append(dir)
        return list_result_search

    def search_by_file_name(self):
        name_file = self.search_criterial.get_file_name()
        path = self.search_criterial.get_path()

        if self.validator.validate_path(path):
            list_result_search = []
            list_dir = self.get_all_files(path)
            for dir in list_dir:
                file_name = os.path.basename(dir)
                if file_name == name_file:
                    list_result_search.append(dir)
            return list_result_search
        else:
            return "Error - path is empty or path invalid"

    def search_by_extension(self):
        extension = self.search_criterial.get_extension()
        path = self.search_criterial.get_path()
        list_result_search = []
        list_files = self.get_all_files(path)
        for dir in list_files:
            file_extension = os.path.splitext(dir)[1]
            if file_extension == extension:
                list_result_search.append(dir)
        return list_result_search

    def search_by_file_size(self):
        size = self.search_criterial.get_size_criteria()
        path = self.search_criterial.get_path()
        type = size[2]
        # Search a file greater than or less than to size
        #print(type)
        file_size_convert = int(self.validator.convert_to_base(int(size[1]),type))
        #convert_base = self.validator.convert_to(int(size[1]), type)
        #print(convert_base, type)

        sign_value = size[0]
        list_result_search = []
        list_files = self.get_all_files(path)
        for dir in list_files:
            file_size = os.path.getsize(dir)
            if sign_value == '>':
                if file_size > file_size_convert:
                    list_result_search.append(dir)
            elif sign_value == '<':
                if file_size < file_size_convert:
                    list_result_search.append(dir)
            elif sign_value == '=':
                if file_size < file_size_convert:
                    list_result_search.append(dir)

        return list_result_search

    def search_by_range_date(self):
        path = self.search_criterial.get_path()
        start_date = self.search_criterial.get_start_date()
        start_date_split = start_date.split('/')
        print (start_date)
        print (start_date_split)
        end_date = self.search_criterial.get_start_date()
        end_date_split = end_date.split('/')

        # define epoch time
        t0 = dt.datetime.utcfromtimestamp(0)

        # define time ranges
        #d1 = (dt.datetime(int(start_date_split[2]), int(start_date_split[0]), int(start_date_split[1])) - t0).total_seconds()
        #d2 = (dt.datetime(int(start_date_split[2]), int(start_date_split[0]), int(start_date_split[1])) - t0).total_seconds()
        d1 = (dt.datetime(2018, 2, 1) - t0).total_seconds()
        d2 = (dt.datetime(2018, 2, 28) - t0).total_seconds()

        #print(d1)
        #print(d2)

        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                #f = '/'.join([dirpath, filename])
                f = os.path.join(dirpath, filename)
                #ctime = os.stat(f)[-1]
                ctime= os.stat(f).st_ctime
                ###ctime = os.path.getctime(f)
                mtime = os.path.getmtime(f)
                atime = os.path.getatime(f)
                #print("-----------------------------------", ctime)
                #print("f--", f)
                #print("c--",ctime)
                #print("m--",mtime)
                #print("a--",atime)
                #print("-----------------------------------", ctime)
                #print(ctime)
                if d1 >= ctime and ctime <= d2:
                    print(ctime)
                    print(f)


"""
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
"""
if __name__ == '__main__':
    search = Search()
    print(search.search_by_range_date())
