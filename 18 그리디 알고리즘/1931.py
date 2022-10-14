import sys

input = sys.stdin.readline

test_number = int(input())

room = []
last_time = 0
count = 0

for i in range(test_number):
    a, b = map(int, input().split())
    room.append([a,b])

room = sorted(room, key=lambda a:a[0])
room = sorted(room, key=lambda a:a[1])

for i in range(test_number):
    if(room[i][0] >= last_time):
        last_time = room[i][1]
        count += 1
    
print(count)



