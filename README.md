# Pisten
**Pisten** (Pi + Listen) is a simple port listener that will forward valid wake-on-lan packets to the broadcast IP address.
Pisten is best suited for use on always-on, low-power devices, such as the Raspberry Pi.

Some routers do not allow port forwarding to the broadcast IP address which necessitates the use of this program. 
Also, it is generally safer to filter out unwanted packets before forwarding to the broadcast IP.


## Usage
On linux, you can use 
```
nohup python3 pisten.py &
```
to run the server.
By default, the server listens on port 1729 and forwards to 255.255.255.255:9.

You can specify what port to listen to and what IP address/port to forward to:
```
python3 pisten.py -L 3141 -F 0 -I 127.127.127.127
```
In this case, we are (-L)istening on port 3141, (-F)orwarding to port 0 and (-I)P address 127.127.127.127.

Alternatively, you could use the `listen` function in your own Python script.
```python
from pisten import listen

listen(listen_port=3141, target_port=0)
```


## Set up port forwarding
All routers can be configured to forward packets from specific ports to specific devices on your network.
You will want to forward a public UDP port of your choice to port 1729 (or whatever port you specify) of the IP address of your server.
You may want to consider creating a DHCP reservation for your server as well.

