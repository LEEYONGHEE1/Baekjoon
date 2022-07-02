a = int(input())
pbn = [0,1]
count = 0
hap = 0
while(count <=18):
    hap = pbn[count] + pbn[count+1]
    pbn.append(hap)
    count +=1
print(pbn[a]) 



        

 

