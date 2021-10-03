n = int(input('insert your number:'))
if 4 < n < 16:
    b = 1
    for i in range(n):
        a = (i+1)
        b = b * a
    print(b)
else:
    print('error')
