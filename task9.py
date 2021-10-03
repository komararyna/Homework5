for x in range(1, 100):
    flag = True
    for i in range(2, x):
        if x % i == 0:
            flag = False
    if flag == True:
        print(x)





