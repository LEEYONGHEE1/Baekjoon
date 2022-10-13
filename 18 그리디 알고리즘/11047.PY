import sys

input = sys.stdin.readline

test_num, price = map(int, input().split())

pocket = []
count = 0
score = 0
num = 0

for _ in range(test_num):
    m = int(input())
    pocket.append(m)

pocket.reverse()

while price > 0:
    if(pocket[count] > price):
        count += 1
    else:
        num = price // pocket[count]
        price = price % pocket[count]
        score += num
        count += 1

print(score)