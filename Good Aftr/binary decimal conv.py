import math
bin=0;i=1
bin=int(input("\nEnter the binary number: "))
deci=0;i=0
while(bin>0):
    deci+=(bin%10)*(math.pow(2,i))
    i+=1
    bin=int(bin/10)
print("The Decimal Equivalent is:", int(deci))
deci=int(input("Enter the decimal number: "))

while(deci>0):
    bin+=(deci%2)*i
    i*=10
    deci=int(deci/2)
print("The Binary Equivalent is:", bin)
