import math
import numpy as np

# a1 = np.array([[1, 2, 3],
#                [4, 5, 6]])

# a2 = np.array([[10, 11],
#                [20, 21],
#                [30, 31]])

# print(np.matmul(a1, a2))

point = [-1, 1, -1, 1]

t = [5, 5, 5]

matrix = np.array([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [t[0], t[1], t[2], 1]])

# point2 = [point[0]*T[0][0]+point[1]*T[1][0]+point[2]*T[2][0]+T[3][0], point[0]*T[0][1]+point[1]*T[1][1]+point[2]*T[2][1]+T[3][1], point[0]*T[0][2]+point[1]*T[1][2]+point[2]*T[2][2]+T[3][2]]

print(np.matmul(point, matrix))

# print(point2)

# var = [(point[i]*matrix[i][0]) for i in range(3) + matrix[3][0]]

# print(var)

# rotation = [0, 0, 0]
# s = [math.sin(rotation[i]) for i in range(3)]
# c = [math.cos(rotation[i]) for i in range(3)]

# Rx = np.array([[1, 0, 0, 0],
#                [0, c[0], -s[0], 0],
#                [0, s[0], c[0], 0],
#                [0, 0, 0, 1]])

# Ry = np.array([[c[1], 0, c[1], 0],
#                [0, 1, 0, 0],
#                [-s[1], 0, c[1], 0],
#                [0, 0, 0, 1]])

# Rz = np.array([[c[2], -s[2], 0, 0],
#                [s[2], c[2], 0, 0],
#                [0, 0, 1, 0],
#                [0, 0, 0, 1]])

# R = np.matmul(Rx, Ry)
# R = np.matmul(R, Rz)

# print(R)


# # Program to multiply two matrices using nested loops

# # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# # result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)