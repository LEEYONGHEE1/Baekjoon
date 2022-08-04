a = input()

result = []
count = 0

for i in range(len(a)):
    for k in range(1, len(a)+1):
        result.append(a[i:k])

print(len(set(result))-1)
