import math
n=input("Enter the Number:- ")
count=len(n)
n=int(n)
c=n;s=0;c=n
while c>0:
    p=c%10
    s=s+math.pow(p,count)
    c=c//10
print(n,"is" if s==n else "is not","an armstrong number")