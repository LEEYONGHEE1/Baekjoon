A, B = [], []

N, M = map(int, input().split())

for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for k in range(M):
        print(A[row][k] + B[row][k], end=' ')
    print()