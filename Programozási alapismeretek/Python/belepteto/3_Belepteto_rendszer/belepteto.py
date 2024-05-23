from functools import total_ordering

@total_ordering
class Idopont:
    def __init__(self, idoStr):
        parts = idoStr.split(":")
        self.h = int(parts[0])
        self.m = int(parts[1])
    
    def __str__(self):
        return "%.2d:%.2d" % (self.h, self.m)
    
    def toMinutes(self):
        return self.h*60+self.m
    
    def __eq__(self, other):
        return self.toMinutes() == other.toMinutes()
    
    def __lt__(self, other):
        return self.toMinutes() < other.toMinutes()

class Esemeny:
    def __init__(self, tanulokod, idopont, esemenykod):
        self.tanulokod = str(tanulokod)
        self.idopont = Idopont(idopont)
        self.esemenykod = int(esemenykod)

class EsemenyList(list):
    def get(self, func, value):
        toReturn = EsemenyList()
        for item in self:
            if func(item) == value:
                toReturn.append(item)
        return toReturn
    
    def between(self, func, minvalue, maxvalue, inclusive=[True, True]):
        toReturn = EsemenyList()
        for item in self:
            toCompare = func(item)
            if (toCompare > minvalue and toCompare < maxvalue) or (inclusive[0] and toCompare == minvalue) or (inclusive[1] and toCompare == maxvalue):
                toReturn.append(item)
        return toReturn

def feladat(feladatszam):
    print("%d. feladat" % feladatszam)

esemenyek = EsemenyList()
with open("bedat.txt", "r", encoding="utf-8") as f:
    while line := f.readline().strip():
        esemenyek.append(Esemeny(*line.split(" ")))


feladat(2)
belepesek = esemenyek.get(lambda x: x.esemenykod, 1)
kilepesek = esemenyek.get(lambda x: x.esemenykod, 2)
print("Az első tanuló %s-kor lépett be a főkapun." % belepesek[0].idopont)
print("Az utolsó tanuló %s-kor lépett ki a főkapun." % kilepesek[-1].idopont)


kesok = belepesek.between(lambda x:x.idopont, Idopont("7:50"), Idopont("8:15"), [False, True])
with open("kesok.txt", "w", encoding="utf-8") as f:
    for keso in kesok:
        f.write("%s %s\n" % (keso.idopont, keso.tanulokod))


feladat(4)
ebedelesek = esemenyek.get(lambda x: x.esemenykod, 3)
print("A menzán aznap %d tanuló ebédelt." % len(ebedelesek))


feladat(5)
kolcsonzesek = esemenyek.get(lambda x: x.esemenykod, 4)
kolcsonzoTanulok = set()
for kolcsonzes in kolcsonzesek:
    kolcsonzoTanulok.add(kolcsonzes.tanulokod)
print("Aznap %d tanuló kölcsönzött a könytárban." % len(kolcsonzoTanulok))
if len(kolcsonzoTanulok) > len(ebedelesek):
    print("Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")


feladat(6)
