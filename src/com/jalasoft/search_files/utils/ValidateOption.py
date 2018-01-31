class ValidateOption:
    
    
    def __init__(self):
        self.value = ''


    def is_number(self, number):
        try:
            value = int(number)
            return True
        except ValueError:
            return False
    
    
    def is_positive(self,value):
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

    def convert_format_type(self,size_value,format_type):
        convert_container = ''
        if format_type == 'KB':
            convert_container = size_value*1024
        elif format_type == 'MB':
            convert_container = size_value
        elif format_type == 'GB':
            convert_container = size_value

        return convert_container

