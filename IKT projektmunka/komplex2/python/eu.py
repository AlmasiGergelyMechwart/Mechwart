class Orszag:
    def __init__(self, nev, csatl):
        self.nev = nev
        self.csatlDatum = Datum(*csatl)

class Datum:
    def __init__(self, ev, honap, nap):
        self.ev = ev
        self.honap = honap
        self.nap = nap
    
    def getDateStr(self):
        return ".".join((str(self.ev), str(self.honap).rjust(2, "0"), str(self.nap).rjust(2, "0")))

    def getDateInSec(self):
        return ((self.ev-1970)*365+self.honap*31-(2 if self.honap>=2 else 0)-self.honap//2+(-1 if self.honap > 7 else 1)+((self.ev-1790)//4))*24*60*60

tagallamok = []
with open("eucsatlakozas.txt", "r", encoding="utf-8") as f:
    while line := f.readline().strip():
        parts = line.split(";")
        tagallamok.append(Orszag(parts[0], map(int, parts[1].split("."))))



print("3. feladat: EU tagállamainak száma: %d db" % len(tagallamok))

cnt = 0
for t in tagallamok:
    if t.csatlDatum.ev == 2007:
        cnt+=1
print("4. feladat: 2007-ben %d ország csatlakozott." % cnt)

for t in tagallamok:
    if t.nev == "Magyarország":
        magyarDatum = t.csatlDatum.getDateStr()
        break
print("5. feladat: Magyarország csatlakozásának dátuma: %s" % magyarDatum)

print("6. feladat: Májusban ", end="")
for t in tagallamok:
    if t.csatlDatum.honap == 5:
        break
else:
    print("nem ", end="")
print("volt csatlakozás!")

print("7. feladat: Legutoljára csatlakozott ország: %s" % (max(tagallamok, key=lambda x: x.csatlDatum.getDateInSec())).nev)