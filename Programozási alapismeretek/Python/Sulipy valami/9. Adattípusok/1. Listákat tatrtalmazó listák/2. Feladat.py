tarolo = []

for i in range(3):
    tempList = []
    for j in range(3):
        tempList.append('O ')
    tarolo.append(tempList)

def printTarolo():
    for i in tarolo:
        for j in i:
            print(j, end="")
        print()

printTarolo()

while True:

    try:
        row = int(input("Sor: "))-1
        col = int(input("Oszlop: "))-1
    except:
        continue

    try:
        tarolo[row][col] = '+ '
    except:
        break

    printTarolo()