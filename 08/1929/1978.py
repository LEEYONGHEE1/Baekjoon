count = 0
result_count = 0
a = int(input())
b = list(map(int, input().split()))


for i in range(a):
    for k in range(1,b[i]+1):
        if(b[i] % k == 0 or b[i] % k == b[i]):
            count+=1
    if(count == 2):
        result_count+=1
    count = 0

print(result_count)