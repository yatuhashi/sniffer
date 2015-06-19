#!/usr/bin/python
#python ver.3.4
import sys
from socket import *

ETH_P_IP = 0x800
s = socket(PF_PACKET, SOCK_RAW, ETH_P_IP)
s.bind(("wlan0", ETH_P_IP))
watch_port=80

def dump_head(p):
    print("DATA: ",p)
    print([x for x in p],"\n")
    print([x for x in p[0:6]]," > ",[x for x in p[6:12]])    
    src = ":".join(["%02x" % x for x in p[0:6]])
    dst = ":".join(["%02x" % x for x in p[6:12]])
    type = ntohs(ord(p[12:13]))
    print("%s > %s, ethertype %04x, length %d" % (src, dst, type, plen))
    print("SourcePort : %02x%02x :" % (p[32], p[33]),int("%02x%02x" % (p[32],p[33]),16))
    print("DestinationPort : %02x%02x :" % (p[34], p[35]),int("%02x%02x" % (p[34],p[35]),16))


def dump_all_data(p):
    for i in range(0, plen, 2):
        try:
            sys.stdout.write("%02x%02x  " % (p[i], p[i+1])),
            if i % 16 == 14:
                print(""),
        except:
            print("\n")

while range(1):
    p = s.recv(2048)
    plen = len(p)
    if watch_port==int("%02x%02x" % (p[32],p[33]),16) or watch_port==int("%02x%02x" % (p[34],p[35]),16):
        print("\n**----------------------------------------------------------------**")
        dump_head(p)
        dump_all_data(p)


