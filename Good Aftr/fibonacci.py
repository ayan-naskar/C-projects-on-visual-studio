print("The Series is:")
a=0;b=1;sum=0
while(1):
    c=b+a
    a=b
    b=c
    if (b>500):
        break
    elif(b>=100):
        print(b,end=' ')
        sum+=b
print("\nThe sum of the series is:",sum)