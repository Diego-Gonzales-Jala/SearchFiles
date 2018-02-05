import os


class Directory:

    def __init__(self, dir_path=""):
        self.dir_path = dir_path

    def set_dir_path(self, new_dir_path):
        self.dir_path = new_dir_path

    def get_dir_name(self):
        dir = os.path.basename(self.get_dir_path())
        return dir

    def get_dir_path(self):
        dir = os.path.abspath(self.dir_path)
        return dir

    def get_dir_size(self):
        folder_size = 0
        for (path, dirs, files) in os.walk(self.dir_path):
            for file in files:
                filename = os.path.join(path, file)
                folder_size += os.path.getsize(filename)

        return folder_size

    def is_directory(self, dir_path):
        dir = os.path.isdir(dir_path)
        return dir


if __name__ == '__main__':
    obj_dir = Directory()
    obj_dir.set_dir_path("D:\_Environment_Game\CocosCreator")
    print("Path: ", obj_dir.get_dir_path())
    print("File name: ", obj_dir.get_dir_name())
    print("File size: ", obj_dir.get_dir_size())
    print("Is Directoryx: ", obj_dir.is_directory("D:\_cpc"))
