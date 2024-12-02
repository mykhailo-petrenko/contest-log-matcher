from configparser import ConfigParser


class Rule:
    name: str
    field: str
    regexp: str
    multiplier: int = 1

    def __init__(self, name: str, field: str, regexp: str, multiplier: int = 1):
        self.name = name
        self.field = field
        self.regexp = regexp
        self.multiplier = multiplier


class Rules:
    isValid: bool
    _config: ConfigParser

    def __init__(self, config: ConfigParser):
        self._config = config
        self.isValid = False
        self._validate()

    @property
    def start_date(self):
        return self._config['contest']['start_date']

    @property
    def end_date(self):
        return self._config['contest']['end_date']

    @property
    def start_hour(self):
        return self._config['contest']['start_hour']

    @property
    def end_hour(self):
        return self._config['contest']['end_hour']

    @property
    def bands(self):
        return int(self._config['contest']['bands'])

    @property
    def scores(self):
        return int(self._config['contest']['scores'])

    def band(self, band_id: int) -> Rule:
        _config = self._config[f"band{band_id}"]

        return Rule(
            _config['name'],
            'band',
            _config['regexp'],
            int(_config['multiplier']),
        )

    def score(self, score_id: int) -> Rule:
        _config = self._config[f"score{score_id}"]

        return Rule(
            _config['name'],
            _config['field'],
            _config['regexp'],
            int(_config['multiplier']),
        )

    def get_bands(self):
        _bands = []

        for i in range(1, self.bands+1):
            _bands.append(self.band(i))

        return _bands

    def get_scores(self):
        _scores = []

        for i in range(1, self.scores+1):
            _scores.append(self.score(i))

        return _scores

    def _validate(self):
        if not self._config.has_section('contest'):
            self.isValid = False
            return

        if not self._config.has_section('band1'):
            self.isValid = False
            return

        if not self._config.has_section('score1'):
            self.isValid = False
            return

        self.isValid = True
