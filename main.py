import sys
from ReplayParser import ReplayParser


def main():
    path = sys.argv[1]
    parser = ReplayParser(path=path, max_replay_load=50, max_event_parsed=75)
    parser.run()


if __name__ == '__main__':
    main()
