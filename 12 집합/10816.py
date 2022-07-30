import sys
input = sys.stdin.readline

count = 0

a1 = int(input())
a2 = list(map(int, input().split()))

dict = {t: 1 for t in a2}

b1 = int(input())
b2 = list(map(int, input().split()))

print(dict)
for i in b2:
    if dict.get(i):
        count += 1
        print(count, end=' ')
    else:
        print(0, end=' ')
    count = 0