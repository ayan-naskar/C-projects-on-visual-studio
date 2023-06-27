import math
b=input("Enter the binary form: ")
d=0;i=len(b)-1
for j in b:
    d=d+(int(j)%10)*(math.pow(2,i))
    i-=1
print("The Decimal form is:", int(d))

d=int(input("Enter the decimal form: "))
b=0;i=1
for j in range(1,32+1):
    b=b+(d%2)*i
    i=i*10
    d=int(d/2)
    if d==0:
        break
print("The Binary form is:", b)