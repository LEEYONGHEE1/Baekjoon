import sys

input = sys.stdin.readline

n, k = map(int,input().split())

arr = list(map(int, input().split()))

# hap = 0
# result = []

# for i in range(len(arr)):
#     if(i == len(arr)- k):
#         hap = sum(arr[i:i+k])
#         result.append(hap)
#         break
#     else:
#         hap = sum(arr[i:i+k])
#         result.append(hap)

# print(max(result))

result2 = []
result2.append(sum(arr[:k]))

print(result2)

for i in range(n-k):
    result2.append(result2[i] - arr[i] + arr[k+i])
    
print(result2)
