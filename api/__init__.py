import importlib
from . import exceptions


def create_plugin(name, address):
    try:
        if name == '_abstract':
            raise ModuleNotFoundError()
        api = importlib.import_module('.' + name, __package__)
        thermostat = api.Thermostat(address)
        thermostat.is_alive()
        return thermostat
    except ModuleNotFoundError:
        raise exceptions.MissingPluginError(name) from None
    except AttributeError:
        raise exceptions.MisconfiguredPluginError(name) from None  # Keep the full stack trace for this one.
    except TypeError:
        raise exceptions.MissingPluginError(name)  # Keep the full stack trace for this one.
