import sys
input = sys.stdin.readline

a1 = int(input())
a2 = list(map(int, input().split()))

dict = {t: 1 for t in a2}

b1 = int(input())
b2 = list(map(int, input().split()))

for i in b2:
    if dict.get(i):
        print(1, end=' ')
    else:
        print(0, end=' ') 


