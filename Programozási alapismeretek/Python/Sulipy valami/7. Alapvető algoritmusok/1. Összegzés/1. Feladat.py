import random

li = []
osszeg = 0

for i in range(5):
    li.append(random.randint(1,10))
    if li[i] % 2 == 0:
        osszeg += li[i]

print(li)
print(osszeg)