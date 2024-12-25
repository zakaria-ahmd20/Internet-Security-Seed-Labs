#!/usr/bin/python3
from scapy.all import *
from scapy.layers.inet import ICMP, IP, UDP
def print_pkt(pkt):
    print(pkt.summary())
pkt=sniff(iface='br-0eb689ce017b',filter='tcp dst port 23 and src host 10.9.0.6',prn=print_pkt)
#filter='icmp'
#filter='dst net 192.168.15.0/24
