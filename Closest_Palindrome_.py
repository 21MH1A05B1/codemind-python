def polin(n):
    t=n
    rev=0
    while t!=0:
        r=t%10
        rev=rev*10+r
        t=t//10
    if n==rev:
        return n
n=int(input())
for i in range(n-1,1,-1):
    if polin(i):
        a=i
        break
g=n+1
while g!=0:
    if polin(g):
        b=g
        break
    g+=1
if(n-a)<(b-n):
    print(a)
elif((n-a)==(b-n)):
    print(a,b)
else:
    print(b)