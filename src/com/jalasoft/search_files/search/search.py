import os


class Search:

    def __init__(self, path):
        self.path = path

    def get_path(self):
        self. path = os.path.abspath(self.path)
        return self.path

    def get_list_paths(self):
        self.path = os.listdir(self.path)
        return self.path

    def set_path(self, new_path):
        self.path = new_path

    def is_directory(self, directory_path):
        dir = os.path.isdir(directory_path)
        return dir

    def is_file(self, file_path):
        file = os.path.isfile(file_path)
        return file

#http://www.w3big.com/es/python/os-file-methods.html