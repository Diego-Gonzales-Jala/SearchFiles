import os
import re

class Validator:
# Constructor where initial parameters include name_path==directory+path and the other is name_file
    def __init__(self,  name_path = '', name_file = ''):
        self.name_path = name_path
        self.name_file = name_file
        self.no_valid_char_path = ['/', '?', '"', '<','>','#', '*']

    def _split_path(self, path):
        return list(path)

    # this method is dedicated to control if a path is the right path in os
    def validator_exist_path(self, absolute_path):
        result = False
        if len(absolute_path) >= 0:
            if os.path.exists(absolute_path):
                result = True
        return result

    # this method track  each character from path.
    def validate_path(self, path):
        result = True
        for i in self.no_valid_char_path:
            for j in path:
                if i == j:
                    result = False
                    break
        return result

    # This meto\hod malidate if the name of path is right along it.
    def validate_name(self, name):
        return self.validate_path(name)

    def validate_file_name(self, file_name):
        while chr(file_name) == "C" | "c" | "d" | "D" | "e" | "E" | "f" | "F":
            return True
        else:
            return False

    def validate_file_size(self, path):
        return os.path.getsize(path)

    # this method validate number options and validate those are not as string.
    def is_number(self, number):
        result = False
        if type(number) != str:
            if number >= 0:
                result = True

        return result


    def is_positive(self, value):
        try:
            if self.is_number(value):
                if int(value) >= 0:
                    return True
                else:
                    return False
            else:
                return False
        except ValueError:
            return False


    def convert_to(self, size_value, format_type):
        convert_container = ''
        if format_type == 'KB':
            convert_container = size_value / 1024
        elif format_type == 'MB':
            convert_container = size_value / (1024 * 1024)
        elif format_type == 'GB':
            convert_container = size_value / (1024*1024*1024)
        elif format_type == 'TB':
            convert_container = size_value / (1024*1024*1024*1024)

        result = str(int(convert_container)), format_type
        return result[0] +" "+ result[1]

    def validate_format_date(self, date):
        date_time = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')
        result = False
        if str(date_time.search(date)) != "None":
            result = True
        return result

if __name__ == '__main__':

    obj_val = Validator()
    path = "D:\\-250"
    path_absolute = "D:\\2507\LEEME.txt"

    print("Passed if srt or number: ", obj_val.is_number(-5))
    print("Passed path_absolute: ", obj_val.validator_exist_path(path_absolute))
    print("Passed path: ", obj_val.validate_path(path))
    print("Passed date: ", obj_val.validate_format_date("02/12/2015"))
    print("Passed name in path: ", obj_val.validate_name("musica-clasico.txt"))
    print("Passed size Type", obj_val.convert_to(10485760, "MB"))


# Priority validation methods
# - nombre de archivo
# file extention
# get size method
#
#    def file_extention(self, file_name_extent):

