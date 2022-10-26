hap = 0
hap_number = 0

count, max_number = map(int, input().split())

number = list(map(int, input().split()))

for i in range(count):
    for j in range(i+1, count):
        for k in range(j+1, count):
            hap = number[i] + number[j] + number[k]
            if hap <= max_number:
                hap_number = max(hap, hap_number)

print(hap_number)