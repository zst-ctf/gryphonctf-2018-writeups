# Desparupto
Cryptography - 300 points

## Challenge 
> I can't decrypt my DES-ECB encrypted flag because my key is corrupted!

> Corrupted Key: 4E3D42021CEF32FB

> Creator - PotatoDrug


## Solution

Given that the key is corrupted, there must be a way of figuring out which part of the key is corrupted

DES uses 56-bit keys, but we are given 64-bits (8 bytes)... Apparently, DES reserves 1 byte as a parity bit.

- https://crypto.stackexchange.com/questions/19232/des-encryption-algorithm-all-64-bits-for-key-instead-of-56-bits
- https://crypto.stackexchange.com/questions/12214/can-you-explain-weak-keys-for-des

---

So with this, check for which bytes are corrupted first by the parity bit
    
    # Check which byte is corrupt
    for i, k in enumerate(key):
        if check_DES_parity(k) == False:
            print(f"Corrupted at {i}:", k)

And then running it, we get 2 bytes as corrupted

	key 4e3d42021cef32fb
	Corrupted at 0: 0x4e
	Corrupted at 2: 0x42

---

So now I do a brute force of each byte
	
	for b0 in range(0x100):
        for b2 in range(0x100):
            key[0] = b0
            key[2] = b2

And then I decrypt it until I find the flag

	b'GCTF{ParrI7y_8i7_S7Ill_US3fuL_oR_Nah}\n\x02\x02'

## Flag

	GCTF{ParrI7y_8i7_S7Ill_US3fuL_oR_Nah}