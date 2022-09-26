#!/usr/bin/python3
for i in range (100):
    if i < 10:
        print('0',end='')
    print(i,end ='')
    if i == 99:
        break
    print(', ',end ='')
print()

for num in range (100):
    print("{:02d}".format(num),end='\n' if num == 99 else ", ")
    
