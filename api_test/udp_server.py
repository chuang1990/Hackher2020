"""
udp_server.py
Part of code for HackHer413
Waiting for a message from the sensor to trigger the notification script
Author: Kunjal Panchal
Date: 02-09-2020
"""
import socket

UDP_IP = "192.168.1.31"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))

while True:
    print("server up, waiting for message")
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)
    if data.decode() == "TRUE":
        exec(open("notification.py").read())
