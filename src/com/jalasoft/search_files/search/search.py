import os
import datetime as dt
import calendar
import datetime
import win32api
import win32con
import win32security
from src.com.jalasoft.search_files.menu.searchcriteria import SearchCriteria
from src.com.jalasoft.search_files.search.directory import Directory
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.utils.validatorPath import ValidatorPath
from src.com.jalasoft.search_files.utils.validatorFileSizeConversor import ValidatorFileSizeConversor
from src.com.jalasoft.search_files.utils.logging_search import logger


class Search:

    def __init__(self):
        self.search_criterial = SearchCriteria()
        self.validate_path_s = ValidatorPath()
        self.validate_size_s = ValidatorFileSizeConversor()
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
            if name_dir in namedir:
                list_result_search.append(dir)
        return list_result_search

    def search_by_file_name(self):
        name_file = self.search_criterial.get_file_name()
        path = self.search_criterial.get_path()

        if self.validate_path_s.validate_path(path):
            list_result_search = []
            list_dir = self.get_all_files(path)
            for dir in list_dir:
                file_name = os.path.basename(dir)
                if name_file in file_name:
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
        file_size_convert = int(self.validate_size_s.convert_to_base(int(size[1]),type))
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
            elif sign_value == '<=':
                if file_size <= file_size_convert:
                    list_result_search.append(dir)
            elif sign_value == '>=':
                if file_size >= file_size_convert:
                    list_result_search.append(dir)

        return list_result_search

    def search_by_string_inside_file(self):
        list_of_string = []
        file_path = self.search_criterial.get_path()
        string = self.search_criterial.get_word_into_file()
        for root, directories, files in os.walk(file_path):
            for file in files:
                dir_file = os.path.join(root, file)
                file_open = open(dir_file, 'r')
                for line in file_open.readlines():
                    #for text in string:
                        if string in line:
                            #list_of_string.append(dir_file)
                            print (dir_file)
        #return set(list_of_string)

    def search_by_owner(self):
        path = self.search_criterial.get_path()
        owner_file = self.search_criterial.get_file_owner()
        list_result_owner = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                f = os.path.join(dirpath, filename)
                open(filename, "w").close()
                dataow = win32api.GetUserNameEx(win32con.NameSamCompatible)
                sd = win32security.GetFileSecurity(filename, win32security.OWNER_SECURITY_INFORMATION)
                owner_sid = sd.GetSecurityDescriptorOwner()
                name, domain, type = win32security.LookupAccountSid(None, owner_sid)
                if name == owner_file:
                    list_result_owner.append(f)
                    #list_result_search = (f + " - owner:" + name)
        return list_result_owner

    def _range_date_ctime(self,start_date, end_date, path_file):
        d_start = start_date.split("/")
        d_end = end_date.split("/")
        boolean = False
        # format date is YYYY/MM/DD
        start = calendar.timegm(datetime.datetime(int(d_start[0]), int(d_start[1]), int(d_start[2]), 0, 0).timetuple())
        end = calendar.timegm(datetime.datetime(int(d_end[0]), int(d_end[1]), int(d_end[2]), 23, 59).timetuple())

        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(path_file)
        # ctime = os.path.getatime(path_file)
        if start <= ctime and ctime <= end:
            boolean = True
        # return (start <= ctime <= end)
        return boolean

    def search_by_date_range_ctime(self):
        file_path = self.search_criterial.get_path()
        start_date = self.search_criterial.get_create_date_start()
        end_date = self.search_criterial.get_create_date_end()
        list_of_found = []
        for root, directories, files in os.walk(file_path):
            for file in files:
                file_dir = os.path.join(root, file)
                if self._range_date_ctime(start_date, end_date, file_dir):
                    list_of_found.append(file_dir)

        return list_of_found

    def _range_date_atime(self,start_date, end_date, path_file):
        d_start = start_date.split("/")
        d_end = end_date.split("/")
        boolean = False
        # format date is YYYY/MM/DD
        start = calendar.timegm(datetime.datetime(int(d_start[0]), int(d_start[1]), int(d_start[2]), 0, 0).timetuple())
        end = calendar.timegm(datetime.datetime(int(d_end[0]), int(d_end[1]), int(d_end[2]), 23, 59).timetuple())

        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(path_file)
        # ctime = os.path.getatime(path_file)
        if start <= atime and atime <= end:
            boolean = True
        # return (start <= ctime <= end)
        return boolean

    def search_by_date_range_atime(self):
        file_path = self.search_criterial.get_path()
        start_date = self.search_criterial.get_access_date_start()
        end_date = self.search_criterial.get_access_date_end()
        list_of_found = []
        for root, directories, files in os.walk(file_path):
            for file in files:
                file_dir = os.path.join(root, file)
                if self._range_date_atime(start_date, end_date, file_dir):
                    list_of_found.append(file_dir)

        return list_of_found

    def _range_date_mtime(self,start_date, end_date, path_file):
        d_start = start_date.split("/")
        d_end = end_date.split("/")
        boolean = False
        # format date is YYYY/MM/DD
        start = calendar.timegm(datetime.datetime(int(d_start[0]), int(d_start[1]), int(d_start[2]), 0, 0).timetuple())
        end = calendar.timegm(datetime.datetime(int(d_end[0]), int(d_end[1]), int(d_end[2]), 23, 59).timetuple())

        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(path_file)
        # ctime = os.path.getatime(path_file)
        if start <= mtime and mtime <= end:
            boolean = True
        # return (start <= ctime <= end)
        return boolean

    def search_by_date_range_mtime(self):
        file_path = self.search_criterial.get_path()
        start_date = self.search_criterial.get_modified_date_start()
        end_date = self.search_criterial.get_modified_date_end()
        list_of_found = []
        for root, directories, files in os.walk(file_path):
            for file in files:
                file_dir = os.path.join(root, file)
                if self._range_date_mtime(start_date, end_date, file_dir):
                    list_of_found.append(file_dir)

        return list_of_found