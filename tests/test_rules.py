import os
from api.contest.rules import Rules
from utils.file import read_ini

ntcqp_valid_rules_path = os.path.dirname(__file__) + os.sep + 'NTCQP-Dec-rules.ini'
ntcqp_valid_rules = read_ini(ntcqp_valid_rules_path)


def test_is_valid():
    rules = Rules(ntcqp_valid_rules)

    assert rules.isValid


def test_contest_params():
    rules = Rules(ntcqp_valid_rules)

    assert rules.start_date == "20240321"
    assert rules.end_date == "20240321"
    assert rules.start_hour == "1800"
    assert rules.end_hour == "2100"
    assert rules.bands == 3
    assert rules.scores == 3
    assert rules.extra_points == 1


def test_bands():
    rules = Rules(ntcqp_valid_rules)

    assert rules.band(1).name == '80m'
    assert rules.band(2).name == '40m'
    assert rules.band(3).name == '20m'

    assert len(rules.get_bands()) == 3


def test_scores():
    rules = Rules(ntcqp_valid_rules)

    assert rules.score(1).name == 'Club Station'
    assert rules.score(2).name == 'Member'
    assert rules.score(3).name == 'NM'

    assert len(rules.get_scores()) == 3


def test_extra_points():
    rules = Rules(ntcqp_valid_rules)

    assert rules.extra_point(1).name == 'Callsign of the month'
    assert len(rules.get_extra_points()) == 1
