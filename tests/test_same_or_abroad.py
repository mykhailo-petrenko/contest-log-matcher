import os
from configparser import ConfigParser

from api.contest.rules import Rules
from api.contest.scoring import Scoring
from cabrillo.cabrillo import QSO
from cabrillo.cabrillo.parser import parse_qso
from utils.file import read_ini

base_path = os.path.dirname(__file__) + os.sep

ntcqp_valid_rules_path = base_path + 'NTCAP.ini'
ntcqp_valid_rules = read_ini(ntcqp_valid_rules_path)


def _parse_qso(raw_qso: str, valid_rules: ConfigParser) -> dict:
    valid = True

    rules = Rules(valid_rules)
    scoring = Scoring(rules)

    qso: QSO = parse_qso(raw_qso, valid)
    results = dict(total=0, score=0)

    scoring.calc_qso_scores(qso, results)

    return results


def test_not_a_member():
    results = _parse_qso(
        "7032 CW 2024-03-21 1902 DL5XL         599  FELIX 80         OK2NO         599  JARDA      NM    ",
        ntcqp_valid_rules
    )

    assert results['total'] == 1
    assert results['40m'] == 1
    assert results['score'] == 1


def test_member_outside_of_country():
    """
    NTC members inside your own country 6
    :return:
    """
    results = _parse_qso(
        "40m CW 2024-03-21 1903 PI4NTC         599  FELIX 80         PD5MI        599  MIKE       204",
        ntcqp_valid_rules
    )

    assert results['total'] == 1
    assert results['40m'] == 1
    assert results['score'] == 6


def test_member_same_country():
    """
    NTC members outside your country 9
    :return:
    """
    results = _parse_qso(
        "3556 CW 2024-03-21 1956 DL5XL         599  FELIX 80         OK2NO        599  Jaroslav   5  ",
        ntcqp_valid_rules
    )

    assert results['total'] == 1
    assert results['80m'] == 1
    assert results['score'] == 9


def test_ntcap_club_station_qso():
    results = _parse_qso(
        "7032 CW 2024-03-21 1903 DL5XL         599  FELIX 80         PI4NTC        599  JO         200",
        ntcqp_valid_rules
    )

    assert results['total'] == 1
    assert results['40m'] == 1
    assert results['score'] == 15
