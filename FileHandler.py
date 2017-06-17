import os


class FileHandler:
    def __init__(self):
        self.path = "/home/loginn/Replays/"
        self.directory = "Clustered"
        os.open(self.path+self.directory)