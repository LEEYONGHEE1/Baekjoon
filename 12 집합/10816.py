import sys
input = sys.stdin.readline

count = 0

a1 = int(input())
a2 = list(map(int, input().split()))


b1 = int(input())
b2 = list(map(int, input().split()))

for i in b2:
    print(a2.count(i), end=' ')
