import sys

n = int(sys.stdin.readline())
max_value=[0]*10001 

for k in range(n):
    max_value[int(sys.stdin.readline())]+=1
    
for i in range(1,10001):
    for j in range(max_value[i]):
        print(i) 
