import argparse
import socket


DEFAULT_LISTEN_PORT = 1729
DEFAULT_TARGET_PORT = 9
DEFAULT_TARGET_IP = '255.255.255.255'


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
    """
    Listens for activity on UDP port specified by listen_port and
    forwards WOL packets to (target_ip, target_port).

    """
    listen_port = kwargs.pop('listen_port', DEFAULT_LISTEN_PORT)
    target_port = kwargs.pop('target_port', DEFAULT_TARGET_PORT)
    target_ip = kwargs.pop('target_ip', DEFAULT_TARGET_IP)
    
    for kw in kwargs:
        raise TypeError('Unexpected keyword argument: {!r}'.format(kw))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', listen_port))
    while True:
        data, _ = s.recvfrom(1024)
        if extract_mac(data):
            forward(data, (target_ip, target_port))


def main(argv=None):
    parser = argparse.ArgumentParser(
            description='Forward wake-on-lan packets to the '
            'broadcast IP address.'
    )
    parser.add_argument('-L',
            metavar='listen port',
            default=DEFAULT_LISTEN_PORT,
            dest='L',
            nargs=1,
            type=int,
            help='The UDP port number you want to listen to '
            '(default 1729).'
    )
    parser.add_argument('-F',
            metavar='forward port',
            default=DEFAULT_TARGET_PORT,
            dest='F',
            nargs=1,
            type=int,
            help='The UDP port number you want to forward WOL '
            'packets to (default 9).'
    )
    parser.add_argument('-I',
            metavar='forward IP',
            default=DEFAULT_TARGET_IP,
            dest='I',
            nargs=1,
            help='The IP address you want to forward WOL packets '
            'to (default 255.255.255.255).'
    )
    args = parser.parse_args(argv)
    print(args)
    listen(listen_port=args.L,
            target_port=args.F,
            target_ip=args.I)


if __name__ == '__main__':
    main()
