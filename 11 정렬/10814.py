user=int(input())

arr=[]
for i in range(user):
    a,b = input().split()
    a = int(a)
    arr.append((a,b))

arr.sort(key= lambda k: k[0])

for i in range(user):
    print(arr[i][0],arr[i][1])