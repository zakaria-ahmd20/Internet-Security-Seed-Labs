#!/usr/bin/python3
from scapy.all import *

def print_pkt(pkt):
    print(pkt.summary())

# Corrected sniff call
pkts = sniff(iface='ens34', filter='icmp', prn=print_pkt)
hexdump(pkts[0])
ls(pkts[0])
