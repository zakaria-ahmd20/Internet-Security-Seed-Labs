#!/usr/bin/python3
from scapy.all import *
from scapy.layers.inet import ICMP, IP, UDP


def spoof_pkt(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8:
        print('Original packet:')
        print('Source IP:', pkt[IP].src)
        print('Destination IP:', pkt[IP].dst)
        # Corrected the order of source and destination IP addresses
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src, ihl=pkt[IP].ihl)
        icmp = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
        # Ensure Raw layer is checked before accessing it
        data = pkt[Raw].load
        newpkt = ip / icmp / data
        print('Spoofed packet has been made:')
        print('Source IP:', newpkt[IP].src)
        print('Destination IP:', newpkt[IP].dst)

        # Sending the spoofed packet
        send(newpkt, verbose=0)


# Sniff for ICMP packets from the specific host (outside of spoof_pkt)
sniff(filter='icmp and src host 192.168.15.195', prn=spoof_pkt)
