str=input("Enter the string: ")
print("The even length words are: ")
str=str+" "
s=""
i=0
for ch in str:
    if ch.isalpha():
        s=s+ch
        i+=1
    elif ch==' ':
        if i%2==0:
            print(s)
        i=0
        s=""