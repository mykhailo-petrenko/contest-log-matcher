from configparser import ConfigParser


class Rule:
    name: str
    field: str
    regexp: str
    multiplier: int = 1
    points: int = 0
    extra_points: int = 0

    def __init__(
            self,
            name: str,
            field: str,
            regexp: str,
    ):
        self.name = name
        self.field = field
        self.regexp = regexp


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

    @property
    def extra_points(self):
        return int(self._config['contest']['extra_points'])

    def band(self, band_id: int) -> Rule:
        _config = self._config[f"band{band_id}"]

        rule = Rule(
            _config['name'],
            'band',
            _config['regexp']
        )

        rule.multiplier = int(_config['multiplier'])

        return rule

    def score(self, score_id: int) -> Rule:
        _config = self._config[f"score{score_id}"]

        rule = Rule(
            _config['name'],
            _config['field'],
            _config['regexp'],
        )

        rule.multiplier = int(_config['multiplier'])
        rule.points = int(_config['points'])

        return rule

    def extra_point(self, extra_point_id: int) -> Rule | None:
        key = f"extra_point{extra_point_id}"

        if key not in self._config:
            return None

        _config = self._config[key]

        rule = Rule(
            _config['name'],
            _config['field'],
            _config['regexp'],
        )

        rule.multiplier = int(_config['multiplier'])
        rule.extra_points = int(_config['extra_points'])

        return rule

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

    def get_extra_points(self):
        _extra_points = []

        for i in range(1, self.extra_points+1):
            _extra_points.append(self.extra_point(i))

        return _extra_points

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
