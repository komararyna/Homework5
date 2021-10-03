x = [0, 5, 2, 4, 7, 1, 3, 19 ]
x = list(map(int, x))
count = 0
for item in range(8):
    if not item % 2:
        print(item)
    else:
        count += 1
print('quantity:', count)
