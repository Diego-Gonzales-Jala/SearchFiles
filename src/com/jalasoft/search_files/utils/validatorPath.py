import os


class ValidatorPath:

    #Constructor.
    def __init__(self,  name_path = '', name_file = ''):
        self.name_path = name_path
        self.name_file = name_file
        self.no_valid_char_path = ['/', '?', '"', '<','>','#', '*']

    # this method track  each character from path.
    def _split_path(self, path):
        return list(path)

    # this method is dedicated to control if a path is the right path in os
    def validator_exist_path(self, absolute_path):
        #logger.info("validator_exist_path: Enter")
        result = False
        if len(absolute_path) >= 0:
            #logger.info("validator_exist_path: compare right path in os")
            if os.path.exists(absolute_path):
                result = True
        #logger.info("validator_exist_path: Exit")
        return result


    def validate_path(self, path):
        #logger.info("validate_path: Enter")
        result = True
        for i in self.no_valid_char_path:
            #logger.info("validate_path: compare invalid char in path")
            for j in path:
                if i == j:
                    result = False
                    break
        #logger.info("validate_path: Exit")
        return result

    # This method validate if the name of path is right along it.
    def validate_name(self, name):
        return self.validate_path(name)

    # This method Validate if the path is empty.

    def validate_path_is_empty(self, path):
        #logger.info("validate_path_is_empty: Enter")
        empty = False
        if len(path) > 0:
            #logger.info("validate_path_is_empty: validate an empty path or sent path")
            if os.path.exists(path):
                empty = True
        #logger.info("validate_path_is_empty: Exit")
            return empty

    # This method is determined to validate the right extension of file.

    def validate_extension(self, path, extension):
        #logger.info("validate_extension: Enter")
        name_file = os.path.splitext(path)
        exten = name_file[1]
        print(name_file)
        if extension == exten:
            #logger.info("validate_extension: compare the search extension")
            return True
        else:
        #logger.info("validate_extension: Exit")
            return False

    def validate_file_name(self, file_name):
        #logger.info("validate_file_name: Enter")
        while chr(file_name) == "C" | "c" | "d" | "D" | "e" | "E" | "f" | "F":
            #logger.info("validate_file_name: validate directory name implicid with file name")
            return True
        else:
        #logger.info("validate_file_name: Exit")
            return False

