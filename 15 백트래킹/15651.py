a, b = map(int, input().split())

s= []

def dfs3():
    if(len(s) == b):
        print(' '.join(map(str,s)))
        return
    for i in range(1, a+1):
        s.append(i)
        dfs3()
        s.pop()
      

dfs3()