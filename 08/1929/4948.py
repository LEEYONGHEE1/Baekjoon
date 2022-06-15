from cgitb import reset
from cmath import sqrt

def isprime(num):
 
    for i in range(num+1 , num*2+1):
        result = []
        sqr = int(i**(1/2))+1
        if num == 1:
            pass
        for j in range(2,sqr):
            if i%j == 0:
                pass
        result.append(i)
    return len(result)
    
while(1):
    user_input = int(input())
    if(user_input == 0):
        break
    else:
        a = isprime(user_input)
        if isprime:
            print(a)