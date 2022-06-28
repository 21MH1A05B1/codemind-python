def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True

n=int(input())
g=n+1
while g!=0:
    if prime(g):
        t=g
        rev=0
        while t:
            r=t%10
            rev=rev*10+r
            t=t//10
        if rev==g:
            print(g)
            break
    g+=1
            