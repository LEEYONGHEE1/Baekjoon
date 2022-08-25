n = int(input())
for _ in range(n):
    m = int(input())
    hap = 1
    dic = {}
    
    for i in range(m):
        m = input().split()
        if m[1] not in dic:
            dic[m[1]] = 1
        else:
            dic[m[1]] += 1
    for i in dic:
        hap *= (dic[i]+1)
    print(hap-1)
