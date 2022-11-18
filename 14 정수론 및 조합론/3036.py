def chg(a, b):
    while(b != 0):
        n = a%b
        a = b
        b = n
    return a

n = int(input())
radius = list(map(int, input().split()))
for i in range(1, n):
    c = chg(radius[0], radius[i])
    print(f'{radius[0]//c}/{radius[i]//c}')
