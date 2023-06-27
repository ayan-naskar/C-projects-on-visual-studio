a=sorted(bin(int(input("Enter the first number:- ")))[2:])
b=sorted(bin(int(input("Enter the second number:- ")))[2:])
if a==b:
    print("The numbers are anagram in their Binary Representation")
else:
    print("The numbers are NOT anagram in their Binary Representation")