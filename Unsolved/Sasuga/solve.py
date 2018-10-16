#!/usr/bin/env python3
from itertools import cycle

# Open up the encrypted image as bytes
with open("Sasuga", "rb") as f:
    png = f.read()

# The first eight bytes of a PNG file always contain the following (decimal) values:
png_header = bytes([137, 80, 78, 71, 13, 10, 26, 10])

# PNG chunk data
png_header += bytes([0, 0, 0, 0x0D, 0x49, 0x48, 0x44, 0x52, 0])
header_len = len(png_header)

# fix header
png = png_header + png[header_len:]

# fix IDAT at index 55
png = png.replace(b'lDAT', b'IDAT', 1)


# Fix filter method
png = png[:61] + b'\xec' + png[62:]

fixed = png
print("IDAT start:", fixed[55:55+4])
print("ZLib compression:", fixed[59:59+2].hex())
print("Filter:", fixed[61:61+4])

print("", fixed[55:55+100])
#print(header_len)
#print("PNG Header:", fixed[0:8])

#print("IDAT:", fixed[0:100])
#print(fixed[17:17+100])

with open("Solved.png", "wb") as f:
    png = f.write(fixed)
