#!/usr/bin/env python3
import socket

HOST = 'www.google.com'
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET / HTTP/1.1\r\nhost: www.google.com\r\n\r\n')
    data = s.recv(1000)

print('Received', repr(data))
