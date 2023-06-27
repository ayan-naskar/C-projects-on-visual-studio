import math
t=int(input())
for tt in range (t):
    x,k=map(int,input().split())
    #k=float(input())
    if x==1:
        print("YES")
        continue
    n=b=0
    while(1):
        if n<x:
            a=(math.log(x-n)//math.log(k))
            if round(pow(k,a+1)==x-n):
                print("YES")
                break
            if b==a:
                print("NO")
                break
            b=a
            n+=pow(k,a)
            print(n)
        elif n==x:
            print("YES")
            break