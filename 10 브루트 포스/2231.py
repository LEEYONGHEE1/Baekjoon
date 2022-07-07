a = input()
b = 9*int(len(a))
c = str(int(a) - b)

res = 0
hap = 0

if(int(a) > 18):
    for i in range(int(c),int(a)):
        d = str(i)
        for j in range(len(d)):
            hap += int(d[j])
        if(hap + i == int(a)):
            res = int(a) - hap
            break
        else:
            res = 0
            hap = 0

else:
    for i in range(1, int(a) + 1):
        d = str(i)
        for k in range(len(d)):
            hap += int(d[k])
        if(hap + i == int(a)):
            res = int(a) - hap
            break
        else:
            res = 0
            hap = 0
print(res)
