import sys
input = sys.stdin.readline

num = [[0]*101 for i in range(101)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(10):
        for k in range(10):
            num[a+i][b+k] = 1

count = 0
for i in num:
    count += sum(i)
print(count)