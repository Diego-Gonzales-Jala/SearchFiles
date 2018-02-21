from src.com.jalasoft.search_files.utils.logging_search import logger

class ValidatorNumber:

    # this method validate number options and validate those are not as string.
    def is_number(self, number):
        logger.info("is_number: Enter")
        num = int(number)
        result = False
        if num != str:
            logger.info("is_number: return a number")
            if num >= 0:
                result = True
            logger.info("is_number: Exit")
        return result


    # This method determine the integer value must be a positive value, not negative.
    def is_positive(self, value):
        logger.info("is_positive: Enter")
        try:
            if self.is_number(value):
                logger.info("is_positive: return a positive number")
                if int(value) >= 0:
                    return True
                else:
                    return False
            else:
                return False
            logger.info("is_positive: Exit")
        except ValueError: 
            return False
