#!/bin/env python3

import socket 
data = b"Hello, Server \n"
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.sendto(data,("192.168.15.1",9090))
