import tkinter as tk
from tkinter import ttk, colorchooser
import math

from object import Object

class GUI(tk.Tk):

    canvasPanelRatio = [0.75, 0.9]

    backgroundColor = "grey"
    canvasColor = "white"
    fillColor = "lightgrey"
    lineColor = "black"

    windowSize = [0, 0]
    canvasSize = [0, 0]
    rightPanelSize = [0, 0]
    bottomPanelSize = [0, 0]

    object = Object("obj/MaleLow.obj")
    # object = Object("obj/cube.obj")
    # object = Object("obj/tank.obj")

    def __init__(self):
        super().__init__()

        # root
        self.minsize(900, 500)
        self.configure(
            bg=self.backgroundColor
        )

        canvasOffset = [0.015, 0.02]

        # canvas
        self.canvas = tk.Canvas(self, background=self.canvasColor)
        self.canvas.place(relx=canvasOffset[0], rely=canvasOffset[1], relwidth=self.canvasPanelRatio[0], relheight=self.canvasPanelRatio[1])
        self.canvas.update()

        # -----x-----

        # right panel
        self.rightPanel = tk.Frame(self, background=self.backgroundColor)
        self.rightPanel.place(relx=canvasOffset[0]+self.canvasPanelRatio[0], rely=canvasOffset[1], relwidth=1-self.canvasPanelRatio[0]-canvasOffset[0], relheight=self.canvasPanelRatio[1])
        self.rightPanel.update()

        self.rightPanelButtonNames = ["reset_zoom", "reset_position", "reset_rotation"]
        self.rightPanelButtons = [0 for i in range(4)]
        numOfButtons = 10
        panelPadding = [0.04, 0.03] # top, bottom
        margin = [0.01, 0.1] # top-bottom, left-right

        self.rotationTypes = ["Local Axis rotation", "Global Axis rotation"]
        self.currentRotationType = tk.StringVar(self)
        self.rightPanelButtons[3] = ttk.OptionMenu(self.rightPanel, self.currentRotationType, self.rotationTypes[0], *self.rotationTypes, command=self.reset_rotation)

        for i in range(len(self.rightPanelButtons)):
            if self.rightPanelButtons[i] == 0:
                self.rightPanelButtons[i] = ttk.Button(self.rightPanel, text=" ".join(self.rightPanelButtonNames[i].split("_")).capitalize(), command=eval("self.%s" % self.rightPanelButtonNames[i]))
            self.rightPanelButtons[i].place(relx=margin[1], rely=panelPadding[0]+margin[0]+i/numOfButtons-sum([panelPadding[n]/numOfButtons*i for n in range(2)]), relwidth=1-margin[1]*2, relheight=1/numOfButtons-margin[0]*2-sum([panelPadding[n]/numOfButtons for n in range(2)]))

        # # reset zoom button
        # id = 0
        # self.resetZoomButton = ttk.Button(self.rightPanel, text="Reset zoom", command=self.reset_zoom)
        # self.resetZoomButton.place(relx=margin[1], rely=panelPadding[0]+margin[0]+id/numOfButtons-sum([panelPadding[i]/numOfButtons*id for i in range(2)]), relwidth=1-margin[1]*2, relheight=1/numOfButtons-margin[0]*2-sum([panelPadding[i]/numOfButtons for i in range(2)]))

        # # reset position button
        # id = 1
        # self.resetPositionButton = ttk.Button(self.rightPanel, text="Reset position", command=self.reset_position)
        # self.resetPositionButton.place(relx=margin[1], rely=panelPadding[0]+margin[0]+id/numOfButtons-sum([panelPadding[i]/numOfButtons*id for i in range(2)]), relwidth=1-margin[1]*2, relheight=1/numOfButtons-margin[0]*2-sum([panelPadding[i]/numOfButtons for i in range(2)]))

        # # reset rotation button
        # id = 2
        # self.resetRotationButton = ttk.Button(self.rightPanel, text="Reset rotation", command=self.reset_rotation)
        # self.resetRotationButton.place(relx=margin[1], rely=panelPadding[0]+margin[0]+id/numOfButtons-sum([panelPadding[i]/numOfButtons*id for i in range(2)]), relwidth=1-margin[1]*2, relheight=1/numOfButtons-margin[0]*2-sum([panelPadding[i]/numOfButtons for i in range(2)]))

        # rotation optionMenu
        # id = 3
        # self.rotationTypes = ["Local Axis rotation", "Global Axis rotation"]
        # self.currentRotationType = tk.StringVar(self)
        # self.rotationOptionMenu = ttk.OptionMenu(self.rightPanel, self.currentRotationType, self.rotationTypes[0], *self.rotationTypes, command=self.reset_rotation)
        # self.rotationOptionMenu.place(relx=margin[1], rely=panelPadding[0]+margin[0]+id/numOfButtons-sum([panelPadding[i]/numOfButtons*id for i in range(2)]), relwidth=1-margin[1]*2, relheight=1/numOfButtons-margin[0]*2-sum([panelPadding[i]/numOfButtons for i in range(2)]))

        # buttons = []
        # numOfButtons = 8
        # panelPadding = [0.04, 0.03] # top, bottom
        # margin = [0.01, 0.1] # top-bottom, left-right
        # for id in range(numOfButtons):
        #     buttons.append(ttk.Button(self.rightPanel))
        #     buttons[id].place(relx=margin[1], rely=panelPadding[0]+margin[0]+id/numOfButtons-sum([panelPadding[i]/numOfButtons*id for i in range(2)]), relwidth=1-margin[1]*2, relheight=1/numOfButtons-margin[0]*2-sum([panelPadding[i]/numOfButtons for i in range(2)]))

        # -----x-----

        # bottom panel
        self.bottomPanel = tk.Frame(self, background=self.backgroundColor)
        self.bottomPanel.place(relx=canvasOffset[0], rely=canvasOffset[1]+self.canvasPanelRatio[1], relwidth=1-canvasOffset[0], relheight=1-self.canvasPanelRatio[1]-canvasOffset[1])
        self.bottomPanel.update()

        self.bottomPanelButtonNames = ["canvas_color", "fill_color", "line_color"]
        self.bottomPanelButtons = [0 for i in range(3)]
        numOfButtons = 4
        # panelPadding = [0.005, 1-self.canvasPanelRatio[0]-canvasOffset[0]+0.005] # left, right
        panelPadding = [0.005, 0.005] # left, right
        margin = [0.1, 0.02] # top-bottom, left-right

        labelButtonRatio = 0.4
        buttonRelSize = [0.8, 0.8]

        for i in range(len(self.bottomPanelButtons)):
            self.bottomPanelButtons[i] = [0, 0]
            self.bottomPanelButtons[i][0] = ttk.Label(self.bottomPanel, text=self.bottomPanelButtonNames[i].replace("_", " ").capitalize()+":", background="lightblue")
            self.bottomPanelButtons[i][0].place(relx=panelPadding[0]+margin[1]+i/numOfButtons-sum([panelPadding[j]/numOfButtons*i for j in range(2)]), rely=margin[0], relwidth=1/numOfButtons-margin[1]*2-sum([panelPadding[j]/numOfButtons for j in range(2)]), relheight=1-margin[0]*2)
            fullwidth = float(self.bottomPanelButtons[i][0].place_info()["relwidth"])
            self.bottomPanelButtons[i][0].place_configure(relwidth=fullwidth*labelButtonRatio)

            varName = "self.%s" % list(map(lambda y: y[0].lower()+y[1:], ["".join(map(lambda x: x[0].upper()+x[1:], self.bottomPanelButtonNames[i].split("_")))]))[0]
            # print(varName)
            self.bottomPanelButtons[i][1] = tk.Button(self.bottomPanel, relief="flat", background=eval(varName), command=lambda: eval("self.change_%s()" % self.bottomPanelButtonNames[i]))
            # print("self.%s" % list(map(lambda y: y[0].lower()+y[1:], ["".join(map(lambda x: x[0].upper()+x[1:], self.bottomPanelButtonNames[i].split("_")))]))[0])
            # print("self.%s" % list(map(lambda y: y[0].lower()+y[1:], ["".join(map(lambda x: x[0].upper()+x[1:], self.bottomPanelButtonNames[i].split("_")))]))[0])

            self.bottomPanelButtons[i][1].place(relx=float(self.bottomPanelButtons[i][0].place_info()["relx"])+fullwidth*labelButtonRatio+fullwidth*(1-labelButtonRatio)*(1-buttonRelSize[0])/2, rely=float(self.bottomPanelButtons[i][0].place_info()["rely"])+float(self.bottomPanelButtons[i][0].place_info()["relheight"])*(1-buttonRelSize[1])/2, relwidth=fullwidth*(1-labelButtonRatio)*buttonRelSize[0], relheight=float(self.bottomPanelButtons[i][0].place_info()["relheight"])*buttonRelSize[1])

        print(self.bottomPanelButtons)

        # fill color picker
        # id = 0
        # fillColorLabelButtonRatio = 0.4
        # fillColorButtonRelSize = [0.8, 0.8]

        # self.fillColorLabel = ttk.Label(self.bottomPanel, text="Fill color:", background=self.backgroundColor)
        # self.fillColorLabel.place(relx=panelPadding[0]+margin[1]+id/numOfButtons-sum([panelPadding[i]/numOfButtons*id for i in range(2)]), rely=margin[0], relwidth=1/numOfButtons-margin[1]*2-sum([panelPadding[i]/numOfButtons for i in range(2)]), relheight=1-margin[0]*2)
        # fillColorFullwidth = float(self.fillColorLabel.place_info()["relwidth"])
        # self.fillColorLabel.place_configure(relwidth=fillColorFullwidth*fillColorLabelButtonRatio)

        # self.fillColorButton = tk.Button(self.bottomPanel, relief="flat", background=self.fillColor, command=lambda: self.change_color("self.fillColor"))
        # self.fillColorButton.place(relx=float(self.fillColorLabel.place_info()["relx"])+fillColorFullwidth*fillColorLabelButtonRatio+fillColorFullwidth*(1-fillColorLabelButtonRatio)*(1-fillColorButtonRelSize[0])/2, rely=float(self.fillColorLabel.place_info()["rely"])+float(self.fillColorLabel.place_info()["relheight"])*(1-fillColorButtonRelSize[1])/2, relwidth=fillColorFullwidth*(1-fillColorLabelButtonRatio)*fillColorButtonRelSize[0], relheight=float(self.fillColorLabel.place_info()["relheight"])*fillColorButtonRelSize[1])


        # buttons = []
        # numOfButtons = 4
        # panelPadding = [0.005, 1-self.canvasPanelRatio[0]-canvasOffset[0]+0.005] # left, right
        # print(panelPadding)
        # margin = [0.1, 0.02] # top-bottom, left-right
        # for id in range(numOfButtons):
        #     buttons.append(ttk.Button(self.bottomPanel))
        #     buttons[id].place(relx=panelPadding[0]+margin[1]+id/numOfButtons-sum([panelPadding[i]/numOfButtons*id for i in range(2)]), rely=margin[0], relwidth=1/numOfButtons-margin[1]*2-sum([panelPadding[i]/numOfButtons for i in range(2)]), relheight=1-margin[0]*2)

        # -----x-----

        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<ButtonRelease-1>", self.move_end)

        self.canvas.bind("<ButtonPress-3>", self.rotate_start)
        self.canvas.bind("<ButtonRelease-3>", self.rotate_end)

        self.canvas.bind("<MouseWheel>", self.zoom_change)

        self.bind("<Configure>", self.on_window_resize)

        self.on_window_resize()

        self.reset_zoom()

        self.reset_position()

        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")

        faces = []

        for i in range(len(self.object.faces)):
            points = []
            vertexNormals = []
            for j in range(len(self.object.faces[i])):
                point = [(self.object.vertices[self.object.faces[i][j][0]-1][n]+self.object.offset[n]) for n in range(3)]
                # multiply by -1 so it is not upside down
                point[1] *= -1

                point = self.rotate_point(point)

                points.append([(point[i]*self.object.zoom+(self.object.position[i] if i < 2 else 0)) for i in range(3)])

                if len(self.object.vertexNormals) > 0:
                    vertexNormal = self.object.vertexNormals[self.object.faces[i][j][2]-1]
                    # vertexNormal[1] *= -1
                    vertexNormal = [vertexNormal[0], -vertexNormal[1], vertexNormal[2]]

                    vertexNormal = self.rotate_point(vertexNormal)

                    vertexNormals.append(vertexNormal)

                    # self.canvas.create_line([points[j][n] for n in range(2)], [points[j][n]+vertexNormal[n]*10 for n in range(2)], fill="orange", width=2)

            if len(vertexNormals) > 0:
                facingZ = max([vertexNormals[m][2] for m in range(len(vertexNormals))])

                # midPoints = [sum([points[m][n] for m in range(len(points))])/len(points) for n in range(2)]
                # midVertexNormals = [sum([vertexNormals[m][n] for m in range(len(vertexNormals))])/len(vertexNormals) for n in range(2)]
                # self.canvas.create_line(midPoints, [midPoints[n]+midVertexNormals[n]*20 for n in range(2)], fill="orange", width=2)

                if facingZ > 0:
                    faces.append(points)
            else:
                faces.append(points)


        # print(faces[0])
        faces.sort(key=lambda points: sum([points[n][2] for n in range(len(points))])/len(points))

        for points in faces:
            points = [[point[n] for n in range(2)] for point in points]
            self.canvas.create_polygon(points, fill=self.fillColor, outline=self.lineColor)

        print("%s/%s" % (len(faces), len(self.object.faces)))

        # for i in verticies:
            # self.canvas.create_rectangle([i.split(";") for n in range(2)], outline="red")

        # for i in self.object.vertices:
        #     i = [i[n]+self.object.offset[n] for n in range(3)]
        #     i[1] *= -1
        #     if self.currentRotationType.get() == self.rotationTypes[0]:
        #         s = math.sin(self.object.rotation["angles"][0])
        #         c = math.cos(self.object.rotation["angles"][0])
        #         Rx = [[ 1,  0,  0],
        #               [ 0,  c, -s],
        #               [ 0,  s,  c]]
        #         s = math.sin(self.object.rotation["angles"][1])
        #         c = math.cos(self.object.rotation["angles"][1])
        #         Ry = [[ c,  0,  s],
        #               [ 0,  1,  0],
        #               [-s,  0,  c]]
        #         i = self.multiply_matricies(self.multiply_matricies(i, Ry), Rx)
        #     elif self.currentRotationType.get() == self.rotationTypes[1]:
        #         i = self.multiply_matricies(i, self.object.rotation["matrix"])
        #     i = [(i[n]*self.object.zoom+self.object.position[n]) for n in range(2)]
        #     self.canvas.create_rectangle(i, i, outline="red")




    def on_window_resize(self, event=""):
        if event != "":
            if event.widget == self and self.windowSize != [event.width, event.height]:
                self.windowSize = [event.width, event.height]
            elif event.widget == self.canvas and self.canvasSize != [event.width, event.height]:
                relCanvasSize = [event.width - self.canvasSize[0], event.height - self.canvasSize[1]]
                self.object.position = [self.object.position[i]+relCanvasSize[i]/2 for i in range(2)]
                self.canvasSize = [event.width, event.height]
                self.update_canvas()
            elif event.widget == self.rightPanel and self.rightPanelSize != [event.width, event.height]:
                self.rightPanelSize = [event.width, event.height]
            elif event.widget == self.bottomPanel and self.bottomPanelSize != [event.width, event.height]:
                self.bottomPanelSize = [event.width, event.height]
        else:
            self.windowSize = [self.winfo_width(), self.winfo_height()]
            self.canvasSize = [self.canvas.winfo_width(), self.canvas.winfo_height()]
            self.rightPanelSize = [self.rightPanel.winfo_width(), self.rightPanel.winfo_height()]
            self.bottomPanelSize = [self.bottomPanel.winfo_width(), self.bottomPanel.winfo_height()]



    def move_start(self, event):
        self.movePrevPos = [event.x, event.y]
        self.moveEventID = self.canvas.bind("<Motion>", self.move)

    def move(self, event):
        moveRelPos = [event.x - self.movePrevPos[0], event.y - self.movePrevPos[1]]
        self.object.position = [self.object.position[i]+moveRelPos[i] for i in range(2)]

        self.update_canvas()

        self.movePrevPos = [event.x, event.y]

    def move_end(self, event):
        self.canvas.unbind("<Motion>", self.moveEventID)

    def reset_position(self):
        self.object.position = [self.canvas.winfo_width()/2, self.canvas.winfo_height()/2]

        self.update_canvas()


    def rotate_start(self, event):
        self.rotatePrevPos = [event.x, event.y]
        self.rotateEventID = self.canvas.bind("<Motion>", self.rotate)

    def rotate(self, event):
        # in pixels
        rotateRelPos = [event.x - self.rotatePrevPos[0], event.y - self.rotatePrevPos[1]]

        # in radians
        angle = [math.radians(rotateRelPos[1-i]/2) for i in range(2)]
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

        self.update_canvas()

        self.rotatePrevPos = [event.x, event.y]

    def rotate_end(self, event):
        self.canvas.unbind("<Motion>", self.rotateEventID)

    def reset_rotation(self):
        self.object.rotation["angles"] = [0, 0]
        self.object.rotation["matrix"] = [[1, 0, 0],
                                          [0, 1, 0],
                                          [0, 0, 1]]

        self.update_canvas()


    def rotate_point(self, point):
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

        return point


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
            self.object.zoom = self.object.zoom*1.1
        elif event.delta < 0:
            self.object.zoom = self.object.zoom/1.1

        self.update_canvas()

    def reset_zoom(self):
        if self.object.size[0] > self.object.size[1]:
            self.object.zoom = self.canvasSize[0]/self.object.size[0]*0.8
        else:
            self.object.zoom = self.canvasSize[1]/self.object.size[1]*0.8
        self.baseZoom = self.object.zoom

        self.update_canvas()

    # def change_color(self, variable):
    #     color = colorchooser.askcolor()
    #     if color[1] != None:
    #         exec("%s = color[1]" % variable)
    #         print(variable)
    #         try:
    #             exec("%sButton['bg'] = color[1]" % variable)
    #         except:
    #             pass
    #     # print()

    #     self.update_canvas()
        
    def change_canvas_color(self):
        color = colorchooser.askcolor()
        if color[1] != None:
            self.canvasColor = color[1]

    def change_fill_color(self):
        color = colorchooser.askcolor()
        if color[1] != None:
            self.fillColor = color[1]

    def change_line_color(self):
        color = colorchooser.askcolor()
        if color[1] != None:
            self.lineColor = color[1]