# Pisten
**Pisten** (Pi + Listen) is a simple port listener that will forward valid wake-on-lan packets to the broadcast IP address.
Pisten allows for wake-on-lan packets with a SecureON password to be forwarded as well.
Pisten is best suited for use on always-on, low-power devices, such as the Raspberry Pi.
 
Pisten filters out any non-magic packet before forwarding to the broadcast address.
This is generally safer than configuring a router to forward _anything_ to the broadcast address.


## Usage
On linux, use 
```
nohup python3 pisten.py <port> &
```
to have the server listen on whichever port you specify.
By default, the server forwards to 255.255.255.255 port 9.

You can override the defaults like so:
```
nohup python3 pisten.py 1729 -p 7 -i 10.0.1.255
```
In this case, we are listening on port 1729 and forwarding to 10.0.1.255:7.
