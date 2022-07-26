number = int(input())
res = []

x = list(map(int,input().split()))
y = x
y = list(sorted(set(x)))


print(y)

for i in range(number):
    for k in range(len(y)):
        if(x[i] == y[k]):
            res.append(k)
            break

for i in res:
    print(i, end=" ")






