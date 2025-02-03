from abc import abstractmethod, ABC
from typing import Any

import re

from pyhamtools import Callinfo

from cabrillo.cabrillo import QSO
from core.qso_query import qso_query_field
from cty_plist import lookup_lib


class Operator(ABC):
    def __int__(self, attributes: dict):
        self.attributes = attributes
        self.parameters = None

    @abstractmethod
    def execute(self, qso: QSO) -> Any:
        pass


class CompositeOperator(Operator):
    def __init__(self, attributes: dict, parameters: list[Operator]):
        self.attributes = attributes
        self.parameters = parameters

    @abstractmethod
    def execute(self, qso: QSO) -> bool:
        pass


class AndOperator(CompositeOperator):
    def execute(self, qso: QSO) -> bool:
        n = len(self.parameters)

        if n == 0:
            return False

        for i in range(0, n):
            if not self.parameters[i].execute(qso):
                return False

        return True


class EqualOperator(CompositeOperator):
    def execute(self, qso: QSO) -> bool:
        n = len(self.parameters)

        if n == 0:
            return False

        first = self.parameters[0].execute(qso)

        for i in range(1, n):
            if first != self.parameters[i].execute(qso):
                return False

        return True


class NotEqualOperator(CompositeOperator):
    def __init__(self, attributes: dict, parameters: list[Operator]):
        super().__init__(attributes, parameters)

        if len(parameters) != 2:
            raise AttributeError("Not Equal should have 2 parameters.")

    def execute(self, qso: QSO) -> bool:
        return self.parameters[0].execute(qso) != self.parameters[1].execute(qso)


class RegexOperator(Operator):
    def execute(self, qso: QSO):
        field_name = self.attributes.get('field')
        regexp = self.attributes.get('regexp')
        value = qso_query_field(qso, field_name)  # @TODO: field getter

        return re.match(regexp, value)


class GetCountryOperator(Operator):
    def __init__(self, attributes: dict):
        super().__init__(attributes)
        self._call_info = Callinfo(lookup_lib)

    def execute(self, qso: QSO):
        field_name = self.attributes.get('field')
        value = qso_query_field(qso, field_name)
        country = self._call_info.get_country_name(value)

        return country
