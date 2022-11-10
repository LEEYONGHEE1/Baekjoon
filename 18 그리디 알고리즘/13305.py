n = int(input())

road = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = road[0] * cost[0]
m = cost[0]
e = 0

for i in range(1, n-1):
    if cost[i] < m:
        result += m*e
        e = road[i]
        m = cost[i]
    else:
        e += road[i]

    if i == n-2:
        result += m*e

print(result)