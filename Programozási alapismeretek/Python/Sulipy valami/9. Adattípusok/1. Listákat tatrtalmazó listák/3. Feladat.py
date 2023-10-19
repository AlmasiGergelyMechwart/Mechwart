import random

li = []

for i in range(5):
    tempList = []
    for j in range(3):
        tempList.append(random.randint(-5, 5))
    li.append(tempList)

print(f"Véletlenszámok:\n{li}")

for i in range(len(li)):
    while True:
        for j in range(len(li[i])):
            if li[i][j] < 0:
                li[i].pop(j)
                break
        else:
            break

print(f"Nemnegatív véletlenszámok:\n{li}")