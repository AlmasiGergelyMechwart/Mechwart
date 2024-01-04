import tkinter as tk
from tkinter import ttk
import math

width = 800
height = 600

root = tk.Tk()
root.geometry("%dx%d" % (width, height))
canvas = tk.Canvas(root, width=width, height=height)
# canvas.pack()

scaleVar = tk.DoubleVar()
scale = ttk.Scale(root, from_=-math.pi, to=math.pi, variable=scaleVar)
label = ttk.Label(root, text="Value: %s" % (1))

def sliderChanged(event):
    label.configure(text="Value: %s" % (scaleVar.get()))

scale.configure(command=sliderChanged)


scale.pack()
label.pack()


root.mainloop()
