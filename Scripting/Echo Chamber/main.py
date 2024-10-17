import subprocess
import re

raw = subprocess.check_output("tshark -r echo_chamber.pcap -Y 'icmp' -T fields -e data", shell=True).decode()
data = bytes([int(b[16:18], 16) for b in raw.split("\n")[::2] if b])

open("flag.png", "wb").write(data)

print(re.findall(rb"flag\{[0-9a-f]{32}\}", data)[0].decode())
