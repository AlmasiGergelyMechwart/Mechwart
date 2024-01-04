import tkinter as tk
import math

width = 800
height = 600

root = tk.Tk()
root.geometry("%dx%d" % (width, height))
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

zoom = 20
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "brown"]

canvas.create_line(width/2, 0, width/2, height)
canvas.create_line(0, height/2, width, height/2)
# canvas.create_rectangle((width/2, height/2)*2, width=5)






test = [[-2, 0], [-1, 1], [0, 2], [1, 1],
        [2, 0], [1, -1], [0, -2], [-1, -1]]
around = [-4, -5]
rotation = -30

canvas.create_rectangle(((width/2)+around[0]*zoom, (height/2)-around[1]*zoom)*2, width=5)

for i in range(len(test)):
    for j in range(len(test[i])):
        test[i][j] += around[j]

for i in reversed(range(len(test))):
    print("A%d: %s" % (i+1, test[i]))
    canvas.create_rectangle(((width/2)+test[i][0]*zoom, (height/2)-test[i][1]*zoom)*2, width=5, outline=colors[i])
    
    r = math.sqrt((test[i][0] - around[0])**2 + (test[i][1] - around[1])**2)
    print("r: %s" % (r))
    
    # b = [r*math.cos(math.radians(rotation)), r*math.sin(math.radians(rotation))]
    # b = list(map(lambda x: round(x, 15), b))
    # print("B offset néklül: %s" % (b))

    # b = [around[0]-r*math.cos(math.radians(rotation)), around[1]-r*math.sin(math.radians(rotation))]
    # b = list(map(lambda x: round(x, 15), b))
    # print("B: %s" % (b))
    # canvas.create_rectangle(((width/2)+b[0]*zoom, (height/2)-b[1]*zoom)*2, width=5, outline=colors[i])

    # b = [r*math.cos(math.radians(rotation))]

    '''
    x, y = point
    ox, oy = origin

    qx = ox + math.cos(radians) * (x - ox) + math.sin(radians) * (y - oy)
    qy = oy + -math.sin(radians) * (x - ox) + math.cos(radians) * (y - oy)
    '''

    b = [0, 0]
    b[0] = around[0] + math.cos(math.radians(rotation)) * (test[i][0] - around[0]) + math.sin(math.radians(rotation)) * (test[i][1] - around[1])
    b[1] = -around[0] + math.sin(math.radians(rotation)) * (test[i][0] - around[0]) + math.cos(math.radians(rotation)) * (test[i][1] - around[1])
    print(b)

    b[0] = around[0] + math.cos(math.radians(rotation)) * (test[i][0] - around[0]) + math.sin(math.radians(rotation)) * (test[i][1] - around[1])
    b[1] = -around[0] + math.sin(math.radians(rotation)) * (test[i][0] - around[0]) + math.cos(math.radians(rotation)) * (test[i][1] - around[1])
    print(b)
    # print(math.cos(math.radians(rotation)))

    print()
#[-2, 0]  [-4, -5]
# temp = math.cos(math.radians(rotation))
# print(temp)
# temp *= (-6 - -4)
# print(temp)
# temp += -4
# print(temp)



# root.mainloop()