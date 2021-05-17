import socket

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(3)
print("waiting for the connections")
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with", addr, name)
    c.send(bytes("welcome to the internet world"))
    c.close()
