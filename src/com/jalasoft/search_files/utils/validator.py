import os


class Validator:
    def __init__(self,  name_path = '', name_file = ''):
        #self.name_dir = name_dir
        self.name_path = name_path
        self.name_file = name_file

    def validator_absolute_path(self, absolute_path):
        absolutePath = absolute_path
        if absolutePath == os.path.join("name_dir", "name_path", "name_file"):
            return True
        else:
            False

    def validator_non_allow_name_file_characters(self, nonCharactersValue):
        while len(nonCharactersValue) == '/ \* ? " <>':
            return " A file name can not contain any of those values:"

    def validator_allowed_name_dir_characters(self, name_dir):
        while chr(name_dir) == "C" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G":
            return True
        else:
            'The filename, directory name, or volume label syntax is incorrect.'

    def validator_size_absolute_path(self, path_absolute):
        self.path_absolute = 'C:\\Python'
        os.path.getsize(path_absolute)

"""      
        os.path.isdir()
        os.path.basename(path)
        os.path.exists()
        os.pathconf(path)
 """

validatepat = ExpressValidator('C:\Python\Python36-32','84j')
print (validatepat.validator_absolute_path('C:\Python\Python36-32'))
print (validatepat.validator_non_allow_name_file_characters('C:\Python\Python36-32'))
print (validatepat.validator_allowed_name_dir_characters('/jfkdf'))
print (validatepat.validator_size_absolute_path('C:\Python\Python36-32'))


