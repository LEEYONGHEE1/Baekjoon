a = int(input())

stack = []

for i in range(a):
    b = int(input())
    if(b != 0):
        stack.append(b)
    else:
        stack.pop()

print(sum(stack))

