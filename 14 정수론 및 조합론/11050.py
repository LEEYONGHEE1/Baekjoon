a, b = map(int, input().split())
res = 1
for i in range(b):
    res *= a
    a -= 1
for k in range(2, b+1):
    res //= k
print(res)
