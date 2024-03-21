import math

TIME = 10 # s
SPEED = 15 # m/s

maxPath = TIME*SPEED

# maxPath = 130

maxE = 0

points = []
relevant = []
f = open("gyongyok.txt", "r", encoding="utf-8")
keys = f.readline().strip("; \n").split(";")
while line := f.readline():
	temp = {x[0]:int(x[1]) for x in zip(keys, line.strip("; \n").split(";"))}
	temp["distance"] =  math.sqrt(temp["x"]**2+temp["y"]**2+temp["z"]**2)
	points.append(temp)
	if temp["distance"] < maxPath/2:
		relevant.append(temp)
		if maxE < temp["e"]:
			maxE = temp["e"]

# https://mathisonian.github.io/kde/
# https://www.youtube.com/watch?v=x5zLaWT5KPs

# https://en.wikipedia.org/wiki/Kernel_density_estimation
# https://en.wikipedia.org/wiki/Kernel_(statistics)

r = 10
for p in relevant:
	# Sűrűség kiszámítása

	density = 0
	for p2 in relevant:
		density += max((1-(math.sqrt((p["x"]-p2["x"])**2+(p["y"]-p2["y"])**2+(p["z"]-p2["z"])**2)/((0.5*maxPath)/r))**2), 0)
		#          |--- p és p2 relatív távolsága (0 és 1 közé eső érték) (ezeket átlagolva lesz sűrűség) ---|   |----- a gyöngy értéke -----|
		#          |-- Ha p és p2 ugyanott vannak akkor 1, ha (0.5*maxPath)/r távolságra vannak akkor 0 az érték --|   |- (0 és 1 közé eső érték) -|
	density /= len(relevant)

	p["density"] = density

	# Ha minden pont ugyanott lenne mint a viszonyítási pont akkor 1 lenne a sűrűség; Ha minden pont (a viszonyítási pontot is beleértve) a viszonyítási ponttól maxPath/2 távolságra lenne akkor lenne 0 a sűrűség

	p["weight"] = density * (p["e"]/maxE) * (1-p["distance"]/(maxPath/2))
	#                       |- a gyöngy értéke és az origótól való távolsága 0 és 1 közé eső értékként -|

	print(p["weight"])


import tkinter as tk

size = 10
dotSize = 3
margin = 5*size
winSize = [max([x["x"] for x in points])*size+margin*2, max([x["y"] for x in points])*size+margin*2]

root = tk.Tk()
root.maxsize(width=winSize[0], height=winSize[1])
root.resizable(False, False)
root.update()

canvas = tk.Canvas(root, width=winSize[0], height=winSize[1], bg="#fff")
canvas.pack(anchor="nw")

canvas.create_rectangle(margin, margin, winSize[0], winSize[1], outline="", fill="#D6FFFF")
canvas.create_line(margin, margin, margin, winSize[1]-margin, arrow="last")
canvas.create_line(margin, winSize[1]-margin+3, margin, winSize[1], dash=3)
canvas.create_line(margin, margin, winSize[0]-margin, margin, arrow="last")
canvas.create_line(winSize[0]-margin+3, margin, winSize[0], margin, dash=3)

import colorsys
def hue_to_hex(h):
	temp = 210
	h = (h*temp+(255-temp))/255
	return "#{:02x}{:02x}{:02x}".format(*map(lambda x: round(x*255), colorsys.hsv_to_rgb(h, 1, 1)))

lineWidth = 3
for i in range(255):
	canvas.create_line(margin+i*lineWidth, margin/3, margin+i*lineWidth, margin*2/3, width=lineWidth, fill=hue_to_hex(i/255))

canvas.create_arc(margin-maxPath/2*size, margin-maxPath/2*size, margin+maxPath/2*size, margin+maxPath/2*size, start=-90, extent=90, style="arc")

maxWeight = max([i["weight"] for i in relevant])
minWeight = min([i["weight"] for i in relevant])
maxDensity = max([i["density"] for i in relevant])
for p in points:
	if p in relevant:
		modWeight = (p["weight"]-minWeight)/(maxWeight-minWeight)
		if modWeight == 0 or modWeight == 1:
			canvas.create_oval(p["x"]*size-dotSize*2.2+margin, p["y"]*size-dotSize*2.2+margin, p["x"]*size+dotSize*2.2+margin, p["y"]*size+dotSize*2.2+margin, outline="black")
		if p["density"] == maxDensity:
			canvas.create_oval(p["x"]*size-dotSize*5+margin, p["y"]*size-dotSize*5+margin, p["x"]*size+dotSize*5+margin, p["y"]*size+dotSize*5+margin, outline="red")
			canvas.create_oval(p["x"]*size-((0.5*maxPath)/r)*size+margin, p["y"]*size-((0.5*maxPath)/r)*size+margin, p["x"]*size+((0.5*maxPath)/r)*size+margin, p["y"]*size+((0.5*maxPath)/r)*size+margin, outline="red")
	else:
		modWeight = -1
	canvas.create_oval(p["x"]*size-dotSize+margin, p["y"]*size-dotSize+margin, p["x"]*size+dotSize+margin, p["y"]*size+dotSize+margin, fill=hue_to_hex(modWeight) if modWeight != -1 else "grey")
	canvas.create_text(p["x"]*size+margin, p["y"]*size+margin+dotSize+10, text=p["e"], anchor="center")

root.mainloop()