#!/usr/bin/env python3
import struct
import gmpy2

mod_value = 2**32

# Extract key
known_header = b"Dear Lupusregina"

with open("Lupusregina", 'rb') as f:
    encrypted = bytearray(f.read())

key = b''
for a, b in zip(encrypted, known_header):
    key += bytes([a ^ b])

# Get lcg values from key
lcg_0 = struct.unpack('>I', key[0:4])[0]
lcg_1 = struct.unpack('>I', key[4:8])[0]
lcg_2 = struct.unpack('>I', key[8:12])[0]

# LCG solver
def lcg(m, a, c, x=0):
    return (a * x + c) % m

def rlcg(m, a, c, x=0):
    ainv = gmpy2.invert(a, m)
    return ainv * (x - c) % m

def solve_a(lcg0, lcg1, lcg2, m):
    a = (lcg2 - lcg1) * gmpy2.invert(lcg1 - lcg0, m) % m
    return a

def solve_c(lcg0, lcg1, m, a):
    c = (lcg1 - a * lcg0) % m
    return c

a = solve_a(lcg_0, lcg_1, lcg_2, mod_value)
c = solve_c(lcg_0, lcg_1, mod_value, a)
seed = rlcg(mod_value, a, c, lcg_0)

print('seed:', seed)
print('a:', a)
print('c:', c)
