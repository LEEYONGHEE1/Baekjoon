n = int(input())

su = []
stack = []
state = True

count = 1

for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        su.append('+')
        count += 1
    if(stack[-1] == num):
        stack.pop()
        su.append('-')
    else:
        state = False
        
if not state:
    print('NO')
else:
    for i in su:
        print(i)


    


