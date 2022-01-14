from socket import *
s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('',1998))
m=s.recvfrom(1500)
print(m)
print("\n\n")
print(len(m[0]))