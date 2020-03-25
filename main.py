import argparse
import config


def configure_profile(namespace):
    old_plugin, old_address = config.default.get_profile(namespace.profile)
    plugin = input('Enter the name of the plugin to use or RETURN to keep the value [{!s:}]: '.format(old_plugin))
    if plugin == '':
        plugin = old_plugin
    address = input('Enter the address of the thermostat or RETURN to keep the value [{!s:}]: '.format(old_address))
    if address == '':
        address = old_address
    config.default.set_profile(namespace.profile, plugin=plugin, address=address)


if __name__ == '__main__':
    global_flags = argparse.ArgumentParser(add_help=False)
    global_flags.add_argument('-p', '--profile', default='default')

    parser = argparse.ArgumentParser()
    parser.set_defaults(func=None)
    subparsers = parser.add_subparsers()

    config_parser = subparsers.add_parser('configure', parents=[global_flags])
    config_parser.set_defaults(func=configure_profile)

    namespace = parser.parse_args()
    if namespace.func is None:
        parser.print_help()
    else:
        namespace.func(namespace)
