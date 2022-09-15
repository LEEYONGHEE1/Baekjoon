# import sys

# # prefix 알고리즘을 쓰지 않는다면 시간 복잡도가 O(nm)이 된다
# # 밑에는 일반 구현
# input = sys.stdin.readline

# n, m = map(int, input().split())

# lst = list(map(int, input().split()))

# for _ in range(m):
#     i, j = map(int, input().split())
#     hap = sum(lst[i-1:j])
#     print(hap)

# # prefix 알고리즘을 써보자 시간 복잡도 O(n+m)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))

# 인덱스를 사용자로부터 받으니 헷갈리지 않기 위해 0을 추가
prefix_sum = [0]

hap = 0

for i in lst:
    hap += i
    prefix_sum.append(hap)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])


