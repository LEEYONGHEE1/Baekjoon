import sys

input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

xd = [x1,x2,x3]
yd = [y1,y2,y3]

for i in range(3):
    if xd.count(xd[i]) == 1:
        x4 = xd[i]
    if yd.count(yd[i]) == 1:
        y4 = yd[i]

print(x4, y4)
