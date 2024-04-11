import random

def paros(szam):
    if szam%2==0:
        return True

parosSzamok = []
paratlanSzamok = []
while (szam := random.randint(0, 50)) != 50 or len(parosSzamok) == 0 or len(paratlanSzamok) == 0:
    if paros(szam):
        parosSzamok.append(szam)
    else:
        paratlanSzamok.append(szam)

print("Páros számok:", *parosSzamok)
print("Páratlan számok:", *paratlanSzamok)

parosOsszeg = sum(parosSzamok)
paratlanOsszeg = sum(paratlanSzamok)
if parosOsszeg > paratlanOsszeg:
    print("A páros számok összege nagyobb mint páratlan számok összege")
elif parosOsszeg < paratlanOsszeg:
    print("A páratlan számok összege nagyobb mint páros számok összege")
else:
    print("A páros és páratlan számok összege megegyezik")

if parosOsszeg/len(parosSzamok) > paratlanOsszeg/len(paratlanSzamok):
    print("A páros számok átlaga nagyobb mint páratlan számok összege")
elif parosOsszeg/len(parosSzamok) < paratlanOsszeg/len(paratlanSzamok):
    print("A páratlan számok átlaga nagyobb mint páros számok összege")
else:
    print("A páros és páratlan számok átlaga megegyezik")


print("%s a számok között 25-ös" % ("Van" if 25 in paratlanSzamok else "Nincs"))