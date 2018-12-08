import argparse
import re
import socket




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
            help='A list of MAC addresses you want to exclusively listen for. Can be a file containing MAC addresses or a list in the command line. By default, forward all wake-on-lan packets.'
    )
    args = parser.parse_args(argv)
    #TODO: pass port/macs to functions

if __name__ == '__main__':
    main()
