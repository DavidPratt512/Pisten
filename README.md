# Pisten
**Pisten** (Pi + Listen) is a simple port listener that will forward valid wake-on-lan packets to the broadcast IP address.
Pisten allows for wake-on-lan packets with a SecureON password to be forwarded as well.
Pisten is best suited for use on always-on, low-power devices, such as the Raspberry Pi.
 
Pisten filters out any non-magic packet before forwarding to the broadcast address.
This is generally safer than configuring a router to forward _anything_ to the broadcast address.


## Installation
**Pisten requires Python 3.**

You can install pisten using pip:
```
python3 -m pip install pisten
```
Or you can clone this repository:
```
git clone https://github.com/davidpratt512/pisten.git
```


## Usage
On linux, you can use 
```
nohup pisten 1729 &
```
to run the server (if your path includes your python scripts).
By default, the server forwards to 255.255.255.255, port 9.
You need to specify a port to listen to.
In the case above, we are listening on port 1729.

You can specify what IP address and port to forward to:
```
pisten 1729 -p 7 -i 10.0.1.255
```
In this case, we are listening on port 1729 and forwarding to 10.0.1.255:7.
