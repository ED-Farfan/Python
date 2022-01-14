import socket

host = ''
port = 51424
server_port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

data = "Secret key : s76fshg23"

try:
    print("Mando")
    #s.sendto(data.encode(), ('<broadcast>', server_port))
    print("HOLA")
    message, address = s.recvfrom(8192)
    print("Got data, addr from server - ")
    print("Data : ", message.decode())
    print("Address : ", address)

except (KeyboardInterrupt, SystemExit):
    exit()