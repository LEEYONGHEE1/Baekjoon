user=int(input())

arr=[]
for i in range(user):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
for i in range(N):
    print(arr[i][0],arr[i][1])