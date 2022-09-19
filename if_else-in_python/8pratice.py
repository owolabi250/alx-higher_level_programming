#!/usr/bin/python3
# def islower(c):
#     if ord(c) >= 97 and ord(c) <= 122:
#         return True
#     else:
#         return False


# print("a is {}".format("lower" if islower("a") else "upper"))
# print("H is {}".format("lower" if islower("H") else "upper"))
# print("A is {}".format("lower" if islower("A") else "upper"))
# print("3 is {}".format("lower" if islower("3") else "upper"))
# print("g is {}".format("lower" if islower("g") else "upper"))




def islower(c):
        return ord(c) >= 97 and ord(c) <= 122

print(islower('O'))
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

if islower('c') == True:
    print('lower')
else:
    print('upper')

if islower('B') == True:
    print('lower')
else:
    print('upper')

print("Z is {}".format('lower' if islower('Z') else 'upper'))




def islower(c):
    if c >= 'a' and c <= 'z':
    # if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

print(islower('O'))
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

if islower('c') == True:
    print('lower')
else:
    print('upper')

if islower('B') == True:
    print('lower')
else:
    print('upper')

print("Z is {}".format('lower' if islower('Z') else 'upper'))