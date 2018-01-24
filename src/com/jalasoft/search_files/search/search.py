import os


class Search:

    def __init__(self, path):
        self.path = path
        self.path_absolute = ''

    def get_directory(self):
        self. path = os.listdir(self.path)
        return self.path

    def set_directory(self, newPath):
        self.path = newPath

    def get_path_absolute(self, newPath):
        self.path_absolute = os.path.abspath(newPath)
        return self.path_absolute

if __name__ == '__main__':
    sDirecotry = Search("C:\\Python")
    list = sDirecotry.get_directory()
    print(list)
    obj = sDirecotry.get_path_absolute("C:\\Python")
    print(obj)

#dir = os.getcwd()

#print(dir)

#list_dir = os.listdir("C:\\")
#print(list_dir)

#for file in os.listdir("C:"):
#    if file.endswith(".txt"):
#        print(os.path.join("/mydir", file))


#for root, directories, files from os.walk(path)
#        for dir from directories
#            print(dir)
