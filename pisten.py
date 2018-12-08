import argparse
import re
import socket


def is_magic_packet(data):
    try:
        data = data.hex()
        prolog = data[:12]
        mac = data[12:24]
        return data == prolog + mac*16
    except:
        return False




def main(argv=None):
    parser = argparse.ArgumentParser(
            description='Forward wake-on-lan packets to the broadcast IP address.'
    )
    parser.add_argument('-p',
            metavar='port',
            default=1729,
            dest='port',
            nargs=1,
            help='The UDP port number you want to listen to (default 1729).'
    )
    parser.add_argument('-m',
            metavar='macs',
            dest='macs',
            help='A list of MAC addresses you want to exclusively listen for. '
            'Can be a file containing MAC addresses or a list in the command line. '
            'By default, forward all wake-on-lan packets.'
    )
    args = parser.parse_args(argv)
    #TODO: pass port/macs to functions

if __name__ == '__main__':
    main()
