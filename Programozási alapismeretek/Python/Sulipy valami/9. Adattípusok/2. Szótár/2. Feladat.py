cat = {}

cat["name"] = input("Név: ")
while True:
    try:
        cat["age"] = int(input("Élerkor: "))
        break
    except:
        continue

print(cat)

while True:
    inp = input(f"Megváltoztatandó adat: ")
    if inp in cat.keys():
        break

while True:
    try:
        cat[inp]=type(cat[inp])(input("%s: " % (inp)))
        break
    except:
        continue

print(cat)