from cabrillo.cabrillo import QSO


def qso_query_field(qso: QSO, field: str) -> str | None:
    field = field.lower()

    if field in ['freq', 'frequency']:
        return qso.freq

    if field in ['mo', 'mode']:
        return qso.mo

    if field == 'date':
        return qso.date

    if field == 'de_call':
        return qso.de_call

    if field == 'valid':
        return qso.valid

    if field == 'dx_call':
        return qso.dx_call

    if field in ['dx_exch[0]', 'rprt', 'report'] and len(qso.dx_exch) >= 1:
        return qso.dx_exch[0]

    if field in ['dx_exch[1]'] and len(qso.dx_exch) >= 2:
        return qso.dx_exch[1]

    if field in ['dx_exch[2]', 'nr'] and len(qso.dx_exch) >= 3:
        return qso.dx_exch[2]

    return None
