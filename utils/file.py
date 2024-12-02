import os

from configparser import ConfigParser

def read_text(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"The file {path} was not found.")

    with open(path, 'r') as _file:
        return _file.read()


def read_ini(path: str):
    config = ConfigParser()
    config.read(path)

    return config