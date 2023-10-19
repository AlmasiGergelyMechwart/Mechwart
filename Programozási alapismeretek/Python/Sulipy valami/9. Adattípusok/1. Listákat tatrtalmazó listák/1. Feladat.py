import random

tarolo = []

for i in range(4):
    tempList = []
    for j in range(3):
        tempList.append(random.randint(0, 25))
    tarolo.append(tempList)

print(tarolo)