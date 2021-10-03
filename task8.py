a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
sum = 0
for item in a:
    x = item
    print(x)
    for item in x:
        sum = sum + item
print(sum)