from cmath import sqrt

def isprime(num):
    sqr = int(num**(1/2))+1
    if num == 1:
        return False
    for j in range(2,sqr):
        if num%j == 0:
            return False
    return True

plate = []
count = 0

while(1):
    user_input = int(input())
    if(user_input == 0):
        break
    else:
        for k in range(user_input+1, 2*user_input+1):
            if isprime(k):
                count += 1
        plate.append(count)
        count = 0

for i in plate:
    print(i)
    