# This file contains parsing functions for Zerg build orders
from RaceParser import RaceParser


class ZergParser(RaceParser):
    def __init__(self, player, max_tuples=50):
        super().__init__(player, max_tuples)
        self.name = "zerg parser"

