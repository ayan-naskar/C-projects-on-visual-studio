import math
a=int(input("Enter the value of coeffecient a: "))
b=int(input("Enter the value of coeffecient b: "))
c=int(input("Enter the value of coeffecient c: "))
d=math.sqrt(b*b - 4*a*c)
print("Answers are: ",(-b+d)/(2*a)," and ",(-b-d)/(2*a))
