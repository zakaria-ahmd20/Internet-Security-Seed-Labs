#!/usr/bin/python3
from scapy.all import *

def print_pkt(pkt):
    print(pkt.summary())

# Corrected sniff call
pkt = sniff(iface='ens34', filter='icmp', prn=print_pkt)
