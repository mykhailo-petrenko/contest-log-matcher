import re

from pyhamtools import Callinfo
from api.contest.rules import Rules
from cabrillo.cabrillo import Cabrillo, QSO
from core.qso_query import qso_query_field
from cty_plist import lookup_lib


class Scoring:
    _rules: Rules

    def __init__(self, rules: Rules):
        self._rules = rules
        self._call_info = Callinfo(lookup_lib)

    def stats(self, log: Cabrillo):
        results = dict()
        results['total'] = 0
        results['score'] = 0

        band_rules = self._rules.get_bands()

        for band_rule in band_rules:
            results[band_rule.name] = 0

        # es = re.match(regexp, band)
        for qso in log.qso:
            self.calc_qso_scores(log, qso, results)

        return results

    def _get_log_field(self, log: Cabrillo, field: str) -> str | None:
        if hasattr(log, field):
            return getattr(log, field)
        return None

    def _get_qso_field(self, qso: QSO, field: str) -> str | None:
        if field == 'get_country':
            country = self._call_info.get_country_name(qso.dx_call)
            return country
        return qso_query_field(qso, field)

    def calc_qso_scores(self, log: Cabrillo, qso: QSO, results: dict):
        points_total = 0
        multiplier_total = 1
        extra_points_total = 0

        for rule in self._rules.get_bands():
            if not re.match(rule.regexp, qso.freq):
                continue

            if rule.name not in results:
                results[rule.name] = 0

            results[rule.name] += 1
            multiplier_total *= rule.multiplier

        for rule in self._rules.get_scores():
            if rule.operator == 'regexp':
                value = self._get_qso_field(qso, rule.field)

                if value is None:
                    continue

                if not re.match(rule.regexp, value):
                    continue
            elif rule.operator == 'member_same_country':
                dx_country = self._call_info.get_country_name(qso.dx_call)
                de_country = self._call_info.get_country_name(qso.de_call)
                control_number = qso_query_field(qso, 'nr')
                is_member = re.match("[0-9]+", control_number)

                if not ((dx_country == de_country) and is_member):
                    continue
            elif rule.operator == 'member_outside_of_country':
                dx_country = self._call_info.get_country_name(qso.dx_call)
                de_country = self._call_info.get_country_name(qso.de_call)
                control_number = qso_query_field(qso, 'nr')
                is_member = re.match("[0-9]+", control_number)

                if not ((dx_country != de_country) and is_member):
                    continue
            else:
                continue

            multiplier_total = multiplier_total * rule.multiplier
            points_total = max(points_total, rule.points)

        for rule in self._rules.get_extra_points():
            if rule.operator == 'regexp':
                value = self._get_qso_field(qso, rule.field)

                if value is None:
                    value = self._get_log_field(log, rule.field)
                    if value is None:
                        continue

                if not re.match(rule.regexp, value):
                    continue
            elif rule.operator == 'member_same_country':
                dx_country = self._call_info.get_country_name(qso.dx_call)
                de_country = self._call_info.get_country_name(qso.de_call)
                control_number = qso_query_field(qso, 'nr')
                is_member = re.match("[0-9]+", control_number)

                if not ((dx_country == de_country) and is_member):
                    continue
            elif rule.operator == 'member_outside_of_country':
                dx_country = self._call_info.get_country_name(qso.dx_call)
                de_country = self._call_info.get_country_name(qso.de_call)
                control_number = qso_query_field(qso, 'nr')
                is_member = re.match("[0-9]+", control_number)

                if not ((dx_country != de_country) and is_member):
                    continue
            else:
                continue

            multiplier_total = multiplier_total * rule.multiplier
            extra_points_total = extra_points_total + rule.extra_points

        score = (points_total + extra_points_total) * multiplier_total

        results['total'] += 1
        results['score'] += score
