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

    def get_full_path(self, path):
        for root, directories, files in os.walk(path):
            # for dir in directories:
            # dirx = os.path.join(root, dir)
            # print(dirx)

            for file in files:
                x = os.path.join(root, file)
                print(x)

if __name__ == '__main__':
    sDirecotry = Search("C:\\Python")
    list = sDirecotry.get_directory()
    print(list)
    obj = sDirecotry.get_path_absolute("C:\\Python")
    print(obj)
    sDirecotry.get_full_path("C:\\Python")


#    for root, directories, files in os.walk("C:\\Python"):
        #for dir in directories:
            #dirx = os.path.join(root, dir)
            #print(dirx)

#        for file in files:
#            x = os.path.join(root, file)
#            print(x)


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
