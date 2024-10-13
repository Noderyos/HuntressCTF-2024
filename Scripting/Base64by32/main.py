from base64 import b64decode

data = open("base64by32").read()

for _ in range(32): data = b64decode(data)

print(data.decode())
