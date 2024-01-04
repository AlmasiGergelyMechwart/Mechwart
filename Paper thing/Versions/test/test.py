import math
import numpy as np
# import random

point = [5 for i in range(3)]
angle = [math.radians(90) for i in range(2)]

c = math.cos(angle[0])
s = math.sin(angle[0])
t = 1 - c
u = [0, 1, 0]

R = [[t*u[0]**2 + c, t*u[0]*u[1] - u[2]*s, t*u[0]*u[2] + u[1]*s],
     [t*u[0]*u[1] + u[2]*s, t*u[1]**2 + c, t*u[1]*u[2] - u[0]*s],
     [t*u[0]*u[2] - u[1]*s, t*u[1]*u[2] + u[0]*s, t*u[2]**2 + c]]

# https://www.euclideanspace.com/maths/geometry/rotations/conversions/angleToMatrix/index.htm

def matrixMul(M1, M2):
    for i in range(2):
        M = [M1, M2]
        if str(type(M[i][0]))[8:-2] == "int":
            M[i] = [M[i]]
            M1, M2 = M[0], M[1]

    if len(M1[0]) != len(M2):
        raise
    Mout = [[0 for i in range(len(M2[0]))] for i in range(len(M1))]

    for i in range(len(Mout)):
        for j in range(len(Mout[0])):
            for k in range(len(M1[0])):
                Mout[i][j] += M1[i][k] * M2[k][j]
    
    if len(Mout) == 1:
        Mout = Mout[0]

    return Mout

# M1 = [[1, 2, 3],
#       [4, 5, 6]]

# M2 = [[10, 11],
#       [20, 21],
#       [30, 31]]

s = math.sin(0)
c = math.cos(0)
t = 1 - c
u = [0, 0, 0]

RT = [[t*u[0]**2 + c,   t*u[0]*u[1],     t*u[0] + u[1]*s],
      [t*u[0]*u[1],     t*u[1]**2 + c,   t*u[1] - u[0]*s],
      [t*u[0] - u[1]*s, t*u[1] + u[0]*s, c              ]]

M3 = matrixMul(point, RT)

# print(point)
print(RT)

# for i in range(len(M3)):
#     print(M3[i])

# print()

# M3 = np.matmul(point, R)

# for i in range(len(M3)):
#     print(M3[i])

# print(str(type(M1))[8:-2])
    



# https://eater.net/quaternions/video/intro
# https://www.sciencedirect.com/topics/computer-science/quaternion-multiplication
# https://danceswithcode.net/engineeringnotes/quaternions/quaternions.html






# Rx = np.array([[c+u[0]**2*(1-c), u[0]*u[1]*(1-c)+u[1]*s, u[0]*u[2]+u[1]*s],
#                [u[0]*u[1]*(1-c)+u[2]*s, c+u[1]**2*(1-c), u[1]*u[2]*(1-c)-u[0]*s],
#                [u[0]*u[2]*(1-c)-u[1]*s, u[1]*u[2]*(1-c)+u[0]*s, c+u[2]**2*(1-c)]])

# u = [0, 1, 0]
# Ry = np.array([[c+u[0]**2*(1-c), u[0]*u[1]*(1-c)+u[1]*s, u[0]*u[2]+u[1]*s],
#                [u[0]*u[1]*(1-c)+u[2]*s, c+u[1]**2*(1-c), u[1]*u[2]*(1-c)-u[0]*s],
#                [u[0]*u[2]*(1-c)-u[1]*s, u[1]*u[2]*(1-c)+u[0]*s, c+u[2]**2*(1-c)]])