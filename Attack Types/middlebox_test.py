#!/usr/bin/env scapy
import random
from scapy.all import *

ipPacket = IP(dst="www.google.com")

port = random.randrange(49152, 65535)
seqnr = random.randrange(0, 255**4)
acknr = random.randrange(0, 255**4)
tcpPacket = TCP(sport=port, dport=80, flags="S", seq=seqnr, ack=acknr, window=65535)/"GET / HTTP/1.1\r\nHost: www.youporn.com\r\n\r\n"
syn = ipPacket/tcpPacket
synack = send(syn)
