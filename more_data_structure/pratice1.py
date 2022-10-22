#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i**2 for i in row] for row in (matrix)]
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)





# def square_matrix_simple(matrix=[]):
#     new = []
#     for row in matrix:
#         sub = []
#         # new.append([num * num for num in row])
#         for num in row:
#             sq = num * num 
#             sub.append(sq)
#         new.append(sub)
#     return new
 
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# new_matrix = square_matrix_simple(matrix)
# print(new_matrix)
# print(matrix)

