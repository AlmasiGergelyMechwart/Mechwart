person = {
    "name": "Sanyi",
    "age": 21,
    "hasDriversLicence": True
}

print(person)

while True:
    key = input("Új kulcs: ")
    person[key] = input("Új érték: ")

    print(person)