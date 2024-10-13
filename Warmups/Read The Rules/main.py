import urllib.request
import re

response = urllib.request.urlopen("https://huntress.ctf.games/rules").read()

flag = re.findall(r"flag\{[0-9a-f]{32}\}", response.decode())[0]

print(flag)
