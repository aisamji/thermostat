from cmd import Cmd
import sys
import os
import importlib


CONFIG_DIR = os.path.expanduser(os.path.join('~', '.thermostat'))
KNOWN_THERMOSTATS_FILE = os.path.join(CONFIG_DIR, 'known_thermostats')


class ThermostatShell(Cmd):
    '''An interactive shell that can manipulate a generic WiFi thermostat.

    The shell uses a particular "strategy" to manipulate the thermostat;
    this "strategy" refers to the API and it varies according to the
    thermostat brand in use. This is accomplished by importing a different
    module for each brand.
    '''

    def __init__(self, address):
        '''Open a shell connected to the thermostat at the specified address.'''
        super(ThermostatShell, self).__init__()
        self._address = address
        self._strategy = self._get_strategy(self._address)

        try:
            plugin = importlib.import_module(self._strategy)
            self._thermostat = plugin.Thermostat(self._address)
        except ModuleNotFoundError:
            exit('No plugin available for {!r:}.'.format(self._strategy))
        except AttributeError:
            exit('Plugin for {!r:} is broken.'.format(self._strategy))

        self.prompt = '({:s}@{:s}) '.format(self._strategy, self._address)

    @staticmethod
    def _get_strategy(address):
        try:
            with open(KNOWN_THERMOSTATS_FILE, 'r') as file:
                for line in file:
                    if line.strip() == '':
                        continue
                    known_address, known_strategy = line.split()
                    if known_address == address:
                        return known_strategy
                raise KeyError
        except (FileNotFoundError, KeyError):
            brand = input(
                'You are connecting to this thermostat for the first time.\n'
                'Please specify enter the brand of the thermostat: '
                )
            os.makedirs(CONFIG_DIR, exist_ok=True)
            with open(KNOWN_THERMOSTATS_FILE, 'a') as file:
                file.write('{:s} {:s}\n'.format(address, brand))
            return brand

    def do_exit(self, arg):
        '''Exit the shell.'''
        return True


if __name__ == '__main__':
    try:
        ThermostatShell(sys.argv[1]).cmdloop()
    except IndexError:
        exit('Usage: thermostat [address]\nThe address is required.')
