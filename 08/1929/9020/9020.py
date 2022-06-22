result = []
user_result = []
hap = []

def isprime(num):
    sqr = int(num**(1/2))+1
    if num == 1:
        return False
    for j in range(2,sqr):
        if num%j == 0:
            return False
    return True

def suso(number):
    i = 0
    while number > result[i]:
        if(result[i] == 9973):
            break
        user_result.append(result[i])
        i +=1

for i in range(1,10001):
    if isprime(i):
        result.append(i)

user_count = int(input())

for i in range(user_count):
    user_number = int(input())
    suso(user_number)
    for i in user_result:
        for k in user_result:
            if(i>k):
                if(i + k == user_number):
                    hap.append(i)
                    hap.append(k)
            else:
                break
    if(int(user_number / 2) in user_result):
        print(f"{int(user_number/2)} {int(user_number/2)}")
    else:
        print(f"{hap[1]} {hap[0]}")
    user_result = []
    hap = []