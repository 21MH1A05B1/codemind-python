def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=n+1
while a!=0:
    if prime(a):
        b=a
        rev=0
        while b:
            r=b%10
            rev=rev*10+r
            b=b//10
        if rev==a:
            print(a)
            break
    a+=1
            