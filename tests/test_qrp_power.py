import os

from api.contest.rules import Rules
from api.contest.scoring import Scoring
from cabrillo.cabrillo.parser import parse_log_file
from utils.file import read_ini

base_path = os.path.dirname(__file__) + os.sep

ntcqp_valid_rules_path = base_path + 'NTCQP-power-rules.ini'
ntcqp_valid_rules = read_ini(ntcqp_valid_rules_path)

log_path_qrp = base_path + 'logs' + os.sep + 'POWER_QRP.log'
log_path_low = base_path + 'logs' + os.sep + 'POWER_LOW.log'


def _get_stats(log_path: str) -> dict[str, int]:
    rules = Rules(ntcqp_valid_rules)
    log = parse_log_file(log_path, ignore_unknown_key=True, check_categories=False)

    scoring = Scoring(rules)

    return scoring.stats(log)


def test_qrp_power():
    scores = _get_stats(log_path_qrp)
    assert scores.get('score') == 21


def test_low_power():
    scores = _get_stats(log_path_low)
    assert scores.get('score') == 6

