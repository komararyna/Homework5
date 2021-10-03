width = int(input('insert width:'))
a = width
print('*' * width)
while a > 1:
    print(' ' * (width - (a - 2)),'*' * (a - 2))
    a = a - 2
while a < (width-2):
    print('' * (a + (a + 2)),'*' * (a + 2))
    a = a + 2
print('*' * width)
