a1 = int(input())
a2 = list(map(int, input().split()))

b1 = int(input())
b2 = list(map(int, input().split()))

for i in range(len(b2)):
    if(b2[i] in a2):
        b2[i] = 1
    else:
        b2[i] = 0

for i in b2:
    print(i, end=' ')
