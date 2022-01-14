# chat server using multicast
# python fork of the original ruby implementation
# http://tx.pignata.com/2012/11/multicast-in-ruby-building-a-peer-to-peer-chat-system.html
# send.py
# usage : $ python send.py message

import socket
import struct
import sys
import time
message = sys.argv[1] if len(sys.argv) > 1 else 'message via multicast'

multicast_addr = '224.0.0.1'
port = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
while 1:
    sock.sendto(message.encode(), (multicast_addr, port))
    time.sleep(3)
sock.close()