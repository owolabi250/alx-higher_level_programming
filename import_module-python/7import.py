#!/usr/bin/python3
from pratice7 import add,sub,mul,div
from sys import argv as h
if len(h) != 4:
    print("Usage: {} <a> <operator> <b>".format(h[0]))
    exit(1)
operator = ['+', '-', '*', '/']
if h[2] not in operator:
   print("Unknown operator. Available operators: +, -, * and /")
   exit(1)
a = int(h[1])
b = int(h[3])

if h[2] == '+':
    print("{} {} {} = {}".format(a,operator[0],b, add(a,b)))
elif h[2] == '-':
    print("{} {} {} = {}".format(a,operator[1],b, sub(a,b)))
elif h[2] == '*':
    print("{} {} {} = {}".format(a,operator[2],b, mul(a,b)))
elif h[2] == '/':
    print("{} {} {} = {}".format(a,operator[3],b, div(a,b)))



