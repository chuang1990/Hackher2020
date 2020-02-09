# to test udp communication between client and server
# sending

import socket
UDP_IP = "192.168.1.238"
UDP_PORT = 5005
MESSAGE = "TRUE"
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

# receiving 
# import socket

# UDP_IP = "192.168.1.31"
# UDP_PORT = 5005

# sock = socket.socket(socket.AF_INET, # Internet
#                      socket.SOCK_DGRAM) # UDP
# sock.bind((UDP_IP, UDP_PORT))

# while True:
#     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#     print ("received message:", data)