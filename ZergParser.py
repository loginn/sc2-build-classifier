from RaceParser import RaceParser


class ZergParser(RaceParser):
    def __init__(self, player):
        super.__init__(player)
        self.name = 'ZergParser'
