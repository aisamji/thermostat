from cmd import Cmd
import sys


class ThermostatShell(Cmd):
    '''An interactive shell that can manipulate a generic WiFi thermostat.

    The shell uses a particular "strategy" to manipulate the thermostat;
    this "strategy" referes to the API and it varies according to the
    thermostat brand in use. This is accomplished by importing a different
    module for each brand.
    '''

    def __init__(self, address):
        '''Open a shell connected to the thermostat at the specified address.'''
        super(ThermostatShell, self).__init__()
        self.address = address
        self.prompt = '(thermostat@{:s}) '.format(self.address)


if __name__ == '__main__':
    try:
        ThermostatShell(sys.argv[1]).cmdloop()
    except IndexError:
        exit('Usage: thermostat [address]\nThe address is required.')
