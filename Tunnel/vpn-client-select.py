#!/usr/bin/env python3

import fcntl
import struct
import os
import time
from scapy.all import *

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000

# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'tun%d', IFF_TUN | IFF_NO_PI)
ifname_bytes  = fcntl.ioctl(tun, TUNSETIFF, ifr)

# Get the interface name
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

# Configure the interface
os.system("ip addr add 192.168.53.99/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))
os.system("ip route add 192.168.60.0/24 dev {}".format(ifname))

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
fds = [sock, tun] # list of files we need to poll between
while True: # initialize our first loop
  # this will block until at least one socket is ready
  ready, _, _ = select.select(fds, [], [])   # block until one of the file descriptors (sock or tun) has data

  for fd in ready:  # for  each file within our list
    if fd is sock:# once the script finds that there is data if it wil ...
       data, (ip, port) = sock.recvfrom(2048) # store some values in these varaibles using tuple unpcaking
       pkt = IP(data) # Converting raw data into a Scapy IP packet
       print("From socket <==: {} --> {}".format(pkt.src, pkt.dst)) # print the src of packet and its dest
       os.write(tun, data) # write the raw data to the packet

    if fd is tun: # if tun has data avalible
       packet = os.read(tun, 2048)  # read  data from the tun and store it
       pkt = IP(packet)  #Converting raw data into a Scapy IP packet
       print("From tun    ==>: {} --> {}".format(pkt.src, pkt.dst)) # # print the src of packet and its dest
       sock.sendto(packet, ('10.9.0.11', 9090) # send ito the vpn server.
