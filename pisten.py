import argparse
import socket


DEFAULT_PORT = 9
DEFAULT_MACS = [None]


def extract_mac(data):
    """
    Checks if a packet is a magic packet, then returns 
    the corresponding MAC address. Returns None if 
    data is not from a magic packet.

    Args:
        data (bytes): the payload from a packet

    """
    try:
        # convert data to lowercase hex string
        data = data.hex().lower()
        
        # magic packets begin with 'f'*12
        prolog = data[:12]

        if prolog == 'f'*12:
            # the mac address follows (next 12 chars)
            mac = data[12:24]
            if data == prolog + mac*16:
                return mac
    except:
        return None


def listen(**kwargs):
    port = kwargs.pop('port', DEFAULT_PORT)
    macs = kwargs.pop('macs', DEFAULT_MACS)
    for kw in kwargs:
        raise TypeError('Unexpected keyword argument: {!r}'.format(kw))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', port))
    while True:
        data, _ = s.recvfrom(1024)
        mac = extract_mac(data)
        if mac not in macs:
            #forward(data)
            pass




def main(argv=None):
    parser = argparse.ArgumentParser(
            description='Forward wake-on-lan packets to the broadcast IP address.'
    )
    parser.add_argument('-p',
            metavar='port',
            default=DEFAULT_PORT,
            dest='port',
            nargs=1,
            type=int,
            help='The UDP port number you want to listen to (default 9).'
    )
    parser.add_argument('-m',
            metavar='macs',
            default=DEFAULT_MACS,
            nargs='+',
            dest='macs',
            help='A list of MAC addresses that you do not wish to wake. '
            'By default, all wake-on-lan packets will be broadcasted.'
    )
    args = parser.parse_args(argv)
    print(args)
    listen(macs=args.macs, port=args.port)


if __name__ == '__main__':
    main()
