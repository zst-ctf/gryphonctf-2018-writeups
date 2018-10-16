#!/usr/bin/env python3
from Crypto.Cipher import DES
import base64

'''
def xor_bytes(a_bytes, b_bytes):
    final = []
    for a, b in zip(a_bytes, b_bytes):
        final.append(a ^ b)
    return bytes(final)
'''

def decrypt(key, data):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(data)

def check_DES_parity(b):
    parity = b & 0x01
    # Remove existing parity bit
    b >>= 1
    # Calculate odd parity
    bits = bin(b).count('1')
    calc_parity = ((bits % 2) == 0)
    # Check if parity correct
    return calc_parity == parity

if __name__ == '__main__':
    assert check_DES_parity(0x01) == True
    assert check_DES_parity(0x1F) == True
    assert check_DES_parity(0xFE) == True

    # Read in values
    key = bytes.fromhex("4E3D42021CEF32FB")
    with open("Desparupto", "r") as f:
        data = f.read()
    data = base64.b64decode(data)

    # Check which byte is corrupt
    # print("data", data.hex())
    print("key", key.hex())
    for i, k in enumerate(key):
        if check_DES_parity(k) == False:
            print(f"Corrupted at {i}:", hex(k))

    # Now, bruteforce values of each byte
    key = list(key)
    for b0 in range(0x100):
        for b2 in range(0x100):
            key[0] = b0
            key[2] = b2
            result = decrypt(bytes(key), data)
            print(result)
            if b"GCTF" in result:
                quit()
