import sys
from ReplayParser import ReplayParser


def main():
    path = sys.argv[1]
    parser = ReplayParser(path=path)
    parser.parse()


if __name__ == '__main__':
    main()
