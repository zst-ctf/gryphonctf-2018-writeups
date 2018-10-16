#!/usr/bin/env python3
from itertools import cycle

# Open up the encrypted image as bytes
with open("Shorty.png", "rb") as f:
    shorty = f.read()

# The first eight bytes of a PNG file always contain the following (decimal) values:
png_header = bytes([137, 80, 78, 71, 13, 10, 26, 10])

# PNG chunk data
png_header += bytes([0, 0, 0, 0x0D, 0x49, 0x48, 0x44, 0x52, 0])

# XOR the png header to get the key
key = b''
for i in range(len(png_header)):
    key += bytes([shorty[i] ^ png_header[i]])

print("png_header", png_header)
print("key", key)

print("png_header", png_header.hex())
print("key", key.hex())

# From inspection, I assume key is 16 bytes
key = key[:16]

# cyclic key XOR & decrypt the PNG
xored_shorty = []
for a, b in zip(shorty, cycle(key)):
    xored_shorty.append(a ^ b)

# Write bytes to file
xored_shorty = bytes(xored_shorty)
with open("Shorty-solved.png", "wb") as f:
    shorty = f.write(xored_shorty)
