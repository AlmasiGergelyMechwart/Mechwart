import random

colors = ["Piros", "Fehér", "Kék", "Rózsaszín", "Narancssárga", "Lila", "Citromsárga", "Zöld"]
# colorsFirstLetter = list(map(lambda x: x[0].upper(), colors))

def greet():
    print("-"*20)
    print("|"+" "*5+"Színözön"+" "*5+"|")
    print("-"*20)
    print("Tippelj 4-et az alábbi színek köszül!")
    print(", ".join(colors))

def guess():
    isValid = False
    while not isValid:
        print()
        for line in history:
            print("".join(line))
        guesses = input("%d. Tipp: " % (len(history)+1)).lower()
        guesses = list(map(lambda x: x[0].upper()+x[1:], guesses.split()))
        if len(guesses) == 4:
            isValid = True
            for guess in guesses:
                if guess not in map(lambda x: x[:len(guess)], colors):
                    isValid = False
                    break
        if not isValid:
            print("Hibás bemenet :/")
    guesses = list(map(lambda x:x[0], guesses))
    history.append(guesses)


solution = [colors[random.randint(0, len(colors)-1)][0] for i in range(4)]
# print(solution)
history = []

greet()
while history[:4] != "".join(solution):
    guess()
    black = 0
    white = 0
    for i,color in enumerate(history[-1]):
        if color in solution:
            if history[-1][i] == solution[i]: # Ez most nem jó ha pl KKKK-t tippelsz mert ha csak egy kék van is ad 3 fehéret és 1 feketét
                black+=1
            else:
                white+=1
    history[-1] += " - "
    history[-1] += ("⚫"*black+"⚪"*white) if black+white > 0 else "Semmi :/"

print()
print("Nyertél! :)")
print("GG")