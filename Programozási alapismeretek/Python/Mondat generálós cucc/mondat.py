import random

part1 = ["Pókember", "Tihamér", "Tanár Úr", "Fekete Balázs"]
part2 = ["kabán", "mordorban", "a szobámban"]
part3 = ["math-et főz", "aranyat talál", "békává változott"]

rnd1 = random.randint(0, len(part1)-1)
rnd2 = random.randint(0, len(part2)-1)
rnd3 = random.randint(0, len(part3)-1)

print(part1[rnd1], part2[rnd2], part3[rnd3]+".")