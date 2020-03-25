#! /usr/bin/env python3
import argparse
import config
from api import create_thermostat


def configure_profile(namespace):
    old_plugin, old_address = config.default.get_profile(namespace.profile)
    plugin = input('Enter the name of the plugin to use or RETURN to keep the value [{!s:}]: '.format(old_plugin))
    if plugin == '':
        plugin = old_plugin
    address = input('Enter the address of the thermostat or RETURN to keep the value [{!s:}]: '.format(old_address))
    if address == '':
        address = old_address
    config.default.set_profile(namespace.profile, plugin=plugin, address=address)


def _generate_display_line(label, value, *, format='{!s:}'):
    line_format = '{:>19s}: ' + format
    return line_format.format(label, value)


def get_status(namespace):
    plugin, address = config.default.get_profile(namespace.profile)
    thermostat = create_thermostat(plugin, address)
    thermostat.load()

    print(_generate_display_line('Current Temperature', thermostat.current_temperature, format='{:.1f}˚F'))
    print(_generate_display_line('Operating State', thermostat.operating_state, format='{.name:}'))
    print(_generate_display_line('Program State', thermostat.program_state, format='{.name}'))
    print(_generate_display_line('Fan State', thermostat.fan_state, format='{.name}'))


if __name__ == '__main__':
    global_flags = argparse.ArgumentParser(add_help=False)
    global_flags.add_argument('-p', '--profile', default='default')

    parser = argparse.ArgumentParser()
    parser.set_defaults(func=None)
    subparsers = parser.add_subparsers()

    config_parser = subparsers.add_parser('configure', parents=[global_flags])
    config_parser.set_defaults(func=configure_profile)

    status_parser = subparsers.add_parser('status', parents=[global_flags])
    status_parser.set_defaults(func=get_status)

    namespace = parser.parse_args()
    if namespace.func is None:
        parser.print_help()
    else:
        namespace.func(namespace)
