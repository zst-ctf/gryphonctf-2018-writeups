#!/usr/bin/env python3
from PIL import Image

im = Image.open('flag.png')
im = im.convert('RGB')

list_of_pixels = list(im.getdata())
size = (300, 300)
im2 = Image.new(im.mode, size)
im2.putdata(list_of_pixels)
im2.save("solved.png")
