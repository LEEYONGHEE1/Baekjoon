a = int(input())

if(a==1):
    pass
else:
    while 1:
        for i in range(2,a+1):
            if(a%i == 0):
                c = i
                break
        a = a // c
        if(a == 0):
            break
        print(c)