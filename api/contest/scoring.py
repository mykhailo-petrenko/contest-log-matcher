import re

from api.contest.rules import Rules
from cabrillo.cabrillo import Cabrillo, QSO


class Scoring:
    _rules: Rules

    def __init__(self, rules: Rules):
        self._rules = rules


    def stats(self, log: Cabrillo):
        results = dict()
        results['total'] = 0
        results['score'] = 0

        band_rules = self._rules.get_bands()

        for band_rule in band_rules:
            results[band_rule.name] = 0

        # es = re.match(regexp, band)
        for qso in log.qso:
            self.calc_qso_scores(qso, results)

        return results

    def calc_qso_scores(self, qso: QSO, results: dict):
        print(qso)
        score = 1

        for rule in self._rules.get_bands():
            if not re.match(rule.regexp, qso.freq):
                continue

            if rule.name not in results:
                results[rule.name] = 0

            results[rule.name] += 1
            score *= rule.multiplier
            break

        scores_multiplier = 1
        for rule in self._rules.get_scores():
            value = ''

            if rule.field == 'dx_call':
                value = qso.dx_call

            if rule.field == 'dx_exch[2]':
                value = qso.dx_exch[2]

            if not re.match(rule.regexp, value):
                continue

            scores_multiplier = max(scores_multiplier, rule.multiplier)

        score *= scores_multiplier

        results['total'] += 1
        results['score'] += score

