import sys

n = int(sys.stdin.readline())
position = [0 for _ in range(n)] 
visited = [False for _ in range(n)] 
count = 0 


def check(x):  # 대각선 체크
    for i in range(x):
        if abs(position[x] - position[i]) == x - i: 
            return False
    return True

def dfs(q): # 체스판의 열을 dfs 탐색
    global count

    if q == n:
        count += 1
        return

    for i in range(n):
        if not visited[i]:
            position[q] = i

            if(check(q)):
                visited[i] = True # 퀸을 놓는다
                dfs(q + 1) # 퀸을 놓을 수 있는 위치 찾기
                visited[i] = False # 다시 초기화

dfs(0)
print(count)
        
