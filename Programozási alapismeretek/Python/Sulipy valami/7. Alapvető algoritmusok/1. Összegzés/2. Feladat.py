li = []
osszeg = 0

while True:
    try:
        szam = int(input("Szám: "))
    except:
        print("Csak szám lehet")
        continue

    if szam not in range(-5, 5 +1):
        break

    li.append(szam)
    osszeg += szam

print(li)
print(osszeg)