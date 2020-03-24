class ThermostatAPIError(Exception):
    pass


class MissingPluginError(ThermostatAPIError):

    def __init__(self, name):
        super().__init__('No plugin named {:s} exists.'.format(name))


class MisconfiguredPluginError(ThermostatAPIError):

    def __init__(self, name):
        super().__init__('The plugin for the {:s} is broken.'.format(name))
