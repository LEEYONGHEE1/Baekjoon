hearX , seeX = map(int, input().split())

arr1 = [] # hearX
arr2 = [] # seeX
result = []

count = 0

for i in range(hearX):
    arr1.append(input())

for i in range(seeX):
    arr2.append(input())

for i in arr1:
    if(i in arr2):
        count += 1
        result.append(i)


result.sort()

print(count)
for i in result:
    print(i)
