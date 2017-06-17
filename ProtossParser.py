# This file contains parsing functions for Protoss build orders

from RaceParser import RaceParser


class ProtossParser(RaceParser):
    def __init__(self, player, max_tuples=50):
        super().__init__(player, max_tuples)
        self.name = "protoss parser"
        self.events_to_accept = {
            # Units
            "Probe",            "Zealot",           "Stalker",
            "Sentry",           "Observer",         "Immortal",
            "WarpPrism",        "Colossus",         "Phoenix",
            "VoidRay",          "HighTemplar",      "DarkTemplar",
            "Archon",           "Carrier",          "Mothership",
            "MothershipCore",   "Oracle",           "Tempest",
            "Adept",            "Disruptor",

            # Buildings
            "Nexus",            "Pylon",            "Gateway",
            "CyberneticsCore",  "Forge",            "PhotonCannon",
            "TwilightCouncil",  "Stargate",         "TemplarArchive",
            "DarkShrine",       "FleetBeacon",      "RoboticsBay",
            "RoboticsFacility", "Assimilator",
        }

    def unit_to_numeric_value(self, name):
        build_map = {
            # Units
            "Probe": 1,             "Zealot": 2,            "Stalker": 3,
            "Sentry": 4,            "Observer": 5,          "Immortal": 6,
            "WarpPrism": 7,         "Colossus": 8,          "Phoenix": 9,
            "VoidRay": 10,          "HighTemplar": 11,      "DarkTemplar": 12,
            "Archon": 13,           "Carrier": 14,          "Mothership": 15,
            "MothershipCore": 16,   "Oracle": 17,           "Tempest": 18,
            "Adept": 19,            "Disruptor": 20,

            # Buildings
            "Nexus": 21,            "Pylon": 22,            "Gateway": 23,
            "CyberneticsCore": 24,  "Forge": 25,            "PhotonCannon": 26,
            "TwilightCouncil": 27,  "Stargate": 28,         "TemplarArchive": 29,
            "DarkShrine": 30,       "FleetBeacon": 31,      "RoboticsBay": 32,
            "RoboticsFacility": 33, "Assimilator": 34
        }
        return build_map[name]