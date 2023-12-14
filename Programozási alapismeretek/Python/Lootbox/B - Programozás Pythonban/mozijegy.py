ar = int(input("Jegy ára: "))
db = int(input("Darabszám: "))

fizetendo = ar * db + 500
print(f"Fizetendő összeg: {fizetendo} Ft")

if fizetendo < 10000:
    kedvezmenyes = fizetendo * 0.9
else:
    kedvezmenyes = fizetendo * 0.85

kedvezmenyes = round(kedvezmenyes)
print(f"Kedvezményes ár: {kedvezmenyes} Ft")