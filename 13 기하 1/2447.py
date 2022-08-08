import sys

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

count = 0

for i in range(6):
    if(distance[i][1] == rect_area_x):
        sub_rectY = abs(distance[i+1][1] - distance[i-1][1])
        count+=1 
        if(count == 2):
            sub_rectX = abs(distance[i+1][1] - distance[i-1][1])
    elif(distance[i][1] == rect_area_y):
        sub_rectX = abs(distance[i+1][1] - distance[i-1][1])

sub_rect = sub_rectX * sub_rectY

total_area = rect_area - sub_rect

print(number*total_area)
