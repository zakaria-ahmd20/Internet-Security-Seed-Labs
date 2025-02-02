#!/usr/bin/python3
import socket
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = b"WHAT ARE THOSE 1\n"
udp.sendto(data,("192.168.15.195", 9090))
