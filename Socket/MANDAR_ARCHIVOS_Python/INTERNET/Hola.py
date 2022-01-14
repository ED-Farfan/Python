from socket import *
s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
#host = 'localhost'
host='192.168.1.255'

s.sendto('Hola Tontos',(host,1998))
