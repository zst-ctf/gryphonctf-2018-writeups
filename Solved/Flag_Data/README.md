# Flag Data
Miscellaneous - 175 points

## Challenge 
> This file contains data for a flag.

> All the characters of the flag are uppercase.

> Creator - PotatoDrug

[flag.dat](flag.dat)

## Solution

All the alphabets are offset by 0x40 where 'A' corresponds to 0x01 (1) and 'Z' corresponds to 0x1A (26)

	 $ python3


	>>> with open("flag.dat", "rb") as f:
	...   data = f.read()
	... 

	>>> data
	b'\x07\x03\x14\x06{\x13\x0f_\r\x01\x0e\x19_\x17\x01\x19\x13_\x14\x0f_\x12\x05\x10\x12\x05\x13\x05\x0e\x14_\x04\x01\x14\x01}'

	>>> for b in data:
	...   if b < 0x5B: b += 0x40
	...   print(chr(b), end='')
	... 
	GCTF{SO_MANY_WAYS_TO_REPRESENT_DATA}
