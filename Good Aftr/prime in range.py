import math

def checkprime(n):
    fl=0;i=2
    while(i<=math.sqrt(n)):
        if(n%i==0): fl=1
        i+=1
    if(fl==0): print(n,end=" ")

def main():
    a, b = input("Enter the range: ").split()
    a=int(a); b=int(b)
    print("The prime numbers are: ")
    while(a<=b):
        checkprime(a)
        a+=1

main()
