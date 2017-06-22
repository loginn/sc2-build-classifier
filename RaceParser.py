from sc2reader.engine import PluginExit


class RaceParser(object):
    def __init__(self, player, max_tuples=50):
        self.player = player
        self.build_tuples = []
        self.numeric_tuples = []
        self.max_tuples = max_tuples
        self.events_to_accept = {}

    def gen_build_tuple(self, event):
        build_tuple = (self.player.supply_used, event.unit_type_name)
        numeric_tuple = (self.player.supply_used, self.unit_to_numeric_value(event.unit_type_name))
        self.build_tuples.append(build_tuple)
        self.numeric_tuples.append(numeric_tuple)

    def unregister_self(self):
        return PluginExit(self, code=0, details=dict(msg="vector filled"))

    def event_handler(self, event):
        if len(self.numeric_tuples) >= self.max_tuples:
            # print('--- Parsing Build Done ---')
            return self.unregister_self()
        elif event.unit_type_name in self.events_to_accept and event.control_pid == self.player.pid:
            self.gen_build_tuple(event)
        return None

    def handleUnitInitEvent(self, event, replay):
        e = self.event_handler(event)
        if e is not None:
            yield (e)

    def handleUnitBornEvent(self, event, replay):
        e = self.event_handler(event)
        if e is not None:
            yield (e)

    def unit_to_numeric_value(self, name):
        pass


'''        self.events_to_ignore = {
            "BeaconArmy", "BeaconDefend", "BeaconAttack", "BeaconHarass",
            "BeaconIdle", "BeaconAuto", "BeaconDetect", "BeaconScout",
            "BeaconClaim", "BeaconExpand", "BeaconRally", "BeaconCustom1",
            "BeaconCustom2", "BeaconCustom3", "BeaconCustom4", "BeaconCustom5",
            "AdeptPhaseShift"
        }
'''