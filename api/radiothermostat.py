from urllib.request import urlopen
import json
from enum import IntEnum
from . import _abstract

PROTOCOL = 'http://'

ENDPOINT_STATUS = '/tstat'
ENDPOINT_HEALTH = '/sys'

KEY_CURRENT_TEMPERATURE = 'temp'
KEY_OPERATING_STATE = 'tstate'


class Thermostat(_abstract.Thermostat):

    def __init__(self, address):
        super().__init__(address)
        self._data = {}

    def is_alive(self):
        try:
            urlopen(PROTOCOL + self._address + ENDPOINT_HEALTH)
            return True
        except Exception:
            return False

    def load(self):
        self._data = json.load(urlopen(PROTOCOL + self._address + ENDPOINT_STATUS))

    def _get_current_temperature(self):
        try:
            return float(self._data[KEY_CURRENT_TEMPERATURE])
        except KeyError:
            return 0.0

    def _get_operating_state(self):
        return HvacMode(int(self._data[KEY_OPERATING_STATE]))


class HvacMode(IntEnum):
    OFF = 0
    COOL = 1
    HEAT = 2
    AUTO = 3
