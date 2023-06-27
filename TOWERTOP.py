t=int(input())
while(t>0):
    t-=1
    x,m =(input().split())
    x=int(x)
    m=int(m)
    x-=1;
    a=x
    b=0
    while(a>0):
        a=a>>1
        b+=1
    b=m-b
    if b<0:
        b=0
    print(b)