a=[]
n=int(input("Enter the size of array:"))
for i in range(n):
    a.append(int(input()))
print("Original List=",a)
b=a[:]
print("The copy of the original list=",b)