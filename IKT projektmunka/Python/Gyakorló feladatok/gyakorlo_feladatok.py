# #1. Feladat
# a = int(input("Négyzet egységnyi odala: "))
# print(f"Kerület: {a*4} egység")
# print(f"Terület: {a**2} egység^2")
# print()

# #2. Feladat
# ar = int(input("1 kg alma ára: "))
# mennyiseg = int(input("Vásárolandó mennyiség (kg): "))
# print(f"{ar*mennyiseg} koronába fog kerülni")
# print()

# #3. Feladat
# szamok = []
# for i in range(3):
#     szamok.append(int(input(f"{i+1}. szám: ")))
# print(f"{szamok[0]*5 + szamok[1]*2 + szamok[2]} koronánk van")
# print()

# #4. Feladat
# tank = float(input("Tankolt mennyiség (l): "))
# tavolsag = int(input("Megtett távolság: (km): "))
# print(f"{round(tank*100/tavolsag, 3)} litert fogyaszt 100 kilóméteren")
# print()

# #5. Feladat
# import random
# print("5-ös lottó számok: ", end="")
# for i in range(5):
#     if i > 0:
#         print(", ", end="")
#     print(random.randint(1, 90), end="")
# print()

# #6. Feladat
# szam = int(input("Egy háromjegyű egész szám: "))
# temp = szam
# osszeg = 0
# for i in range(3):
#     osszeg += (temp%10)**3
#     temp = int(temp/10)
# if szam == osszeg:
#     print(f"A {szam} egy Amsztong szám")
# else:
#     print(f"A {szam} nem Amsztong szám")
# print()

# #7. Feladat
# hossz = int(input("Az út hossza (km): "))
# i = 5
# while True:
#     if hossz <= i:
#         print(f"{i*100} Ft.- fizrtést kap a futár")
#         break
#     else:
#         i+=5
# print()

# #8. Feladat
# szamok = []
# for i in range(3):
#     szamok.append(int(input(f"{i+1}. szám: ")))
# if len(szamok) == len(set(szamok)):
#     print("A három érték különböző")
# else:
#     print("A három érték között van azonos")
# print()

# #9. Feladat
# pontszam = int(input("Dolgozat pontszáma: "))
# if pontszam <= 17:
#     jegy = 1
# elif pontszam <= 34:
#     jegy = 2
# elif pontszam <= 51:
#     jegy = 3
# elif pontszam <= 68:
#     jegy = 4
# elif pontszam <= 85:
#     jegy = 5
# print(f"A dolgozat érdemjegye: {jegy}")
# print()

# #10. Feladat
# start = int(input("Első érték: "))
# end = int(input("Második érték: "))
# i = start
# osszeg = 0
# while i <= end:
#     if i%2 == 0:
#         osszeg += i
#     i+=1
# print(f"A két érték közötti páros számok összege: {osszeg}")
# print()

# #11. Feladat
# szam = int(input("Szám: "))
# osszeg = 1
# for i in range(szam):
#     osszeg*=i+1
# print(osszeg)
# print()

#12. Feladat
