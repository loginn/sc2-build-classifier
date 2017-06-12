from RaceParser import RaceParser


class TerranParser(RaceParser):
    def __init__(self, player):
        super.__init__(player)
        self.name = 'TerranParser'
