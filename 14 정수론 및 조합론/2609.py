import sys
input = sys.stdin.readline

a, b = sorted(map(int, input().split()))

num, div = b, a
rest = num % div
while rest != 0:
    num = div
    div = rest
    rest = num % div
print(div)
print(a*b // div)