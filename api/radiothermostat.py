from urllib.request import urlopen
import json
from . import _abstract

PROTOCOL = 'http://'

ENDPOINT_STATUS = '/tstat'
ENDPOINT_HEALTH = '/sys'

KEY_CURRENT_TEMPERATURE = 'temp'


class Thermostat(_abstract.Thermostat):

    def is_alive(self):
        try:
            urlopen(PROTOCOL + self._address + ENDPOINT_HEALTH)
            return True
        except Exception:
            return False

    def _load(self):
        self._data = json.load(urlopen(PROTOCOL + self._address + ENDPOINT_STATUS))

    def _get_current_temperature(self):
        self._load()
        return float(self._data[KEY_CURRENT_TEMPERATURE])
