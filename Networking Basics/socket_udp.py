#!/usr/bin/env python3
import socket

HOST = "8.8.8.8"
PORT = 53

MESSAGE =  b"\xc3\x7a\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x04\x74\x65\x73\x74\x03\x63\x6f\x6d\x00\x00\x01\x00\x01"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (HOST, PORT))
