import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a udp socket
udp.bind(('0.0.0.0', 9090))  # Corrected: bind should be a tuple

while True: # forever loop
    data, (ip, port) = udp.recvfrom(1024) # 
    print("From {}:{}:{}".format(ip, port, str(data, 'utf-8')))  # Corrected: use 'ip' and 'port'
    udp.sendto(b'Thank you!\n', (ip, port))  # sends a thank you back
