import math

class Object:
    vertices = []
    faces = []
    min = [math.inf, math.inf, math.inf]
    max = [-math.inf, -math.inf, -math.inf]
    size = [0, 0, 0]
    offset = [0, 0]
    position = [0, 0]
    rotation = {
        "axis": [0, 0],
        "matrix": [[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]]
    }

    def __init__(self, file):
        f = open(file, "r")
        for line in f.readlines():
            if line[:2] == "v ":
                vertex = list(map(float, line[2:].split()))
                self.vertices.append(vertex)
                for i in range(3):
                    if   vertex[i] > self.max[i]: self.max[i] = vertex[i]
                    elif vertex[i] < self.min[i]: self.min[i] = vertex[i]
            elif line[:2] == "f ":
                # faces.append(list(map(int, line[2:].split())))
                self.faces.append(list(map(lambda x: int(x.split("/")[0]), line[2:].split())))
        f.close()

        self.size = [(self.max[i]-self.min[i]) for i in range(3)]
        self.offset = [(-self.min[i]-self.size[i]/2) for i in range(3)]