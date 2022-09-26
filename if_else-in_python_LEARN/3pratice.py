#!/usr/bin/python3
for abc in range(97, 123):
    print(f"{chr(abc)}",end ='')
    print("{:c}".format(abc),end ='')
    print("{}".format(chr(abc)))
