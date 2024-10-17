import socket

HOST = "challenge.ctf.games"
PORT = 30463

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = ""
f = False

while True:
	c = s.recv(1)[0]
	if c == 0x1b:
		f = True
		continue
	if c == ord("m"):
		f = False
		continue
	if not f and c != 0x20: data += chr(c)
	if c == ord("}"):break
print(data)