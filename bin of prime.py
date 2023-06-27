t=int(input())
while(t>0):
    t-=1
    b=input()
    if (b.find("10")>=0 or b.find("11")>=0):
        print("Yes")
    else:
        print("NO")