for i in range(1,1001):
    n=i
    s=0
    for j in range(1, n):
        if(n % j == 0):
            s = s + j
    if (s == n):
        print(i)