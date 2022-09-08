def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
x=int(input())
for i in range(x):
    n=int(input())
    m=n
    for i in range(n,1,-1):
        if prime(i):
            a=i
            break
    while m:
        if prime(m):
            b=m
            break
        m+=1
    if n-a>b-n:
        print(b)
    else:
        print(a)
    