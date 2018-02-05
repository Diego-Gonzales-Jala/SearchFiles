import os


class File:

    def __init__(self, file_path=""):
        self.file_path = file_path

    def set_file_path(self, new_file_path):
        self.file_path = new_file_path

    def get_file_extension(self):
        file = os.path.splitext(self.file_path)[1]
        return file

    def get_file_name(self):
        file = os.path.basename(self.get_file_path())
        return file

    def get_file_path(self):
        file = os.path.abspath(self.file_path)
        return file

    def get_file_size(self):
        file = os.path.getsize(self.file_path)
        return file

    def is_file(self):
        file = os.path.isfile(self.file_path)
        return file


if __name__ == '__main__':
    obj_file = File()
    obj_file.set_file_path("D:\\_cpc\BlueJ.msi")
    print("Path: ", obj_file.get_file_path())
    print("File name: ", obj_file.get_file_name())
    print("File extension: ", obj_file.get_file_extension())
    print("File size: ", obj_file.get_file_size())
    print("Is File: ", obj_file.is_file())

