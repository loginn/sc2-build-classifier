# This file contains parsing functions for Protoss build orders
from sc2reader.engine import PluginExit

from RaceParser import RaceParser


class ProtossParser(RaceParser):
    def __init__(self, player, max_tuples=50):
        super().__init__(player)
        self.max_tuples = max_tuples
        self.name = "protoss parser"
        self.build_tuples = []
        self.event_count = 0

    def gen_build_tuple(self, event):
        build_tuple = (self.player.supply_used, event.unit_type_name)
        self.build_tuples.append(build_tuple)
        if len(self.build_tuples) >= self.max_tuples:
            print(len(self.build_tuples), self.build_tuples)
            return self.unregister_self()
        return None

    def unregister_self(self):
        return PluginExit(self, code=0, details=dict(msg="vector filled"))

    def handleUnitInitEvent(self, event, replay):
        self.event_count += 1
        if event.control_pid == self.player.pid and (self.player.supply_used > 12 or self.event_count > 300):
            e = self.gen_build_tuple(event)
            if e is not None:
                yield(e)

    def handleUnitBornEvent(self, event, replay):
        self.event_count += 1
        if event.control_pid == self.player.pid and (self.player.supply_used > 12 or self.event_count > 300):
            e = self.gen_build_tuple(event)
            if e is not None:
                yield(e)
