import re
from src.com.jalasoft.search_files.utils.logging_search import logger


class ValidatorDate:

    #This method validate a right format # MM/DD/YYYY, on Search it is using format date as YYYY/MM/DD
    #that is whay it is converted.
    def validate_format_date(self, date):
        date_split = date.split("/")
        convert_date = str(date_split[1]) + "/" + str(date_split[2]) + "/" + str(date_split[0])
        logger.info("validate_format_date: Enter")
        # MM/DD/YYYY
        date_time = re.compile(r'^(0?[1-9]|1[1-12])/(0?[1-9]|[12][0-9]|3[01])/((19|20)\d\d)$')
        result = False
        logger.info("validate_format_date: validate_date")
        if str(date_time.search(convert_date)) != "None":
            result = True
        logger.info("validate_format_date: Exit")
        return result