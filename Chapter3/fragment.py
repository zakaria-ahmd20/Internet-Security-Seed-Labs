from scapy.all import *
from scapy.layers.inet import ICMP, IP, UDP,TCP

#!/usr/bin/python3

ID = 1000
dst_ip = "192.168.15.210"

#fragment #1
#----------------------#
ip = IP(dst=dst_ip,id=ID, frag=0, flags=1) # first fragment , # set to allow fragments
udp = UDP(sport=7070,dport=9090, chksum=0) #
udp.len(8+32+40+20) # header is 8 bytes
payload= "A" * 31 + "\n" # 32 bytes of data
#frag = (32+8)/8 = 5
pkt1 = ip/udp/payload
#fragment #2
#----------------------#
ip = IP(dst=dst_ip,id=ID, frag=5, flags=1) # 2 fragment , # set to allow fragments
ip.proto = 17
payload= "B" * 39 + "\n" # 40 bytes of data
#frag = (40+40)/8 = 10

pkt2 = ip/payload

#fragment #3
#----------------------#
ip = IP(dst=dst_ip,id=ID, frag=10, flags=0) # 2 fragment , # set to allow fragments
ip.proto = 17
payload= "C" * 19 + "\n" # 40 bytes of data
pkt3 = ip/payload

# send it out
send(pkt1)
send(pkt2)
send(pkt3)



