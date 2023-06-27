import math
n=float(input("Enter the number: "))
n1=float(input("Enter the number: "))
a=math.ceil(n);print("ceil(N):",a);
a=math.floor(n);print("floor(N):",a)
a=math.fabs(n);print("fabs(N):",a)
a=math.factorial(int(n)) if n>0 else math.factorial(int(n1));print("factorial():",a)
a=math.copysign(n1,n);print("copysign():",a);
a=math.gcd((int(n1)),(int(n)));print("gcd():",a)