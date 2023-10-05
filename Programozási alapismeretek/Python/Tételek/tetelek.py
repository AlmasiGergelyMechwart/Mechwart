# Programozási tételek

#Összegzés
t = [1, 4, 7, 9, 6]
osszeg = 0
for szam in t:
    osszeg = osszeg + szam
print("Összeg:", osszeg)

#Megszámlálás
t = [1, 4, 7, 9, 6]
darab = 0
for szam in t:
    if szam > 3:
        darab += 1
print("Darabszám:", darab)

#Eldöntés
t = [1, 5, 7, 12, 9]
a = 5
for szam in t:
    if szam == a:
        print(f'"{a}" benne van a listában')
        break

#Keresés
t = [1, 5, 7, 12, 9, 7, 21]
a = 7
res = []
for i in range(len(t)):
    if t[i] == a:
        res.append(i)
if len(res) == 0:
    print("Nincs benne")
else:
    print(f'"{a}" benne van a listában a(z) {res} index{"ek" if len(res) > 1 else ""}en')

#Minimum kiválasztás
t = [11, 4, -3, 14, 8, 3]
min = t[0]
for szam in t:
    if szam < min:
        min = szam
print("Minimum:", min)

#Maximum kiválasztás
t = [11, 4, -3, 14, 8, 3]
max = t[0]
for szam in t:
    if szam > max:
        max = szam
print("Maximum:", max)

#Szétválogatás
t = [-1, 4, -7, 9, 8]
pos = []
neg = []
for szam in t:
    if szam < 0:
        neg.append(szam)
    else:
        pos.append(szam)
print("Pozitív:", pos)
print("Negatív:", neg)