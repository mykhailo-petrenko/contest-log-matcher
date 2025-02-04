from os import path

VERSION_FILE = path.join(path.dirname(__file__), "../", "version.txt")


def version():
    with open(VERSION_FILE, 'r') as version_file:
        return version_file.readline().strip()

