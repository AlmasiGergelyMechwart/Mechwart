f = open("szavazatok.txt", "r", encoding="utf-8")
lines = map(lambda x: x.strip(), f.readlines())
f.close()

szavazasraJogosultak = 12345
keys = ["kerület", "szavazatok", "név", "párt"]
jeloltek = []
for line in lines:
    parts = line.split()
    parts[2] = " ".join(parts[2:4])
    parts.pop(3)
    jeloltek.append({x:y for x,y in zip(keys, parts)})

def sep():
    print()
    print("x".join(["-"*15]*2))
    print()
sep()


print("2. feladat")
print("A helyhatósági választáson %s képviselőjelölt indult." % len(jeloltek))
sep()


print("3. feladat")
inp = input("Képviselőjelölt neve: ")
for jelolt in jeloltek:
    if jelolt["név"].lower() == inp.lower():
        print("%s %s szavazatot kapott." % (jelolt["név"], jelolt["szavazatok"]))
        break
else:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
sep()


print("4. feladat")
print("A választáson {} állampolgár, a jogosultak {}%-a vett részt.".format(szavazasraJogosultak, round((sum(map(lambda x: int(x["szavazatok"]), jeloltek))/szavazasraJogosultak)*100, 2)))
sep()


print("5. feladat")
names = {"GYEP": "Gyümölcsevők Pártja", "HEP": "Húsevők Pártja", "TISZ": "Tejivók Szövetsége", "ZEP": "Zöldségevők Pártja", "-": "Független jelöltek"}
osszesSzavazat = sum(map(lambda x: int(x["szavazatok"]), jeloltek))
for key, value in names.items():
    print("{}: {}%".format(value, round(sum(map(lambda x: int(x["szavazatok"]), [i for i in jeloltek if i["párt"] == key]))/osszesSzavazat*100, 2)))
sep()


print("6. feladat")
for jelolt in [i for i in jeloltek if int(i["szavazatok"]) == max(map(lambda x: int(x["szavazatok"]), jeloltek))]:
    print("%s %s" % (jelolt["név"], jelolt["párt"] if jelolt["párt"] != "-" else "független"))

sep()

f = open("kepviselok.txt", "w", encoding="utf-8")
for kerulet in sorted(list(set(map(lambda x: int(x["kerület"]), jeloltek)))):
    kepviselo = max([i for i in jeloltek if int(i["kerület"]) == kerulet], key=lambda x: int(x["szavazatok"]))
    f.write("%d. kerület: %s %s\n" % (kerulet, kepviselo["név"], kepviselo["párt"] if kepviselo["párt"] != "-" else "független"))