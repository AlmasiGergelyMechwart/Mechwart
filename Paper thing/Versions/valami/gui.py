import tkinter as tk
from tkinter import ttk
import math

from object import Object

class GUI(tk.Tk):

    windowSize = [900, 500]
    canvasSize = [800, 400]
    
    panelSize = []
    
    object = Object("obj/MaleLow.obj")
    # object = Object("obj/cube2.obj")

    zoom = 15

    def __init__(self):
        super().__init__()

        self.minsize(self.windowSize[0], self.windowSize[1])
        self.configure(
            bg="lightgrey"
        )

        # def onWindowResize(event):
        #     pass

        # root.bind("<Configure>", onWindowResize)

        self.canvas = tk.Canvas(self, width=self.canvasSize[0], height=self.canvasSize[1])
        self.canvas.pack(anchor="nw")

        self.canvas.bind("<ButtonPress-3>", self.rotate_start)
        self.canvas.bind("<ButtonRelease-3>", self.rotate_end)

        self.angle = 0
        self.axis = [0, 0, 0]
        self.prevAngle = 0
        self.prevAxis = [0, 0, 0]

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

                s = math.sin(-self.angle)
                c = math.cos(-self.angle)

                # self.point = [self.point[0]*(prevC+self.axis[0]**2*(1-prevC))+self.point[1]*(self.axis[1]*self.axis[0]*(1-prevC))+self.point[2]*(-self.axis[1]*prevS), self.point[0]*(self.axis[0]*self.axis[1]*(1-prevC))+self.point[1]*(prevC+self.axis[1]**2*(1-prevC))+self.point[2]*(self.axis[0]*prevS), self.point[0]*(self.axis[1]*prevS)+self.point[1]*(-self.axis[0]*prevS)+self.point[2]*(prevC)]

                # self.point = [self.point[0]*(c+self.axis[0]**2*(1-c))+self.point[1]*(self.axis[1]*self.axis[0]*(1-c)+self.axis[2]*s)+self.point[2]*(self.axis[2]*self.axis[0]*(1-c)-self.axis[1]*s), self.point[0]*(self.axis[0]*self.axis[1]*(1-c)-self.axis[2]*s)+self.point[1]*(c+self.axis[1]**2*(1-c))+self.point[2]*(self.axis[2]*self.axis[1]*(1-c)+self.axis[0]*s), self.point[0]*(self.axis[0]*self.axis[2]*(1-c)+self.axis[1]*s)+self.point[1]*(self.axis[1]*self.axis[2]*(1-c)-self.axis[0]*s)+self.point[2]*(c+self.axis[2]**2*(1-c))]
                self.point = [self.point[0]*(c+self.axis[0]**2*(1-c))+self.point[1]*(self.axis[1]*self.axis[0]*(1-c))+self.point[2]*(-self.axis[1]*s), self.point[0]*(self.axis[0]*self.axis[1]*(1-c))+self.point[1]*(c+self.axis[1]**2*(1-c))+self.point[2]*(self.axis[0]*s), self.point[0]*(self.axis[1]*s)+self.point[1]*(-self.axis[0]*s)+self.point[2]*(c)]
                
                
                
                # q     = math.cos(self.angle/2) + self.point[0] * ( self.axis[0] * math.sin(self.angle/2)) + self.point[1] * ( self.axis[1] * math.sin(self.angle/2)) + self.point[2] * ( self.axis[2] * math.sin(self.angle/2))
                # conjq = math.cos(self.angle/2) - self.point[0] * ( self.axis[0] * math.sin(self.angle/2)) - self.point[1] * ( self.axis[1] * math.sin(self.angle/2)) - self.point[2] * ( self.axis[2] * math.sin(self.angle/2))

                # q = math.cos(self.angle/2) + self.axis[0]*math.sin(self.angle/2) + self.axis[1]*math.sin(self.angle/2) + self.axis[2]*math.sin(self.angle/2)
                # q = math.cos(self.angle/2) - self.axis[0]*math.sin(self.angle/2) - self.axis[1]*math.sin(self.angle/2) - self.axis[2]*math.sin(self.angle/2)

                # self.point = [q * self.point[i] * conjq for i in range(3)]



                

                points.append([(self.point[i]*self.zoom+self.object.position[i]) for i in range(2)])
            
            self.canvas.create_polygon(points, fill="", outline="black")


    def rotate_start(self, event):
        # print("Start")
        # print(event.x, event.y)
        self.rotateStartPos = [event.x, event.y]
        self.rotateEventID = self.canvas.bind("<Motion>", self.rotate)

    def rotate(self, event):
        # print("Rotating")
        rotateRelPos = [event.x - self.rotateStartPos[0], self.rotateStartPos[1] - event.y]
        self.angle = math.sqrt(rotateRelPos[0]**2 + rotateRelPos[1]**2)
        self.axis = [(rotateRelPos[1-i] / self.angle) for i in range(2)]
        # ZeroDivisionError

        self.angle /= 100
        self.update()

    def rotate_end(self, event):
        # print("End")
        # print(event.x, event.y)
        # self.prevAngle = self.angle
        # self.prevAxis = self.axis
        self.canvas.unbind("<Motion>", self.rotateEventID)