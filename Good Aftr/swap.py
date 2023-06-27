FIRST=int(input("Enter the first number:- "))
SECOND=int(input("Enter the second number:- "))
print("Before swapping FIRST = ",FIRST,"and SECOND = ",SECOND)
FIRST=FIRST+SECOND
SECOND=FIRST-SECOND
FIRST=FIRST-SECOND
print("After swapping FIRST = ",int(FIRST),"and SECOND =",int(SECOND))