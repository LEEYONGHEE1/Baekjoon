a, b = map(int, input().split())

s = []

def dfs4(n):
    if(len(s) == b):
        print(' '.join(map(str, s)))
        return
    for i in range(n, a+1):
        s.append(i)
        dfs4(i)
        s.pop()

dfs4(1)