import time

from gui import GUI


gui = GUI()

print(f"Verticies:\n%s" % gui.object.vertices)
print(f"Faces:\n%s" % gui.object.faces)
print(f"Min/Max of each coordinate:\n%s" % gui.object.min, gui.object.max)
print(f"Size:\n%s" % gui.object.size)
print(f"Offset:\n%s" % gui.object.offset)

startTime = 0

tick = time.time() - startTime

startTime = time.time()

gui.mainloop()