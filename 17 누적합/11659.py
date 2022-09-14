import sys

input = sys.stdin.readline

x, y = map(int, input().split())
nums = [0] + list(map(int, input().split()))

t = [0] * (x + 1)
for i in range(1, x + 1):
    t[i] = t[i - 1] + nums[i]

for _ in range(y):
    a, b = map(int, input().split())
    print(t[b] - t[a - 1])