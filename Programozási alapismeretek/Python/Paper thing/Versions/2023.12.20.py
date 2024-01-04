import tkinter as tk
from tkinter import ttk
import math
import time

root = tk.Tk()
root.minsize(900, 500)
root.configure(
    bg="lightgrey"
)

cSize = [800, 400]

canvas = tk.Canvas(root, width=cSize[0], height=cSize[1])
canvas.pack(anchor="nw")

object = {
    "vertices": [],
    "faces": [],
    "min": [math.inf, math.inf, math.inf],
    "max": [-math.inf, -math.inf, -math.inf],
    "size": [0, 0, 0],
    "offset": [0, 0],
    "position": [0, 0]
}

f = open("obj/MaleLow.obj", "r")
for line in f.readlines():
    if line[:2] == "v ":
        vertex = list(map(float, line[2:].split()))
        object["vertices"].append(vertex)
        for i in range(3):
            if   vertex[i] > object["max"][i]: object["max"][i] = vertex[i]
            elif vertex[i] < object["min"][i]: object["min"][i] = vertex[i]
    elif line[:2] == "f ":
        # faces.append(list(map(int, line[2:].split())))
        object["faces"].append(list(map(lambda x: int(x.split("/")[0]), line[2:].split())))
f.close()

zoom = 15
object["size"] = [(object["max"][i]-object["min"][i]) for i in range(3)]
object["offset"] = [(-object["min"][i]-object["size"][i]/2) for i in range(3)]

print(object["vertices"])
print(object["faces"])
print(object["min"], object["max"])
print(object["size"])
print(object["offset"])

startTime = 0

def main():
    tick = time.time() - startTime
    canvas.delete("all")

    # canvas.create_rectangle(cSize[0]/2-object["size"][0]/2*zoom, cSize[1]/2-object["size"][1]/2*zoom, cSize[0]/2+object["size"][0]/2*zoom, cSize[1]/2+object["size"][1]/2*zoom, fill="green")

    # canvas.create_line(cSize[0]/2, 0, cSize[0]/2, cSize[1])
    # canvas.create_line(0, cSize[1]/2, cSize[0], cSize[1]/2)

    # rotation = [math.radians(tick*10), math.radians(tick*10), math.radians(tick*10)]
    rotation = [0, -math.radians(tick*10), 0]
    
    s = [(math.sin(rotation[i])) for i in range(3)]
    c = [(math.cos(rotation[i])) for i in range(3)]

    for face in object["faces"]:
        points = []
        for f in face:
            point = [(object["vertices"][f-1][i]+object["offset"][i]) for i in range(3)]
            point[1] *= -1

            object["position"] = [cSize[0]/2, cSize[1]/2]
            
            #https://www.symbolab.com/solver/matrix-multiply-calculator/%5Cbegin%7Bpmatrix%7D1%260%260%260%5C%5C%20%200%26%5Ccos%5Cleft(%5Calpha%5Cright)%26-sin%5Cleft(%5Calpha%5Cright)%260%5C%5C%20%200%26sin%5Cleft(%5Calpha%5Cright)%26cos%5Cleft(%5Calpha%5Cright)%260%5C%5C%20%200%260%260%261%5Cend%7Bpmatrix%7D%5Ccdot%5Cbegin%7Bpmatrix%7Dcos%5Cleft(%5Cbeta%5Cright)%260%26sin%5Cleft(%5Cbeta%5Cright)%260%5C%5C%20%200%261%260%260%5C%5C%20%20-sin%5Cleft(%5Cbeta%5Cright)%260%26cos%5Cleft(%5Cbeta%5Cright)%260%5C%5C%20%200%260%260%260%5Cend%7Bpmatrix%7D%5Ccdot%5Cbegin%7Bpmatrix%7Dcos%5Cleft(%5Cgamma%5Cright)%26-sin%5Cleft(%5Cgamma%5Cright)%260%260%5C%5C%20%20sin%5Cleft(%5Cgamma%5Cright)%26cos%5Cleft(%5Cgamma%5Cright)%260%260%5C%5C%20%200%260%261%260%5C%5C%20%200%260%260%261%5Cend%7Bpmatrix%7D?or=input
            
            # RotationMatrix = [[c[1]*c[2],                -c[1]*s[2],               s[1],       0],
            #                   [s[0]*s[1]*c[2]+c[0]*s[2], c[0]*c[2]-s[0]*s[1]*s[2], -s[0]*c[1], 0],
            #                   [s[0]*s[2]-c[0]*s[1]*c[2], c[0]*s[1]*s[2]+s[0]*c[2], c[0]*c[1],  0],
            #                   [0,                        0,                        0,          0]]
            
            point = [point[0]*(c[1]*c[2])+point[1]*(s[0]*s[1]*c[2]+c[0]*s[2])+point[2]*(s[0]*s[2]-c[0]*s[1]*c[2]), point[0]*(-c[1]*s[2])+point[1]*(c[0]*c[2]-s[0]*s[1]*s[2])+point[2]*(c[0]*s[1]*s[2]+s[0]*c[2])]

            points.append([(point[i]*zoom+object["position"][i]) for i in range(2)])
        
        canvas.create_polygon(points, fill="", outline="black")
    
    root.after(10, main)

main()
startTime = time.time()

root.mainloop()