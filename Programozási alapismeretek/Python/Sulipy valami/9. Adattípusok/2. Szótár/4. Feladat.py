import random
from pprint import pprint

vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "Hanna" ]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér" ]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]
  

diakok = []

for i in range(8):
    diak = {
        "nev": f"{random.choice(vezeteknevek)} {random.choice(keresztnevek)}",
        "eletkor": random.randint(14, 19),
        "evfolyam": random.randint(9, 12),
        "osztaly": random.choice(("A", "B", "C", "D")),
        "cim": {
            "telepules": random.choice(telepulesek),
            "utca": random.choice(utcak),
            "hazszam": random.randint(1, 50)
        }
    }
    diakok.append(diak)

pprint(diakok, sort_dicts=False)