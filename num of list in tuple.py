tuple=eval(input("Enter the input: "))
n=0
for i in tuple:
    if type(i) is list:
        n+=1
print("The length of tuple is:",n)