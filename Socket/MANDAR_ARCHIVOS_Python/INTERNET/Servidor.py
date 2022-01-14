import socket

host = ''
port = 51424
server_port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print("Hola")
s.bind((host, port))
print("Hola")
data = "Secret key : s76fshg23"

try:
    message, address = s.recvfrom(8192)
    print("Got data, addr from client - ")
    print("Data : ", message.decode())
    print("Address : ", address)
    print("Mando")
    s.sendto(data.encode(), ('<broadcast>', server_port))
    
except (KeyboardInterrupt, SystemExit):
    exit()
