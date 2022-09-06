while 1:
    stack = []
    b = input()
    if(b == "."):
        break


    for i in b:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if(len(stack) != 0 and stack[-1] == "("):
                stack.pop()
            else:
                stack.append(")")
                break
        elif i == "[":
            stack.append(i)
        elif i == "]":
            if(len(stack) != 0 and stack[-1] == "["):
                stack.pop()
            else:
                stack.append("]")
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
    
    