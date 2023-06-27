a=50
b=120
print("The Fibonacci Series is:")
f1=0
f2=1
i=1
s1=0
for i in range(a,b):
    if f2>b:
        break
    if f2>=a:
        print(f2)
        s1+=f2
    s=f1+f2
    f1=f2
    f2=s
    i=a
print("The sum of the series:",s1)