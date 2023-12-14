import random

n = int(input("Mennyi húzás legyen: "))

targyak = []
osszeg = 0
print("A húzott számok:")
for i in range(n):
    targyak.append(random.randint(1, 40))
    print(targyak[i])
    osszeg += targyak[i]

print("legendary tárgyak: ", end="")
for i in range(n):
    if targyak[i]%5 == 0:
        print("%d:%d " % (i, targyak[i]), end="")
print()

print("Rare tárgyak: ", end="")
for i in range(n):
    if targyak[i]%5 != 0 and targyak[i]%2 == 1:
        print("%d:%d " % (i, targyak[i]), end="")
print()


# A tárgyak id-inek összege alaplán kap jutalmat?
# Hát ok
print("A húzások összege:", osszeg)
print("A húzások átlaga:", round(osszeg/n))