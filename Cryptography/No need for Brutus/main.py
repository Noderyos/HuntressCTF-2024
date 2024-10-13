import hashlib

a = ord("a")

rotate = lambda s,i:''.join(chr((c-a+i)%26+a)for c in s.encode())

rotated = rotate(open("input.txt").read().strip(), 10)

md5 = hashlib.md5()
md5.update(rotated.encode())

print("flag{"+md5.hexdigest()+"}")
