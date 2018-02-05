import os

class Validator:
# Constructor where initial parameters include name_path==directory+path and the other is name_file
    def __init__(self,  name_path = '', name_file = ''):
        self.name_path = name_path
        self.name_file = name_file
        self.no_valid_char_path = ['/', '*', '?', '"', '<','>','#']

    def split_path(self, path):
        return list(path)

    def validator_exist_path(self, absolute_path):
        if absolute_path != '':
            #f absolutePath == os.path.join("name_path", "name_file"):
            if os.path.exists(absolute_path) == True:
                return os.path.isdir(absolute_path)
        else:
            False

# Path validator that walk all path by fragmenting it and comparing non of this chars /*,?"<>,# are valid.
    def validate_path(self, path):
        lenght = len(path)
        path_frag = self.split_path(path)

        for i in range (lenght):
            for j in range (len(self.no_valid_char_path)):
                #print (self.no_valid_char_path[j])
                if self.no_valid_char_path[j] == path_frag[i]:
                    value = False
                    break
                else:
                    value = True
        return value

    def validate_file_name(self, file_name):
        while chr(file_name) == "C" | "c" | "d" | "D" | "e" | "E" | "f" | "F":
            return True
        else:
            return False

    def validate_file_size(self, path):
        return os.path.getsize(path)

validatepat = Validator()
#print ("path ",validatepat.validator_exist_path('C:\Python\Python36-32'))
print ("",validatepat.validate_path('C:\Python\#*'))
#print ("",validatepat.validate_file_size('C:\Python\Python36-32\LICENSE.txt'))
#print (validatepat.validator_allowed_name_dir_characters('/jfkdf'))


name = "C:\Python\Python36-32"
#print(list(name))