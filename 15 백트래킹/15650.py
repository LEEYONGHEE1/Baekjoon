a, b = map(int, input().split())

s= []

def dfs2(n):
    if(len(s) == b):
        print(' '.join(map(str,s)))
        return
    for i in range(n, a+1):
        if i not in s:
            s.append(i)
            dfs2(i+1)
            s.pop()

dfs2(1)