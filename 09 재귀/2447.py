def star(n):
    for x in range(1,n+1):
        for y in range(1,n+1):
            if(x == n/3+1 and y == n/3+1):
                print(" ",end ='')
            else:
                print("*" ,end ='')
        print()
    star()
    

star(9)