import math
print("The prime numbers are:")
for i in range(100,200+1):
    n=i
    flag=1
    for j in range(2,(int)(math.sqrt(n)+1)):
        if(n%j==0):
            flag=0
            break
    if flag==1:
        print(i,end=" ")