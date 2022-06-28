def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
m=n
if n==1 or n==2 or n==3 or n==5:
    print('0')
else:
    for i in range(n,2,-1):
        if prime(i):
            a=i
            break
    while m!=0:
        if prime(m):
            b=m
            break
        m+=1
if b-n>n-a or b-n==n-a:
    print(abs(n-a))
else:
    print(abs(b-n))
