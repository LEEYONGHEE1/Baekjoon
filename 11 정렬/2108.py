import sys
from collections import Counter

a = int(sys.stdin.readline()) # a는 홀수다 

b = []
sum1 = 0
result = 0

for i in range(a):
    b.append(int(sys.stdin.readline()))

b.sort()

# 산술 평균
result = round(sum(b) / a)
print(result)
# 중앙값
middle = b[int(a/2)]
print(middle)
if(a == 1):
    print(b[0])
    print(0)
else:
    #최빈값
    counter = Counter(b).most_common()
    if(counter[0][1] == counter[1][1]):
        print(counter[1][0])
    else:
        print(counter[0][0])
    #범위
    print(abs(b[-1] - b[0]))

