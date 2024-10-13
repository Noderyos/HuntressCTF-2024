import sys
import struct

if len(sys.argv) != 2:
    print("Please provide image file")
    exit(1)

def read(f, n):
    d = f.read(n)
    if len(d) != n:
        print("ERROR : Unexpected EOF")
        exit(1)
    return d

islower = lambda x:x > ord("Z")

def read_section(f):
    print("Section :")
    length = struct.unpack(">I", read(f, 4))[0]
    print("    Length     :", length)

    chk_type = read(f, 4)
    print("    Chunk Type :", chk_type)
    print("    Flags      :", 
          "ancillary" if islower(chk_type[0]) else "critical",
          "private" if islower(chk_type[1]) else "public",
          "safe_to_copy" if islower(chk_type[3]) else "unsafe_to_copy",
          "INVALID" if islower(chk_type[2]) else ""
    )
    chk_data = read(f, length)
    print("    Chunk Data :", chk_data)

    CRC = read(f, 4)
    print("    CRC        :", CRC.hex())
    print()
    return 4 + 4 + length + 4


f = open(sys.argv[1], "rb")

size = f.seek(0, 2)
f.seek(0, 0)

if f.read(8) != b"\x89PNG\x0d\x0a\x1a\x0a":
    print("Not a PNG file")
    exit(1)

size -= 8

while size: size -= read_section(f)
