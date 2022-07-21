user=int(input())

arr=[]
for i in range(user):
    a = input()
    arr.append(a)

# 중복 제거
arr_sort = set(arr)

arr_sort2 = []

for i in arr_sort:
    arr_sort2.append((len(i),i))

b = sorted(arr_sort2)

print(b)

for i, j in b:
    print(j)


