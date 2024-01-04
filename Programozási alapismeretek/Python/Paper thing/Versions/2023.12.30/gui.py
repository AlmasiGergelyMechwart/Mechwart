import tkinter as tk
from tkinter import ttk
import math
import time

from object import Object

class GUI(tk.Tk):

    CANVASPANELRATIO = [0.75, 0.9]

    continous = True

    windowSize = [0, 0]
    canvasSize = [0, 0]
    rightPanelSize = [0, 0]

    # object = Object("obj/MaleLow.obj")
    object = Object("obj/cube4.obj")

    zoom = 50

    def __init__(self):
        super().__init__()

        self.startTime = time.time()

        # root
        self.minsize(900, 500)
        self.configure(
            bg="lightblue"
        )
   
        # canvas
        self.canvas = tk.Canvas(self)
        self.canvas.place(relwidth=self.CANVASPANELRATIO[0], relheight=self.CANVASPANELRATIO[1])
        self.canvas.update()

        # right panel
        self.rightPanel = tk.Frame(self, background="lightgrey")
        self.rightPanel.place(relx=self.CANVASPANELRATIO[0], relwidth=1-self.CANVASPANELRATIO[0], relheight=self.CANVASPANELRATIO[1])

        # rotation optionMenu
        self.rotationTypes = ["Local Axis rotation", "Global Axis rotation"]
        self.currentRotationType = tk.StringVar(self)
        self.rotationOptionMenu = ttk.OptionMenu(self.rightPanel, self.currentRotationType, self.rotationTypes[0], *self.rotationTypes, command=self.reset_rotation)
        self.rotationOptionMenu.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.08)

        # buttons = []
        # for i in range(10):
        #     buttons.append(ttk.Button(self.rightPanel))
        #     buttons[i].place(relx=0.1, rely=0.01+i/10, relwidth=0.8, relheight=0.08)

        self.canvas.bind("<ButtonPress-3>", self.rotate_start)
        self.canvas.bind("<ButtonRelease-3>", self.rotate_end)

        self.canvas.bind("<MouseWheel>", self.zoom_change)

        self.bind("<Configure>", self.on_window_resize)

        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")

        faces = []

        for i in range(len(self.object.faces)):
            points = []
            for faceID in self.object.faces[i]:
                point = [(self.object.vertices[faceID-1][i]+self.object.offset[i]) for i in range(3)]
                # multiply by -1 so it is not upside down
                point[1] *= -1

                self.object.position = [self.canvas.winfo_width()/2, self.canvas.winfo_height()/2]


                if self.currentRotationType.get() == self.rotationTypes[0]:
                    s = math.sin(self.object.rotation["angles"][0])
                    c = math.cos(self.object.rotation["angles"][0])

                    Rx = [[ 1,  0,  0],
                          [ 0,  c, -s],
                          [ 0,  s,  c]]

                    s = math.sin(self.object.rotation["angles"][1])
                    c = math.cos(self.object.rotation["angles"][1])

                    Ry = [[ c,  0,  s],
                          [ 0,  1,  0],
                          [-s,  0,  c]]

                    point = self.multiply_matricies(self.multiply_matricies(point, Ry), Rx)

                elif self.currentRotationType.get() == self.rotationTypes[1]:
                    point = self.multiply_matricies(point, self.object.rotation["matrix"])

                self.object.position.append(0)
                points.append([(point[i]*self.zoom+self.object.position[i]) for i in range(3)])

            # self.canvas.create_polygon(points, fill="", outline="black")
            faces.append(points)

        # for i in range(len(faces)):
        #     middle = [0, 0, 0]
        #     for j in range(len(faces[i])):
        #         middle = [middle[n] + faces[i][j][n] for n in range(3)]
        #     middle = [middle[n]/len(faces[i]) for n in range(3)]

        #     faces[i] = [faces[i], middle[2]]

        #     middle = [middle[n] for n in range(2)]
        #     self.canvas.create_polygon(middle, fill="", outline="blue")


        # faces.sort(key=lambda x: x[1])
            



        for i in range(len(faces)):
            for j in range(i, len(faces)):
                # check if they have a common vertex
                for k in range(len(faces[i])):
                    # print()
                    if faces[i][k] in faces[j]:
                        # print("%s and %s have the same vertex %s" % (faces[i], faces[j], faces[i][k]))
                        l = len(faces[i])-1 if k == 0 else k-1
                        h = 0 if k == len(faces[i])-1 else k+1
                        # print(l, k, h)
                        str = (math.sin(time.time() - self.startTime))-1
                        # str = -(time.time() - self.startTime)/5
                        # str = 10
                        # print(str)
                        point = [(faces[i][l][n]+faces[i][h][n]+faces[i][k][n]*str)/(2+str) for n in range(3)]
                        # point = [faces[i][k][n]+point[n]/10 for n in range(3)]
                        # print(faces[i][k])
                        # print(point)
                        asd1 = [faces[i][k][n] for n in range(2)]
                        asd2 = [point[n] for n in range(2)]
                        self.canvas.create_rectangle(asd1, asd1, fill="", outline="red")
                        self.canvas.create_rectangle(asd2, asd2, fill="", outline="blue")
                        # point = math.sqrt(faces[i][k-1]**2 + faces[i][k+1]**2)



        for i in range(len(faces)):
            points = []
            for j in range(len(faces[i])):
                points.append([faces[i][j][n] for n in range(2)])

            self.canvas.create_polygon(points, fill="", outline="black")





        # for i in range(len(facesZ)):
        #     for j in range(i, len(facesZ)):
        #         faceIZ = -math.inf
        #         for a in range(len(facesZ[i])):
        #             if faceIZ < facesZ[i][2]:
        #                 faceIZ = facesZ[i][2]
            
        # print(faces)
            
        # facesZ = []
        # for i in range(len(faces)):
        #     faceZ = -math.inf
        #     for j in range(len(faces[i])):
        #         if faceZ < faces[i][j][2]:
        #             faceZ = faces[i][j][2]
        #     facesZ.append([i, faceZ])

        #     for n in range(len(faces[i])):
        #         faces[i][n] = [faces[i][n][k] for k in range(2)]

        # # print(sorted(facesZ, key=lambda x: x[1]))
        # facesZ.sort(key=lambda x: x[1])
        # # print(facesZ)

        # # print(faces)


        # polygons = []
        # for i in range(len(facesZ)):
        #     polygon = (self.canvas.create_polygon(faces[facesZ[i][0]], fill="grey", outline="black"))
        #     # print(polygon)
        #     # self.canvas.delete(polygon)

            
        # for i in range(len(faces)): # faces
        #     print("-----x-----")
        #     fac = []
        #     fac2 = []
        #     poin = []
        #     facSum = [0, 0, 0]
        #     for j in range(len(faces[i])): # points
        #         fac.append([faces[i][j][n] for n in range(3)])
        #         facSum = [facSum[n] + faces[i][j][n] for n in range(3)]
        #         fac[j] = [fac[j][n] for n in range(2)]
        #     facSum = [facSum[n]/len(faces[i]) for n in range(3)]

        #     print(facSum)

        #     facSum = [facSum[n] for n in range(2)]

        #     self.canvas.create_polygon(fac, fill="", outline="black")
        #     self.canvas.create_polygon(facSum, fill="", outline="blue")



        # for i in range(len(faces)):
        #     for j in range(len(faces[i])):
        #         self.canvas.create_rectangle(faces[i][j][0], faces[i][j][1], faces[i][j][0], faces[i][j][1], outline="red")
        
        if self.continous == True:
            self.after(1, self.update_canvas)
        



    def rotate_start(self, event):
        self.prevPos = [event.x, event.y]
        self.rotateEventID = self.canvas.bind("<Motion>", self.rotate)

    def rotate(self, event):
        # in pixels
        relPos = [event.x - self.prevPos[0], event.y - self.prevPos[1]]

        # in radians
        angle = [math.radians(relPos[1-i]/2) for i in range(2)]
        angle[1] *= -1

        # 2 pixel moved by cursor is 1 degree rotation
        
        if self.currentRotationType.get() == self.rotationTypes[0]:
            self.object.rotation["angles"] = [self.object.rotation["angles"][i] + angle[i] for i in range(2)]

        elif self.currentRotationType.get() == self.rotationTypes[1]:
            s = math.sin(angle[0])
            c = math.cos(angle[0])

            Rx = [[ 1,  0,  0],
                  [ 0,  c, -s],
                  [ 0,  s,  c]]

            s = math.sin(angle[1])
            c = math.cos(angle[1])

            Ry = [[ c,  0,  s],
                  [ 0,  1,  0],
                  [-s,  0,  c]]

            self.object.rotation["matrix"] = self.multiply_matricies(self.multiply_matricies(self.object.rotation["matrix"], Ry), Rx)


        if self.continous == False:
            self.update_canvas()

        self.prevPos = [event.x, event.y]


    def rotate_end(self, event):
        self.canvas.unbind("<Motion>", self.rotateEventID)


    def reset_rotation(self, *args):
        self.object.rotation["angles"] = [0, 0]
        self.object.rotation["matrix"] = [[1, 0, 0],
                                          [0, 1, 0],
                                          [0, 0, 1]]
        
        if self.continous == False:
            self.update_canvas()
        

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
    

    def zoom_change(self, event):
        if event.delta > 0:
            self.zoom = self.zoom*1.1
        elif event.delta < 0:
            self.zoom = self.zoom/1.1

        if self.continous == False:
            self.update_canvas()
    

    def on_window_resize(self, event):
        if event.widget == self and self.windowSize != [event.width, event.height]:
            self.windowSize = [event.width, event.height]
        elif event.widget == self.canvas and self.canvasSize != [event.width, event.height]:
            self.canvasSize = [event.width, event.height]
            if self.continous == False:
                self.update_canvas()
        elif event.widget == self.rightPanel and self.rightPanelSize != [event.width, event.height]:
            self.rightPanelSize = [event.width, event.height]



