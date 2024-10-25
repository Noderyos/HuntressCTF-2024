import socket
import time

HOST = "challenge.ctf.games"
PORT = 32661

def recvuntil(s, seq):
	data = b""
	while not data.endswith(seq):
		data += s.recv(1)
		if b"}" in data: print(data)
	return data

to_hex = lambda x:''.join(hex(i)[2:] for i in x)

key = [0]*8
idx = 0
prev = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for _ in range(8):
	for i in range(16):
		d = to_hex(key).encode() + b"\n"
		print(to_hex(key))
		start = time.time()
		s.send(d)
		recvuntil(s, b"I")
		dt = time.time() - start
		if key[idx] and dt - prev > 0.05:
			break
		prev = dt
		key[idx] += 1
	idx += 1
s.close()

