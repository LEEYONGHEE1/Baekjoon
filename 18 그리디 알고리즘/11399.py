import sys

input = sys.stdin.readline

test_num = int(input())
user = list(map(int, input().split()))

hap = 0
result_time = 0
user.sort()

for i in range(test_num):
    hap += user[i] 
    result_time += hap

print(result_time)



