#!/usr/bin/python3

from scapy.all import *
import random

# Network broadcast address (adjust for your network)
target_ip = "192.168.15.255"  # Broadcast to all hosts in subnet
target_port = 19  # Echo service (or use 19 for Chargen)

# Source IP (can be spoofed or real)
src_ip = "192.168.15.179"

# Construct the UDP packet
udp_packet = IP(src=src_ip, dst=target_ip) / \
             UDP(sport=11, dport=target_port) / \
             Raw(load="Test Packet")

print("Sending 1 packet to", target_ip)

# Send a single UDP packet
send(udp_packet, verbose=True)

# Listen for 4 response packets
