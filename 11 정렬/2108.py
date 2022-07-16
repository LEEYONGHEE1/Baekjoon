from collections import Counter

a = int(input()) # a는 홀수다 

b = []
sum1 = 0
result = 0

for i in range(a):
    c = int(input())
    b.append(c)
    sum1 += c

b.sort()

# 산술 평균
result = round(sum1 / a)
print(result)
# 중앙값
middle = b[int(a/2)]
print(middle)
if(a == 1):
    print(b[0])
    print(0)
else:
    #최빈값
    counter = Counter(b)
    print(counter)
    print(f"{counter.most_common(1)} asdas")
    
    print(b[1])
    #범위
    print(abs(b[-1] - b[0]))

