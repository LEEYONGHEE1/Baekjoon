n = int(input())

def star(k):
    if k == 3:
        return ['***','* *','***']

    arr = star(k//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(k//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(n)))