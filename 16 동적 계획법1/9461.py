n = [0 for i in range(101)]
n[1] = 1
n[2] = 1
n[3] = 1
for i in range(0, 98):
    n[i + 3] = n[i] + n[i + 1]
t = int(input())
for i in range(t):
    s = int(input())
    print(n[s])