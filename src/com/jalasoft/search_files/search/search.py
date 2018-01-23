import os


class SearchDirectory:

    def __init__(self, path):
        self.path = path

    def get_directory(self):
        self. path = os.listdir(self.path)
        return self.path

    def set_directory(self, newPath):
        self.path = newPath


if __name__ == '__main__':
    sDirecotry = SearchDirectory("C:\\Python")
    list = sDirecotry.get_directory()
    print(list)

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
