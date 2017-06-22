import sys
from ReplayParser import ReplayParser


def main():
    path = sys.argv[1]
    parser = ReplayParser(path=path, max_replay_load=10, max_event_parsed=125)
    parser.run()


if __name__ == '__main__':
    main()
