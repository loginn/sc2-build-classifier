# This file contains parsing functions for Terran build orders
from RaceParser import RaceParser


class TerranParser(RaceParser):
    def __init__(self, player, max_tuples=50):
        super().__init__(player, max_tuples)
        self.name = "terran parser"

    def unit_to_numeric_value(self, name):
        pass