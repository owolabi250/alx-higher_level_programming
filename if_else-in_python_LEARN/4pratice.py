#!/usr/bin/python3
for e in range (97, 101):
    print("{:c}".format(e), end ='')
for s in range (102, 113):
    print("{:c}".format(s), end ='')
for z in range (114, 123):
    print("{:c}".format(z),end='')
print()

for alphabet in range (97, 123):
    if alphabet == 101 or alphabet == 113:
        continue
    print("{:c}".format(alphabet), end ='')
print()

for eq in range (97, 123):
    if eq != 101 and eq != 113:
         print("{:c}".format(eq), end ='')
