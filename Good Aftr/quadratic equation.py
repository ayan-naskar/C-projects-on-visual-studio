import math
print("Enter the coefficients: ")
a=int(input())
b=int(input())
c=int(input())
if a==0:
    print("Wrong equation coefficients")
else:
    dis=b*b-4*a*c
    sq=math.sqrt(abs(dis))
    if(dis>0):
        print("Real and different roots are ",(-b+sq)/(2*a),"and",(-b-sq)/(2*a))
    elif dis==0:
        print("Real and same roots is ",(-b/(2*a)))
    else: 
        print("Complex roots are ",-b/(2*a),"+i",sq,"and",-b/(2*a),"-i",sq)