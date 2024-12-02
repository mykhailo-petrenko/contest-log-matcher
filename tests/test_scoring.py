import os

from api.contest.rules import Rules
from api.contest.scoring import Scoring
from cabrillo.cabrillo import QSO
from cabrillo.cabrillo.parser import parse_log_file, parse_qso
from utils.file import read_ini

base_path = os.path.dirname(__file__) + os.sep

ntcqp_valid_rules_path = base_path + 'NTCQP-rules.ini'
ntcqp_valid_rules = read_ini(ntcqp_valid_rules_path)
log_path = base_path + 'logs' + os.sep + 'DL5XL.log'

def test_apply_scores():
    rules = Rules(ntcqp_valid_rules)
    log = parse_log_file(log_path, ignore_unknown_key=True, check_categories=False)

    scoring = Scoring(rules)

    results = scoring.stats(log)

    assert results['total'] == 44
    assert results['score'] == 81
    assert results['80m'] == 23
    assert results['40m'] == 21
    assert results['20m'] == 0


def _init_qso_results(raw_qso: str) -> dict:
    valid = True

    rules = Rules(ntcqp_valid_rules)
    scoring = Scoring(rules)

    qso: QSO = parse_qso(raw_qso, valid)
    results = dict(total=0, score=0)

    scoring.calc_qso_scores(qso, results)

    return results


def test_not_a_member_qso():
    results = _init_qso_results("7032 CW 2024-03-21 1902 DL5XL         599  FELIX 80         OK2NO         599  JARDA      NM    ")

    assert results['total'] == 1
    assert results['40m'] == 1
    assert results['score'] == 1


def test_member_qso():
    results = _init_qso_results("3556 CW 2024-03-21 1956 DL5XL         599  FELIX 80         PA3EEG        599  RUUD       5  ")

    assert results['total'] == 1
    assert results['80m'] == 1
    assert results['score'] == 2


def test_club_station_qso():
    results = _init_qso_results("7032 CW 2024-03-21 1903 DL5XL         599  FELIX 80         PI4NTC        599  JO         200")

    assert results['total'] == 1
    assert results['40m'] == 1
    assert results['score'] == 3