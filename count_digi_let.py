str=input("Enter the Sentence: ")
n1=0;n2=0
for i in str:
    if i.isdigit():
        n1+=1
    elif i.isalpha():
        n2+=1
print("Number of digits:",n1,"and Number of letters:",n2)