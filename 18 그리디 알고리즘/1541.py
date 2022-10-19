a = input().split('-')

hap = []


for i in a:
  count = 0
  s = i.split("+")
  for k in s:
    count += int(k)
  hap.append(count)

n1 = hap[0]

for i in range(1, len(hap)):
  n1 -= hap[i]

print(n1)