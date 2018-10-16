#!/usr/bin/env python3

# Open up the image as bytes
with open("cinnamonroll.jpg", "rb") as f:
    jpg = f.read()

# http://www.file-recovery.com/jpg-signature-format.htm
header = bytes([0xff, 0xd8, 0xff, 0xe0, 0x00, 0x10])
header += bytes([0x4a, 0x46, 0x49, 0x46, 0x00])

# fix header and create file
jpg = header + jpg[len(header):]
with open("Fixed.png", "wb") as f:
    f.write(jpg)
