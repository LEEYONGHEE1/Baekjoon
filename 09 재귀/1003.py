count1 = 0
count2 = 0
 
def fibo(n):
    global count1
    global count2
 
    if n==0:
        count1 +=1
        return 0
    elif n==1:
        count2 +=1
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
 
a = int(input())
 
for _ in range(a):
    n = int(input())
    fibo(n)
    print(count1, count2)
    count1 = 0
    count2 = 0