class ValidatorFileSizeConversor:

    # This method determine the bytes conversion get from os to measurement unit format_type available, for example:
    # bytes -> KB | # bytes -> MB | # bytes -> GB |  # bytes -> TB |
    def convert_to_base(self, size_value, format_type):
        logger.info("convert_to_base: Enter")
        convert_container = ''
        if format_type == 'KB' or format_type == 'kb':
        logger.info("convert_to_base: File_size_BaseConversor")    
            convert_container = size_value * 1024
        elif format_type == 'MB' or format_type == 'mb':
            convert_container = size_value * (1024 * 1024)
        elif format_type == 'GB' or format_type == 'gb':
            convert_container = size_value * (1024 *1024 *1024)
        elif format_type == 'TB' or format_type == 'tb':
            convert_container = size_value * (1024 *1024 *1024 *1024)

        result = str(int(convert_container)), format_type
        logger.info("convert_to_base: Exit")
        return result[0]