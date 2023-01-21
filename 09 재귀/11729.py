n = int(input())

def hanoi(n,a,b,c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
        
count = 0
for _ in range(n):
    count = 2*count + 1
print(count)
hanoi(n,1,2,3)