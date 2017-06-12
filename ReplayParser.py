from sc2reader.factories import SC2Factory
from sc2reader import engine
from sc2reader.engine.plugins.supply import SupplyTracker
from ProtossParser import ProtossParser
from ZergParser import ZergParser
from TerranParser import TerranParser


class ReplayParser:
    def __init__(self, path):
        self.factory = SC2Factory()
        self.replays = SC2Factory.load_replays(self.factory, sources=path, load_level=3)

    def parse(self):
        for replay in self.replays:
            if replay.type == "1v1":
                self.parse_replay(replay)

    def parse_replay(self, replay):
        for team in replay.teams:
            for player in team.players:
                parser = self.get_parser(player)
                if parser is not None:
                    engine.register_plugin(SupplyTracker())
                    engine.register_plugin(parser)
                    engine.run(replay)

    def get_parser(self, player):
        race = player.detail_data['race']
        if race == 'Protoss':
            return ProtossParser(player)
        else:
            return None


'''        elif race == 'Terran':
            return TerranParser(player)
        else:
            return ZergParser(player)'''
