from collections import deque
import queue

deq = deque()
remove = []

n, k = map(int, input().split())

for i in range(1, n+1):
    deq.append(i)

while deq:
    for i in range(k-1):
        deq.append(deq.popleft())
    remove.append(deq.popleft())
    print(deq)

print("<",end='')
for i in range(len(remove)-1):
    print("%d, "%remove[i], end='')
print(remove[-1], end='')
print(">")