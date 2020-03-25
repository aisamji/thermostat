from abc import ABC, abstractmethod


class Thermostat(ABC):

    def __init__(self, address):
        self._address = address
        if not self.is_alive:
            raise ValueError(
                'Could not connect to {:s}. Ensure you have typed it '
                'correctly and that you have access to the address.'
                )

    @abstractmethod
    def is_alive(self):
        pass

    @property
    def current_temperature(self):
        return self._get_current_temperature()

    @abstractmethod
    def _get_current_temperature(self):
        pass
