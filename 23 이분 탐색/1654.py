import sys

a, b = map(int, input().split())
len = [int(sys.stdin.readline()) for _ in range(a)]
start, end = 1, max(len)

while start <= end:
    mid = (start + end) // 2 
    line = 0 
    for i in len:
        line += i // mid 
    if line >= b:
        start = mid + 1
    else:
        end = mid - 1
print(end)