n=int(input("Enter the marks of student: "))
a=n//10
print("Your grade is:")
if a>=9:
    print("A+")
elif a==8:
    print("A")
elif a==7:
    print("B")
elif a==5:
    print("C")
else:
    print("Fail")