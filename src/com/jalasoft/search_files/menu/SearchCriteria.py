class SearchCriteria:

    def __init__(self):
        self.search_criteria = {
            "file_name": '',
            "path": 'C:',
            "owner": '',
            "create_date": '',
            "modified_date":'',
            "end_date":'',
            "start_date": '',
            "ext": '',
            "word_into_file":''
                                }
        self.size_criteria = ['=','','MB']

    #Get file name of dictionary
    def get_file_name(self):
        return self.search_criteria['file_name']

    # Get path of dictionary
    def get_path(self):
        return self.search_criteria['path']

    # Get file owner of dictionary
    def get_file_owner(self):
        return self.search_criteria['owner']

    # Get create date of file  - from dictionary
    def get_create_date(self):
        return self.search_criteria['create_date']

    # Get modified date of file  - from dictionary
    def get_modified_date(self):
        return self.search_criteria['modified_date']

    # Get file extension of dictionary
    def get_extension(self):
        return self.search_criteria['ext']

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

    def get_dictionary(self):
        return self.search_criteria

    def set_file_name(self, new_name):
        self.search_criteria['file_name'] = new_name

    def set_path(self,new_path):
        self.search_criteria['path'] = new_path

    def set_file_owner(self,new_owner):
        self.search_criteria['owner'] = new_owner

    def set_create_date(self,update_date):
        self.search_criteria['create_date'] = update_date

    def set_modified_date(self,update_mod_date):
        self.search_criteria['modified_date'] = update_mod_date

    def set_extension(self, extension):
        self.search_criteria['ext'] = extension

    def set_word_into_file(self,word_into_file_t):
        self.search_criteria['word_into_file'] = word_into_file_t

    def set_size_criteria(self,sign_value,size,format_type):
        self.size_criteria[0] = sign_value
        self.size_criteria[1] = size
        self.size_criteria[2] = format_type

    def set_end_date(self,end_date_usr):
        self.search_criteria['end_date'] = end_date_usr

    def set_start_date(self,start_date_usr):
        self.search_criteria['start_date'] = start_date_usr


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
