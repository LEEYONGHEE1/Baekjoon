number = int(input())
x = list(map(int,input().split()))
y = list(sorted(set(x)))

dic = {y[i]:i for i in range (len(y))}

for i in x:
    print(dic[i],end=' ')









