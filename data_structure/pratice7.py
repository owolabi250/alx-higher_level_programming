#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j < len(matrix[i]) - 1:
                    print(f"{matrix[i][j]:d} ", end="")
                else:
                    print(f"{matrix[i][j]:d}", end="")
            print()

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for a in range(len(matrix[i])):
            if a < len(matrix[i]) - 1:
            #     print("{} ".format(matrix[i][a]),end='')
            # if a % 3 != 0:
                print("{:d} ".format(matrix[i][a]),end='')
            else:
                print("{:d}".format(matrix[i][a]),end='')
               # print()
        print()
    # print()



# def print_matrix_integer(matrix=[[]]):
#     for i in range(len(matrix)):
#         for a in range(len(matrix[i])):
#             if a < len(matrix[i]) - 1:
#                 print("{} ".format(matrix[i][a]),end='')
#             # if a % 3 != 0:
#                 # print(a,end=" ")
#             else:
#                 print("{}".format(matrix[i][a]),end='')
#                # print()
#         print()
#     # print()



# def print_matrix_integer(matrix=[[]]):
#     for l in matrix:
#         for i in range(len(l)):
#             print(l[i],end ="")
#             if i < len(l) - 1:
#                 print(" ",end ="")
#             else:
#                 print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
