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
            if self.is_number(value) and value >= 0:
                return True
        except ValueError:
            return False
