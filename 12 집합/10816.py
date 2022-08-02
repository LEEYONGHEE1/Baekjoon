import sys
from typing import Counter
input = sys.stdin.readline

count = 0

a1 = int(input())
a2 = sorted(list(map(int, input().split())))

b1 = int(input())
b2 = list(map(int, input().split()))

counter = Counter(a2)

for i in range(len(b2)):
    if b2[i] in counter:
        print(counter[b2[i]], end = ' ')
    else:
        print(0, end=' ')
