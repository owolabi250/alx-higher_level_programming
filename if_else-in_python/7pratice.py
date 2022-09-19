#!/usr/bin/python3
for i in range(10):
    for a in range (10):
        if i < a:
            print(f"{i}{a}",end='')
            if i == 8 and a == 9:
                break
            print(', ',end='')

