import os
from utils.file import read_ini

VALID_CONTESTS_ID = [
    'NTCQP-2024-December',
    'NTCQP-2025-01',
    'NTCAP-2025-31',
    'NTCQP-2025-02',
    'NTCQP-2025-03',
    'NTCQP-2025-04',
    'NTCQP-2025-05',
    'NTCQP-2025-06',
    'NTCQP-2025-07',
]


def get_contest_rules_config(contest_id=None):
    if contest_id not in VALID_CONTESTS_ID:
        return None

    path_to_config = os.path.dirname(__file__) + os.path.sep + f'{contest_id}.ini'
    config = read_ini(path_to_config)

    return config
