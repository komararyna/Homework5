import random
a = []
for i in range(4):
    a.append(random.randint(1, 20))
print(a)
a = list(map(int, a))
for item in a:
    b = item * 2
    a = list(a)
    a.append(b)
print(a)
