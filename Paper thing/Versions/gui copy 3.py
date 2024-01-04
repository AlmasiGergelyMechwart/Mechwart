import tkinter as tk
from tkinter import ttk
import math

# import numpy as np

from object import Object

class GUI(tk.Tk):

    windowSize = [900, 500]
    canvasSize = [800, 400]

    panelSize = [200, 100]
    # Should make a save

    # object = Object("obj/MaleLow.obj")
    object = Object("obj/cube4.obj")

    zoom = 50

    def __init__(self):
        super().__init__()

        self.minsize(self.windowSize[0], self.windowSize[1])
        self.configure(
            bg="lightgrey"
        )

        # def onWindowResize(event):
        #     pass

        self.bind("<Configure>", self.on_window_resize)

        # self.on_window_resize()
   
        self.canvas = tk.Canvas(self, width=self.canvasSize[0], height=self.canvasSize[1])
        self.canvas.pack(anchor="nw")

        self.rotationTypes = ["Local Axis rotation", "Global Axis rotation"]
        self.currentRotationType = tk.StringVar(self)
        self.rotationOptionMenu = ttk.OptionMenu(self, self.currentRotationType, self.rotationTypes[0], *self.rotationTypes, command=self.rotation_type_change)
        self.rotationOptionMenu.pack()
        self.rotation_type_change()

        self.canvas.bind("<ButtonPress-3>", self.rotate_start)
        self.canvas.bind("<ButtonRelease-3>", self.rotate_end)

        # self.angle = 0
        # self.axis = [0, 0, 0]
        # self.prevAngle = 0
        # self.prevAxis = [0, 0, 0]
        # self.prevPos = [0, 0]
        # self.rotation = [0, 0]


        # self.rotScale = [(ttk.Scale(self, from_=-math.pi, to=math.pi)) for i in range(3)]
        # self.rotScale[0].configure(command=self.rotate_x)
        # self.rotScale[1].configure(command=self.rotate_y)
        # self.rotScale[2].configure(command=self.rotate_z)
        # [self.rotScale[i].pack() for i in range(3)]

        # self.rotEntry = [ttk.Entry(self) for i in range(3)]
        # for i in range(3): self.rotEntry[i].insert(0, "0")
        # for i in range(3): self.rotEntry[i].pack()

        # self.rotButton = ttk.Button(self, text="Rotate", command=self.update)
        # self.rotButton.pack()

        self.update()

    def update(self):
        self.canvas.delete("all")

        # canvas.create_rectangle(canvasSize[0]/2-object["size"][0]/2*zoom, canvasSize[1]/2-object["size"][1]/2*zoom, canvasSize[0]/2+object["size"][0]/2*zoom, canvasSize[1]/2+object["size"][1]/2*zoom, fill="green")

        # canvas.create_line(canvasSize[0]/2, 0, canvasSize[0]/2, canvasSize[1])
        # canvas.create_line(0, canvasSize[1]/2, canvasSize[0], canvasSize[1]/2)

        # rotation = [math.radians(tick*10), math.radians(tick*10), math.radians(tick*10)]
        # rotation = [0, math.radians(tick*10), 0]
        # rotation = [self.rotScale[i].get() for i in range(3)]

        # rotBefore = self.object.rotation
        # rotation = [(math.radians(float(self.rotEntry[i].get()))) for i in range(3)]
        # for i in range(3): self.object.rotation[i] += rotation[i]

        # s = [(math.sin(self.object.rotation[i])) for i in range(3)]
        # c = [(math.cos(self.object.rotation[i])) for i in range(3)]

        for face in self.object.faces:
            points = []
            for f in face:
                self.point = [(self.object.vertices[f-1][i]+self.object.offset[i]) for i in range(3)]
                self.point[1] *= -1

                self.object.position = [self.canvasSize[0]/2, self.canvasSize[1]/2]

                #https://www.symbolab.com/solver/matrix-multiply-calculator/%5Cbegin%7Bpmatrix%7D1%260%260%260%5C%5C%20%200%26%5Ccos%5Cleft(%5Calpha%5Cright)%26-sin%5Cleft(%5Calpha%5Cright)%260%5C%5C%20%200%26sin%5Cleft(%5Calpha%5Cright)%26cos%5Cleft(%5Calpha%5Cright)%260%5C%5C%20%200%260%260%261%5Cend%7Bpmatrix%7D%5Ccdot%5Cbegin%7Bpmatrix%7Dcos%5Cleft(%5Cbeta%5Cright)%260%26sin%5Cleft(%5Cbeta%5Cright)%260%5C%5C%20%200%261%260%260%5C%5C%20%20-sin%5Cleft(%5Cbeta%5Cright)%260%26cos%5Cleft(%5Cbeta%5Cright)%260%5C%5C%20%200%260%260%260%5Cend%7Bpmatrix%7D%5Ccdot%5Cbegin%7Bpmatrix%7Dcos%5Cleft(%5Cgamma%5Cright)%26-sin%5Cleft(%5Cgamma%5Cright)%260%260%5C%5C%20%20sin%5Cleft(%5Cgamma%5Cright)%26cos%5Cleft(%5Cgamma%5Cright)%260%260%5C%5C%20%200%260%261%260%5C%5C%20%200%260%260%261%5Cend%7Bpmatrix%7D?or=input

                # RotationMatrix = [[c[1]*c[2],                -c[1]*s[2],               s[1],       0],
                #                   [s[0]*s[1]*c[2]+c[0]*s[2], c[0]*c[2]-s[0]*s[1]*s[2], -s[0]*c[1], 0],
                #                   [s[0]*s[2]-c[0]*s[1]*c[2], c[0]*s[1]*s[2]+s[0]*c[2], c[0]*c[1],  0],
                #                   [0,                        0,                        0,          0]]

                # X, Y, Z rotation
                # point = [point[0]*(c[1]*c[2])+point[1]*(s[0]*s[1]*c[2]+c[0]*s[2])+point[2]*(s[0]*s[2]-c[0]*s[1]*c[2]), point[0]*(-c[1]*s[2])+point[1]*(c[0]*c[2]-s[0]*s[1]*s[2])+point[2]*(c[0]*s[1]*s[2]+s[0]*c[2]), point[0]*(s[1])+point[1]*(-s[0]*c[1])+point[2]*(c[0]*c[1])]

                # X rotation
                # point = [point[0], point[1]*c[0]+point[2]*s[0], point[1]*-s[0]+point[2]*c[0]]

                # self.axis = [0.5, 0.5, 0]
                # s = math.sin(self.angle)
                # c = math.sin(self.angle)

                # self.point = [self.point[0]*((1-c)*self.axis[0]**2+c)+self.point[1]*((1-c)*self.axis[0]*self.axis[1]+self.axis[2]*s)+]
                # self.point = [self.point[0]*((1-c)*self.axis[0]**2 + c)+self.point[1]*((1-c)*self.axis[0]*self.axis[1] + self.axis[2]*s)+self.point[2]*((1-c)*self.axis[0]*self.axis[2] - self.axis[1]*s), self.point[0]*((1-c)*self.axis[0]*self.axis[1] - self.axis[2]*s)+self.point[1]*((1-c)*self.axis[1]**2 + c)+self.point[2]*((1-c)*self.axis[1]*self.axis[2] + self.axis[0]*s), self.point[0]*((1-c)*self.axis[0]*self.axis[2] + self.axis[1]*s)+self.point[1]*((1-c)*self.axis[1]*self.axis[2] - self.axis[0]*s)+self.point[2]*((1-c)*self.axis[2]**2 + c)]


                # s = [(math.sin(rotBefore[i])) for i in range(3)]
                # c = [(math.cos(rotBefore[i])) for i in range(3)]
                # # self.point = [-1*(self.point[0]*(c[1]*c[2])+self.point[1]*(s[0]*s[1]*c[2]+c[0]*s[2])+self.point[2]*(s[0]*s[2]-c[0]*s[1]*c[2])), -1*(self.point[0]*(-c[1]*s[2])+self.point[1]*(c[0]*c[2]-s[0]*s[1]*s[2])+self.point[2]*(c[0]*s[1]*s[2]+s[0]*c[2])), -1*(self.point[0]*(s[1])+self.point[1]*(-s[0]*c[1])+self.point[2]*(c[0]*c[1]))]
                # # self.point = [self.point[0]*-(c[1]*c[2])+self.point[1]*(-s[0]*s[1]*c[2]-c[0]*s[2])+self.point[2]*(-s[0]*s[2]+c[0]*s[1]*c[2]), self.point[0]*(c[1]*s[2])+self.point[1]*(-c[0]*c[2]+s[0]*s[1]*s[2])+self.point[2]*(-c[0]*s[1]*s[2]-s[0]*c[2]), self.point[0]*(-s[1])+self.point[1]*(s[0]*c[1])+self.point[2]*(-c[0]*c[1])]
                # self.point = [self.point[0]*(c[1]*c[2])+self.point[1]*(-s[0]*s[1]*c[2]-c[0]*s[2])+self.point[2]*(-s[0]*s[2]+c[0]*s[1]*c[2]), self.point[0]*(c[1]*s[2])+self.point[1]*(c[0]*c[2]-s[0]*s[1]*s[2])+self.point[2]*(-c[0]*s[1]*s[2]-s[0]*c[2]), self.point[0]*(-s[1])+self.point[1]*(s[0]*c[1])+self.point[2]*(c[0]*c[1])]

                # s = [(math.sin(rotation[i])) for i in range(3)]
                # c = [(math.cos(rotation[i])) for i in range(3)]
                # self.point = [self.point[0]*(c[1]*c[2])+self.point[1]*(s[0]*s[1]*c[2]+c[0]*s[2])+self.point[2]*(s[0]*s[2]-c[0]*s[1]*c[2]), self.point[0]*(-c[1]*s[2])+self.point[1]*(c[0]*c[2]-s[0]*s[1]*s[2])+self.point[2]*(c[0]*s[1]*s[2]+s[0]*c[2]), self.point[0]*(s[1])+self.point[1]*(-s[0]*c[1])+self.point[2]*(c[0]*c[1])]
                # # self.point = [self.point[0]*(c[1]*c[2])+self.point[1]*(-s[0]*s[1]*c[2]-c[0]*s[2])+self.point[2]*(-s[0]*s[2]+c[0]*s[1]*c[2]), self.point[0]*(c[1]*s[2])+self.point[1]*(c[0]*c[2]-s[0]*s[1]*s[2])+self.point[2]*(-c[0]*s[1]*s[2]-s[0]*c[2]), self.point[0]*(-s[1])+self.point[1]*(s[0]*c[1])+self.point[2]*(c[0]*c[1])]

                # s = [(math.sin(rotBefore[i])) for i in range(3)]
                # c = [(math.cos(rotBefore[i])) for i in range(3)]
                # self.point = [self.point[0]*(c[1]*c[2])+self.point[1]*(s[0]*s[1]*c[2]+c[0]*s[2])+self.point[2]*(s[0]*s[2]-c[0]*s[1]*c[2]), self.point[0]*(-c[1]*s[2])+self.point[1]*(c[0]*c[2]-s[0]*s[1]*s[2])+self.point[2]*(c[0]*s[1]*s[2]+s[0]*c[2]), self.point[0]*(s[1])+self.point[1]*(-s[0]*c[1])+self.point[2]*(c[0]*c[1])]
                # # self.point = [self.point[0]*(c[1]*c[2])+self.point[1]*(s[0]*s[1]*c[2]+c[0]*s[2])+self.point[2]*(s[0]*s[2]-c[0]*s[1]*c[2]), self.point[0]*(-c[1]*s[2])+self.point[1]*(c[0]*c[2]-s[0]*s[1]*s[2])+self.point[2]*(c[0]*s[1]*s[2]+s[0]*c[2]), self.point[0]*(s[1])+self.point[1]*(-s[0]*c[1])+self.point[2]*(c[0]*c[1])]

                # u = [(c[0]*s[1]*s[2]+s[0]*c[2]) - (-s[0]*c[1]), (s[1]) - (s[0]*s[2]-c[0]*s[1]*c[2]), (s[0]*s[1]*c[2]+c[0]*s[2]) - (-c[1]*s[2])]

                # print("-"*5+"x"+"-"*5)
                # print(self.object.rotation)
                # print(rotation)


                # u = [(1 if self.rotEntry[i].get() != "0" else 0) for i in range(3)]
                # angle = 0
                # for i in range(3):
                #     angle = math.radians(float(self.rotEntry[i].get())) if self.rotEntry[i].get() != "0" else angle
                # if self.prevAxis[0] + self.prevAxis[1] == 0:
                #     self.axis = [(self.prevAxis[i] + self.axis[i])/2 for i in range(2)]
                # else:
                #     self.axis = [(self.axis[i]) for i in range(2)]
                # s = math.sin(self.angle)
                # c = math.cos(self.angle)

                # prevS = math.sin(self.prevAngle)
                # prevC = math.cos(self.prevAngle)

                # u = self.prevAxis
                # s = math.sin(self.prevAngle)
                # c = math.cos(self.prevAngle)

                # self.point = [self.point[0]*(c+u[0]**2*(1-c))+self.point[1]*(u[1]*u[0]*(1-c))+self.point[2]*(-u[1]*s), self.point[0]*(u[0]*u[1]*(1-c))+self.point[1]*(c+u[1]**2*(1-c))+self.point[2]*(u[0]*s), self.point[0]*(u[1]*s)+self.point[1]*(-u[0]*s)+self.point[2]*(c)]


                # s = math.sin(self.angle)
                # c = math.cos(self.angle)
                # t = 1 - c
                # u = self.axis

                # # R = [[t*u[0]**2 + c, t*u[0]*u[1] - u[2]*s, t*u[0]*u[2] + u[1]*s],
                # #     [t*u[0]*u[1] + u[2]*s, t*u[1]**2 + c, t*u[1]*u[2] - u[0]*s],
                # #     [t*u[0]*u[2] - u[1]*s, t*u[1]*u[2] + u[0]*s, t*u[2]**2 + c]]

                # R = [[t*u[0]**2 + c,   t*u[0]*u[1],     t*u[0] + u[1]*s],
                #      [t*u[0]*u[1],     t*u[1]**2 + c,   t*u[1] - u[0]*s],
                #      [t*u[0] - u[1]*s, t*u[1] + u[0]*s, c              ]]

                # print(R)

                # print(self.point)
                # print(self.multiply_matricies(self.point, M2))
                # self.point = self.multiply_matricies(self.point, R)

                # self.point = [self.point[0]*(c+u[0]**2*(1-c))+self.point[1]*(u[1]*u[0]*(1-c))+self.point[2]*(-u[1]*s), self.point[0]*(u[0]*u[1]*(1-c))+self.point[1]*(c+u[1]**2*(1-c))+self.point[2]*(u[0]*s), self.point[0]*(u[1]*s)+self.point[1]*(-u[0]*s)+self.point[2]*(c)]

                # self.prevAxis = self.axis

                # R1 = np.array([[c+u[0]**2*(1-c), u[0]*u[1]*(1-c)-u[2]*s, u[0]*u[2]*(1-c)+u[1]*s],
                #                [u[1]*u[2]*(1-c)+u[2]*s, c+u[1]**2*(1-c), u[1]*u[2]*(1-c)+u[0]*s],
                #                [u[0]*u[2]*(1-c)-u[1]*s, u[1]*u[2]*(1-c)+u[0]*s, c+u[2]**2*(1-c)]])


                # R2 = np.array([[c+u[0]**2*(1-c), u[0]*u[1]*(1-c)-u[2]*s, u[0]*u[2]*(1-c)+u[1]*s],
                #                [u[1]*u[2]*(1-c)+u[2]*s, c+u[1]**2*(1-c), u[1]*u[2]*(1-c)+u[0]*s],
                #                [u[0]*u[2]*(1-c)-u[1]*s, u[1]*u[2]*(1-c)+u[0]*s, c+u[2]**2*(1-c)]])

                # self.point = np.matmul(self.point, R1)

                # self.point = [self.point[0]*(prevC+self.axis[0]**2*(1-prevC))+self.point[1]*(self.axis[1]*self.axis[0]*(1-prevC))+self.point[2]*(-self.axis[1]*prevS), self.point[0]*(self.axis[0]*self.axis[1]*(1-prevC))+self.point[1]*(prevC+self.axis[1]**2*(1-prevC))+self.point[2]*(self.axis[0]*prevS), self.point[0]*(self.axis[1]*prevS)+self.point[1]*(-self.axis[0]*prevS)+self.point[2]*(prevC)]
                # self.point = [self.point[0]*(c+self.axis[0]**2*(1-c))+self.point[1]*(self.axis[1]*self.axis[0]*(1-c))+self.point[2]*(-self.axis[1]*s), self.point[0]*(self.axis[0]*self.axis[1]*(1-c))+self.point[1]*(c+self.axis[1]**2*(1-c))+self.point[2]*(self.axis[0]*s), self.point[0]*(self.axis[1]*s)+self.point[1]*(-self.axis[0]*s)+self.point[2]*(c)]

                # full
                # self.point = [self.point[0]*(c+self.axis[0]**2*(1-c))+self.point[1]*(self.axis[1]*self.axis[0]*(1-c)+self.axis[2]*s)+self.point[2]*(self.axis[2]*self.axis[0]*(1-c)-self.axis[1]*s), self.point[0]*(self.axis[0]*self.axis[1]*(1-c)-self.axis[2]*s)+self.point[1]*(c+self.axis[1]**2*(1-c))+self.point[2]*(self.axis[2]*self.axis[1]*(1-c)+self.axis[0]*s), self.point[0]*(self.axis[0]*self.axis[2]*(1-c)+self.axis[1]*s)+self.point[1]*(self.axis[1]*self.axis[2]*(1-c)-self.axis[0]*s)+self.point[2]*(c+self.axis[2]**2*(1-c))]


                # https://www.symbolab.com/solver/matrix-multiply-calculator/%5Cbegin%7Bpmatrix%7Dcos%5Cleft(%5Ctheta%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5E%7B2%7D%5Ccdot%5Cleft(1-cos%5Cleft(%5Ctheta%5Cright)%5Cright)%26u%5Cleft%5B0%5Cright%5D%5Ccdot%20u%5Cleft%5B1%5Cright%5D%5Ccdot%5Cleft(1-cos%5Cleft(%5Ctheta%5Cright)%5Cright)-u%5Cleft%5B2%5Cright%5D%5Ccdot%20sin%5Cleft(%5Ctheta%5Cright)%26u%5Cleft%5B0%5Cright%5D%5Ccdot%20u%5Cleft%5B2%5Cright%5D%5Ccdot%5Cleft(1-cos%5Cleft(%5Ctheta%5Cright)%5Cright)%2Bu%5Cleft%5B1%5Cright%5D%5Ccdot%20sin%5Cleft(%5Ctheta%5Cright)%5C%5C%20%20u%5Cleft%5B1%5Cright%5D%5Ccdot%20u%5Cleft%5B2%5Cright%5D%5Ccdot%5Cleft(1-cos%5Cleft(%5Ctheta%5Cright)%5Cright)%2Bu%5Cleft%5B2%5Cright%5D%5Ccdot%20sin%5Cleft(%5Ctheta%5Cright)%26cos%5Cleft(%5Ctheta%5Cright)%2Bu%5Cleft%5B1%5Cright%5D%5E%7B2%7D%5Ccdot%5Cleft(1-cos%5Cleft(%5Ctheta%5Cright)%5Cright)%26u%5Cleft%5B1%5Cright%5D%5Ccdot%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5Ccdot%20sin%5Cleft(%5Ctheta%20%5Cright)%5C%5C%20u%5Cleft%5B0%5Cright%5D%5Ccdot%20u%5Cleft%5B2%5Cright%5D%5Ccdot%5Cleft(1-cos%5Cleft(%5Ctheta%5Cright)%5Cright)-u%5Cleft%5B1%5Cright%5D%5Ccdot%20sin%5Cleft(%5Ctheta%5Cright)%26u%5Cleft%5B1%5Cright%5D%5Ccdot%20u%5Cleft%5B2%5Cright%5D%5Ccdot%5Cleft(1-cos%5Cleft(%5Ctheta%5Cright)%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5Ccdot%20sin%5Cleft(%5Ctheta%5Cright)%26cos%5Cleft(%5Ctheta%5Cright)%2Bu%5Cleft%5B2%5Cright%5D%5E%7B2%7D%5Ccdot%5Cleft(1-cos%5Cleft(%5Ctheta%5Cright)%5Cright)%5Cend%7Bpmatrix%7D?or=input

                # https://www.euclideanspace.com/
                # https://www.euclideanspace.com/maths/geometry/rotations/index.htm
                # https://ai.stackexchange.com/questions/14041/how-can-i-derive-the-rotation-matrix-from-the-axis-angle-rotation-vector


                #temp
                # https://www.symbolab.com/solver/matrix-multiply-calculator/%5Cbegin%7Bpmatrix%7Dcos%5Cleft(%5Ctheta%20%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5E%7B2%7D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%26u%5Cleft%5B0%5Cright%5D%5Ccdot%20%20u%5Cleft%5B1%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)-u%5Cleft%5B2%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%26u%5Cleft%5B0%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B1%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%5C%5C%20%20%20%20u%5Cleft%5B1%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B2%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%26cos%5Cleft(%5Ctheta%20%5Cright)%2Bu%5Cleft%5B1%5Cright%5D%5E%7B2%7D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%26u%5Cleft%5B1%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%5C%5C%20%20%20u%5Cleft%5B0%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)-u%5Cleft%5B1%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%26u%5Cleft%5B1%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%26cos%5Cleft(%5Ctheta%20%5Cright)%2Bu%5Cleft%5B2%5Cright%5D%5E%7B2%7D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%5Cend%7Bpmatrix%7D%5Ccdot%5Cbegin%7Bpmatrix%7Dcos%5Cleft(%5Ctheta%20%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5E%7B2%7D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%26u%5Cleft%5B0%5Cright%5D%5Ccdot%20%20u%5Cleft%5B1%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)-u%5Cleft%5B2%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%26u%5Cleft%5B0%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B1%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%5C%5C%20%20%20%20u%5Cleft%5B1%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B2%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%26cos%5Cleft(%5Ctheta%20%5Cright)%2Bu%5Cleft%5B1%5Cright%5D%5E%7B2%7D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%26u%5Cleft%5B1%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%5C%5C%20%20%20u%5Cleft%5B0%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)-u%5Cleft%5B1%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%26u%5Cleft%5B1%5Cright%5D%5Ccdot%20%20u%5Cleft%5B2%5Cright%5D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%2Bu%5Cleft%5B0%5Cright%5D%5Ccdot%20%20sin%5Cleft(%5Ctheta%20%5Cright)%26cos%5Cleft(%5Ctheta%20%5Cright)%2Bu%5Cleft%5B2%5Cright%5D%5E%7B2%7D%5Ccdot%20%5Cleft(1-cos%5Cleft(%5Ctheta%20%5Cright)%5Cright)%5Cend%7Bpmatrix%7D?or=input

                # q     = math.cos(self.angle/2) + self.point[0] * ( self.axis[0] * math.sin(self.angle/2)) + self.point[1] * ( self.axis[1] * math.sin(self.angle/2)) + self.point[2] * ( self.axis[2] * math.sin(self.angle/2))
                # conjq = math.cos(self.angle/2) - self.point[0] * ( self.axis[0] * math.sin(self.angle/2)) - self.point[1] * ( self.axis[1] * math.sin(self.angle/2)) - self.point[2] * ( self.axis[2] * math.sin(self.angle/2))

                # q = math.cos(self.angle/2) + self.axis[0]*math.sin(self.angle/2) + self.axis[1]*math.sin(self.angle/2) + self.axis[2]*math.sin(self.angle/2)
                # q = math.cos(self.angle/2) - self.axis[0]*math.sin(self.angle/2) - self.axis[1]*math.sin(self.angle/2) - self.axis[2]*math.sin(self.angle/2)

                # self.point = [q * self.point[i] * conjq for i in range(3)]


                if self.currentRotationType.get() == self.rotationTypes[0]:
                    s = math.sin(self.rotation[1])
                    c = math.cos(self.rotation[1])

                    Rx = [[ 1,  0,  0],
                          [ 0,  c, -s],
                          [ 0,  s,  c]]

                    s = math.sin(self.rotation[0])
                    c = math.cos(self.rotation[0])

                    Ry = [[ c,  0,  s],
                          [ 0,  1,  0],
                          [-s,  0,  c]]

                    self.point = self.multiply_matricies(self.point, Ry)
                    self.point = self.multiply_matricies(self.point, Rx)

                elif self.currentRotationType.get() == self.rotationTypes[1]:
                    self.point = self.multiply_matricies(self.point, self.rotation)



                points.append([(self.point[i]*self.zoom+self.object.position[i]) for i in range(2)])

            self.canvas.create_polygon(points, fill="", outline="black")


    def rotate_start(self, event):
        # print("Start")
        # print(event.x, event.y)
        # self.rotateStartPos = [event.x, event.y]
        self.prevPos = [event.x, event.y]
        self.rotateEventID = self.canvas.bind("<Motion>", self.rotate)

    def rotate(self, event):
        # print("Rotating")
        # rotateRelPos = [event.x - self.rotateStartPos[0], self.rotateStartPos[1] - event.y]
        # self.angle = math.sqrt(rotateRelPos[0]**2 + rotateRelPos[1]**2)
        # self.axis = [(rotateRelPos[1-i] / self.angle) for i in range(2)]


        # relPos = [event.x - self.prevPos[0], event.y - self.prevPos[1]]
        # angle = math.sqrt(relPos[0]**2 + relPos[1]**2)
        # axis = [(relPos[1-i] / angle) for i in range(2)]
        # axis.append(0)
        # self.Mpos = [relPos[i] + self.Mpos[i] for i in range(2)]
        # print()
        # print(relPos)
        # print(self.Mpos)
        # angle /= 100

        # s = math.sin(angle)
        # c = math.cos(angle)
        # t = 1 - c
        # u = axis

        # R = [[t*u[0]**2 + c, t*u[0]*u[1] - u[2]*s, t*u[0]*u[2] + u[1]*s],
        #      [t*u[0]*u[1] + u[2]*s, t*u[1]**2 + c, t*u[1]*u[2] - u[0]*s],
        #      [t*u[0]*u[2] - u[1]*s, t*u[1]*u[2] + u[0]*s, t*u[2]**2 + c]]

        # self.rotation = self.multiply_matricies(self.rotation, R)



        relPos = [event.x - self.prevPos[0], event.y - self.prevPos[1]]
        
        if self.currentRotationType.get() == self.rotationTypes[0]:
            self.rotation = [self.rotation[i] + relPos[i]/100 for i in range(2)]

        elif self.currentRotationType.get() == self.rotationTypes[1]:
            s = math.sin(relPos[1]/100)
            c = math.cos(relPos[1]/100)

            Rx = [[ 1,  0,  0],
                [ 0,  c, -s],
                [ 0,  s,  c]]

            s = math.sin(relPos[0]/100)
            c = math.cos(relPos[0]/100)

            Ry = [[ c,  0,  s],
                [ 0,  1,  0],
                [-s,  0,  c]]

            self.rotation = self.multiply_matricies(self.rotation, Rx)
            self.rotation = self.multiply_matricies(self.rotation, Ry)








        # print()
        # print(self.axis)
        # print(self.angle)

        #########################
        ### ZeroDivisionError ###
        #########################

        # relPos = [self.prevPos[0] - event.x, event.y - self.prevPos[1]]

        # self.rotation = [self.rotation[i] + relPos[i] + self.canvasSize[i]/2 for i in range(2)]



        # self.rotation = [300, 300]

        self.update()
        # self.canvas.create_rectangle(self.Mpos[0]-5, self.Mpos[1]-5, self.Mpos[0]+5, self.Mpos[1]+5, fill="red")
        # self.canvas.create_rectangle(self.rotation[0]-5, self.rotation[1]-5, self.rotation[0]+5, self.rotation[1]+5, fill="red")


        self.prevPos = [event.x, event.y]

        # self.prevPos = relPos
        # self.prevAngle += self.angle
        # self.prevAxis = [(relPos[1-i] / self.angle*100) for i in range(2)]

    def rotate_end(self, event):
        # print("End")
        # print(event.x, event.y)
        # self.prevAngle = self.angle
        # self.prevAxis = self.axis
        self.canvas.unbind("<Motion>", self.rotateEventID)


    def rotation_type_change(self, *args):
        currentRotationType = self.currentRotationType.get()
        if currentRotationType == self.rotationTypes[0]:
            self.rotation = [0, 0]
        elif currentRotationType == self.rotationTypes[1]:
            self.rotation = [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]]
        
        self.update()
        

    def multiply_matricies(self, M1, M2):
        for i in range(2):
            M = [M1, M2]
            if str(type(M[i][0]))[8:-2] != "list":
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
    

    def on_window_resize(self, event):
        if event.widget == self:
            asd = [event.width - self.panelSize[0], event.height - self.panelSize[1]]
            self.canvas.configure(width=asd[0], height=asd[1])