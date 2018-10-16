#!/usr/bin/env python3
import socket
import time
s = socket.socket()
s.connect(('prog.chal.gryphonctf.com', 18300))


def calculate_one(equ_list, target_operation):
    i_operation = equ_list.index(target_operation)
    i_target = i_operation - 1
    first = equ_list.pop(i_target)
    operation = equ_list.pop(i_target)
    second = equ_list.pop(i_target)

    result = str(eval(' '.join([first, operation, second])))
    equ_list.insert(i_target, result)

    print ("Progress", ' '.join(equ_list))
    return equ_list


def calculate(equ):
    equ_list = equ.split(' ')

    for operation in ['+', '*', '-', '/']:
        while operation in equ_list:
            equ_list = calculate_one(equ_list, operation)

    assert len(equ_list) == 1

    return float(equ_list[0])




print(calculate('14 + 15 * 9 * 2 / 10 / 3'))

while True:
    data = s.recv(4096).decode().strip()
    if not data:
        continue

    print("Received:", data)

    if "Let's go!" in data:
        s.send(b"\n")

    elif 'Sum: ' in data:
        expression = data.replace('Sum:', '').replace('Answer:', '').strip()
        answer = calculate(expression)
        answer = ("%.25f" % answer)

        print("Sending:", answer)
        s.send(answer.encode() + b"\n")

    else:
        pass

    if 'GTCF{' in data:
        quit()
