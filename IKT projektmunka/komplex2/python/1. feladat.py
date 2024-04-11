szamlalo = int(input("Kérem a számlálót: "))
while True:
    nevezo = int(input("Kérem a nevezőt: "))
    if nevezo != 0:
        break

if szamlalo/nevezo == szamlalo//nevezo:
    print("Egész, %d/%d=%d" % (szamlalo, nevezo, szamlalo/nevezo))
else:
    print("Nem egész")