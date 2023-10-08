import random
import io

wordsFile = io.open("magyar-szavak.txt", mode="r", encoding="utf-8")
words = []

while (True):
    try:
        temp = wordsFile.readline()
        if temp != "":
            words.append(temp.strip())
        else:
            break
    except:
        break

wordsFile.close()

word = words[random.randint(0, len(words)-1)]
print(word)
wordL = word.lower()
state = "_"*len(word)

MAX_FAILS = 10
currentFails = 0
charsNotInWord = []


while word != state:
    
    print(state)
    
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
    elif c in charsNotInWord:
        print("Ezt már próbáltad, nincs benne")
    else:
        currentFails+=1
        charsNotInWord.append(c)
        print("Hibák száma:", currentFails)

    if currentFails >= MAX_FAILS:
        print("Vesztettél")
        print(f'A szó "{word}" volt')
        break
else:
    print("Gratulálok, nertél")
