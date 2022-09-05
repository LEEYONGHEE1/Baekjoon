a = int(input())

for _ in range(a):
    b = input()
    stack = list(b)
    sum = 0

    for i in stack:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")