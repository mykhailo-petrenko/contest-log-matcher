from cabrillo.cabrillo.parser import parse_log_file, InvalidLogException, InvalidQSOException


def _debug_a_log():
    file = "logs/missed-report-NTCQP-March-2025.log"
    log = parse_log_file(file, ignore_unknown_key=True, check_categories=False)
    print(log.qso)
    pass


# How to validate reports?
# is it defined in the specification (pi4ntc)?


if __name__ == '__main__':
    _debug_a_log()
