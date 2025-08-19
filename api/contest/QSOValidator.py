from api.contest.rules import Rules
from cabrillo.cabrillo import QSO


class QSOValidator:
    _rules: Rules

    def __int__(self, rules: Rules):
        self._rules = rules

    def validate_log(self, qso_list: list[QSO]):
        if not self._rules:
            pass

        for qso in qso_list:
            print(qso)
