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

    @property
    def operating_state(self):
        return self._get_operating_state()

    @abstractmethod
    def _get_operating_state(self):
        pass

    @property
    def program_state(self):
        return self._get_program_state()

    @abstractmethod
    def _get_program_state(self):
        pass

    @property
    def fan_state(self):
        return self._get_fan_state()

    @abstractmethod
    def _get_fan_state(self):
        pass
