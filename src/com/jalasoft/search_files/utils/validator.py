import os


class Validator:
    def __init__(self,  name_path = '', name_file = ''):
        self.name_path = name_path
        self.name_file = name_file
        self.no_valid_char_path = ['/', '*', '?', '"', '<','>','#']

    def split_path(self,path):
        return list(path)

    def validator_exist_path(self, absolute_path):
        if absolute_path != '':
            if os.path.exists(absolute_path) == True:
                return True
        else:
            False

    def validator_non_allow_name_file_characters(self, path):
        lenght = len(path)
        path_frag = self.split_path(path)

        for i in range (lenght):
            for j in range (len(self.no_valid_char_path)):
                if self.no_valid_char_path[j] == path_frag[i]:
                    value = False
                    break
                else:
                    value = True

        return value

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

validatepat = Validator()
#print ("path ",validatepat.validator_exist_path('C:\Python\Python36-32'))
print ("",validatepat.validator_non_allow_name_file_characters('C:\Python\Python#36-32\mono'))
#print (validatepat.validator_allowed_name_dir_characters('/jfkdf'))
#print (validatepat.validator_size_absolute_path('C:\Python\Python36-32'))



"""
f=open("archivo","r")
it = (row for i,row in enumerate(r) if i>=0)
for linea in it:
  print linea


def verify_ext(path, exten1)
os.path.splitText(path)[1]
if=exten1 == exten2:
    return True
else:
    return false
"""

