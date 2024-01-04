import tkinter as tk
import math

width = 800
height = 600

root = tk.Tk()
root.geometry("%dx%d" % (width, height))
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

zoom = 50
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "brown"]


# canvas.create_rectangle((width/2, height/2)*2, width=5)






test = [[-1,  1], [ 0,  1], [ 1,  1], [ 1,  0], [ 1, -1], [ 0, -1], [-1, -1], [-1,  0]]
around = [0, 0]
rotation = 0

for i in range(len(test)):
    for j in range(len(test[i])):
        test[i][j] += around[j]

# canvas.create_rectangle(((width/2)+around[0]*zoom, (height/2)-around[1]*zoom)*2, width=5)

def func(rotation):
    canvas.delete("all")
    canvas.create_line(width/2, 0, width/2, height)
    canvas.create_line(0, height/2, width, height/2)

    for i in range(len(test)):
        # canvas.create_rectangle(((width/2)+test[i][0]*zoom, (height/2)-test[i][1]*zoom)*2, width=5, outline=colors[i])

        point = [0, 0]
        # point[0] = around[0] + (test[i][0] * math.cos(math.radians(rotation)) + test[i][1] * math.sin(math.radians(rotation)))
        # point[1] = around[0] + (-test[i][0] * math.sin(math.radians(rotation)) + test[i][1] * math.cos(math.radians(rotation)))



        relX = (test[i][0] - around[0])
        relY = (test[i][1] - around[1])
        c = math.cos(rotation)
        s = math.sin(rotation)
        point[0] = around[0] + c * relX + s * relY
        point[1] = around[1] + -s * relX + c * relY


        canvas.create_rectangle(((width/2)+point[0]*zoom, (height/2)-point[1]*zoom)*2, width=20, outline=colors[i])
        
    rotation += math.radians(10)
    # if rotation < math.radians(360):
    root.after(100, func, rotation)

root.after(100, func, rotation)

root.mainloop()