while 1:
    b = input()
    if(b == "."):
        break
    stack = list(b)
    sum = 0
    sum2 = 0

    for i in stack:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        elif i == "[":
            sum2 += 1
        elif i == "]":
            sum2 -= 1
        if sum < 0 or sum2 < 0:
            print("no")
            break
    
    if sum > 0 or sum2 > 0:
        print("no")
    elif sum == 0 or sum2 == 0:
        print("yes")
    