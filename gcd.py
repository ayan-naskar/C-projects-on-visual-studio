num=1
arr=[969, 2584, 3553, 7429, 9367, 6137 ]
for i in range (1,arr[0]+1):
    f=0
    for each in arr:
        if(each%i!=0):
            f=1
    if(f==0):
        num=i
print("GCD =",num)