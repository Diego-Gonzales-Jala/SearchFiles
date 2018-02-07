"""
SearchCriteria class stores all criteria tha a user enter from menu
And this parameter are used to search in disk.
"""
class SearchCriteria:

    def __init__(self):
        self.search_criteria = {
            "search_type": '',
            "file_name": '',
            "path": '',
            "file_size": '',
            "owner": '',
            "create_date": '',
            "modified_date": '',
            "start_date": '',
            "end_date": '',
            "file_ext": '',
            "search_text": '',
            "kind": ''
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
        return self.search_criteria['file_ext']

    # Get file kind of dictionary
    def get_file_kind(self):
        return self.search_criteria['kind']

    # Get size criteria of file - from array
    def get_size_criteria(self):
        return self.size_criteria

    #Get file size to search
    def get_file_size(self):
        return self.search_criteria['file_size']

    # Get end date of file from dictionary
    def get_end_date(self):
        return self.search_criteria['end_date']

    # Get start date file from dictionary
    def get_start_date(self):
        return self.search_criteria['start_date']

    # Get all data from dictionary
    def get_dictionary(self):
        return self.search_criteria

    # Get search type  from dictionary
    def get_search_type(self):
        return self.search_criteria['search_type']

    # Set file name in dictionary
    def set_file_name(self, new_name):
        self.search_criteria['file_name'] = new_name

    # Set path in dictionary for searching on this root, else 'C:\' by default
    def set_path(self,new_path):
        self.search_criteria['path'] = new_path

    # Set file owner in dictionary
    def set_file_owner(self,new_owner):
        self.search_criteria['owner'] = new_owner

    # Set created date of a file in dictionary
    def set_create_date(self,update_date):
        self.search_criteria['create_date'] = update_date

    # Set modified date of a file in dictionary
    def set_modified_date(self,update_mod_date):
        self.search_criteria['modified_date'] = update_mod_date

    # Set file extension in dictionary
    def set_extension(self, extension):
        self.search_criteria['file_ext'] = extension

    def set_file_kind(self,update_kind):
        self.search_criteria['kind'] = update_kind

    #set size criteria in dictionary for searching greater than or less than or equal to file size
    def set_size_criteria(self,sign_value,size,format_type):
        self.size_criteria[0] = sign_value
        self.size_criteria[1] = size
        self.size_criteria[2] = format_type

    # Set file size generic in dictionary to search
    def set_file_size(self,file_size_cr):
        self.search_criteria['file_size'] = file_size_cr

    # Set end date for searching a file
    def set_end_date(self,end_date_usr):
        self.search_criteria['end_date'] = end_date_usr

    # Set start date for searching a file
    def set_start_date(self,start_date_usr):
        self.search_criteria['start_date'] = start_date_usr

    # Set search type 1 as basic or 2 as advanced
    def set_search_type(self,search_type_u):
        self.search_criteria['search_type'] = search_type_u


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
