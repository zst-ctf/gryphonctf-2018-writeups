# Lupusregina
Cryptography - 500 points

## Challenge 
> I have intercepted this encrypted EMAIL message sent to Lupusregina, see if you can find any useful intel.

> Creator - PotatoDrug

[Lupusregina](Lupusregina)

[Lupusregina.py](Lupusregina.py)


## Hint
> What is the first line when you write emails?

## Solution

Similar to [AngstromCTF 2018 - OFB](https://github.com/zst123/angstromctf-2018-writeups/tree/master/Solved/ofb)

However, we needed to guess that the starting bytes were "Dear Lupusregina" as per the hint.

#### Procedure

1. lcg values are used as the key
	- recover key using XOR of the known starting bytes with the encrypted text.
2. Extract the first 3 consecutive DWORD (4 bytes) which is the lcg values.
3. Now we can solve for `a` using inverse mod `a = (lcg_2 – lcg_1) / (lcg_1 – lcg_0) (mod m)`
4. Solve for `c`...
5. To decrypt, apply XOR again.

#### Solving...

	$ python3 solve.py
	seed: 5
	a: 1284865837
	c: 12820163
	
	$ python3 Lupusregina.py -f Lupusregina -o Solved.txt -a 1284865837 -c 12820163 -s 5
	Encrypted Lupusregina
	
	$ cat Solved.txt 
	Dear Lupusregina,

	Please displose of the Crown Price.

	GCTF{8R0k3N_Rn9_M4K35_8r0k3N_C1ph3R2}

	Regards, Ainz Ooal Gown

## Flag

	GCTF{8R0k3N_Rn9_M4K35_8r0k3N_C1ph3R2}
