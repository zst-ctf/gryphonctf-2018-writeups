#!/usr/bin/env python3
import socket
import time
s = socket.socket()
s.connect(('prog.chal.gryphonctf.com', 18301))

game_start = False
count = 0
while True:
    data = s.recv(4096).decode().strip()
    if not data:
        continue

    print("Received:", data)

    if 'Times up, Press Enter' in data:
        s.send(b"\n")

    elif 'Press any button to start' in data:
        s.send(b'hi\n')

    elif count < 300:
        # Remove color characters
        word = data.replace('\x1b[94m', '').replace('\x1b[0m', '')
        count += 1
        s.send(word.encode() + b"\n")
        print(f"Sent ({count}): {word}")
        time.sleep(0.1)


    if 'GTCF{' in data:
        quit()
