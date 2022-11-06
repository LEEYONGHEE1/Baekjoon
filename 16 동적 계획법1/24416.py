def fib(n):
    global count
    cnt += 1
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        
def fib2(n):
    global count2
    cnt2 += 1
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    for i in range(3, n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt2

n=int(input())
cnt1, cnt2 = 0, 0
print(fib(n),fib2( n))