print("The numbers are: 2000",end='')
for i in range(2001,4001):
    s=str(i)
    f=0
    for each in s:
        if(int(each)%2!=0):
            f=1
            break
    if(f==0):
        print(",",i,end='')
