import random
a = []
for i in range(12):
    a.append(random.randint(7500, 12000))
a = list(map(int, a))
sum = 0
for item in a:
    sum = sum + item
salary = sum / len(a)
print(a, round(salary))

