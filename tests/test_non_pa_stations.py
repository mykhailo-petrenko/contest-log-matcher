import os
from configparser import ConfigParser

from api.contest.rules import Rules
from api.contest.scoring import Scoring
from cabrillo.cabrillo import QSO, Cabrillo
from cabrillo.cabrillo.parser import parse_qso
from utils.file import read_ini

base_path = os.path.dirname(__file__) + os.sep

ntcqp_non_pa_rules = read_ini(base_path + 'NTCQP-country-NOT-NL.ini')


def _parse_qso(raw_qso: str, valid_rules: ConfigParser) -> dict:
    log = Cabrillo()
    valid = True

    rules = Rules(valid_rules)
    scoring = Scoring(rules)

    qso: QSO = parse_qso(raw_qso, valid)
    results = dict(total=0, score=0)

    scoring.calc_qso_scores(log, qso, results)

    return results


def test_non_pa_not_a_member_not_dutch():
    results = _parse_qso(
        "7032 CW 2024-03-21 1902 DL5XL         599  FELIX 80         OK2NO         599  JARDA      NM    ",
        ntcqp_non_pa_rules
    )

    assert results['total'] == 1
    assert results['40m'] == 1
    assert results['score'] == 2


def test_non_pa_member_not_dutch():
    results = _parse_qso(
        "3556 CW 2024-03-21 1956 DL5XL         599  FELIX 80         OK2NO        599  RUUD       5  ",
        ntcqp_non_pa_rules
    )

    assert results['total'] == 1
    assert results['80m'] == 1
    assert results['score'] == 3


def test_non_pa_member_and_dutch():
    results = _parse_qso(
        "7032 CW 2024-03-21 1903 DL5XL         599  FELIX 80         PD5MI        599  JO         204",
        ntcqp_non_pa_rules
    )

    assert results['total'] == 1
    assert results['40m'] == 1
    assert results['score'] == 2


def test_non_pa_special_member_and_dutch():
    results = _parse_qso(
        "7032 CW 2024-03-21 1903 DL5XL         599  FELIX 80         PI4NTC        599  JO         200",
        ntcqp_non_pa_rules
    )

    assert results['total'] == 1
    assert results['40m'] == 1
    assert results['score'] == 3
