#!/usr/bin/env python3
from PIL import Image
import os
from multiprocessing.pool import ThreadPool


# https://stackoverflow.com/questions/11599226/how-to-convert-binary-string-to-ascii-string-in-python
def bin_to_ascii(bin_text):
    return ''.join(chr(int(bin_text[i:i+8], 2)) for i in range(0, len(bin_text), 8))


def search_file(file):
    print(f"Doing: {file}")
    im = Image.open(DIR + file)
    im = im.convert('RGB')

    width, height = im.size

    data = ''
    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            data += str(pixel[0] & 1)
            data += str(pixel[1] & 1)
            data += str(pixel[2] & 1)
    assert(len(data) % 8 == 0), len(data)

    if 'GCTF{' in bin_to_ascii(data).upper():
        print(bin_to_ascii(data))

    return 0


pool = ThreadPool(processes=50)


DIR = "./images/"
for i, file in enumerate(os.listdir(DIR)):
    if not file.endswith(".jpg"):
        continue

    arguments = (file, )
    async_results = []
    async_result = pool.apply_async(search_file, arguments)
    async_results.append((async_result))

# Get results
for async_result in async_results:
    valid = async_result.get()

quit()

'''
if valid:
    intermediate_ch = bytes([ch[0] ^ count])
    progress = intermediate_ch + progress
    print(f"\rBlock {block_number} - #{count}: {progress} {valid}", end='')
    break
'''

