class SearchCriteria:

    def __init__(self):
        self.search_criteria = {
            "search_type": '',
            "file_name": '',
            "path": '',
            "owner": '',
            "create_date": {"c_start_date": '', "c_end_date": ''},
            "modified_date": {"m_start_date": '', "m_end_date": ''},
            "access_date": {"a_start_date": '', "a_end_date": ''},
            "file_extension": '',
            "word_into_file": ''}

        self.size_criteria = ['=', '', 'MB']

    # Get file name of dictionary
    def get_file_name(self):
        return self.search_criteria['file_name']

    # Get path of dictionary
    def get_path(self):
        return self.search_criteria['path']

    # Get file owner of dictionary
    def get_file_owner(self):
        return self.search_criteria['owner']

    # Get create date of file  - from dictionary
    def get_create_date_start(self):
        return self.search_criteria['create_date']['c_start_date']

    # Get create date of file  - from dictionary
    def get_create_date_end(self):
        return self.search_criteria['create_date']['c_end_date']

    # Get modified date of file  - from dictionary
    def get_modified_date_start(self):
        return self.search_criteria['modified_date']['m_start_date']

    # Get modified date of file  - from dictionary
    def get_modified_date_end(self):
        return self.search_criteria['modified_date']['m_end_date']

    # Get access date of file  - from dictionary
    def get_access_date_start(self):
        return self.search_criteria['access_date']['a_start_date']

    # Get access date of file  - from dictionary
    def get_access_date_end(self):
        return self.search_criteria['access_date']['a_end_date']

    # Get modified date of file  - from dictionary
    def get_create_date(self):
        return self.search_criteria['create_date']

    def get_modified_date(self):
        return self.search_criteria['modified_date']

    def get_access_date(self):
        return self.search_criteria['access_date']

    # Get file extension of dictionary
    def get_extension(self):
        return self.search_criteria['file_extension']

    # Get file kind of dictionary
    def get_word_into_file(self):
        return self.search_criteria['word_into_file']

    # Get size criteria of file - from array
    def get_size_criteria(self):
        return self.size_criteria

    # Get end date of file from dictionary
    def get_end_date(self):
        return self.search_criteria['end_date']

    # Get start date file from dictionary
    def get_start_date(self):
        return self.search_criteria['start_date']

    # Get search type to search from dictionary
    def get_search_type(self):
        return self.search_criteria['search_type']

    # Get all data from dictionary
    def get_dictionary(self):
        return self.search_criteria

    # Set file name into dictionary
    def set_file_name(self, new_name):
        self.search_criteria['file_name'] = new_name

    # Set file path into dictionary
    def set_path(self, new_path):
        self.search_criteria['path'] = new_path

    # Set file owner into dictionary
    def set_file_owner(self, new_owner):
        self.search_criteria['owner'] = new_owner

    # Set create date of file into dictionary
    def set_create_date(self, start_date, end_date):
        self.search_criteria['create_date']['c_start_date'] = start_date
        self.search_criteria['create_date']['c_end_date'] = end_date

    # Set modified date of file into dictionary
    def set_modified_date(self, start_date, end_date):
        self.search_criteria['modified_date']['m_start_date'] = start_date
        self.search_criteria['modified_date']['m_end_date'] = end_date

    # Set create date of file into dictionary
    def set_access_date(self, start_date, end_date):
        self.search_criteria['modified_date']['a_start_date'] = start_date
        self.search_criteria['modified_date']['a_end_date'] = end_date

    # Set file extension into dictionary
    def set_extension(self, extension):
        self.search_criteria['file_extension'] = extension

    # Set word to search in the files into dictionary
    def set_word_into_file(self, word_into_file_t):
        self.search_criteria['word_into_file'] = word_into_file_t

    # Set size criteria of file into dictionary
    def set_size_criteria(self, sign_value, size, format_type):
        self.size_criteria[0] = sign_value
        self.size_criteria[1] = size
        self.size_criteria[2] = format_type

    # Get search type to search from dictionary
    def set_search_type(self, search_type_usr):
        self.search_criteria['search_type'] = search_type_usr


class BasicSearch(SearchCriteria):

    def __init__(self):
        self.basic_search_criteria = {"basic_flag": 0}

    def get_basic_flag(self):
        return self.basic_search_criteria['basic_flag']

    def set_basic_flag(self,upd_basic_flag):
        self.basic_search_criteria['basic_flag'] = upd_basic_flag


class AdvancedSearch(SearchCriteria):

    def __init__(self):
        self.adv_search_criteria ={
            "adv_flag": 0,
            "file_content": '',
            "System_files": 0,
            "zipped_files": 0
                                    }

    def get_advanced_flag(self):
        return self.adv_search_criteria['adv_flag']

    def get_file_content(self):
        return self.adv_search_criteria['file_content']

    def get_system_files_value(self):
        return self.adv_search_criteria['System_files']

    def get_zipped_files_value(self):
        return self.adv_search_criteria['zipped_files']

    def set_advanced_flag(self,update_flag_adv):
        self.adv_search_criteria['adv_flag'] = update_flag_adv

    def set_file_content(self,word_cont):
        self.adv_search_criteria['file_content'] = word_cont

    def set_system_files_value(self,flag_sys):
        self.adv_search_criteria['System_files'] = flag_sys

    def set_zipped_files_value(self,flag_zipp):
        self.adv_search_criteria['zipped_files'] = flag_zipp
