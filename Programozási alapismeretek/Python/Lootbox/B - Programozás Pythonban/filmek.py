f = open("movies.txt", "r", encoding="utf-8")
lines = list(map(lambda x: x.strip(), f.readlines()))
f.close()

print("Filmek száma:", len(lines))

print("Love szó szerepel a film nevében:")
for i in range(len(lines)):
    title = lines[i].split(";")[0]
    if "love" in title.lower():
        print(title)

while True:
    try:
        also = int(input("Alsó határ: "))
        felso = int(input("Felső határ: "))
        if also <= felso:
            break
        else:
            raise
    except:
        print("Hibás bevitel")

szamlalo = 0
f = open("100felett.txt", "w", encoding="utf-8")
for line in lines:
    parts = line.split(";")
    if int(parts[1]) < also or int(parts[1]) > felso:
        continue
    if float(parts[2]) > 100:
        szamlalo += 1
        f.write(parts[0]+"\n")
if szamlalo == 0:
    f.write("Nem található 100 millió dollár feletti bevételű film.")
f.close()
print("100 millió dollár feletti bevétel:", szamlalo)

dollar = 0.9

def dollarToEuro(arfolyam,ertek):
    return round(arfolyam*ertek,2)

bevetelosszeg = 0
bevetelszamlalo = 0
for line in lines:
    parts = line.split(";")
    if int(parts[3]) >= 70:
        bevetelosszeg += dollarToEuro(dollar, float(parts[2]))
        bevetelszamlalo += 1
print(f"Legalább 70%-ra értékelt filmek átlagos bevétele: {round(bevetelosszeg/bevetelszamlalo, 1)} millió Euró")