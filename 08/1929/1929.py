from cmath import sqrt
import sys
import math

def isprime(num):
    sqr = int(num**(1/2))+1
    if num == 1:
        return False
    for j in range(2,sqr):
        if num%j == 0:
            return False
    return True

a, b = map(int, sys.stdin.readline().split())

for i in range(a, b+1):
    if isprime(i):
        print(i)
