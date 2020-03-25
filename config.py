import configparser
import os


class Configuration:

    default_config_file = os.path.join('~', '.config', 'thermostat')
    config_file = os.path.expanduser(os.environ.get('THERMOSTAT_CONFIG', default_config_file))

    PLUGIN_TYPE_KEY = 'plugin'
    ADDRESS_KEY = 'address'

    def __init__(self):
        self._data = configparser.ConfigParser()
        self._data.read(self.config_file)

    def get_profile(self, name):
        try:
            name = str(name)
            plugin = self._data.get(name, self.PLUGIN_TYPE_KEY)
            address = self._data.get(name, self.ADDRESS_KEY)
            if plugin == '':
                plugin = None
            if address == '':
                address = None
            return plugin, address
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None, None

    def set_profile(self, name, *, plugin, address):
        try:
            name = str(name)
            self._data.set(name, self.PLUGIN_TYPE_KEY, plugin)
            self._data.set(name, self.ADDRESS_KEY, address)
            with open(self.config_file, 'w') as file:
                self._data.write(file)
        except configparser.NoSectionError:
            self._data.add_section(name)
            self.set_profile(name, plugin=plugin, address=address)


default = Configuration()
