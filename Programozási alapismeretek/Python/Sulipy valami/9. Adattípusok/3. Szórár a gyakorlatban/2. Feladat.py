'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

print(autok)


print(f"{"-"*13} 1. feladat {"-"*13}")
max = autok[0]['kor']
maxIdx = 0
for i in range(len(autok)):
    if autok[i]['kor'] > max:
        max = autok[i]['kor']
        maxIdx = i
print("A legöregebb autó: %s, %s %s, %d éves." % (autok[maxIdx]['rendszam'], autok[maxIdx]['marka'], autok[maxIdx]['tipus'], autok[maxIdx]['kor']))

print(f"\n{"-"*13} 2. feladat {"-"*13}")
print("A már megjavított autók rendszáma:")
for i in range(len(autok)):
    if autok[i]['javitva']:
        print(autok[i]['rendszam'])

print(f"\n{"-"*13} 3. feladat {"-"*13}")
ossz = 0
for i in range(len(autok)):
    ossz += autok[i]['koltseg']
atlag = ossz/len(autok)
print("Az egy autóra jutó átlagos javítási költség: %d Ft." % (atlag))

print(f"\n{"-"*13} 4. feladat {"-"*13}")
inp = input("Adjon meg egy rendszámot (pl. ABC-123)! ").upper()
for i in range(len(autok)):
    if inp == autok[i]['rendszam']:
        print("A megadott rendszámú autó a műhelyben van.")
        break
else:
    print("A megadott rendszámú autó nincs a műhelyben.")

print(f"\n{"-"*13} 5. feladat {"-"*13}")
inp = input("Adjon meg egy betűt! ").lower()
print("A megadott betű az alábbi autók márka- vagy típusmegnevezésében fordul elő:")
for i in range(len(autok)):
    if inp in autok[i]['marka'].lower() or inp in autok[i]['tipus'].lower():
        print(autok[i]['marka'], autok[i]['tipus'])