dog = {}

dog["name"] = input("Név: ")
while True:
    try:
        dog["age"] = int(input("Élerkor: "))
        break
    except:
        continue
dog["breed"] = input("Fajta: ")
while True:
    inp = input("Van-e veszettség elleni oltása (I/H): ")
    if inp.lower() == "i":
        dog["isVaccinated"] = True
        break
    elif inp.lower() == "h":
        dog["isVaccinated"] = False
        break

print(dog)