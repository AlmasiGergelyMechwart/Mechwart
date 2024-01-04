import tkinter as tk
from tkinter import ttk
import math

# import numpy as np

from object import Object

class GUI(tk.Tk):

    windowSize = [900, 500]
    canvasSize = [800, 400]

    # object = Object("obj/MaleLow.obj")
    object = Object("obj/cube4.obj")

    zoom = 50

    def __init__(self):
        super().__init__()

        # root
        self.minsize(self.windowSize[0], self.windowSize[1])
        self.configure(
            bg="lightgrey"
        )
   
        # canvas
        self.canvas = tk.Canvas(self, width=self.canvasSize[0], height=self.canvasSize[1])
        self.canvas.pack(anchor="nw")

        # rotation optionMenu
        self.rotationTypes = ["Local Axis rotation", "Global Axis rotation"]
        self.currentRotationType = tk.StringVar(self)
        self.rotationOptionMenu = ttk.OptionMenu(self, self.currentRotationType, self.rotationTypes[0], *self.rotationTypes, command=self.reset_rotation)
        self.rotationOptionMenu.pack()

        self.canvas.bind("<ButtonPress-3>", self.rotate_start)
        self.canvas.bind("<ButtonRelease-3>", self.rotate_end)


        self.update()

    def update(self):
        self.canvas.delete("all")

        for face in self.object.faces:
            points = []
            for f in face:
                self.point = [(self.object.vertices[f-1][i]+self.object.offset[i]) for i in range(3)]
                # multiply by -1 so it is not upside down
                self.point[1] *= -1

                self.object.position = [self.canvasSize[0]/2, self.canvasSize[1]/2]


                if self.currentRotationType.get() == self.rotationTypes[0]:
                    s = math.sin(self.object.rotation["axis"][1])
                    c = math.cos(self.object.rotation["axis"][1])

                    Rx = [[ 1,  0,  0],
                          [ 0,  c, -s],
                          [ 0,  s,  c]]

                    s = math.sin(self.object.rotation["axis"][0])
                    c = math.cos(self.object.rotation["axis"][0])

                    Ry = [[ c,  0,  s],
                          [ 0,  1,  0],
                          [-s,  0,  c]]

                    self.point = self.multiply_matricies(self.multiply_matricies(self.point, Ry), Rx)

                elif self.currentRotationType.get() == self.rotationTypes[1]:
                    self.point = self.multiply_matricies(self.point, self.object.rotation["matrix"])


                points.append([(self.point[i]*self.zoom+self.object.position[i]) for i in range(2)])

            self.canvas.create_polygon(points, fill="", outline="black")


    def rotate_start(self, event):
        self.prevPos = [event.x, event.y]
        self.rotateEventID = self.canvas.bind("<Motion>", self.rotate)

    def rotate(self, event):
        # in pixels
        relPos = [event.x - self.prevPos[0], event.y - self.prevPos[1]]

        # in radians
        angle = [math.radians(relPos[i]) for i in range(2)]

        # 1 pixel moved by cursor is 1 degree rotation
        
        if self.currentRotationType.get() == self.rotationTypes[0]:
            self.object.rotation["axis"] = [self.object.rotation["axis"][i] + angle[i] for i in range(2)]

        elif self.currentRotationType.get() == self.rotationTypes[1]:
            s = math.sin(angle[1])
            c = math.cos(angle[1])

            Rx = [[ 1,  0,  0],
                  [ 0,  c, -s],
                  [ 0,  s,  c]]

            s = math.sin(angle[0])
            c = math.cos(angle[0])

            Ry = [[ c,  0,  s],
                  [ 0,  1,  0],
                  [-s,  0,  c]]

            self.object.rotation["matrix"] = self.multiply_matricies(self.multiply_matricies(self.object.rotation["matrix"], Ry), Rx)


        self.update()

        self.prevPos = [event.x, event.y]


    def rotate_end(self, event):
        self.canvas.unbind("<Motion>", self.rotateEventID)


    def reset_rotation(self, *args):
        self.object.rotation["axis"] = [0, 0]
        self.object.rotation["matrix"] = [[1, 0, 0],
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