from sc2reader.factories import SC2Factory
from sc2reader import engine
from sc2reader.engine.plugins.supply import SupplyTracker
from ProtossParser import ProtossParser
import os
from ZergParser import ZergParser
from TerranParser import TerranParser
from FileHandler import FileHandler
from Clustering import Clustering


class ReplayParser:
    def __init__(self, path, max_replay_load=10, max_event_parsed=50):
        self.factory = SC2Factory()
        self.folder = path
        self.training_builds = {"Protoss": [], "Terran": [], "Zerg": []}
        self.predict_builds = {"Protoss": [], "Terran": [], "Zerg": []}
        self.training_replays = []
        self.predict_replays = []
        self.success_replay = []
        self.max_replay_load = max_replay_load
        self.max_event_parsed = max_event_parsed
        self.dir_list = os.listdir(self.folder)
        self.clustering = Clustering()

    def run(self):
        self.parse()

    def parse(self):
        print('Begin replay loading...')
        self.load_replays(self.max_replay_load, self.training_replays)
        print('Done\n')

        print('Begin replay parsing...')
        for replay in self.training_replays:
            self.parse_replay(replay, self.training_builds)
        print('Done\n')
        print('Number of builds parsed : ',
              sum([len(self.training_builds["Protoss"]),
                   len(self.training_builds["Terran"]),
                   len(self.training_builds["Zerg"])]))
        self.train_cluster_builds()
        self.predict()

    def load_replays(self, max_replays, replay_array):
        count = 0
        for filename in self.dir_list:
            if count >= max_replays:
                break
            try:
                print("Loading replay : ", filename)
                replay = SC2Factory.load_replay(self.factory, os.path.join(self.folder, filename))
                replay_array.append(replay)
            except UnicodeDecodeError:
                pass
            if max_replays != -1:
                count += 1

    def parse_replay(self, replay, build_dict):
        for team in replay.teams:
            for player in team.players:
                if player.detail_data['race'] == 'Protoss':
                    parser = self.get_parser(player)
                    engine.register_plugin(SupplyTracker())
                    engine.register_plugin(parser)
                    engine.run(replay)
                    self.update_builds(player, parser, replay, build_dict)

    def predict(self, max_replays=50):
        self.load_replays(max_replays, self.predict_replays)
        for replay in self.predict_replays:
            self.parse_replay(replay, self.predict_builds)
        self.predict_cluster_builds()

    def print_builds(self):
        for build in self.training_builds["Protoss"]:
            print(build)

    def train_cluster_builds(self):
        self.clustering.train(self.training_builds["Protoss"])

    def predict_cluster_builds(self):
        self.clustering.predict(self.predict_builds["Protoss"])

    def update_builds(self, player, parser, replay, build_dict):
        if len(parser.numeric_tuples) == self.max_event_parsed:
            self.success_replay.append(replay)
            if player.detail_data['race'] == 'Protoss':
                build_dict["Protoss"].append(parser.numeric_tuples)
            elif player.detail_data['race'] == 'Terran':
                build_dict["Terran"].append(parser.numeric_tuples)
            if player.detail_data['race'] == 'Zerg':
                build_dict["Zerg"].append(parser.numeric_tuples)

    def get_parser(self, player):
        race = player.detail_data['race']
        if race == 'Protoss':
            return ProtossParser(player, self.max_event_parsed)
        elif race == 'Terran':
            return TerranParser(player, self.max_event_parsed)
        else:
            return ZergParser(player, self.max_event_parsed)


'''     print('Waiting on replay loading...')
        self.thread_pool.wait_completion()
        print('Done')

        print('Replay parsing starting')
        self.thread_pool.map(self.parse_replay, self.training_replays)
        print('Waiting on replay parsing...')
        self.thread_pool.wait_completion()
        print('Done')'''
'''    def thread_loader(self, filename, replays):
        try:
            replay = SC2Factory.load_replay(self.factory, os.path.join(self.folder, filename))
            replays.append(replay)
        except UnicodeDecodeError:
            pass
        pass'''
