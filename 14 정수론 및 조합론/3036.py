n = int(input())
radius = list(map(int, input().split()))    
for i in range(n - 1):  
    x = radius[0]   
    y = radius[i+1]    
while(x % y != 0):      
    r = x % y       
    x = y        
    y = r    
denom = radius[0] // y   
numer = radius[i+1] // y  
print(f'{denom}/{numer}')
