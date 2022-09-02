a = int(input())

stack = []

for i in range(a):
    b = input()
    if(b[:2] == "pu"):
        stack.append(b[5:])
    elif(b == "pop"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif(b == "size"):
        print(len(stack))
    elif(b == "empty"):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(b =="top"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
    
    


