import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = set([input() for i in range(n)])
count = 0

for i in range(m):
    a = input()
    if a in arr:
        count += 1

print(count)

