a = input()

def divide(s):
    b = sorted(s, reverse=True)
    res = ""
    for i in b:
        res += i
    return res

print(divide(a)) 

