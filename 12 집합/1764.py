hearX , seeX = map(int, input().split())

arr1 = set() # hearX
arr2 = set() # seeX

for i in range(hearX):
    arr1.add(input())

for i in range(seeX):
    arr2.add(input())

arr3 =sorted(list(arr1 & arr2))

print(len(arr3))
for i in arr3:
    print(i)

# 집합을 이용해 풀자