#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            i = ord(i) - 32
            new_str += chr(i)
        else:
            new_str += i
    print('{}'.format(new_str))       
uppercase("beSt")
uppercase("Best School 98 Battery street")
