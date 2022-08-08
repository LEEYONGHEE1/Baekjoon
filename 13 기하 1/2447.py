import sys
from this import d

number = int(input())

distance = []

for i in range(6):
    dir, dis = map(int, sys.stdin.readline().split())
    xy = [dir, dis]
    distance.append(xy)

ymax = []
xmax = []

for i in range(6):
    if(distance[i][0] == 3 or distance[i][0] == 4):
        ymax.append(distance[i][1])
    else:
        xmax.append(distance[i][1])

rect_area_y = max(ymax)
rect_area_x = max(xmax)

rect_area = rect_area_x * rect_area_y


for i in range(3):
    if (max(ymax) > ymax[i]):
        a = ymax[i]
        break
    elif (max(xmax) > xmax[i]):
        a = xmax[i]
        break

for i in range(6):
    if(distance[i][1] == a):
        sub_rect = distance[i+1][1] * distance[i+2][1]
        break

total_area = rect_area - sub_rect

print(number*total_area)
