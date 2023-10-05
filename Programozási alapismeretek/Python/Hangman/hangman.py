import random
import io

wordFile = io.open("magyar-szavak.txt", mode="r", encoding="utf-8")
words = []
i=0
while (True):
    try:
        temp = wordFile.readline()
        if temp != "":
            words.append(temp)
        else:
            break
    except:
        break

    # print(words[i])
    # i+=1
# print(i)
wordFile.close()

word = "Alma"
word = words[random.randint(0, len(words)-1)].strip()
# print(word)
wordL = word.lower()
state = "_"*len(word)

MAX_FAILS = 10
currentFails = 0
notIn = []

print(state)

while word != state:
    
    c = input("Tipp: ").lower()
    if len(c) > 1:
        print("A tipp csak egy betűből állhat")
        continue
    
    if c in wordL:
        for i in range(len(wordL)):
            if wordL[i] == c:
                stateList = list(state)
                stateList[i] = word[i]
                state = "".join(stateList)
    elif c in notIn:
        print("Ezt már próbáltad, nincs benne") #valamiért betűkkel nem működik
    else:
        currentFails+=1
        notIn.append(c)
        print("Hibák száma:", currentFails)

    print(state)

    if word == state:
        print("Gratulálok, nertél ^^")
    elif currentFails >= MAX_FAILS:
        print("Vesztettél :<")
        print(f'A szó "{word}" volt')
        break