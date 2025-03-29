#!/usr/bin/env python3

import fcntl
import struct
import os
import time
import socket
from scapy.all import IP
from scapy.all import *

TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'tun%d', IFF_TUN | IFF_NO_PI)  # Create a TUN device without packet info
ifname_bytes = fcntl.ioctl(tun, TUNSETIFF, ifr) # Configure the interface

# Get the interface name
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

# Set up the IP address and bring the interface up
os.system("ip addr add 192.168.53.100/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))


IP_A = "0.0.0.0"
PORT = 9090
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP_A, PORT))
ip   = '10.9.0.5'
port = 10000
fds = [sock, tun]
while True:
  # this will block until at least one socket is ready
  ready, _, _ = select.select(fds, [], []) # a function that monitors multiple file descriptors (FDs) and waits until one has one ready

  for fd in ready: # now for each object within ready
    if fd is sock: # if sock has data than send that reciveve that data and send it to the tunnel
       data, (ip, port) = sock.recvfrom(2048) 
       pkt = IP(data)
       print("From socket <==: {} --> {}".format(pkt.src, pkt.dst))
       os.write(tun, data)

    if fd is tun: # hey code if tun has data avalible
       packet = os.read(tun, 2048) # read from the tun
       pkt = IP(packet) #  is a function provided by Scapy that parses raw bytes into a structured IP packet object so we may use src etc
       print("From tun    ==>: {} --> {}".format(pkt.src, pkt.dst)) # print the src and dst
       sock.sendto(packet, (ip, port)) # send to the udp server
