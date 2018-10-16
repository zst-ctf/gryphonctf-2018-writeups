# Sasuga
Forensics - 400 points

## Challenge 
> We need to recover this picture of the Supreme One!

> Creator - PotatoDrug


## Solution

References:

- IHDR Chunk
	- http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html
https://github.com/ctfs/write-ups-2015/tree/master/plaidctf-2015/forensics/png-uncorrupt
- IDAT
	- https://myers.io/2014/07/30/everything-you-ever-wanted-to-know-about-png/
https://stackoverflow.com/questions/9050260/what-does-a-zlib-header-look-like/43170354#43170354



Looks like a PNG file with a corrupted header. (IHDR is from the PNG header)

Fixing the 8 byte header & first IHDR chunk (lHDR instead of IHDR)

	$ xxd Sasuga | head
	00000000: ef3a 8f26 0d14 7794 0000 000d 4948 4452  .:.&..w.....IHDR
	00000010: 0000 0500 0000 02d0 0806 0000 00cf 7ddd  ..............}.
	00000020: 5600 0000 0662 4b47 4400 ff00 ff00 ffa0  V....bKGD.......
	00000030: bda7 9331 857e 4c6c 4441 5478 daec bdd9  ...1.~LlDATx....
	00000040: af65 d97d dff7 59c3 1ece 70a7 bab7 86ae  .e.}..Y...p.....
	00000050: ea99 6437 69aa 45b2 6951 b264 4980 28d9  ..d7i.E.iQ.dI.(.
	00000060: 96e2 4882 61c0 4960 2379 4a10 f80f c943  ..H.a.I`#yJ....C
	00000070: 12e4 2970 80f8 2189 9118 f04b 9010 3025  ..)p..!....K..0%
	00000080: 5352 3418 12ad 8843 689a 2db2 a96e 8a3d  SR4....Ch.-..n.=
	00000090: b0aa bbab ea4e 67d8 7baf 210f 6b38 6b9f  .....Ng.{.!.k8k.

---

Check progress


	$ pngcheck -v Solved.png 
	File: Solved.png (1159576 bytes)
	  chunk IHDR at offset 0x0000c, length 13
	    1280 x 720 image, 32-bit RGB+alpha, non-interlaced
	  chunk bKGD at offset 0x00025, length 6
	    red = 0x00ff, green = 0x00ff, blue = 0x00ff
	  chunk IDAT at offset 0x00037, length 830832204
	    zlib: deflated, 32K window, maximum compression
	    invalid row-filter type (10)

	    private (invalid?) row-filter type (138) (warning)

	    private (invalid?) row-filter type (249) (warning)

	    private (invalid?) row-filter type (251) (warning)
	    invalid row-filter type (10)

	    private (invalid?) row-filter type (169) (warning)
	    invalid row-filter type (16)
	    invalid row-filter type (37)
	    invalid row-filter type (37)
	    invalid row-filter type (68)

	    private (invalid?) row-filter type (133) (warning)
	    invalid row-filter type (96)


## Flag

	??