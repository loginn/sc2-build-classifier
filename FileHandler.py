from shutil import copy


class FileHandler:
    def __init__(self):
        self.path = "/home/loginn/Replays/"
        self.out_directory = "Clustered/"
        self.in_directory = "master/"

    def put_builds_in_folders(self, build_dict):
        for build in build_dict:
            print(build[1].filename)
            copy(self.path+self.in_directory+build[1].filename,
                 self.path+self.out_directory+build[0] + "/" + build[1].filename)
