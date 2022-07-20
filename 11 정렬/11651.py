a = int(input())
 
b = []
for _ in range(a):
    xy = list(map(int,input().split()))
    b.append([xy[1],xy[0]])
 
b.sort()
 
for i in b:
    print(i[1],i[0])