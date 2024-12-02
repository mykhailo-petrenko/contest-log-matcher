import os
from utils.file import read_ini


def get_contest_rules_config():
    path_to_config = os.path.dirname(__file__) + os.path.sep + 'NTCQP-2024-December.ini'
    config = read_ini(path_to_config)

    return config