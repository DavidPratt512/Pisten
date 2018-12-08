import argparse
import re
import socket


def is_magic_packet(data):
    try:
        # convert data to lowercase hex string
        data = data.hex().lower()
        
        # magic packets begin with 'f'*12
        prolog = data[:12]

        if prolog == 'f'*12:
            # the mac address follows (next 12 chars)
            mac = data[12:24]
            return data == prolog + mac*16
        else:
            return False
    except:
        return False



def main(argv=None):
    parser = argparse.ArgumentParser(
            description='Forward wake-on-lan packets to the broadcast IP address.'
    )
    parser.add_argument('-p',
            metavar='port',
            default=9,
            dest='port',
            nargs=1,
            type=int,
            help='The UDP port number you want to listen to (default 9).'
    )
    parser.add_argument('-m',
            metavar='macs',
            nargs='+',
            dest='macs',
            help='A list of MAC addresses you want to exclusively listen for. '
            'By default, forward all wake-on-lan packets.'
    )
    args = parser.parse_args(argv)
    print(args)
    #TODO: pass port/macs to functions

if __name__ == '__main__':
    main()
