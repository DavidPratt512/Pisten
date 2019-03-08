#!/usr/bin/python3
import argparse
import socket


DEFAULT_TARGET_PORT = 9
DEFAULT_TARGET_IP = '255.255.255.255'


def is_magic_packet(data):
    """
    Checks if a packet is a magic packet, returns
    True or False.

    Args:
        data (bytes): the payload from a packet

    """
    # convert data to lowercase hex string
    data = data.hex().lower()

    # magic packets begin with 'f'*12 (called a synchronization stream)
    sync = data[:12]

    if sync == 'f'*12:
        # the mac address follows (next 12 chars)
        mac = data[12:24]

        # and the mac address is repeated 16 times
        magic = sync + mac*16

        if len(data) == len(magic):
            return magic == data
        else:
            # allow for a SecureON password, which adds another
            # 12-character hex string to the end of the packet
            return magic == data[:-12]
    else:
        return False


def listen(listen_port,
           target_port=DEFAULT_TARGET_PORT,
           target_ip=DEFAULT_TARGET_IP):
    """
    Listens for activity on UDP port specified by listen_port and
    forwards WOL packets to (target_ip, target_port).

    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', listen_port))
    while True:
        data, _ = s.recvfrom(1024)
        if is_magic_packet(data):
            forward(data, target_ip, target_port)


def forward(data, ip, port):
    """
    Forwards the data to the specified IP address.

    Args:
        data (bytes): data from payload of the magic packet
        ip (str): target ip address
        port (int): target port number

    """
    # create a UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # allow it to broadcast
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect((ip, port))
    s.send(data)
    s.close()


def main(argv=None):
    parser = argparse.ArgumentParser(
            description='Forward wake-on-lan packets to the '
            'broadcast IP address.'
    )
    parser.add_argument(
        'port',
        metavar='listen port',
        type=int,
        help='The UDP port number you want to listen to.'
    )
    parser.add_argument(
        '-p',
        metavar='forward port',
        default=DEFAULT_TARGET_PORT,
        dest='fp',
        type=int,
        help='The UDP port number you want to forward WOL '
        'packets to (default 9).'
    )
    parser.add_argument(
        '-i',
        metavar='forward IP',
        default=DEFAULT_TARGET_IP,
        dest='i',
        help='The IP address you want to forward WOL packets '
        'to (default 255.255.255.255).'
    )
    args = parser.parse_args(argv)
    listen(listen_port=args.port, target_port=args.fp, target_ip=args.i)


if __name__ == '__main__':
    main()

