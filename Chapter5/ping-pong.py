#!/usr/bin/python3
from scapy.all import *

ip = IP(src="192.168.15.210", dst="192.168.15.195")
udp = UDP(sport=9090, dport=9090)
data = "ping 0-> pong"
pkt = ip/udp/data  # Data is used as the payload
send(pkt, verbose=0)  
