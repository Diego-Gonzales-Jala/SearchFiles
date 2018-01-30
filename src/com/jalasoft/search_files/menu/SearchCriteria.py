class SearchCriteria:

    def __init__(self):
        self.search_criteria = {
            "file_name": '',
            "path": 'C:',
            "owner": '',
            "create_date": '',
            "modified_date":'',
            "ext": '',
            "kind":''
                                }
        self.size_criteria = ['=','','MB']

    def get_file_name(self):
        return self.search_criteria['file_name']

    def get_path(self):
        return self.search_criteria['path']

    def get_file_owner(self):
        return self.search_criteria['owner']

    def get_create_date(self):
        return self.search_criteria['create_date']

    def get_modified_date(self):
        return self.search_criteria['modified_date']

    def get_extension(self):
        return self.search_criteria['ext']

    def get_file_kind(self):
        return self.search_criteria['kind']

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

    def set_file_kind(self,update_kind):
        self.search_criteria['kind'] = update_kind

class BasicSearch(SearchCriteria):

    def __init__(self):
        self.adv_search_criteria = {"flag_basic": 0}

    def get_basic_flag(self):
        return self.adv_search_criteria['flag_basic']

    def set_basic_flag(self,upd_basic_flag):
        self.adv_search_criteria['flag_basic'] = upd_basic_flag


class AdvancedSearch(SearchCriteria):

    def __init__(self):
        self.adv_search_criteria ={
            "flag_adv": 0,
            "file_content": '',
            "System_files": 0,
            "zipped_files": 0
                                    }

    def get_advanced_flag(self):
        return self.adv_search_criteria['flag_adv']

    def get_file_content(self):
        return self.adv_search_criteria['file_content']

    def get_system_files_value(self):
        return self.adv_search_criteria['System_files']

    def get_zipped_files_value(self):
        return self.adv_search_criteria['zipped_files']

    def set_advanced_flag(self,update_flag_adv):
        self.adv_search_criteria['flag_adv'] = update_flag_adv

    def set_file_content(self,word_cont):
        self.adv_search_criteria['file_content'] = word_cont

    def set_system_files_value(self,flag_sys):
        self.adv_search_criteria['System_files'] = flag_sys

    def get_zipped_files_value(self,flag_zipp):
        self.adv_search_criteria['zipped_files'] = flag_zipp
