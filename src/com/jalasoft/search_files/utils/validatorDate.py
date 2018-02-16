import re
#from logging import logger
class ValidatorDate:

    def validate_format_date(self, date):
    	#logger.info("validate_format_date: Enter")
        #date_time = re.compile(r'^(0?[1-9]|1[1-12])/(0?[1-9]|[12][0-9]|3[01])/((19|20)\d\d)$')
        date_time = re.compile(r'^(((19|20)/(0?[1-9]|1[1-12])/(0?[1-9]|[12][0-9]|3[01])\d\d)$')
        result = False
        #logger.info("validate_format_date: validate_date")
        if str(date_time.search(date)) != "None":	
            result = True
        #logger.info("validate_format_date: Exit")
        return result