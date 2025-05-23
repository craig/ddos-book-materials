#!/usr/bin/env python
from scapy.all import *
import sys
try:
	dst = sys.argv[1]
	dport = int(sys.argv[2])
except:
	print("%s [IP] [port]" % sys.argv[0])
	sys.exit(1)

res = sr1(IP(dst=dst)/TCP(dport=dport,flags="S",options=[('TFO', '')]), verbose=False)
supportstfo = 'TFO' in dict(res[1].options)

if supportstfo:
	print ("%s supports TFO" % sys.argv[1])
else:
	print ("%s does not support TFO" % sys.argv[1])
