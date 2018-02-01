import os
from src.com.jalasoft.search_files.search.search import Search


class File(Search):

    files = []

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
        file = os.path.dirname(self.file_path)
        return file

    def get_file_size(self):
        file = os.path.getsize(self.file_path)
        return file

    def is_file(self, file_path):
        return self.is_file(file_path)


if __name__ == '__main__':
    obj_file = File()
    obj_file.set_file_path("C:\Python\Python36-32\LICENSE.txt")
    print("Path: ", obj_file.get_file_path())
    print("File name: ", obj_file.get_file_name())
    print("File extension: ", obj_file.get_file_extension())
    print("File size: ", obj_file.get_file_size())
    #print("Is File: ", obj_file.is_file("D:\_cpc\BlueJ.msi"))



    #for root, directories, files in os.walk("C:\\"):
    #    for dir in directories:
    #        path = os.path.join(root, dir)

    #    for file in files:
    #        x = os.path.join(root, file)
    #        #print(x)

#- busqueda de un nombre de archivo con o sin extencion
#- busqueda con extenciones.
#- listar archivos  *
#- listar directorios *
#- busqueda por tama;o * valida q sea numero y positivo
"""
 os.path.getsize(path)¶

    Return the size, in bytes, of path. Raise os.error if the file does not exist or is inaccessible.
    """
