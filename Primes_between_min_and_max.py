def prime(n):
    if n==1:
        return False
    for i in range(2,int(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()))
maxi=a.index(max(a))
mini=a.index(min(a))
d=0
if mini<maxi:
    for i in range(mini,maxi+1):
        if prime(a[i]):
            d+=1
    print(d)
else:
    for i in range(maxi,mini+1):
        if prime(a[i]):
            d+=1
    print(d)
 