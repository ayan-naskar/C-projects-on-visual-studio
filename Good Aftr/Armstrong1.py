n=input("Enter the number: ")
l=len(n)
s=0
for i in n:
    s=s+pow(int(i),l)

if s==int(n):
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")