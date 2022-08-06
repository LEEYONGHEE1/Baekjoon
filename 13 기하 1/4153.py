import sys
input = sys.stdin.readline

res = []

while 1:
    a, b, c = map(int, input().split())
    if(a + b + c == 0):
        break
    else:
        so = [a,b,c]
        so.sort()
        res.append(so)

for i in range(len(res)):
    if(res[i][0]**2 + res[i][1]*res[i][1] == pow(res[i][2],2)):
        print("right")
    else:
        print("wrong")


