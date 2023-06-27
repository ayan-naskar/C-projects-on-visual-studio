import math
n=int(input("Enter the number: "))
fl=0;i=2
if(n==1): print("The number is neither prime nor composite")
else:
    while(i<=math.sqrt(n)):
        if(n%i==0): fl=1
        i+=1
    print("The number is","prime" if fl==0 else "not prime")