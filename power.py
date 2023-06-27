def power(n,i,p):
    if i>0:
        power(n,i-1,n*p)
    else:
        print(p)

num=int(input("Enter the number: "))
pow=int(input("Enter the power: "))
print("The answer is:")
power(num, pow, 1)