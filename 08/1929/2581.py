count = 0
result = []
a = int(input())
b = int(input())

for i in range(a, b+1):
    if(i == 2 or i == 3 or i == 5 or i ==7):
        result.append(i)
    if(i % 2 == 0 or i % 3==0 or i % 5 ==0 or i % 7 == 0):
        pass
    else:
        for k in range(1,i+1):
            if(i % k == 0 or i % k == i):
                count+=1
        if(count == 2):
            result.append(i)
        count = 0

if(len(result) == 0):
    print(-1)
else:
    print(sum(result))
    print(min(result))