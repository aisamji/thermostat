class ThermostatError(Exception):
    pass


class ThermostatPluginError(ThermostatError):

    def __init__(self, name):
        super().__init__('Something is wrong with the {!r:} plugin.'.format(name))


class MissingPluginError(ThermostatPluginError):

    def __init__(self, name):
        super().__init__('No plugin named {!r:} exists.'.format(name))


class MisconfiguredPluginError(ThermostatPluginError):

    def __init__(self, name):
        super().__init__('The plugin for the {!r:} is broken.'.format(name))
