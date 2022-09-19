#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            i = i - 'a'
        else:
            i = 'A'

uppercase("best")
uppercase("Best School 98 Battery street")
        
