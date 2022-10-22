#!/usr/bin/python3
# def no_c(my_string):
#     a = ''
#     for i in my_string:    
#         if i != 'c' and i != 'C':
#             # print(i,end='' )
#             a = a+i
#     return a





def no_c(my_string):
    for i in range(len(my_string)):    
        if i == 'c' or i == 'C':
            continue
        print(f"{my_string[i]}", end="")
            # print("{:c}".format(my_string(i)))
            # print(str(my_string(i),end='' ))
           



def no_c(my_string):
    a = ""
    for i in my_string:
        if i =="c" or i == "C":
            continue
        a = a+i
    return a

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

no_c("Best School")
no_c("Chicago")
no_c("C is fun!")


print("Best School")
print("Chicago")
print("C is fun!")