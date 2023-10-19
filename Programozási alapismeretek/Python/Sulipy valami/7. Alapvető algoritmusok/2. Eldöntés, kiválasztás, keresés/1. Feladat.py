import random

li = []

for i in range(5):
    li.append(random.randint(1,7))

try:
    szam = int(input("Szám: "))
except:
    print("Csak szám lehet")
    exit()

if szam in li:
    print("Benne van")
else:
    print("Nincs benne")

print(li)