a = int(input('insert width:'))
b = int(input('insert length:'))
print('*' * a)
for i in range(b-2):
    print('*', ' ' * (b-2), '*')
print('*' * a)
