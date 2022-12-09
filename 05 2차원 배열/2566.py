x = 0
y = 0
max = 0
for i in range(0,9):
    a = list(map(int, input().split(" ")))
    m = max(a)

    if max <= m:
        max = m
        x = a.index(m)
        y = i

print(max)
print(y+1, x+1)