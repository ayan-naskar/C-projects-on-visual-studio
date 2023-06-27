def cal(arr,todo,n):
    a=0;k=0
    for i in range (n):
        a+=arr[i]
        if a==todo:
            k+=1
            a=0
    if a!=0:
        return n
    return n-k


t=int(input())
for test in range (t):
    n=int(input())
    ar = list(map(int, input().split()))
    min=n-1
    b=0
    for i in range (n):
        b+=ar[i]
        a=cal(ar,b,n)
        if min>a:
            min=a
    print(min)
