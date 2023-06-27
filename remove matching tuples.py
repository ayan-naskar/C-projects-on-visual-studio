list=eval(input("Enter the tuples: "))
fl=0;i=0
while(1):
    if list[i] in list[i+1:]:
        list.remove(list[i])
    else:
        i+=1;
    if i==len(list):
        break
print("The final list is:",list)
